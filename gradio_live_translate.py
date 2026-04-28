from concurrent.futures import ProcessPoolExecutor, as_completed
from src.config import UserConfig

from app.abus_path import *
from app.abus_translate_deep import *
from app.abus_translate_azure import *
from app.abus_live import *
from app.abus_genuine import *

from app.abus_asr_faster_whisper import *
from app.abus_asr_whisper import *
from app.abus_asr_whisper_timestamped import *
from app.abus_asr_whisperx import *

from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()


class GradioLiveTranslate:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
             
        source_language = user_config.get("translate_source_language", "English")
        translate_language = user_config.get("translate_target_language", 'English')
        
        asr_engine = self.user_config.get("asr_engine", 'faster-whisper')
        self.whisper_inf = self.switch_case(asr_engine)           
        
        self.whisper_live = WhisperLive(self.whisper_inf)
        self.generator = ParallelTextGenerator(source_language, translate_language)
        


    def switch_case(self, case):
        switch_dict = {
            'faster-whisper': lambda: FasterWhisperInference(),
            'whisper': lambda: WhisperInference(),
            'whisper-timestamped': lambda: WhisperTimestampedInference(),
            'whisperX': lambda: WhisperXInference()
        }
        return switch_dict.get(case, lambda: FasterWhisperInference())()    

            
    def gradio_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def gradio_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    
                    
    def get_asr_engines(self):
        return ['faster-whisper', 'whisper', 'whisper-timestamped']
    
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
      
    
    def get_translate_languages(self) -> list:
        return self.generator.get_languages()
    
    
    def get_audio_sources(self) -> list:
        return self.whisper_live.all_devices_name()
    
    
    def gradio_stop(self):
        logger.debug(f'[gradio_stop] ==>>')
        message = i18n("Stop Live")
        gr.Info(message)        

        self.whisper_live.stop_thread()
        
        
    def gradio_start(self, 
                     audio_source, asr_engine, modelName, whisper_language, compute_type, denoise_level, source_language, translate_language):
        logger.debug(f'[gradio_start] ==>>')
        self.user_config.set("asr_engine", asr_engine)
        self.user_config.set(f'{asr_engine.replace("-", "_")}_model', modelName)
        self.user_config.set("whisper_language", whisper_language)
        self.user_config.set("whisper_compute_type", compute_type)
        self.user_config.set("denoise_level", denoise_level)
        self.user_config.set("translate_source_language", source_language)            
        self.user_config.set("translate_target_language", translate_language)            

        self.whisper_live.stop_thread()
        
        params = WhisperParameters(model_size=modelName, 
                            lang=whisper_language.lower(), 
                            compute_type=compute_type,
                            vad_filter=True,
                            denoise_level=denoise_level,
                            word_timestamps=True)       # word_timestamps  
        
        self.whisper_inf = self.switch_case(asr_engine)
        self.whisper_live = WhisperLive(self.whisper_inf)                

        self.generator.set_languages(source_language, translate_language)
        self.whisper_live.start_thread(audio_source, params)
        
        message = i18n("Start Live")
        gr.Info(message)        
    
    
    def gradio_clear(self):
        logger.debug(f'[gradio_clear] ==>>')
        self.generator.clear_segments()
        self.whisper_live.clear_audio()
        return "", ""
    

    def gradio_save(self, audio_format: str = 'mp3'):
        logger.debug(f'[abus_ui_live.py] gradio_save')
        message = i18n("Saving files...")
        gr.Info(message)
                
        self.generator.save()
        self.whisper_live.save_audio(audio_format)
    
    
    def get_transcriptions(self):
        def inner():
            segments = self.whisper_live.get_segments()
            if len(segments) > 0:
                self.generator.add_segments(segments)
            return self.generator.vtt_source
            
        return inner        
        
    def get_translations(self):
        def inner():
            return self.generator.vtt_target
        return inner        

    
class ParallelTextGenerator:
    def __init__(self, source_language, target_language):
        self.source_language = source_language
        self.target_language = target_language
        
       
        self.translator = AzureTranslator() if azure_text_api_working() == True else DeepTranslator()
        
        self.segments = []
        self.vtt_source = ""
        self.vtt_target = ""
        self.vtt_idx = 1
        
        
    def get_languages(self):
        return self.translator.get_languages()
    
    def set_languages(self, source_language, target_language):
        self.source_language = source_language
        self.target_language = target_language

    def add_segments(self, segments):
        self.vtt_idx = len(self.segments) + 1
        
        # source language
        self.vtt_source += get_vtt_block(segments, self.vtt_idx)
        
        # target language
        segments_target = self.translate_segments(segments)
        self.vtt_target += get_vtt_block(segments_target, self.vtt_idx)
                
        self.segments.extend(segments)
        
        
    def clear_segments(self):
        self.segments = []
        self.vtt_source = ""
        self.vtt_target = ""
        self.vtt_idx = 1
        
        
        
    def translate_segments(self, segments):
        if self.source_language == self.target_language:        
            return segments
        else:
            new_segments = []
            for segment in segments or []:
                segment['text'] = self.translator.translate_text(self.source_language, self.target_language, segment['text'])
                new_segments.append(segment)
            return new_segments
        
        
    def save(self):
        self.vtt_source = "WebVTT\n\n" + self.vtt_source        
        vtt_source_path = os.path.join(path_live_folder(), f'live-{time.time()}-{self.source_language}.vtt')        
        write_file(self.vtt_source, vtt_source_path)

        self.vtt_target = "WebVTT\n\n" + self.vtt_target
        vtt_target_path = os.path.join(path_live_folder(), f'live-{time.time()}-{self.target_language}.vtt')        
        write_file(self.vtt_target, vtt_target_path)
        
        
