# Code modified from Rafael Valle's implementation https://github.com/NVIDIA/waveglow/blob/5bc2a53e20b3b533362f974cfa1ea0267ae1c2b1/denoiser.py

"""Waveglow style denoiser can be used to remove the artifacts from the HiFiGAN generated audio."""
import torch


class Denoiser(torch.nn.Module):
    """Removes model bias from audio produced with waveglow"""

    def __init__(self, vocoder, filter_length=1024, n_overlap=4, win_length=1024, mode="zeros"):
        super().__init__()
        self.filter_length = filter_length
        self.hop_length = int(filter_length / n_overlap)
        self.win_length = win_length

        dtype, device = next(vocoder.parameters()).dtype, next(vocoder.parameters()).device
        self.device = device
        if mode == "zeros":
            mel_input = torch.zeros((1, 80, 88), dtype=dtype, device=device)
        elif mode == "normal":
            mel_input = torch.randn((1, 80, 88), dtype=dtype, device=device)
        else:
            raise Exception(f"Mode {mode} if not supported")

        def stft_fn(audio, n_fft, hop_length, win_length, window):
            spec = torch.stft(
                audio,
                n_fft=n_fft,
                hop_length=hop_length,
                win_length=win_length,
                window=window,
                return_complex=True,
            )
            spec = torch.view_as_real(spec)
            return torch.sqrt(spec.pow(2).sum(-1)), torch.atan2(spec[..., -1], spec[..., 0])

        self.stft = lambda x: stft_fn(
            audio=x,
            n_fft=self.filter_length,
            hop_length=self.hop_length,
            win_length=self.win_length,
            window=torch.hann_window(self.win_length, device=device),
        )
        self.istft = lambda x, y: torch.istft(
            torch.complex(x * torch.cos(y), x * torch.sin(y)),
            n_fft=self.filter_length,
            hop_length=self.hop_length,
            win_length=self.win_length,
            window=torch.hann_window(self.win_length, device=device),
        )

        with torch.no_grad():
            bias_audio = vocoder(mel_input).float().squeeze(0)
            bias_spec, _ = self.stft(bias_audio)

        self.register_buffer("bias_spec", bias_spec[:, :, 0][:, :, None])

    @torch.inference_mode()
    def forward(self, audio, strength=0.0005):
        audio_spec, audio_angles = self.stft(audio)
        audio_spec_denoised = audio_spec - self.bias_spec.to(audio.device) * strength
        audio_spec_denoised = torch.clamp(audio_spec_denoised, 0.0)
        audio_denoised = self.istft(audio_spec_denoised, audio_angles)
        return audio_denoised
