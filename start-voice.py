import argparse
import os
import sys
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Monkey-patch Gradio 5.x Progress.tqdm API change
# Gradio 5.14 Progress.tqdm() returns the Progress object itself instead of a
# wrapped iterable, causing 'NoneType object is not iterable' errors when
# iterating. Replace with standard tqdm so all existing code works.
import gradio as gr
from tqdm import tqdm

_original_progress_tqdm = gr.Progress.tqdm

def _patched_progress_tqdm(self, iterable=None, desc=None, total=None, unit="steps", _tqdm=None):
    if iterable is not None:
        return tqdm(iterable, desc=desc, total=total, unit=unit)
    return self

gr.Progress.tqdm = _patched_progress_tqdm


# Monkey-patch Gradio 5.x FileData validation to be more lenient.
# Some frontend versions or cached clients may send FileData payloads with
# missing/None meta fields, causing pydantic validation errors during upload.
# We inject the default meta when it's missing so uploads never break.
import gradio.data_classes as _gdc

_original_filedata_validate = _gdc.FileData.model_validate

@classmethod
def _patched_filedata_validate(cls, obj, *args, **kwargs):
    if isinstance(obj, dict) and obj.get("meta") is None:
        obj = dict(obj)
        obj["meta"] = {"_type": "gradio.FileData"}
    return _original_filedata_validate(obj, *args, **kwargs)

_gdc.FileData.model_validate = _patched_filedata_validate


# Monkey-patch torchaudio.AudioMetaData for pyannote.audio compatibility.
# In some torchaudio builds (especially CPU wheels), AudioMetaData is not
# re-exported at the top level. pyannote.audio expects it there.
try:
    import torchaudio
    if not hasattr(torchaudio, 'AudioMetaData'):
        from torchaudio.backend.common import AudioMetaData
        torchaudio.AudioMetaData = AudioMetaData
except Exception:
    pass


from src.config import UserConfig
from app.abus_hf import AbusHuggingFace
from app.abus_genuine import genuine_init
from app.abus_app_voice import create_ui
from app.abus_path import path_workspace_folder, path_gradio_folder

# ABUS - start voice
genuine_init()
AbusHuggingFace.initialize(app_name="voice")

# AbusHuggingFace.hf_download_models(file_type='mdxnet-model', level=0)
AbusHuggingFace.hf_download_models(file_type='demucs', level=0)
# AbusHuggingFace.hf_download_models(file_type='f5-tts', level=0)
# AbusHuggingFace.hf_download_models(file_type='vocos-mel-24khz', level=0)
# AbusHuggingFace.hf_download_models(file_type='rvc-model', level=0)
# AbusHuggingFace.hf_download_models(file_type='rvc-voice', level=0)
AbusHuggingFace.hf_download_models(file_type='edge-tts', level=0)
AbusHuggingFace.hf_download_models(file_type='kokoro', level=0)
AbusHuggingFace.hf_download_models(file_type='cosyvoice', level=0)

path_workspace_folder()
path_gradio_folder()


user_config_path = os.path.join(Path(__file__).resolve().parent, "app", "config-user.json5")
user_config = UserConfig(user_config_path)

create_ui(user_config=user_config)