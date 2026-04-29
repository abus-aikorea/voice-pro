from src.config import UserConfig
from app.abus_path import *
from app.abus_genuine import *
from app.abus_files import *
from app.abus_ffmpeg import *
from app.abus_tts_cosyvoice import *


import gradio as gr

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()



class GradioCosyVoice:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        
        self.tts = CosyVoiceInference()


            
    def gradio_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def gradio_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    
    def gradio_upload_file(self, file_obj):
        if file_obj is not None:
            text = self._read_file(gradio_file_path(file_obj))
            return text
        return "No file uploaded"   
    
    
    def gradio_cosy_default(self):
        return ["Zero-Shot", 1.0, "mp3"]
        
    
    def gradio_tts_dubbing_single(self, dubbing_text:str, celeb_audio, celeb_transcript, model_choice, speed_factor, audio_format: str):
        if not (dubbing_text and dubbing_text.strip()):
            message = i18n("Input error")
            gr.Warning(message)
            return None, None           

        input_text = dubbing_text
        logger.debug(f"[gradio_tts_cosyvoice.py] gradio_tts_dubbing_single - input_text: {input_text}")    
        
        try:
            dubbing_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{audio_format}"))
            self.tts.infer_single(input_text.strip(), dubbing_file, celeb_audio, celeb_transcript, model_choice, speed_factor, audio_format)
            return dubbing_file, dubbing_file
        except Exception as e:
            logger.error(f"[gradio_tts_cosyvoice.py] gradio_tts_dubbing_single - error: {e}")
            gr.Warning(f'{e}')
            return None, None            

   
    def _read_file(self, filepath):    
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except UnicodeDecodeError:
            return "Error: The file is not a valid text file or uses an unsupported encoding."
        except IOError:
            return "Error: Unable to read the file."
           
        

