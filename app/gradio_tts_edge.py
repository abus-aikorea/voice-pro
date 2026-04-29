from src.config import UserConfig
from app.abus_path import *

from app.abus_voice_ms import *
from app.abus_tts_edge import *
from app.abus_tts_azure import *

# from app.abus_translate_deep import *
# from app.abus_translate_azure import *
from app.abus_genuine import *
from app.abus_files import *


import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()


class GradioEdgeTTS:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        
        self.voice_manager = MSVoiceManager(self.user_config.get('ms_language', "English"))
        self.tts = AzureTTS() if azure_text_api_working() else EdgeTTS()

            
    def gradio_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def gradio_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    
    def gradio_upload_file(self, file_obj):
        if file_obj is not None:
            text = self._read_file(gradio_file_path(file_obj))
            languageName = AbusText.detect_language_name(text[:200])
            return languageName, text
        return "English", "No file uploaded"   
            

    def gradio_edge_default(self):
        return [0, 0, 0, "mp3"]
    
    def gradio_tts_dubbing(self, text: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format: str = 'mp3'):
        self.user_config.set("edge_tts_pitch", semitones)     
        self.user_config.set("edge_tts_rate", speed_factor)
        self.user_config.set("edge_tts_volume", volume_factor)     
        self.user_config.set("audio_format", audio_format)
        
        logger.debug(f'[gradio_tts_edge.py] gradio_tts_dubbing - text = {text}, \
            voice_name = {voice_name}, semitones = {semitones}, speed_factor = {speed_factor}, volume_factor = {volume_factor}, audio_format = {audio_format}')

        input_text = text
        logger.debug(f"[gradio_tts_edge.py] gradio_tts_dubbing - input_text: {input_text}")   
              
        try:
            ms_voice = self.voice_manager.get_voice(voice_name)
            
            if ms_voice and input_text:
                aidub_audio_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{audio_format}"))
                self.tts.infer(input_text, aidub_audio_file, ms_voice.name, semitones, speed_factor, volume_factor, audio_format)
                return aidub_audio_file, aidub_audio_file
            else:
                message = i18n("Error")
                gr.Warning(message)
                return None, None            
        except Exception as e:
            logger.error(f"[gradio_tts_edge.py] gradio_tts_dubbing - error: {e}")
            gr.Warning(f'{e}')
            return None, None  
    
    def gradio_save(self, file_obj, target_lang, audio_format, text, audio_obj):
        logger.debug(f'[GradioEdgeTTS] gradio_save')
        message = i18n("Saving files...")
        gr.Info(message)
        
    
    def _read_file(self, filepath):    
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except UnicodeDecodeError:
            return "Error: The file is not a valid text file or uses an unsupported encoding."
        except IOError:
            return "Error: Unable to read the file."
