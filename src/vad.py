# original: https://github.com/snakers4/silero-vad/blob/master/utils_vad.py

import os
import subprocess
import torch
import numpy as np
import onnxruntime


import structlog
logger = structlog.get_logger()


class VoiceActivityDetection():

    def __init__(self, force_onnx_cpu=True):
        path = os.path.join(os.getcwd(), 'model', 'vad', 'silero_vad.onnx')


        opts = onnxruntime.SessionOptions()
        opts.log_severity_level = 3

        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = 1

        if force_onnx_cpu and 'CPUExecutionProvider' in onnxruntime.get_available_providers():
            self.session = onnxruntime.InferenceSession(path, providers=['CPUExecutionProvider'], sess_options=opts)
        else:
            self.session = onnxruntime.InferenceSession(path, providers=['CUDAExecutionProvider'], sess_options=opts)

        self.reset_states()
        self.sample_rates = [8000, 16000]

    def _validate_input(self, x, sr: int):
        if x.dim() == 1:
            x = x.unsqueeze(0)
        if x.dim() > 2:
            raise ValueError(f"Too many dimensions for input audio chunk {x.dim()}")

        if sr != 16000 and (sr % 16000 == 0):
            step = sr // 16000
            x = x[:, ::step]
            sr = 16000

        if sr not in self.sample_rates:
            raise ValueError(f"Supported sampling rates: {self.sample_rates} (or multiply of 16000)")

        if sr / x.shape[1] > 31.25:
            raise ValueError(f"Input audio chunk is too short dim={x.dim()}, shape={x.shape}")

        return x, sr

    def reset_states(self, batch_size=1):
        self._h = np.zeros((2, batch_size, 64)).astype('float32')
        self._c = np.zeros((2, batch_size, 64)).astype('float32')
        self._last_sr = 0
        self._last_batch_size = 0

    def __call__(self, x, sr: int):

        x, sr = self._validate_input(x, sr)
        batch_size = x.shape[0]

        if not self._last_batch_size:
            self.reset_states(batch_size)
        if (self._last_sr) and (self._last_sr != sr):
            self.reset_states(batch_size)
        if (self._last_batch_size) and (self._last_batch_size != batch_size):
            self.reset_states(batch_size)

        if sr in [8000, 16000]:
            ort_inputs = {'input': x.numpy(), 'h': self._h, 'c': self._c, 'sr': np.array(sr, dtype='int64')}
            ort_outs = self.session.run(None, ort_inputs)
            out, self._h, self._c = ort_outs
        else:
            raise ValueError()

        self._last_sr = sr
        self._last_batch_size = batch_size

        out = torch.tensor(out)
        return out

    def audio_forward(self, x, sr: int, num_samples: int = 512):
        outs = []
        x, sr = self._validate_input(x, sr)

        if x.shape[1] % num_samples:
            pad_num = num_samples - (x.shape[1] % num_samples)
            x = torch.nn.functional.pad(x, (0, pad_num), 'constant', value=0.0)

        self.reset_states(x.shape[0])
        for i in range(0, x.shape[1], num_samples):
            wavs_batch = x[:, i:i+num_samples]
            out_chunk = self.__call__(wavs_batch, sr)
            outs.append(out_chunk)

        stacked = torch.cat(outs, dim=1)
        return stacked.cpu()

    @staticmethod
    def download(model_url="https://github.com/snakers4/silero-vad/blob/master/files/silero_vad.onnx"):
        target_dir = os.path.expanduser("~/.cache/whisper-live/")

        # Ensure the target directory exists
        os.makedirs(target_dir, exist_ok=True)

        # Define the target file path
        model_filename = os.path.join(target_dir, "silero_vad.onnx")

        # Check if the model file already exists
        if not os.path.exists(model_filename):
            # If it doesn't exist, download the model using wget
            try:
                print("Start to download the model using wget.")
                subprocess.run(["wget", "-O", model_filename, model_url], check=True)
            except subprocess.CalledProcessError:
                print("Failed to download the model using wget.")
        return model_filename


class VoiceActivityDetector:
    def __init__(self, threshold=0.5, frame_rate=16000):
        """
        Initializes the VoiceActivityDetector with a voice activity detection model and a threshold.

        Args:
            threshold (float, optional): The probability threshold for detecting voice activity. Defaults to 0.5.
        """
        self.model = VoiceActivityDetection()
        self.threshold = threshold
        self.frame_rate = frame_rate

    def __call__(self, audio_frame):
        """
        Determines if the given audio frame contains speech by comparing the detected speech probability against
        the threshold.

        Args:
            audio_frame (np.ndarray): The audio frame to be analyzed for voice activity. It is expected to be a
                                      NumPy array of audio samples.

        Returns:
            bool: True if the speech probability exceeds the threshold, indicating the presence of voice activity;
                  False otherwise.
        """
        speech_prob = self.model(torch.from_numpy(audio_frame), self.frame_rate).item()
        # logger.debug(f'[VAD] speech_prob = {speech_prob}')
        # return speech_prob > self.threshold
        return speech_prob
