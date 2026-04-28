from src.config import UserConfig
from app.abus_path import *

from app.abus_voice_ms import *
from app.abus_tts_edge import *
from app.abus_tts_azure import *
from app.abus_translate_deep import *
from app.abus_translate_azure import *
from app.abus_genuine import *
from app.abus_files import *
from app.abus_rvc import *


import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()


from app.abus_tts_rvc import *


class GradioTTSRVC:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config

        self.voice_manager = MSVoiceManager(self.user_config.get('ms_language', "English"))
        # self.tts = AzureTTS() if azure_text_api_working() == True else EdgeTTS()
        # self.rvc = RVC()
        
        # self.translator = AzureTranslator() if azure_text_api_working() == True else DeepTranslator()
        
        self.ttsrvc = TTSRVC()

            
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
            
    def gradio_translate_languages(self) -> list:
        return self.ttsrvc.get_languages()        
    
    
    def gradio_rvc_models(self):
        return self.ttsrvc.get_voices()
              
    
    def gradio_update_tts_voices(self, languageName: str):
        value = self.ttsrvc.get_language_value(languageName)
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
    
    
    def gradio_update_rvc_voice(self):
        voice_list =self.ttsrvc.get_voices()
        if len(voice_list) > 0:
            return gr.update(choices=voice_list, value=voice_list[0])
        else:
            return gr.update(choices=voice_list, value=None)


    def gradio_rvc_voice_folder(self):
        rvc_voice_folder = os.path.join(os.getcwd(), 'model', 'rvc-voice')
        cmd_open_explorer(rvc_voice_folder)  

    
    def gradio_deep_voice(self, text: str, target_lang, tts_voice: str, semitones, speed_factor, volume_factor, rvc_voice, audio_format: str = 'mp3'):
        self.user_config.set("edge_tts_pitch", semitones)     
        self.user_config.set("edge_tts_rate", speed_factor)
        self.user_config.set("edge_tts_volume", volume_factor)     
        self.user_config.set("audio_format", audio_format)
        self.user_config.set("rvc_voice", rvc_voice)

        
        if not (text and text.strip()):
            message = i18n("Input error")
            gr.Warning(message)
            return None, None, None       

        input_text = text
        logger.debug(f"[gradio_tts_rvc.py] gradio_deep_voice - input_text: {input_text}")            
        
        try:
            ms_voice = self.voice_manager.get_voice(tts_voice)
                   
            tts_audio_file, rvc_audio_file = self.ttsrvc.infer(input_text.strip(), ms_voice.name, semitones, speed_factor, volume_factor, audio_format, rvc_voice)
            return tts_audio_file, rvc_audio_file, [tts_audio_file, rvc_audio_file]            
        except Exception as e:
            logger.error(f"[gradio_tts_rvc.py] gradio_deep_voice error: {e}")
            gr.Warning(f'{e}')
            return None, None, None

        
    def gradio_default(self):
        rvc_voice = gr.Dropdown(label=i18n("RVC Voice"), choices=self.ttsrvc.get_voices(), value=self.user_config.get("rvc_voice"))
        return [0, 0, 0, rvc_voice]
    
    
    def gradio_save(self, file_obj, target_lang, audio_format, text, audio_obj):
        logger.debug(f'[gradio_tts_rvc.py] gradio_save')
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
        
    
    # def _text_to_voice(self, text, tts_voice: str, semitones, speed_factor, volume_factor,  audio_format, rvc_voice, progress=gr.Progress()):
    #     # output file - tts, rvc
    #     tts_audio_file = os.path.join(path_dubbing_folder(), path_new_filename(ext = f".{audio_format}"))
    #     rvc_audio_file = path_add_postfix(tts_audio_file, f"-{rvc_voice}", f".{audio_format}")        
              
    #     self.tts.text_to_voice(text.strip(), tts_audio_file, tts_voice, semitones, speed_factor, volume_factor, audio_format)
    #     self.rvc.simple_inference(tts_audio_file, rvc_audio_file, rvc_voice, audio_format)    
    
    #     return tts_audio_file, rvc_audio_file
    
    
    # def _srt_to_voice(self, subtitle_file: str, tts_voice: str, semitones, speed_factor, volume_factor, audio_format, rvc_voice, progress=gr.Progress()):
    #     # formatted_time = path_time_string()
    #     tts_audio_file = path_add_postfix(subtitle_file, f"-{tts_voice}", f".{audio_format}")
    #     rvc_audio_file = path_add_postfix(subtitle_file, f"-{tts_voice}-{rvc_voice}", f".{audio_format}")        
    #     rvc_subtitle_file = path_add_postfix(subtitle_file, f"-{tts_voice}-{rvc_voice}", ".srt")
        
    #     tts_segments_folder = path_tts_segments_folder(subtitle_file)   
    #     rvc_segments_folder = path_rvc_segments_folder(subtitle_file)      

    #     combined_tts_audio = AudioSegment.empty()
    #     combined_rvc_audio = AudioSegment.empty()

    #     subs = pysubs2.load(subtitle_file, encoding="utf-8")
    #     for i in progress.tqdm(range(len(subs)), desc='Generating...'):
    #         line = subs[i]
    #         next_line = subs[i+1] if i < len(subs)-1 else None

    #         if i == 0:
    #             silence = AudioSegment.silent(duration=line.start)
    #             combined_tts_audio += silence
    #             combined_rvc_audio += silence

    #         tts_segment_file = os.path.join(tts_segments_folder, f'tts_{i+1:06}.{audio_format}')    
    #         if False == self.tts.text_to_voice(line.text, tts_segment_file, tts_voice, semitones, speed_factor, volume_factor, audio_format):
    #             silence = AudioSegment.silent(duration=next_line.start-line.start)
    #             combined_tts_audio += silence
    #             combined_rvc_audio += silence
    #             continue
            
    #         rvc_segment_file = os.path.join(rvc_segments_folder, f'rvc_{i+1:06}.{audio_format}')    
    #         self.rvc.simple_inference(tts_segment_file, rvc_segment_file, rvc_voice, audio_format)
            
    #         combined_tts_audio += AudioSegment.from_file(tts_segment_file)
    #         combined_rvc_audio += AudioSegment.from_file(rvc_segment_file)
            
    #         line.end = len(combined_rvc_audio)
            
    #         if next_line and len(combined_rvc_audio) < next_line.start:
    #             silence_length = next_line.start - len(combined_rvc_audio)
    #             silence = AudioSegment.silent(duration=silence_length)
    #             combined_tts_audio += silence
    #             combined_rvc_audio += silence
    #         elif next_line:
    #             next_line.start = len(combined_rvc_audio)
    #             next_line.end = next_line.start + (next_line.end - next_line.start)

    #     combined_tts_audio.export(tts_audio_file, format=audio_format)
    #     combined_rvc_audio.export(rvc_audio_file, format=audio_format)     
    #     subs.save(rvc_subtitle_file)
        
    #     return tts_audio_file, rvc_audio_file
        

