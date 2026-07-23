import asyncio
import edge_tts
import time
import pysubs2
import re
import unicodedata
import string

from pydub import AudioSegment
from pydub.silence import detect_leading_silence
import numpy as np
import gradio as gr

from app.abus_genuine import *
from app.abus_path import *
from app.abus_ffmpeg import *
from app.abus_text import *
from app.abus_nlp_spacy import *
from app.abus_audio import *

import structlog
logger = structlog.get_logger()


class EdgeTTS:
    def __init__(self):
        pass
    
    async def generate_audio(self, text, voice, output_file, rate=0, volume=0, pitch=0):
        rate_options = f'+{rate}%' if rate>=0 else f'{rate}%'
        volume_options = f'+{volume}%' if volume>=0 else f'{volume}%'
        pitch_options = f'+{pitch}Hz' if pitch>= 0 else f'{pitch}Hz'
        
        logger.debug(f'[abus_tts_edge.py] generate_audio - text = {text}, voice = {voice}, rate_options = {rate_options}, volume_options = {volume_options}, pitch_options = {pitch_options}')
        communicate = edge_tts.Communicate(text, voice, rate=rate_options, volume=volume_options, pitch=pitch_options)
        await communicate.save(output_file)
    
    
    def request_tts(self, line: str, output_file: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format):
        output_voice_file = os.path.join(path_dubbing_folder(), path_new_filename(ext = f".{audio_format}"))
        line = AbusText.normalize_text(line)
        if len(line) < 1:
            logger.warning(f"[abus_tts_edge.py] request_tts - error: no line")
            return False
        
        logger.debug(f'[abus_tts_edge.py] request_tts - line = {line}, voice_name = {voice_name}')
        
        asyncio.run(self.generate_audio(line, voice_name, output_voice_file, rate=speed_factor, volume=volume_factor, pitch=semitones))
        
        logger.debug(f'[abus_tts_edge.py] request_tts - output_voice_file = {output_voice_file}')
        
        trimed_voice_file = path_add_postfix(output_voice_file, "_trimed")
        AbusAudio.trim_silence_file(output_voice_file, trimed_voice_file)
        
        ffmpeg_to_stereo(trimed_voice_file, output_file)
        
        try:
            os.remove(output_voice_file)
            os.remove(trimed_voice_file)
        except Exception as e:
            logger.error(f"[abus_tts_edge.py] request_tts - error: {e}")
            return False
        
        return True
    

    def srt_to_voice(self, subtitle_file: str, output_file: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        tts_subtitle_file = path_add_postfix(subtitle_file, f"-{voice_name}", ".srt")
        
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
            tts_result = self.request_tts(line.text, tts_segment_file, voice_name, semitones, speed_factor, volume_factor, audio_format)

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
      
    
    def text_to_voice(self, text: str, output_file: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        segments_folder = path_tts_segments_folder(output_file)  
        
        use_punctuation = AbusText.has_punctuation_marks(text)
        lines = AbusText.split_into_sentences(text, use_punctuation)
        lines = lines
        
        combined_audio = AudioSegment.empty() 
        for i in progress.tqdm(range(len(lines)), desc='Generating...'):
            tts_segment_file = os.path.join(segments_folder, f'tts_{i+1:06}.{audio_format}')    
            tts_result = self.request_tts(lines[i], tts_segment_file, voice_name, semitones, speed_factor, volume_factor, audio_format)
            if tts_result == False:
                continue
            combined_audio += AudioSegment.from_file(tts_segment_file)
            
        combined_audio.export(output_file, format=audio_format)

    
    def infer(self, text: str, output_file: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        logger.debug(f'[abus_tts_edge.py] infer - text = {text}')
        
        subtitle_file = None
        if AbusText.is_subtitle_format(text):
            subs = pysubs2.SSAFile.from_string(text)
            subtitle_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{subs.format}"))
            subs.save(subtitle_file)
        
        if subtitle_file:    
            self.srt_to_voice(subtitle_file, output_file, voice_name, semitones, speed_factor, volume_factor, audio_format, progress)
        else:
            self.text_to_voice(text, output_file, voice_name, semitones, speed_factor, volume_factor, audio_format, progress)
            
            
            
              
