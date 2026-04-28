from src.config import UserConfig
from app.abus_path import *
from app.abus_genuine import *
from app.abus_files import *
from app.abus_ffmpeg import *
from app.abus_tts_cosyvoice import *
from app.abus_voice_celeb import *

import gradio as gr
from lingua import Language, LanguageDetectorBuilder

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()



class GradioCelebVoice:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        self.voice_manager = CelebVoiceManager()
        self.selected_language = "English"

    def gradio_languages(self):
        languages = self.voice_manager.languages()
        # logger.debug(f"[gradio_voice_celeb.py] gradio_languages: languages = {languages}")
        return languages
    
    def gradio_f5_languages(self):
        return ["English", "Chinese", "Japanese"]
    
    def gradio_change_language(self, lanugage):   
        self.selected_language = lanugage
        voice_names = self.voice_manager.voice_names(lanugage)

        if len(voice_names) > 0:
            return gr.update(choices=voice_names, value=voice_names[0])
        else:
            return gr.update(choices=voice_names, value=None)
        
    
    def gradio_voices(self):
        voice_names = self.voice_manager.voice_names(self.selected_language)
        return voice_names
    
    def gradio_change_voice(self, voice_name):
        celeb = self.voice_manager.find_voice(voice_name)
        if celeb:
            return celeb.audio_path(), celeb.transcript, celeb.image_path()
        else:
            return None, None, None
        
    def gradio_clear_voice(self):
        return None, None
        
