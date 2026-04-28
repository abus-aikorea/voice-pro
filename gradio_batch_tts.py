
import json
import asyncio

from src.config import UserConfig
from app.abus_downloader import *
from app.abus_path import *
from app.abus_ffmpeg import *

from app.abus_voice_ms import *
from app.abus_tts_edge import *
from app.abus_tts_azure import *
from app.abus_translate_deep import *
from app.abus_translate_azure import *
from app.abus_demucs import *
from app.abus_genuine import *
from app.abus_files import *
from app.abus_batch import *

from app.abus_asr_faster_whisper import *
from app.abus_asr_whisper import *
from app.abus_asr_whisper_timestamped import *
from app.abus_asr_whisperx import *


import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()


class GradioBatchTTS:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        
        # self.fm = FileManager()
        self.batch_manager = BatchManager()

        # self.downloader = YoutubeDownloader()
        self.voice_manager = MSVoiceManager(self.user_config.get('ms_language', "English"))
        self.tts = AzureTTS() if azure_text_api_working() == True else EdgeTTS()
        
        self.translator = AzureTranslator() if azure_text_api_working() == True else DeepTranslator()

        asr_engine = self.user_config.get("asr_engine", 'faster-whisper')
        self.whisper_inf = self.switch_case(asr_engine)   
        
        self.mdxnet_models_dir = os.path.join(os.getcwd(), 'model', 'mdxnet-model')
        with open(os.path.join(self.mdxnet_models_dir, 'model_data.json')) as infile:
            self.mdx_model_params = json.load(infile)


    def switch_case(self, case):
        switch_dict = {
            'faster-whisper': lambda: FasterWhisperInference(),
            'whisper': lambda: WhisperInference(),
            'whisper-timestamped': lambda: WhisperTimestampedInference(),
            'whisperX': lambda: WhisperXInference()
        }
        return switch_dict.get(case, lambda: FasterWhisperInference())()    
            
            
    def gradio_select_folder(self):
        last_folder = cmd_select_folder(self.user_config.get('last_folder'))
        self.user_config.set('last_folder', last_folder)
        return last_folder
    
    def gradio_workspace_folder(self):
        last_folder = self.user_config.get('last_folder')
        cmd_open_explorer(last_folder)
    
    def gradio_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
        
    def get_asr_engines(self):
        return ['faster-whisper', 'whisper', 'whisper-timestamped', 'whisperX']
    
    def update_whisper_models(self, asr_engine):
        whisper_inf = self.switch_case(asr_engine)       
        model_list = whisper_inf.available_models()
        if len(model_list) > 0:
            model_name = self.user_config.get(f'{asr_engine.replace("-", "_")}_model', 'large')
            return gr.update(choices=model_list, value=model_name)
        
        return gr.update(choices=[], value=None)  
                    
    def get_whisper_models(self):
        return self.whisper_inf.available_models()
        
    def get_whisper_languages(self):
        return self.whisper_inf.available_langs()

    def get_whisper_compute_types(self):
        return FasterWhisperInference.available_compute_types()
            
    # return Video, Audio, File    
    def gradio_whisper(self, 
                      folder_path, audio_format: str,
                      asr_engine, modelName, whisper_language, compute_type, denoise_level):
        
        self.user_config.set("audio_format", audio_format)
        self.user_config.set("asr_engine", asr_engine)
        self.user_config.set(f'{asr_engine.replace("-", "_")}_model', modelName)
        self.user_config.set("whisper_language", whisper_language)
        self.user_config.set("whisper_compute_type", compute_type)
        self.user_config.set("denoise_level", denoise_level)
        try:
            logger.debug(f'gradio_upload_files: folder_path={folder_path}')
            files = path_av_subfiles(folder_path)
            logger.debug(f'gradio_upload_files: files={files}')
            for file in files:          
                fm = self._upload_file_batch(file, audio_format)
                if fm == None:
                    continue
                                                        
                source_audio = fm.get_split("Source.audio")
                denoise_inst_path, denoise_vocal_path = self._denoise_batch(fm, denoise_level)
                input_path = denoise_vocal_path if os.path.exists(denoise_vocal_path) else source_audio

                params = WhisperParameters(model_size=modelName, 
                                        lang=whisper_language.lower(), 
                                        compute_type=compute_type)
                
                self.whisper_inf = self.switch_case(asr_engine)                            
                subtitles = self.whisper_inf.transcribe_file(input_path, params, False, gr.Progress())
                fm.set_subtitles(subtitles, whisper_language, source_audio) 
                
                key = fm.get_split("Source")
                self.batch_manager.set_fm(key, fm)
            
            return self.batch_manager.get_all_files()
        except Exception as e:
            logger.error(f"[gradio_batch_tts.py] gradio_upload_source - Error transcribing file: {e}")
            gr.Warning(f'{e}')
            return self.batch_manager.get_all_files()    
        

    def _upload_file_batch(self,
                source_file, audio_format: str):
        if os.path.exists(source_file) == False:
            return None
                
        fm = FileManager()
        fm.set_split("Source", source_file)
        
        has_audio, has_video = ffmpeg_codec_type(source_file)
        logger.debug(f'_upload_file: source_file={source_file}, has_audio={has_audio}, has_video={has_video}')
        if has_audio == False:     # error
            return None
        elif has_video == False:   # audio-only
            fm.set_split("Source.video", None)
            fm.set_split("Source.audio", source_file)   
        else:
            input_audio_file = path_change_ext(source_file, f'.{audio_format}')
            ffmpeg_extract_audio(source_file, input_audio_file, audio_format)    
            fm.set_split("Source.video", source_file)
            fm.set_split("Source.audio", input_audio_file)
       
        return fm     
    
    
    def _denoise_batch(self, fm, denoise_level=2):
        if denoise_level == 1:
            return self._demucs_htdemucs(fm)
        elif denoise_level ==2:
            return self._demucs_htdemucs_ft(fm)
        else:
            return "", ""    
             
            
    def _demucs_htdemucs(self, fm):
        source_audio = fm.get_split("Source.audio")
        _, extension = os.path.splitext(os.path.basename(source_audio))
        output_dir = os.path.dirname(source_audio)
        
        inst_audio_file, vocal_audio_file = demucs_split_file(source_audio, output_dir, 'htdemucs', extension[1:])
        fm.set_split("Instrumental.audio", inst_audio_file)
        fm.set_split("Vocals.audio", vocal_audio_file)

        return inst_audio_file, vocal_audio_file

    def _demucs_htdemucs_ft(self, fm):
        source_audio = fm.get_split("Source.audio")
        _, extension = os.path.splitext(os.path.basename(source_audio))
        output_dir = os.path.dirname(source_audio)
        
        inst_audio_file, vocal_audio_file = demucs_split_file(source_audio, output_dir, 'htdemucs_ft', extension[1:])
        fm.set_split("Instrumental.audio", inst_audio_file)
        fm.set_split("Vocals.audio", vocal_audio_file)

        return inst_audio_file, vocal_audio_file
                           
            
            
    def get_translate_languages(self) -> list:
        return self.translator.get_languages()
    

    def gradio_translate_batch(self, source_lang, target_lang):
        self.user_config.set("translate_target_language", target_lang)
        try:
            for fm in self.batch_manager.get_all_fm():
                self._translate_srt_batch(fm, source_lang, target_lang)

            return self.batch_manager.get_all_files()
        except Exception as e:
            logger.error(f"[gradio_batch_tts.py] gradio_translate - Error transcribing file: {e}")
            gr.Warning(f'{e}')
            return None
                    
            
    def _translate_srt_batch(self, fm, source_lang, target_lang):
        srt_file = fm.get_subtitle('.srt')
        srt_translated_file = path_add_postfix(srt_file, f"_{target_lang}")
        self.translator.translate_file(source_lang, target_lang, srt_file, srt_translated_file)
        
        target_lang_code = self.translator.get_language_code(target_lang)
        fm.set_translation(target_lang_code, srt_translated_file)
        return srt_translated_file
        
            
    def gradio_translate_languages(self) -> list:
        return self.translator.get_languages()        
            
    
    def update_tts_voices(self, languageName: str):
        value = self.translator.get_language_value(languageName)
        if value:
            self.voice_manager.select_language(value)
            voice_list = self.get_tts_voices()
            if len(voice_list) > 0:
                return gr.update(choices=voice_list, value=voice_list[0])
        
        return gr.update(choices=[], value=None)
            

    def get_tts_voices(self) -> list:
        selectedLanguageName = self.voice_manager.selectedLanguageName
        voice_list = self.voice_manager.get_voices(selectedLanguageName)
        display_names = [voice.getDisplayName() for voice in voice_list]
        return display_names        
    

    
    def gradio_dubbing_batch(self, voice_name: str, semitones, speed_factor, volume_factor, audio_format: str):
        return None     
            
    
    def gradio_default_tts(self):
        return [0, 0, 0]
        

