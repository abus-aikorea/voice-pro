import time
import pysubs2
import re
import unicodedata
import string

from pydub import AudioSegment
from pydub.silence import detect_leading_silence
import numpy as np
import gradio as gr
import torch
import gc

from app.abus_genuine import *
from app.abus_path import *
from app.abus_ffmpeg import *
from app.abus_text import *
from app.abus_nlp_spacy import *
from app.abus_audio import *

import structlog
logger = structlog.get_logger()


import soundfile as sf


from cached_path import cached_path
from f5_tts.model import DiT, UNetT
from f5_tts.infer.utils_infer import (
    load_vocoder,
    load_model,
    preprocess_ref_audio_text,
    infer_process,
    remove_silence_for_generated_wav,
    save_spectrogram,
)

try:
    import spaces
    USING_SPACES = True
except ImportError:
    USING_SPACES = False

def gpu_decorator(func):
    if USING_SPACES:
        return spaces.GPU(func)
    else:
        return func


class ModelPathManager:
    def __init__(self, config_path="abus_tts_f5_models.json"):
        self.config_path = config_path
        self.model_configs = self._load_config()
        
    def _load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
            
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in configuration file: {self.config_path}")
    
    def get_model_paths(self, model_name):
        if model_name not in self.model_configs:
            raise KeyError(f"Model '{model_name}' not found in configuration")
            
        return self.model_configs[model_name]
    
    def list_available_models(self):
        return list(self.model_configs.keys())



class F5TTS:
    def __init__(self):
        config_path = os.path.join(Path(__file__).resolve().parent, "abus_tts_f5_models.json")
        self.manager = ModelPathManager(config_path)
        self.vocoder = load_vocoder()
        


    def available_models(self):
        models = self.manager.list_available_models()
        models.append("SWivid/E2-TTS")    
        return models        
    

    def load_f5tts(self, model_name: str = "SWivid/F5-TTS_v1"):
        model_paths = self.manager.get_model_paths(model_name)
        default_cfg = dict(dim=1024, depth=22, heads=16, ff_mult=2, text_dim=512, conv_layers=4)
        
        vocab_path = str(cached_path(model_paths['vocab_path'])) if 'vocab_path' in model_paths else ""
        ckpt_path = str(cached_path(model_paths['model_path'])) if 'model_path' in model_paths else ""
        model_cfg = model_paths['config'] if 'config' in model_paths else default_cfg
            
        return load_model(DiT, model_cfg, ckpt_path, vocab_file=vocab_path)


    def load_e2tts(self):
        ckpt_path = str(cached_path("hf://SWivid/E2-TTS/E2TTS_Base/model_1200000.safetensors"))
        model_cfg = dict(dim=1024, depth=24, heads=16, ff_mult=4, text_mask_padding=False, pe_attn_head=1)
        return load_model(UNetT, model_cfg, ckpt_path)
    

    
    def select_model(self, model_choice):
        if model_choice == "SWivid/E2-TTS":
            self.ema_model = self.load_e2tts()
        else:
            self.ema_model = self.load_f5tts(model_choice)
        
    
    
    @staticmethod
    def release_cuda_memory():
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.reset_max_memory_allocated()
            logger.debug(f'[abus_tts_f5.py] release_cuda_memory - OK!! ')
                
                
    @gpu_decorator
    def generate_audio(self, dubbing_text:str, output_file, ref_audio, ref_text, speed_factor, progress=gr.Progress()):
        logger.debug(f'[abus_tts_f5.py] generate_audio - {dubbing_text}')
        
        try:
            final_wave, final_sample_rate, _ = infer_process(
                ref_audio,
                ref_text,
                dubbing_text,
                self.ema_model,
                self.vocoder,
                cross_fade_duration=0.15,
                nfe_step=32,                # denoising steps, 4 ~ 64
                speed=speed_factor,
                progress=progress
            )
            logger.debug(f'[abus_tts_f5.py] final_sample_rate - {final_sample_rate}')
            logger.debug(f'[abus_tts_f5.py] final_wave - {final_wave}')
            
            sf.write(output_file, final_wave, final_sample_rate)
        except Exception as e:
            logger.error(f"[abus_tts_f5.py] infer_process - error: {e}")        
        
        
                    
    
    
    def request_tts(self, line: str, output_file: str, ref_audio, ref_text, speed_factor, audio_format):
        output_voice_file = os.path.join(path_dubbing_folder(), path_new_filename(ext = f".{audio_format}"))
        line = AbusText.normalize_text(line)
        if len(line) < 1:
            logger.warning(f"[abus_tts_f5.py] request_tts - error: no line")
            return False
        
        logger.debug(f'[abus_tts_f5.py] request_tts - line = {line}')
        self.generate_audio(line, output_voice_file, ref_audio, ref_text, speed_factor)
        
        trimed_voice_file = path_add_postfix(output_voice_file, "_trimed")
        AbusAudio.trim_silence_file(output_voice_file, trimed_voice_file)        
        ffmpeg_to_stereo(trimed_voice_file, output_file)
        
        try:
            os.remove(output_voice_file)
            os.remove(trimed_voice_file)
        except Exception as e:
            logger.error(f"[abus_tts_f5.py] request_tts - error: {e}")
            return False        
        return True
    

    def srt_to_voice(self, subtitle_file: str, output_file: str, ref_audio, ref_text, speed_factor, audio_format, progress=gr.Progress()):
        tts_subtitle_file = path_add_postfix(subtitle_file, f"-f5-tts", ".srt")
        
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
            tts_result = self.request_tts(line.text, tts_segment_file, ref_audio, ref_text, speed_factor, audio_format)

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
      
    
    def text_to_voice(self, dubbing_text: str, output_file: str, ref_audio, ref_text, speed_factor, audio_format, progress=gr.Progress()):
        segments_folder = path_tts_segments_folder(output_file)          

        use_punctuation = AbusText.has_punctuation_marks(dubbing_text)
        lines = AbusText.split_into_sentences(dubbing_text, use_punctuation)
        lines = lines
        
        combined_audio = AudioSegment.empty() 
        for i in progress.tqdm(range(len(lines)), desc='Generating...'):
            tts_segment_file = os.path.join(segments_folder, f'tts_{i+1:06}.{audio_format}')    
            tts_result = self.request_tts(lines[i], tts_segment_file, ref_audio, ref_text, speed_factor, audio_format)
            if tts_result == False:
                continue
            combined_audio += AudioSegment.from_file(tts_segment_file)
            
        combined_audio.export(output_file, format=audio_format)

    
    
    def infer_single(self, dubbing_text:str, output_file, celeb_audio, celeb_transcript, model_choice, speed_factor, audio_format: str, progress=gr.Progress()):
        self.select_model(model_choice)
        ref_audio, ref_text = preprocess_ref_audio_text(celeb_audio, celeb_transcript)
        
        subtitle_file = None
        if AbusText.is_subtitle_format(dubbing_text):
            subs = pysubs2.SSAFile.from_string(dubbing_text)
            subtitle_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{subs.format}"))
            subs.save(subtitle_file)
            
        if subtitle_file:
            self.srt_to_voice(subtitle_file, output_file, ref_audio, ref_text, speed_factor, audio_format, progress)
        else:
            self.text_to_voice(dubbing_text, output_file, ref_audio, ref_text, speed_factor, audio_format, progress)
                
        del self.ema_model
        self.ema_model = None
        self.release_cuda_memory()

            
    def infer_multi(self, dubbing_text:str, output_file, celeb_audio1, celeb_transcript1, celeb_audio2, celeb_transcript2, model_choice, speed_factor, audio_format: str, progress=gr.Progress()):
        self.select_model(model_choice)
        ref_audio1, ref_text1 = preprocess_ref_audio_text(celeb_audio1, celeb_transcript1)
        ref_audio2, ref_text2 = preprocess_ref_audio_text(celeb_audio2, celeb_transcript2)
        
        try:
            segments_folder = path_tts_segments_folder(output_file)          
            conversations = self._parse_conversation_regex(dubbing_text)
            conversations = conversations
                
            combined_audio = AudioSegment.empty() 
            for i in progress.tqdm(range(len(conversations)), desc='Generating...'):
                tts_segment_file = os.path.join(segments_folder, f'tts_{i+1:06}.{audio_format}') 
                
                conversation = conversations[i]
                if conversation['speaker'] == 'spk1':
                    tts_result = self.request_tts(conversation['message'], tts_segment_file, ref_audio1, ref_text1, speed_factor, audio_format)
                else:
                    tts_result = self.request_tts(conversation['message'], tts_segment_file, ref_audio2, ref_text2, speed_factor, audio_format)
                
                if tts_result == False:
                    continue
                combined_audio += AudioSegment.from_file(tts_segment_file)
        
            combined_audio.export(output_file, format=audio_format)
        except Exception as e:
            logger.error(f"[abus_tts_f5.py] infer_multi - An error occurred: {e}")
        finally:
            del self.ema_model
            self.ema_model = None
            self.release_cuda_memory()



    def _parse_conversation_regex(self, text):
        pattern = r'\{(\w+)\}\s*(.*)'
        conversations = []
        
        for line in text.splitlines():
            if line.strip():
                match = re.match(pattern, line)
                if match:
                    speaker, message = match.groups()
                    conversations.append({
                        'speaker': speaker,
                        'message': message.strip()
                    })
        
        return conversations
