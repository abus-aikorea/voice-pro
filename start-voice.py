import argparse
import os
import sys
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from src.config import ApplicationConfig, UserConfig
from src.hf_models import hf_download_models
from app.abus_genuine import genuine_init, genuine_is_paid
from app.abus_app_voice import create_ui
from app.abus_path import path_workspace_folder, path_gradio_folder

# ABUS - start Gulliver
genuine_init()
hf_download_models(file_type='mdxnet-model', level=0)
hf_download_models(file_type='demucs', level=0)

path_workspace_folder()
path_gradio_folder()

config_filename = "config" + ("-paid" if genuine_is_paid() else "-free") + ".json5"
config_path = os.path.join(Path(__file__).resolve().parent, "app", config_filename)
default_app_config = ApplicationConfig.parse_file(config_path)       

user_config_path = os.path.join(Path(__file__).resolve().parent, "app", "config-user.json5")
user_config = UserConfig(user_config_path)

create_ui(app_config=default_app_config, user_config=user_config)