import os
import subprocess
import sys

from app.abus_ffmpeg import *
from app.abus_path import *
from app.abus_downloader import *


import structlog
logger = structlog.get_logger()



# step1. split to wav / step2. convert to flac,mp3 ...
def demucs_split_file(input_path: str, output_dir, demucs_model: str, audio_format: str, progress = gr.Progress()):
    temp_directory = os.path.join(path_workspace_folder(), "demucs")
    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory, exist_ok=True)
        
    output_option = "--float32"        
    file_name = os.path.splitext(os.path.basename(input_path))[0]  
    
    logger.debug(f'temp_directory: {temp_directory}')
    logger.debug(f'demucs_model: {demucs_model}')
    logger.debug(f'file_name: {file_name}')
    logger.debug(f'audio_format: {audio_format}')
    
    demucs_inst_file = os.path.join(temp_directory, demucs_model, file_name, "no_vocals.wav")
    demucs_vocal_file = os.path.join(temp_directory, demucs_model, file_name, "vocals.wav")

    command = f'{sys.executable} -m demucs.separate -n {demucs_model} --two-stems=vocals "{input_path}" -o "{temp_directory}" {output_option}'
    command += f' --repo model/demucs'
    logger.debug(f'[abus:demucs_split_file] {command}')
    
    with subprocess.Popen(command, text=True, shell=True, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True) as sp:
        for line in sp.stderr:
            print(f'{line}', end='', flush=True)
            tokens = [item for item in line.split("%|") if item]
            if len(tokens) < 2:
                continue
            progress(float(tokens[0]) / 100.0, desc="Demucs")
            
            
    inst_audio_file = os.path.join(output_dir, file_name + f"_{demucs_model}_inst." + audio_format)
    vocal_audio_file = os.path.join(output_dir, file_name + f"_{demucs_model}_vocal." + audio_format)
    
    ffmpeg_convert_audio(demucs_inst_file, inst_audio_file, audio_format)
    ffmpeg_convert_audio(demucs_vocal_file, vocal_audio_file, audio_format)
    os.remove(demucs_inst_file)
    os.remove(demucs_vocal_file)

    return inst_audio_file, vocal_audio_file

