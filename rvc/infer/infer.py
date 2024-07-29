import os
import time
import torch
import numpy as np
import soundfile as sf
import librosa
import noisereduce as nr
from scipy.io import wavfile
from rvc.infer.pipeline import Pipeline as VC
# from audio_upscaler import upscale
from rvc.lib.utils import load_audio, load_embedding
from rvc.lib.tools.split_audio import process_audio, merge_audio
from rvc.lib.algorithm.synthesizers import (
    SynthesizerV1_F0,
    SynthesizerV1_NoF0,
    SynthesizerV2_F0,
    SynthesizerV2_NoF0,
)
from rvc.configs.config import Config

# import logging

# logging.getLogger("httpx").setLevel(logging.WARNING)
# logging.getLogger("httpcore").setLevel(logging.WARNING)


class VoiceConverter:
    """
    A class for performing voice conversion using the Retrieval-Based Voice Conversion (RVC) method.
    """

    def __init__(self):
        """
        Initializes the VoiceConverter with default configuration, and sets up models and parameters.
        """
        self.config = Config()  # Load RVC configuration
        self.hubert_model = (
            None  # Initialize the Hubert model (for embedding extraction)
        )
        self.tgt_sr = None  # Target sampling rate for the output audio
        self.net_g = None  # Generator network for voice conversion
        self.vc = None  # Voice conversion pipeline instance
        self.cpt = None  # Checkpoint for loading model weights
        self.version = None  # Model version
        self.n_spk = None  # Number of speakers in the model

    def load_hubert(self, embedder_model, embedder_model_custom):
        """
        Loads the HuBERT model for speaker embedding extraction.

        Args:
            embedder_model: Path to the pre-trained embedder model.
            embedder_model_custom: Path to a custom embedder model (if any).
        """
        models, _, _ = load_embedding(embedder_model, embedder_model_custom)
        self.hubert_model = models[0].to(self.config.device)
        self.hubert_model = (
            self.hubert_model.half()
            if self.config.is_half
            else self.hubert_model.float()
        )
        self.hubert_model.eval()

    @staticmethod
    def remove_audio_noise(input_audio_path, reduction_strength=0.7):
        """
        Removes noise from an audio file using the NoiseReduce library.

        Args:
            input_audio_path: Path to the input audio file.
            reduction_strength: Strength of noise reduction (0.0 to 1.0).

        Returns:
            The audio data with noise reduced, or None if an error occurs.
        """
        try:
            # reduction_strength를 float로 변환하고 범위를 제한합니다
            reduction_strength = float(reduction_strength)
            reduction_strength = max(0.0, min(1.0, reduction_strength))

            # librosa를 사용하여 오디오 파일 읽기
            data, rate = librosa.load(input_audio_path, sr=None)
            
            # 스테레오를 모노로 변환 (필요한 경우)
            if len(data.shape) > 1:
                data = np.mean(data, axis=1)
            
            # 데이터 타입을 float32로 변환
            data = data.astype(np.float32)
            
            # 노이즈 감소 적용
            reduced_noise = nr.reduce_noise(
                y=data, sr=rate, prop_decrease=reduction_strength, use_torch=False
            )
            
            # 결과를 float32로 유지
            reduced_noise = reduced_noise.astype(np.float32)
            
            return reduced_noise
        except Exception as error:
            print(f"Error cleaning audio: {error}")
            return None    
    


    @staticmethod
    def convert_audio_format(input_path, output_path, output_format):
        """
        Converts an audio file to a specified output format.

        Args:
            input_path: Path to the input audio file.
            output_path: Path for the output audio file.
            output_format: Desired output format (e.g., "MP3", "WAV").

        Returns:
            The path to the converted audio file, or None if conversion fails.
        """
        try:
            if output_format != "WAV":
                print(f"Converting audio to {output_format} format...")
                audio, sample_rate = librosa.load(input_path, sr=None)
                common_sample_rates = [
                    8000,
                    11025,
                    12000,
                    16000,
                    22050,
                    24000,
                    32000,
                    44100,
                    48000,
                ]
                target_sr = min(common_sample_rates, key=lambda x: abs(x - sample_rate))
                audio = librosa.resample(
                    audio, orig_sr=sample_rate, target_sr=target_sr
                )
                sf.write(output_path, audio, target_sr, format=output_format.lower())
            return output_path
        except Exception as error:
            print(f"Failed to convert audio to {output_format} format: {error}")

    def voice_conversion(
        self,
        sid=0,
        input_audio_path=None,
        f0_up_key=None,
        f0_file=None,
        f0_method=None,
        file_index=None,
        index_rate=None,
        resample_sr=0,
        rms_mix_rate=None,
        protect=None,
        hop_length=None,
        output_path=None,
        split_audio=False,
        f0_autotune=False,
        filter_radius=None,
        embedder_model=None,
        embedder_model_custom=None,
    ):
        """
        Performs voice conversion on the input audio using the loaded model and settings.

        Args:
            sid: Speaker ID for the target voice.
            input_audio_path: Path to the input audio file.
            f0_up_key: Pitch shift value in semitones.
            f0_file: Path to an external F0 file for pitch guidance.
            f0_method: F0 estimation method to use.
            file_index: Path to the FAISS index for speaker embedding retrieval.
            index_rate: Weighting factor for speaker embedding retrieval.
            resample_sr: Target sampling rate for resampling.
            rms_mix_rate: Mixing ratio for adjusting RMS levels.
            protect: Protection level for preserving the original pitch.
            hop_length: Hop length for F0 estimation.
            output_path: Path for saving the converted audio.
            split_audio: Whether to split the audio into segments for processing.
            f0_autotune: Whether to apply autotune to the F0 contour.
            filter_radius: Radius for median filtering of the F0 contour.
            embedder_model: Path to the embedder model.
            embedder_model_custom: Path to a custom embedder model.

        Returns:
            A tuple containing the target sampling rate and the converted audio data,
            or an error message if conversion fails.
        """
        
        # print(f"voice_conversion: input_audio_path = {input_audio_path}, output_path = {output_path}, \
        #     file_index = {file_index}, split_audio = {split_audio}, ")
        
        
        f0_up_key = int(f0_up_key)
        try:
            audio = load_audio(input_audio_path, 16000)
            audio_max = np.abs(audio).max() / 0.95

            if audio_max > 1:
                audio /= audio_max

            if not self.hubert_model:
                self.load_hubert(embedder_model, embedder_model_custom)
            if_f0 = self.cpt.get("f0", 1)

            file_index = (
                file_index.strip()
                .strip('"')
                .strip("\n")
                .strip('"')
                .strip()
                .replace("trained", "added")
            )
            if self.tgt_sr != resample_sr >= 16000:
                self.tgt_sr = resample_sr


            if split_audio == "True":
                result, new_dir_path = process_audio(input_audio_path)
                if result == "Error":
                    return "Error with Split Audio", None

                dir_path = (
                    new_dir_path.strip().strip('"').strip("\n").strip('"').strip()
                )
                if dir_path:
                    paths = [
                        os.path.join(root, name)
                        for root, _, files in os.walk(dir_path, topdown=False)
                        for name in files
                        if name.endswith(".wav") and root == dir_path
                    ]
                try:
                    for path in paths:
                        self.voice_conversion(
                            sid,
                            path,
                            f0_up_key,
                            None,
                            f0_method,
                            file_index,
                            index_rate,
                            resample_sr,
                            rms_mix_rate,
                            protect,
                            hop_length,
                            path,
                            False,
                            f0_autotune,
                            filter_radius,
                            embedder_model,
                            embedder_model_custom,
                        )
                except Exception as error:
                    print(error)
                    return f"Error {error}"
                print("Finished processing segmented audio, now merging audio...")
                merge_timestamps_file = os.path.join(
                    os.path.dirname(new_dir_path),
                    f"{os.path.basename(input_audio_path).split('.')[0]}_timestamps.txt",
                )
                self.tgt_sr, audio_opt = merge_audio(merge_timestamps_file)
                os.remove(merge_timestamps_file)
            else:
                audio_opt = self.vc.pipeline(
                    self.hubert_model,
                    self.net_g,
                    sid,
                    audio,
                    input_audio_path,
                    f0_up_key,
                    f0_method,
                    file_index,
                    index_rate,
                    if_f0,
                    filter_radius,
                    self.tgt_sr,
                    resample_sr,
                    rms_mix_rate,
                    self.version,
                    protect,
                    hop_length,
                    f0_autotune,
                    f0_file=f0_file,
                )

            if output_path:
                sf.write(output_path, audio_opt, self.tgt_sr, format="WAV")

            return self.tgt_sr, audio_opt

        except Exception as error:
            print(error)

    def get_vc(self, weight_root, sid):
        """
        Loads the voice conversion model and sets up the pipeline.

        Args:
            weight_root: Path to the model weight file.
            sid: Speaker ID (currently not used).
        """
        if sid == "" or sid == []:
            self.cleanup_model()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

        self.load_model(weight_root)

        if self.cpt is not None:
            self.setup_network()
            self.setup_vc_instance()

    def cleanup_model(self):
        if self.hubert_model is not None:
            print("clean_empty_cache")
            del self.net_g, self.n_spk, self.vc, self.hubert_model, self.tgt_sr
            self.hubert_model = self.net_g = self.n_spk = self.vc = self.tgt_sr = None
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

        del self.net_g, self.cpt
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        self.cpt = None

    def load_model(self, weight_root):
        self.cpt = (
            torch.load(weight_root, map_location="cpu")
            if os.path.isfile(weight_root)
            else None
        )

    def setup_network(self):
        if self.cpt is not None:
            self.tgt_sr = self.cpt["config"][-1]
            self.cpt["config"][-3] = self.cpt["weight"]["emb_g.weight"].shape[0]
            if_f0 = self.cpt.get("f0", 1)

            self.version = self.cpt.get("version", "v1")
            synthesizer_class = {
                ("v1", 0): SynthesizerV1_NoF0,
                ("v1", 1): SynthesizerV1_F0,
                ("v2", 0): SynthesizerV2_NoF0,
                ("v2", 1): SynthesizerV2_F0,
            }.get((self.version, if_f0), SynthesizerV1_NoF0)

            self.net_g = synthesizer_class(
                *self.cpt["config"], is_half=self.config.is_half
            )
            del self.net_g.enc_q
            self.net_g.load_state_dict(self.cpt["weight"], strict=False)
            self.net_g.eval().to(self.config.device)
            self.net_g = (
                self.net_g.half() if self.config.is_half else self.net_g.float()
            )

    def setup_vc_instance(self):
        if self.cpt is not None:
            self.vc = VC(self.tgt_sr, self.config)
            self.n_spk = self.cpt["config"][-3]

    def infer_pipeline(
        self,
        f0_up_key,
        filter_radius,
        index_rate,
        rms_mix_rate,
        protect,
        hop_length,
        f0_method,
        audio_input_path,
        audio_output_path,
        model_path,
        index_path,
        split_audio,
        f0_autotune,
        clean_audio,
        clean_strength,
        export_format,
        embedder_model,
        embedder_model_custom,
        upscale_audio,
        f0_file,
    ):
        """
        Main inference pipeline for voice conversion.

        Args:
            f0_up_key: Pitch shift value.
            filter_radius: Filter radius for F0 smoothing.
            index_rate: Speaker embedding retrieval rate.
            rms_mix_rate: RMS mixing ratio.
            protect: Pitch protection level.
            hop_length: Hop length for F0 estimation.
            f0_method: F0 estimation method.
            audio_input_path: Input audio file path.
            audio_output_path: Output audio file path.
            model_path: Model weight file path.
            index_path: FAISS index file path.
            split_audio: Whether to split audio.
            f0_autotune: Whether to apply autotune.
            clean_audio: Whether to apply noise reduction.
            clean_strength: Noise reduction strength.
            export_format: Output audio format.
            embedder_model: Embedder model path.
            embedder_model_custom: Custom embedder model path.
            upscale_audio: Whether to upscale audio.
        """
        self.get_vc(model_path, 0)

        try:
            start_time = time.time()
            print(f"Converting audio '{audio_input_path}'...")
            # if upscale_audio == "True":
            #     upscale(audio_input_path, audio_input_path)

            self.voice_conversion(
                sid=0,
                input_audio_path=audio_input_path,
                f0_up_key=f0_up_key,
                f0_file=f0_file,
                f0_method=f0_method,
                file_index=index_path,
                index_rate=float(index_rate),
                rms_mix_rate=float(rms_mix_rate),
                protect=float(protect),
                hop_length=hop_length,
                output_path=audio_output_path,
                split_audio=split_audio,
                f0_autotune=f0_autotune,
                filter_radius=filter_radius,
                embedder_model=embedder_model,
                embedder_model_custom=embedder_model_custom,
            )

            if clean_audio == "True":
                cleaned_audio = self.remove_audio_noise(
                    audio_output_path, clean_strength
                )
                if cleaned_audio is not None:
                    sf.write(
                        audio_output_path, cleaned_audio, self.tgt_sr, format="WAV"
                    )

            output_path_format = audio_output_path.replace(
                ".wav", f".{export_format.lower()}"
            )
            audio_output_path = self.convert_audio_format(
                audio_output_path, output_path_format, export_format
            )

            elapsed_time = time.time() - start_time
            print(
                f"Conversion completed at '{audio_output_path}' in {elapsed_time:.2f} seconds."
            )

        except Exception as error:
            print(f"Voice conversion failed: {error}")
