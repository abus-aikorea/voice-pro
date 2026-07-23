import os
import platform


import pysubs2
import re
import unicodedata

from pydub import AudioSegment
from pydub.silence import detect_leading_silence
import gradio as gr

from kokoro import KPipeline
import soundfile as sf

from app.abus_genuine import *
from app.abus_path import *
from app.abus_ffmpeg import *
from app.abus_voice_kokoro import *
from app.abus_text import *
from app.abus_nlp_spacy import *
from app.abus_audio import *

from phonemizer.backend.espeak.wrapper import EspeakWrapper


import structlog
logger = structlog.get_logger()


class KokoroTTS:
    def __init__(self):      
        self.set_environment()        
       
       
    @staticmethod
    def set_environment():
        system = platform.system()
        if system != "Windows":
            return
        
        # program_files = os.environ.get('PROGRAMFILES')
        # libespeak_ng_path = os.path.join(program_files, "eSpeak NG", "libespeak-ng.dll")

        espeak_path = os.path.join(path_model_folder(), "kokoro", "eSpeak NG")
        libespeak_ng_path = os.path.join(path_model_folder(), "kokoro", "eSpeak NG", "libespeak-ng.dll")
        espeak_ng_data_path = os.path.join(path_model_folder(), "kokoro", "eSpeak NG", "espeak-ng-data")
        espeak_ng_exe_path = os.path.join(path_model_folder(), "kokoro", "eSpeak NG", "espeak-ng.exe")
                
        user_path = os.environ.get('PATH', '')
        if espeak_path not in user_path:
            new_path = f"{user_path};{espeak_path}"
            os.environ['PATH'] = new_path
            logger.debug(f"[abus_tts_kokoro.py] set_environment - PATH에 다음 경로가 추가되었습니다: {espeak_path}")
            
            # 사용자 환경변수에 영구 저장
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path)
            winreg.CloseKey(key)               
        
        os.environ['PHONEMIZER_ESPEAK_LIBRARY'] = libespeak_ng_path        
        os.environ['PHONEMIZER_ESPEAK_PATH'] = espeak_ng_exe_path
        
        EspeakWrapper.set_library(libespeak_ng_path)
        EspeakWrapper.set_data_path(espeak_ng_data_path) # or './espeak-ng-data' 
         


    
    def request_tts(self, line: str, output_file: str, kokoro_voice, speed_factor, audio_format):
        output_voice_file = os.path.join(path_dubbing_folder(), path_new_filename(ext = f".{audio_format}"))
        line = AbusText.normalize_text(line)
        if len(line) < 1:
            logger.warning(f"[abus_tts_kokoro.py] request_tts - error: no line")
            return False
        
        # logger.debug(f'[abus_tts_kokoro.py] request_tts - line = {line}, kokoro_voice = {kokoro_voice}')
        
        try:
            pipeline = KPipeline(lang_code=kokoro_voice.lang_code)
        except Exception as e:
            logger.error(f"[abus_tts_kokoro.py] request_tts - Failed to initialize KPipeline: {e}")
            return False
                
        # pipeline = KPipeline(lang_code=kokoro_voice.lang_code)
        # logger.debug(f'[abus_tts_kokoro.py] request_tts - pipeline = {pipeline}')
        
        generator = pipeline(
            line, 
            voice=kokoro_voice.voice_code,
            speed=speed_factor, 
            split_pattern=None
        )
        
        # logger.debug(f'[abus_tts_kokoro.py] request_tts - generator = {generator}')
        
        for i, (gs, ps, audio) in enumerate(generator):
            # print(i)  # i => index
            # print(gs) # gs => graphemes/text
            # print(ps) # ps => phonemes
            sf.write(output_voice_file, audio, 24000)
            break
                
        # logger.debug(f'[abus_tts_kokoro.py] request_tts - output_voice_file = {output_voice_file}')
        
        trimed_voice_file = path_add_postfix(output_voice_file, "_trimed")
        AbusAudio.trim_silence_file(output_voice_file, trimed_voice_file)
        
        ffmpeg_to_stereo(trimed_voice_file, output_file)
        
        try:
            os.remove(output_voice_file)
            os.remove(trimed_voice_file)
        except Exception as e:
            logger.error(f"[abus_tts_kokoro.py] request_tts - error: {e}")
            return False
        
        return True
    
    
    def srt_to_voice(self, subtitle_file: str, output_file: str, kokoro_voice, speed_factor, audio_format, progress=gr.Progress()):
        tts_subtitle_file = path_add_postfix(subtitle_file, f"-{kokoro_voice.display_name}", ".srt")
        
        # AbusText.process_subtitle_for_tts(subtitle_file, tts_subtitle_file)
        AbusSpacy.process_subtitle_for_tts(subtitle_file, tts_subtitle_file)
        

        segments_folder = path_tts_segments_folder(subtitle_file)
        full_subs = pysubs2.load(tts_subtitle_file, encoding="utf-8")
        subs = full_subs
        
        combined_audio = AudioSegment.empty()
        for i in progress.tqdm(range(len(subs)), desc='Generating...'):
            line = subs[i]
            next_line = subs[i+1] if i < len(subs)-1 else None
            
            if i == 0:
                silence = AudioSegment.silent(duration=line.start)
                combined_audio += silence   

            tts_segment_file = os.path.join(segments_folder, f'tts_{i+1}.{audio_format}')
            tts_result = self.request_tts(line.text, tts_segment_file, kokoro_voice, speed_factor, audio_format)

            if tts_result == False:
                if next_line:
                    silence = AudioSegment.silent(duration=next_line.start-line.start)
                    combined_audio += silence
                continue        
            
            combined_audio += AudioSegment.from_file(tts_segment_file)

            if next_line and len(combined_audio) < next_line.start:
                silence_length = next_line.start - len(combined_audio)
                silence = AudioSegment.silent(duration=silence_length)
                combined_audio += silence
            elif next_line:
                AbusAudio.move_subtitle_start_preserve_duration(next_line, len(combined_audio))
                
        combined_audio.export(output_file, format=audio_format)                 
        cmd_delete_file(tts_subtitle_file)    
        
    
    def text_to_voice(self, text: str, output_file: str, kokoro_voice, speed_factor, audio_format, progress=gr.Progress()):
        segments_folder = path_tts_segments_folder(output_file)  
        
        use_punctuation = AbusText.has_punctuation_marks(text)
        lines = AbusText.split_into_sentences(text, use_punctuation)
        lines = lines
        
        combined_audio = AudioSegment.empty() 
        for i in progress.tqdm(range(len(lines)), desc='Generating...'):
            tts_segment_file = os.path.join(segments_folder, f'tts_{i+1:06}.{audio_format}')    
            tts_result = self.request_tts(lines[i], tts_segment_file, kokoro_voice, speed_factor, audio_format)
            if tts_result == False:
                continue
            combined_audio += AudioSegment.from_file(tts_segment_file)
            
        combined_audio.export(output_file, format=audio_format)

    
    def infer(self, text: str, output_file: str, kokoro_voice, speed_factor, audio_format, progress=gr.Progress()):
        logger.debug(f'[abus_tts_kokoro.py] infer - text = {text}')
        
        subtitle_file = None
        if AbusText.is_subtitle_format(text):
            subs = pysubs2.SSAFile.from_string(text)
            subtitle_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{subs.format}"))
            subs.save(subtitle_file)
        
        if subtitle_file:    
            self.srt_to_voice(subtitle_file, output_file, kokoro_voice, speed_factor, audio_format, progress)
        else:
            self.text_to_voice(text, output_file, kokoro_voice, speed_factor, audio_format, progress)
            
