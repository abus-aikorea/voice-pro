import gc
import hashlib
import os
import queue
import threading
import warnings

import librosa
import numpy as np
import onnxruntime as ort
import soundfile as sf
import torch
from tqdm import tqdm

# UI
import gradio as gr

import structlog
logger = structlog.get_logger()


warnings.filterwarnings("ignore")
stem_naming = {'Vocals': 'Instrumental', 'Other': 'Instruments', 'Instrumental': 'Vocals', 'Drums': 'Drumless', 'Bass': 'Bassless'}

DEFAULT_SR = 48000


class MDXModel:
    def __init__(self, device, dim_f, dim_t, n_fft, hop=1024, stem_name=None, compensation=1.000):
        self.dim_f = dim_f
        self.dim_t = dim_t
        self.dim_c = 4
        self.n_fft = n_fft
        self.hop = hop
        self.stem_name = stem_name
        self.compensation = compensation

        self.n_bins = self.n_fft // 2 + 1
        self.chunk_size = hop * (self.dim_t - 1)
        self.window = torch.hann_window(window_length=self.n_fft, periodic=True).to(device)

        out_c = self.dim_c

        self.freq_pad = torch.zeros([1, out_c, self.n_bins - self.dim_f, self.dim_t]).to(device)

    def stft(self, x):
        x = x.reshape([-1, self.chunk_size])
        x = torch.stft(x, n_fft=self.n_fft, hop_length=self.hop, window=self.window, center=True, return_complex=True)
        x = torch.view_as_real(x)
        x = x.permute([0, 3, 1, 2])
        x = x.reshape([-1, 2, 2, self.n_bins, self.dim_t]).reshape([-1, 4, self.n_bins, self.dim_t])
        return x[:, :, :self.dim_f]

    def istft(self, x, freq_pad=None):
        freq_pad = self.freq_pad.repeat([x.shape[0], 1, 1, 1]) if freq_pad is None else freq_pad
        x = torch.cat([x, freq_pad], -2)
        # c = 4*2 if self.target_name=='*' else 2
        x = x.reshape([-1, 2, 2, self.n_bins, self.dim_t]).reshape([-1, 2, self.n_bins, self.dim_t])
        x = x.permute([0, 2, 3, 1])
        x = x.contiguous()
        x = torch.view_as_complex(x)
        x = torch.istft(x, n_fft=self.n_fft, hop_length=self.hop, window=self.window, center=True)
        return x.reshape([-1, 2, self.chunk_size])


class MDX:
    # Unit: seconds
    DEFAULT_CHUNK_SIZE = 0 * DEFAULT_SR
    DEFAULT_MARGIN_SIZE = 1 * DEFAULT_SR

    def __init__(self, model_path: str, params: MDXModel):

        # Set the device and the provider (CPU or CUDA)
        self.device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
        # self.provider = ['CUDAExecutionProvider'] if processor >= 0 else ['CPUExecutionProvider']

        self.model = params

        # Load the ONNX model using ONNX Runtime
        # self.ort = ort.InferenceSession(model_path, providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
        
        if 'CUDAExecutionProvider' in ort.get_available_providers():
            # providers = [("CUDAExecutionProvider", {"device_id": torch.cuda.current_device(),
            #                                         "user_compute_stream": str(torch.cuda.current_stream().cuda_stream)})]
            # sess_options = ort.SessionOptions()
            # self.ort = ort.InferenceSession(model_path, sess_options=sess_options, providers=providers)             

            sess_options = ort.SessionOptions()
            sess_options.log_severity_level = 3
            sess_options.inter_op_num_threads = 1
            sess_options.intra_op_num_threads = 1            
            self.ort = ort.InferenceSession(model_path, sess_options=sess_options, providers=['CUDAExecutionProvider'])
        else:
            sess_options = ort.SessionOptions()
            sess_options.log_severity_level = 3
            sess_options.inter_op_num_threads = 1
            sess_options.intra_op_num_threads = 1            
            self.ort = ort.InferenceSession(model_path, sess_options=sess_options, providers=['CPUExecutionProvider'])
                
        logger.debug(f'MDX onnx device is {ort.get_device()}')
        # Preload the model for faster performance
        self.ort.run(None, {'input': torch.rand(1, 4, params.dim_f, params.dim_t).numpy()})
        self.process = lambda spec: self.ort.run(None, {'input': spec.cpu().numpy()})[0]

        self.prog = None


    @staticmethod
    def get_hash(model_path):
        try:
            with open(model_path, 'rb') as f:
                f.seek(- 10000 * 1024, 2)
                model_hash = hashlib.md5(f.read()).hexdigest()
        except:
            model_hash = hashlib.md5(open(model_path, 'rb').read()).hexdigest()

        return model_hash

    @staticmethod
    def segment(wave, combine=True, chunk_size=DEFAULT_CHUNK_SIZE, margin_size=DEFAULT_MARGIN_SIZE):
        """
        Segment or join segmented wave array

        Args:
            wave: (np.array) Wave array to be segmented or joined
            combine: (bool) If True, combines segmented wave array. If False, segments wave array.
            chunk_size: (int) Size of each segment (in samples)
            margin_size: (int) Size of margin between segments (in samples)

        Returns:
            numpy array: Segmented or joined wave array
        """

        if combine:
            processed_wave = None  # Initializing as None instead of [] for later numpy array concatenation
            for segment_count, segment in enumerate(wave):
                start = 0 if segment_count == 0 else margin_size
                end = None if segment_count == len(wave) - 1 else -margin_size
                if margin_size == 0:
                    end = None
                if processed_wave is None:  # Create array for first segment
                    processed_wave = segment[:, start:end]
                else:  # Concatenate to existing array for subsequent segments
                    processed_wave = np.concatenate((processed_wave, segment[:, start:end]), axis=-1)

        else:
            processed_wave = []
            sample_count = wave.shape[-1]

            if chunk_size <= 0 or chunk_size > sample_count:
                chunk_size = sample_count

            if margin_size > chunk_size:
                margin_size = chunk_size

            for segment_count, skip in enumerate(range(0, sample_count, chunk_size)):

                margin = 0 if segment_count == 0 else margin_size
                end = min(skip + chunk_size + margin_size, sample_count)
                start = skip - margin

                cut = wave[:, start:end].copy()
                processed_wave.append(cut)

                if end == sample_count:
                    break

        return processed_wave

    def pad_wave(self, wave):
        """
        Pad the wave array to match the required chunk size

        Args:
            wave: (np.array) Wave array to be padded

        Returns:
            tuple: (padded_wave, pad, trim)
                - padded_wave: Padded wave array
                - pad: Number of samples that were padded
                - trim: Number of samples that were trimmed
        """
        n_sample = wave.shape[1]
        trim = self.model.n_fft // 2
        gen_size = self.model.chunk_size - 2 * trim
        pad = gen_size - n_sample % gen_size

        # Padded wave
        wave_p = np.concatenate((np.zeros((2, trim)), wave, np.zeros((2, pad)), np.zeros((2, trim))), 1)

        mix_waves = []
        for i in range(0, n_sample + pad, gen_size):
            waves = np.array(wave_p[:, i:i + self.model.chunk_size])
            mix_waves.append(waves)

        mix_waves = torch.tensor(mix_waves, dtype=torch.float32).to(self.device)

        return mix_waves, pad, trim

    def _process_wave(self, mix_waves, trim, pad, q: queue.Queue, _id: int):
        """
        Process each wave segment in a multi-threaded environment

        Args:
            mix_waves: (torch.Tensor) Wave segments to be processed
            trim: (int) Number of samples trimmed during padding
            pad: (int) Number of samples padded during padding
            q: (queue.Queue) Queue to hold the processed wave segments
            _id: (int) Identifier of the processed wave segment

        Returns:
            numpy array: Processed wave segment
        """
        
        progress=gr.Progress()
        mix_waves = mix_waves.split(1)
        with torch.no_grad():
            pw = []
            for mix_wave in progress.tqdm(mix_waves, desc="MDX-Net"):
                # self.prog.update()
                spec = self.model.stft(mix_wave)
                processed_spec = torch.tensor(self.process(spec))
                processed_wav = self.model.istft(processed_spec.to(self.device))
                processed_wav = processed_wav[:, :, trim:-trim].transpose(0, 1).reshape(2, -1).cpu().numpy()
                pw.append(processed_wav)
        processed_signal = np.concatenate(pw, axis=-1)[:, :-pad]
        q.put({_id: processed_signal})
        return processed_signal

    def process_wave(self, wave: np.array, mt_threads=1):
        """
        Process the wave array in a multi-threaded environment

        Args:
            wave: (np.array) Wave array to be processed
            mt_threads: (int) Number of threads to be used for processing

        Returns:
            numpy array: Processed wave array
        """
        # self.prog = progress.tqdm(total=0)
        chunk = wave.shape[-1] // mt_threads
        waves = self.segment(wave, False, chunk)

        # Create a queue to hold the processed wave segments
        q = queue.Queue()
        threads = []
        for c, batch in enumerate(waves):
            mix_waves, pad, trim = self.pad_wave(batch)
            self._process_wave(mix_waves, trim, pad, q, c)
            # self.prog.total = len(mix_waves) * mt_threads
        #     thread = threading.Thread(target=self._process_wave, args=(mix_waves, trim, pad, q, c))
        #     thread.start()
        #     threads.append(thread)
        # for thread in threads:
        #     thread.join()
        # self.prog.close()

        processed_batches = []
        while not q.empty():
            processed_batches.append(q.get())
        processed_batches = [list(wave.values())[0] for wave in
                             sorted(processed_batches, key=lambda d: list(d.keys())[0])]
        assert len(processed_batches) == len(waves), 'Incomplete processed batches, please reduce batch size!'
        return self.segment(processed_batches, True, chunk)
