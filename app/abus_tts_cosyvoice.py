import os
import pysubs2

from pydub import AudioSegment
import gradio as gr
import torch
import gc

from app.abus_genuine import *
from app.abus_path import *
from app.abus_ffmpeg import *
from app.abus_hf_file import *
from app.abus_text import *
from app.abus_nlp_spacy import *
from app.abus_audio import *

import structlog
logger = structlog.get_logger()


# import soundfile as sf
# from f5_tts.model import DiT, UNetT
from f5_tts.infer.utils_infer import preprocess_ref_audio_text



import librosa
import random

max_val = 0.8
prompt_sr = 16000

import torchaudio
from cosyvoice.cli.cosyvoice import CosyVoice2, CosyVoice3
from cosyvoice.utils.file_utils import load_wav
from cosyvoice.utils.common import set_all_random_seed

# logging.getLogger().setLevel(logging.WARNING)
# logging.getLogger('matplotlib').setLevel(logging.WARNING)
# logging.basicConfig(level=logging.WARNING,
#                     format='%(asctime)s %(levelname)s %(message)s')


os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = 'True'

# 지원 모델. CosyVoice2-0.5B는 ABUS-AI zip으로 선다운로드되고 (abus_hf_files-voice.json),
# Fun-CosyVoice3-0.5B(한국어 포함 9개 언어)는 최초 사용 시 공식 HF 리포에서 받는다.
COSYVOICE_MODEL_CHOICES = ["CosyVoice2-0.5B", "Fun-CosyVoice3-0.5B"]
COSYVOICE3_HF_REPO = "FunAudioLLM/Fun-CosyVoice3-0.5B-2512"


class CosyVoiceInference:
    def __init__(self, model_name: str = "CosyVoice2-0.5B"):
        self.model_name = model_name if model_name in COSYVOICE_MODEL_CHOICES else COSYVOICE_MODEL_CHOICES[0]
        self._cosyvoice = None


    def set_model(self, model_name: str):
        if model_name not in COSYVOICE_MODEL_CHOICES or model_name == self.model_name:
            return
        logger.debug(f"[abus_tts_cosyvoice.py] set_model - {self.model_name} -> {model_name}")
        self.model_name = model_name
        if self._cosyvoice is not None:
            self._cosyvoice = None
            self.release_cuda_memory()


    def _model_dir(self):
        return os.path.join(path_model_folder(), "cosyvoice", self.model_name)


    def _create_model(self):
        model_dir = self._model_dir()
        if self.model_name == "Fun-CosyVoice3-0.5B":
            # 최초 사용 시 공식 HF 리포에서 다운로드 (idempotent, 이어받기 지원)
            if not os.path.exists(os.path.join(model_dir, "llm.pt")):
                logger.info(f"[abus_tts_cosyvoice.py] downloading {COSYVOICE3_HF_REPO} to {model_dir} ...")
                from huggingface_hub import snapshot_download
                snapshot_download(repo_id=COSYVOICE3_HF_REPO, local_dir=model_dir)
            print("Creating CosyVoice3...")
            return CosyVoice3(model_dir)

        # ABUS-AI zip은 구버전 레이아웃(cosyvoice.yaml)이므로, 재벤더링된 코드가 요구하는
        # cosyvoice2.yaml이 없으면 공식 리포에서 보충한다 (기존 설치본 자동 치유).
        if not os.path.exists(os.path.join(model_dir, "cosyvoice2.yaml")):
            logger.info(f"[abus_tts_cosyvoice.py] fetching cosyvoice2.yaml into {model_dir} ...")
            from huggingface_hub import hf_hub_download
            hf_hub_download(repo_id="FunAudioLLM/CosyVoice2-0.5B", filename="cosyvoice2.yaml", local_dir=model_dir)
        print("Creating CosyVoice2...")
        return CosyVoice2(model_dir)


    def __getattr__(self, name):
        if name == "cosyvoice":
            if self._cosyvoice is None:
                self._cosyvoice = self._create_model()
            return self._cosyvoice
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


    @staticmethod
    def release_cuda_memory():
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.reset_max_memory_allocated()
            logger.debug(f'[abus_tts_cosyvoice.py] release_cuda_memory - OK!! ')
                
    def set_random_seed(self):
        seed = random.randint(1, 100000000)
        set_all_random_seed(seed)
    
    
    def _prepare_prompt_wav(self, ref_audio):
        # 업스트림 inference_* API는 이제 텐서 대신 wav 파일 경로를 받는다.
        # 기존 전처리(무음 트림/정규화)를 유지하기 위해 임시 wav로 저장해 경로를 넘긴다.
        speech = self.postprocess(load_wav(ref_audio, prompt_sr))
        prompt_wav = os.path.join(path_dubbing_folder(), path_new_filename(ext=".wav"))
        torchaudio.save(prompt_wav, speech, prompt_sr)
        return prompt_wav


    def _is_cv3(self):
        return self.model_name.startswith("Fun-CosyVoice3")

    # CosyVoice3는 시스템 프롬프트 + <|endofprompt|> 마커를 요구한다 (업스트림 example.py 참조).
    # 누락 시 LLM 스레드가 조용히 죽어 빈 오디오가 생성된다.
    CV3_SYSTEM_PROMPT = "You are a helpful assistant.<|endofprompt|>"


    def generate_audio_zero_shot(self, dubbing_text:str, output_file, ref_audio, ref_text, speed_factor):
        logger.debug(f"[abus_tts_cosyvoice.py] generate_audio_zero_shot - ref_audio = {ref_audio}, ref_text = {ref_text}, dubbing_text = {dubbing_text}")

        # zero_shot usage
        prompt_wav = self._prepare_prompt_wav(ref_audio)
        prompt_text = self.CV3_SYSTEM_PROMPT + ref_text if self._is_cv3() else ref_text
        for i, j in enumerate(self.cosyvoice.inference_zero_shot(dubbing_text, prompt_text, prompt_wav, stream=False, speed=speed_factor, text_frontend=False)):
            torchaudio.save(output_file, j['tts_speech'], self.cosyvoice.sample_rate)


    def generate_audio_cross_lingual(self, dubbing_text:str, output_file, ref_audio, ref_text, speed_factor):
        logger.debug(f"[abus_tts_cosyvoice.py] generate_audio_cross_lingual - ref_audio = {ref_audio}, ref_text = {ref_text}, dubbing_text = {dubbing_text}")

        # fine grained control, for supported control, check cosyvoice/tokenizer/tokenizer.py#L248
        prompt_wav = self._prepare_prompt_wav(ref_audio)
        tts_text = self.CV3_SYSTEM_PROMPT + dubbing_text if self._is_cv3() else dubbing_text
        for i, j in enumerate(self.cosyvoice.inference_cross_lingual(tts_text, prompt_wav, speed=speed_factor, stream=False)):
            torchaudio.save(output_file, j['tts_speech'], self.cosyvoice.sample_rate)

    def generate_audio_instruct(self, dubbing_text:str, output_file, ref_audio, ref_text, speed_factor):
        logger.debug(f"[abus_tts_cosyvoice.py] generate_audio_instruct - ref_audio = {ref_audio}, ref_text = {ref_text}, dubbing_text = {dubbing_text}")

        # instruct usage
        prompt_wav = self._prepare_prompt_wav(ref_audio)
        instruct_text = self.CV3_SYSTEM_PROMPT if self._is_cv3() else ''
        for i, j in enumerate(self.cosyvoice.inference_instruct2(dubbing_text, instruct_text, prompt_wav, stream=False)):
            torchaudio.save(output_file, j['tts_speech'], self.cosyvoice.sample_rate)


    def postprocess(self, speech, top_db=60, hop_length=220, win_length=440):
        speech, _ = librosa.effects.trim(
            speech, top_db=top_db,
            frame_length=win_length,
            hop_length=hop_length
        )
        if speech.abs().max() > max_val:
            speech = speech / speech.abs().max() * max_val
        speech = torch.concat([speech, torch.zeros(1, int(self.cosyvoice.sample_rate * 0.2))], dim=1)
        return speech    
    
    
    
    def request_tts(self, line: str, output_file: str, ref_audio, ref_text, inference_mode, speed_factor, audio_format):
        output_voice_file = os.path.join(path_dubbing_folder(), path_new_filename(ext = f".{audio_format}"))
        line = AbusText.normalize_text(line)
        if len(line) < 1:
            logger.warning(f"[abus_tts_cosyvoice.py] request_tts - error: no line")
            return False
        
        logger.debug(f'[abus_tts_cosyvoice.py] request_tts - line = {line}')

        if inference_mode == "Cross-Lingual":
            self.generate_audio_cross_lingual(line, output_voice_file, ref_audio, ref_text, speed_factor)
        elif inference_mode == "Instruct":
            self.generate_audio_instruct(line, output_voice_file, ref_audio, ref_text, speed_factor)            
        else:
            self.generate_audio_zero_shot(line, output_voice_file, ref_audio, ref_text, speed_factor)
            
        
        trimed_voice_file = path_add_postfix(output_voice_file, "_trimed")
        AbusAudio.trim_silence_file(output_voice_file, trimed_voice_file)        
        ffmpeg_to_stereo(trimed_voice_file, output_file)
        
        try:
            os.remove(output_voice_file)
            os.remove(trimed_voice_file)
        except Exception as e:
            logger.error(f"[abus_tts_cosyvoice.py] request_tts - error: {e}")
            return False        
        return True
    

    def srt_to_voice(self, subtitle_file: str, output_file: str, ref_audio, ref_text, inference_mode, speed_factor, audio_format, progress=gr.Progress()):
        tts_subtitle_file = path_add_postfix(subtitle_file, f"-cosyvoice", ".srt")
        
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
            tts_result = self.request_tts(line.text, tts_segment_file, ref_audio, ref_text, inference_mode, speed_factor, audio_format)

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
     
    
    def text_to_voice(self, dubbing_text: str, output_file: str, ref_audio, ref_text, inference_mode, speed_factor, audio_format, progress=gr.Progress()):
        segments_folder = path_tts_segments_folder(output_file)
                  
        use_punctuation = AbusText.has_punctuation_marks(dubbing_text)
        lines = AbusText.split_into_sentences(dubbing_text, use_punctuation)
        lines = lines
        
        combined_audio = AudioSegment.empty() 
        for i in progress.tqdm(range(len(lines)), desc='Generating...'):
            tts_segment_file = os.path.join(segments_folder, f'tts_{i+1:06}.{audio_format}')    
            tts_result = self.request_tts(lines[i], tts_segment_file, ref_audio, ref_text, inference_mode, speed_factor, audio_format)
            if tts_result == False:
                continue
            combined_audio += AudioSegment.from_file(tts_segment_file)
            
        combined_audio.export(output_file, format=audio_format)

    
    
    def infer_single(self, dubbing_text:str, output_file, celeb_audio, celeb_transcript, inference_mode, speed_factor, audio_format: str, progress=gr.Progress()):
        self.set_random_seed()
                
        ref_audio, ref_text = preprocess_ref_audio_text(celeb_audio, celeb_transcript)
        
        subtitle_file = None
        if AbusText.is_subtitle_format(dubbing_text):
            subs = pysubs2.SSAFile.from_string(dubbing_text)
            subtitle_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{subs.format}"))
            subs.save(subtitle_file)               

        if subtitle_file:
            self.srt_to_voice(subtitle_file, output_file, ref_audio, ref_text, inference_mode, speed_factor, audio_format, progress)
        else:
            self.text_to_voice(dubbing_text, output_file, ref_audio, ref_text, inference_mode, speed_factor, audio_format, progress)

        # del self.ema_model
        # self.ema_model = None
        self.release_cuda_memory()

            
