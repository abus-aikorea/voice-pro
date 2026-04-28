from src.config import UserConfig
from app.abus_path import *
from app.abus_genuine import *
from app.abus_files import *
from app.abus_ffmpeg import *

# from app.abus_tts_cosyvoice import *
# from app.abus_voice_celeb import *
# from app.abus_voice_ms import *
from app.abus_voice_kokoro import *

import gradio as gr
from lingua import Language, LanguageDetectorBuilder

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()



class GradioKokoroVoice:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        self.voice_manager = KokoroVoiceManager()
        self.selected_language = "American English"

                
    def gradio_languages(self):
        languages = self.voice_manager.languages()
        # logger.debug(f"[gradio_voice_kokoro.py] gradio_languages: languages = {languages}")
        return languages
    
    def gradio_change_language(self, lanugage):       
        self.selected_language = lanugage        
        
        voice_list = self.voice_manager.voice_list(lanugage)
        display_names = [voice.display_name for voice in voice_list]
        
        if len(display_names) > 0:        
            return gr.update(choices=display_names, value=display_names[0])
        else:
            return gr.update(choices=display_names, value=None)
    
    def gradio_voices(self):
        voice_list = self.voice_manager.voice_list(self.selected_language)
        display_names = [voice.display_name for voice in voice_list]
        # logger.debug(f"[gradio_voice_kokoro.py] gradio_voices: display_names = {display_names}")
        return display_names    
    
    def gradio_change_voice(self, voice_name):
        kokoro_voice = self.voice_manager.find_voice(self.selected_language, voice_name)
        if kokoro_voice:
            return kokoro_voice.audio_path(), kokoro_voice.transcript
        else:
            return None, None
        
