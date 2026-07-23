import time
import pysubs2
import re
import unicodedata
import string

from pydub import AudioSegment
from pydub.silence import detect_leading_silence
import numpy as np
import gradio as gr

from app.abus_path import *
from app.abus_ffmpeg import *

import structlog
logger = structlog.get_logger()

from app.abus_genuine import *
from app.abus_voice_ms import *
from app.abus_tts_edge import *
from app.abus_tts_azure import *
from app.abus_translate_deep import *
from app.abus_translate_azure import *
from app.abus_rvc import *
from app.abus_text import *
from app.abus_audio import *


class TTSRVC:
    def __init__(self):
        self.tts = AzureTTS() if azure_text_api_working() == True else EdgeTTS()
        self.rvc = RVC()
        self.translator = AzureTranslator() if azure_text_api_working() == True else DeepTranslator()
    
    
    
    def get_voices(self):
        return self.rvc.get_voices()
    
    def get_languages(self) -> list:
        return self.translator.get_languages()      
    
    def get_language_value(self, languageName: str):
        return self.translator.get_language_value(languageName)    
    
        
    def srt_to_voice(self, subtitle_file: str, tts_voice: str, semitones, speed_factor, volume_factor, audio_format, rvc_voice, progress=gr.Progress()):
        logger.debug(f"[abus_tts_rvc.py] srt_to_voice - subtitle_file: {subtitle_file}")
        tts_audio_file = path_add_postfix(subtitle_file, f"-{tts_voice}", f".{audio_format}")
        rvc_audio_file = path_add_postfix(subtitle_file, f"-{tts_voice}-{rvc_voice}", f".{audio_format}")        
        rvc_subtitle_file = path_add_postfix(subtitle_file, f"-{tts_voice}-{rvc_voice}", ".srt")
        
        tts_segments_folder = path_tts_segments_folder(subtitle_file)   
        rvc_segments_folder = path_rvc_segments_folder(subtitle_file)      

        combined_tts_audio = AudioSegment.empty()
        combined_rvc_audio = AudioSegment.empty()

        full_subs = pysubs2.load(subtitle_file, encoding="utf-8")
        subs = full_subs
        
        for i in progress.tqdm(range(len(subs)), desc='Generating...'):
            line = subs[i]
            next_line = subs[i+1] if i < len(subs)-1 else None

            if i == 0:
                silence = AudioSegment.silent(duration=line.start)
                combined_tts_audio += silence
                combined_rvc_audio += silence

            tts_segment_file = os.path.join(tts_segments_folder, f'tts_{i+1:06}.{audio_format}')    
            if False == self.tts.line_to_voice(line.text, tts_segment_file, tts_voice, semitones, speed_factor, volume_factor, audio_format):
                silence = AudioSegment.silent(duration=next_line.start-line.start)
                combined_tts_audio += silence
                combined_rvc_audio += silence
                continue
            
            rvc_segment_file = os.path.join(rvc_segments_folder, f'rvc_{i+1:06}.{audio_format}')    
            self.rvc.simple_inference(tts_segment_file, rvc_segment_file, rvc_voice, audio_format)
            
            combined_tts_audio += AudioSegment.from_file(tts_segment_file)
            combined_rvc_audio += AudioSegment.from_file(rvc_segment_file)
            
            line.end = len(combined_rvc_audio)
            
            if next_line and len(combined_rvc_audio) < next_line.start:
                silence_length = next_line.start - len(combined_rvc_audio)
                silence = AudioSegment.silent(duration=silence_length)
                combined_tts_audio += silence
                combined_rvc_audio += silence
            elif next_line:
                AbusAudio.move_subtitle_start_preserve_duration(next_line, len(combined_rvc_audio))

        combined_tts_audio.export(tts_audio_file, format=audio_format)
        combined_rvc_audio.export(rvc_audio_file, format=audio_format)     
        subs.save(rvc_subtitle_file)
        
        return tts_audio_file, rvc_audio_file
        
    
    
    def text_to_voice(self, text, tts_voice: str, semitones, speed_factor, volume_factor,  audio_format, rvc_voice, progress=gr.Progress()):
        logger.debug(f"[abus_tts_rvc.py] text_to_voice - text: {text}")
        tts_audio_file = os.path.join(path_dubbing_folder(), path_new_filename(ext = f".{audio_format}"))
        rvc_audio_file = path_add_postfix(tts_audio_file, f"-{rvc_voice}", f".{audio_format}") 
              
        self.tts.text_to_voice(text.strip(), tts_audio_file, tts_voice, semitones, speed_factor, volume_factor, audio_format, progress)
        self.rvc.simple_inference(tts_audio_file, rvc_audio_file, rvc_voice, audio_format)    
    
        return tts_audio_file, rvc_audio_file

    
    
    def infer(self, text, tts_voice: str, semitones, speed_factor, volume_factor,  audio_format, rvc_voice, progress=gr.Progress()):
        subtitle_file = None
        if AbusText.is_subtitle_format(text):
            subs = pysubs2.SSAFile.from_string(text)
            subtitle_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{subs.format}"))
            subs.save(subtitle_file)
            
        if subtitle_file:    
            tts_audio_file, rvc_audio_file = self.srt_to_voice(subtitle_file, tts_voice, semitones, speed_factor, volume_factor, audio_format, rvc_voice, progress)
            return tts_audio_file, rvc_audio_file
        else:
            tts_audio_file, rvc_audio_file = self.text_to_voice(text, tts_voice, semitones, speed_factor, volume_factor,  audio_format, rvc_voice, progress)
            return tts_audio_file, rvc_audio_file
         
