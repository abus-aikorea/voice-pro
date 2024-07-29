from enum import Enum
import urllib

import os
from typing import List
from urllib.parse import urlparse
import json5
import torch

from tqdm import tqdm

import structlog
logger = structlog.get_logger()

class UserConfig:
    def __init__(self, user_config_path):
        self.user_config_path = user_config_path
        self.default_user_config = {
            "whisper_core": "faster-whisper",
            "gradio_language": "Korean",
            "whisper_model_name": "medium",            
            "whisper_language": "korean",
            "word_timestamps": False,
            "denoise": False,
            "burn_subtitles": False,
            "video_quality": "best",
            "audio_format": "flac",
            "demucs_model": "htdemucs",
            "karaoke_mode": "Instrumental",
            "pitch_change": 0,
            "pitch_change_all": 0,
            "index_rate": 0.5,
            "filter_radius": 3,
            "rms_mix_rate": 0.25,
            "protect": 0.33,
            "main_vocal_gain": 0,
            "backup_vocal_gain": 0,
            "inst_gain": 0,
            "reverb_rm_size": 0.15,
            "reverb_wet": 0.2,
            "reverb_dry": 0.8,
            "reverb_damping": 0.7,
            "demixing_model": "htdemucs",
            "demixing_audio_format": "flac",
            "translate_language": "korean",
            "audio_source": "No Audio",
            "denoise_level" : 0,
            "whisper_compute_type" : 'default',
            "whisper_highlight_words" : False,
            "last_folder" : ".",     
            "xtts_language": "Korean",                                
            "xtts_voice": "",
            "xtts_rate": 1,
            "xtts_volume": 1,
            "xtts_pitch": 0,
            "tts_language": "English",
            "tts_voice": "UNITED STATES-Ana-Female",
            "tts_pitch": 0,
            "tts_rate": 0,
            "tts_volume": 0,
            "rvc_voice": "choi",
            "rvc_f0_up_key": 0,
            "rvc_filter_radius": 3,
            "rvc_index_rate": 0.3,
            "rvc_rms_mix_rate": 1,
            "rvc_protect": 0.23,
            "rvc_hop_length": 256,
            "rvc_clean_strength": 0.2,        
            }
        self.user_config = self.load_user_config()


    def load_user_config(self):
        try:
            with open(self.user_config_path, "r") as file:
                return json5.load(file)
        except Exception as e:
            logger.error(f"[config.py] load_user_config - Error transcribing file: {e}")
            return self.default_user_config

    def save_user_config(self):
        with open(self.user_config_path, "w") as file:
            json5.dump(self.user_config, file, indent=4)

    def get(self, key, default=None):
        value = self.user_config.get(key, default)
        if value != None:
            return value
        else:
            return self.default_user_config.get(key, key)

    def set(self, key, value):
        self.user_config[key] = value
        self.save_user_config()


class ModelConfig:
    def __init__(self, name: str, url: str, path: str = None, type: str = "whisper"):
        """
        Initialize a model configuration.

        name: Name of the model
        url: URL to download the model from
        path: Path to the model file. If not set, the model will be downloaded from the URL.
        type: Type of model. Can be whisper or huggingface.
        """
        self.name = name
        self.url = url
        self.path = path
        self.type = type

VAD_INITIAL_PROMPT_MODE_VALUES=["prepend_all_segments", "prepend_first_segment", "json_prompt_mode"]

class VadInitialPromptMode(Enum):
    PREPEND_ALL_SEGMENTS = 1
    PREPREND_FIRST_SEGMENT = 2
    JSON_PROMPT_MODE = 3

    @staticmethod
    def from_string(s: str):
        normalized = s.lower() if s is not None else None

        if normalized == "prepend_all_segments":
            return VadInitialPromptMode.PREPEND_ALL_SEGMENTS
        elif normalized == "prepend_first_segment":
            return VadInitialPromptMode.PREPREND_FIRST_SEGMENT
        elif normalized == "json_prompt_mode":
            return VadInitialPromptMode.JSON_PROMPT_MODE
        elif normalized is not None and normalized != "":
            raise ValueError(f"Invalid value for VadInitialPromptMode: {s}")
        else:
            return None

class ApplicationConfig:
    def __init__(self, models: List[ModelConfig] = [], input_audio_max_duration: int = 600, 
                 share: bool = False, server_name: str = None, server_port: int = 7870, 
                 queue_concurrency_count: int = 1, delete_uploaded_files: bool = True,
                 whisper_implementation: str = "whisper",
                 default_model_name: str = "medium", default_vad: str = "silero-vad", 
                 vad_parallel_devices: str = "", vad_cpu_cores: int = 1, vad_process_timeout: int = 1800, 
                 auto_parallel: bool = False, output_dir: str = None,
                 model_dir: str = None, device: str = None, 
                 verbose: bool = True, task: str = "transcribe", language: str = "Korean",
                 vad_initial_prompt_mode: str = "prepend_first_segment ", 
                 vad_merge_window: float = 5, vad_max_merge_size: float = 30,
                 vad_padding: float = 1, vad_prompt_window: float = 3,
                 temperature: float = 0, best_of: int = 5, beam_size: int = 5,
                 patience: float = None, length_penalty: float = None,
                 suppress_tokens: str = "-1", initial_prompt: str = None,
                 condition_on_previous_text: bool = True, fp16: bool = True,
                 compute_type: str = "float16", 
                 temperature_increment_on_fallback: float = 0.2, compression_ratio_threshold: float = 2.4,
                 logprob_threshold: float = -1.0, no_speech_threshold: float = 0.6,
                 # Word timestamp settings
                 word_timestamps: bool = False, prepend_punctuations: str = "\"\'“¿([{-",
                 append_punctuations: str = "\"\'.。,，!！?？:：”)]}、", 
                 highlight_words: bool = False,
            ):
        
        self.models = models
        
        # WebUI settings
        self.input_audio_max_duration = input_audio_max_duration
        self.share = share
        self.server_name = server_name
        self.server_port = server_port
        self.queue_concurrency_count = queue_concurrency_count
        self.delete_uploaded_files = delete_uploaded_files

        self.whisper_implementation = whisper_implementation
        self.default_model_name = default_model_name
        self.default_vad = default_vad
        self.vad_parallel_devices = vad_parallel_devices
        self.vad_cpu_cores = vad_cpu_cores
        self.vad_process_timeout = vad_process_timeout
        self.auto_parallel = auto_parallel
        self.output_dir = output_dir

        self.model_dir = model_dir
        self.device = device
        self.verbose = verbose
        self.task = task
        self.language = language
        self.vad_initial_prompt_mode = vad_initial_prompt_mode
        self.vad_merge_window = vad_merge_window
        self.vad_max_merge_size = vad_max_merge_size
        self.vad_padding = vad_padding
        self.vad_prompt_window = vad_prompt_window
        self.temperature = temperature
        self.best_of = best_of
        self.beam_size = beam_size
        self.patience = patience
        self.length_penalty = length_penalty
        self.suppress_tokens = suppress_tokens
        self.initial_prompt = initial_prompt
        self.condition_on_previous_text = condition_on_previous_text
        self.fp16 = fp16
        self.compute_type = compute_type
        self.temperature_increment_on_fallback = temperature_increment_on_fallback
        self.compression_ratio_threshold = compression_ratio_threshold
        self.logprob_threshold = logprob_threshold
        self.no_speech_threshold = no_speech_threshold
        
        # Word timestamp settings
        self.word_timestamps = word_timestamps
        self.prepend_punctuations = prepend_punctuations
        self.append_punctuations = append_punctuations
        self.highlight_words = highlight_words
        
        
    def get_model_names(self):
        return [ x.name for x in self.models ]

    def update(self, **new_values):
        result = ApplicationConfig(**self.__dict__)

        for key, value in new_values.items():
            setattr(result, key, value)
        return result

    @staticmethod
    def create_default(**kwargs):
        app_config = ApplicationConfig.parse_file(os.environ.get("WHISPER_WEBUI_CONFIG", "config.json5"))

        # Update with kwargs
        if len(kwargs) > 0:
            app_config = app_config.update(**kwargs)
        return app_config

    @staticmethod
    def parse_file(config_path: str):
        import json5

        with open(config_path, "r", encoding="utf-8") as f:
            # Load using json5
            data = json5.load(f)
            data_models = data.pop("models", [])

            models = [ ModelConfig(**x) for x in data_models ]

            return ApplicationConfig(models, **data)
