import json
from src.config import UserConfig

from app.abus_downloader import *
from app.abus_ffmpeg import *
from app.abus_genuine import *
from app.abus_path import *
from app.abus_demucs import *
from app.abus_mdx import *
from app.abus_files import *
from app.abus_hf import AbusHuggingFace

from app.abus_asr_faster_whisper import *
from app.abus_asr_whisper import *
from app.abus_asr_whisper_timestamped import *
from app.abus_asr_whisperx import *

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()


class GradioKara:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config

        self.fm = FileManager()
        
        self.downloader = YoutubeDownloader()   
             
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


    def open_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def open_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    
    def open_model_folder(self):
        cmd_open_explorer(self.mdxnet_models_dir)        


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
    def upload_source(self, 
                      file_obj, mic_file, youtube_url: str, video_quality: str, audio_format: str):
        self.user_config.set("video_quality", video_quality)
        self.user_config.set("audio_format", audio_format)

        try:
            logger.debug(f'upload_source: file_obj={file_obj}, mic_file={mic_file}, youtube_url={youtube_url}')            
            self.fm = FileManager()
            if self._upload(file_obj, mic_file, youtube_url, video_quality, audio_format) == False:
                return None, None, None

            return self.fm.get_split("Source.video"), self.fm.get_split("Source.audio"), self.fm.get_all_files()
        except Exception as e:
            logger.error(f"[gradio_kara.py] upload_source - Error transcribing file: {e}")
            gr.Warning(f'{e}')
            return None, None, None
                

    def _upload(self,
                file_obj, mic_file, youtube_url: str, video_quality: str, audio_format: str):
        if (file_obj is not None):
            uploaded_file = cmd_copy_file_to(gradio_file_path(file_obj), path_workspace_subfolder(gradio_file_path(file_obj)))
        elif mic_file and mic_file.strip():
            uploaded_file = cmd_copy_file_to(mic_file, path_workspace_subfolder(mic_file))
        elif youtube_url and youtube_url.strip():
            youtube_file = self.downloader.yt_download(youtube_url, path_youtube_folder(), video_quality)
            uploaded_file = cmd_copy_file_to(youtube_file, path_workspace_subfolder(youtube_file))
        else:
            return False
        
        self.source_file = uploaded_file
        
        self.has_audio, self.has_video = ffmpeg_codec_type(self.source_file)
        logger.debug(f'upload_source: source_file={self.source_file}, has_audio={self.has_audio}, has_video={self.has_video}')
        if self.has_audio == False:     # error
            return False
        elif self.has_video == False:   # audio-only
            self.fm.set_split("Source.video", None)
            self.fm.set_split("Source.audio", self.source_file)   
        else:
            input_audio_file = path_change_ext(self.source_file, f'.{audio_format}')
            ffmpeg_extract_audio(self.source_file, input_audio_file, audio_format)    
            self.fm.set_split("Source.video", self.source_file)
            self.fm.set_split("Source.audio", input_audio_file)
        return True   

    # return Dropdown, Dropdown
    def update_demixing_models(self):
        local_models = AbusHuggingFace.hf_demixing_names(has_local_file=True)
        local_dropdown = gr.Dropdown(label=i18n("MDX Models"), choices=local_models, value=self.user_config.get("demixing_model", "htdemucs"))
        return local_dropdown 


    
    # return Video, Audio, Video, Audio, File
    def demixing(self,
                 demixing_model, audio_format):
        self.user_config.set("demixing_model", demixing_model)
        self.user_config.set("demixing_audio_format", audio_format)
        
        try:
            self._demixing(demixing_model, audio_format)             
            return self.fm.get_split("Instrumental.video"), self.fm.get_split("Instrumental.audio"), self.fm.get_split("Vocals.video"), self.fm.get_split("Vocals.audio"), self.fm.get_all_files()
        except Exception as e:
            logger.error(f"[gradio_kara.py] demixing - Error transcribing file: {e}")
            gr.Warning(f'{e}')
            return None, None, None, None, None
    
    
    def _demixing(self,
                demixing_model, audio_format):
        progress = gr.Progress()
        
        input_audio_file = self.fm.get_split("Source.audio")
        file_name = os.path.splitext(os.path.basename(input_audio_file))[0]  
        output_dir = os.path.dirname(input_audio_file)      
        
        if demixing_model in ['htdemucs', 'htdemucs_6s', 'htdemucs_ft', 'mdx_extra']:                  
            inst_audio_file, vocal_audio_file = demucs_split_file(input_audio_file, output_dir, demixing_model, audio_format)
        else:
            mdx_model = AbusHuggingFace.hf_get_from_name(demixing_model)
            mdx_model_path = os.path.join(self.mdxnet_models_dir, mdx_model.file_name)
            main_filepath, invert_filepath = run_mdx(self.mdx_model_params, output_dir, mdx_model_path, input_audio_file, denoise=True, keep_orig=True)
            
            inst_audio_file = os.path.join(path_workspace_folder(), file_name + f"_{demixing_model}_main." + audio_format)
            vocal_audio_file = os.path.join(path_workspace_folder(), file_name + f"_{demixing_model}_invert." + audio_format)
            shutil.move(main_filepath, inst_audio_file)
            shutil.move(invert_filepath, vocal_audio_file)
            
                     
        self.fm.set_split("Instrumental.audio", inst_audio_file)
        self.fm.set_split("Vocals.audio", vocal_audio_file)
        
        if self.has_video:
            input_video_file = self.fm.get_split("Source.video")
            
            progress(0.2, desc=f'encoding instrumentals-only video...')
            inst_video_file = path_add_postfix(input_video_file, f"_{demixing_model}_inst")
            ffmpeg_replace_audio(input_video_file, inst_audio_file, inst_video_file)
            self.fm.set_split("Instrumental.video", inst_video_file)
            
            progress(0.6, desc=f'encoding vocal-only video...')
            vocal_video_file = path_add_postfix(input_video_file, f"_{demixing_model}_vocal")
            ffmpeg_replace_audio(input_video_file, vocal_audio_file, vocal_video_file)
            self.fm.set_split("Vocals.video", vocal_video_file)
            
            progress(1, desc=f'video creation complete')
    


    def transcribe(self, 
                  asr_engine, modelName, whisper_language, compute_type, highlight_words, denoise_level):
        self.user_config.set("asr_engine", asr_engine)
        self.user_config.set(f'{asr_engine.replace("-", "_")}_model', modelName)
        self.user_config.set("whisper_language", whisper_language)
        self.user_config.set("whisper_compute_type", compute_type)
        self.user_config.set("whisper_highlight_words", highlight_words)
        self.user_config.set("denoise_level", denoise_level)        
        
        try: 
            source_audio = self.fm.get_split("Source.audio")
            denoise_inst_path, denoise_vocal_path = self._denoise(source_audio, denoise_level)
            input_path = denoise_vocal_path if os.path.exists(denoise_vocal_path) else source_audio
            
            params = WhisperParameters(model_size=modelName, 
                                       lang=whisper_language.lower(), 
                                       compute_type=compute_type)
            
            self.whisper_inf = self.switch_case(asr_engine)                            
            subtitles = self.whisper_inf.transcribe_file(input_path, params, highlight_words, gr.Progress())
            self.fm.set_subtitles(subtitles, whisper_language, source_audio) 
            
            
            srt_file = self.fm.get_subtitle('.srt')
            inst_video = self.fm.get_split("Instrumental.video")
            vocal_video = self.fm.get_split("Vocals.video")                            
            if(self.has_video and ffmpeg_browser_compatible(self.source_file)):
                if inst_video and vocal_video:
                    if srt_file:
                        return (self.source_file, srt_file), (inst_video, srt_file), (vocal_video, srt_file), self.fm.get_all_files()      
                    else:
                        return self.source_file, inst_video, vocal_video, self.fm.get_all_files()
                else:
                    if srt_file:
                        return (self.source_file, srt_file), None, None, self.fm.get_all_files()      
                    else:
                        return self.source_file, None, None, self.fm.get_all_files()
            else:
                return None, None, None, self.fm.get_all_files()   
            
        except Exception as e:
            logger.error(f"[gradio_kara.py] transcribe - Error transcribing file: {e}")
            gr.Warning(f'{e}')
            return None, None, None, None    
 
 
    def _denoise(self, source_audio, denoise_level=2):
        if denoise_level == 1:
            return self._denoise_demucs(source_audio)
        elif denoise_level ==2:
            return self._denoise_mdx3(source_audio)
        else:
            return "", ""
                
        
    def _denoise_mdx3(self, source_audio):
        progress = gr.Progress()
        
        output_dir = os.path.dirname(source_audio)
            
        progress(0.2, desc=f'Separating vocals and instrumental...')
        mdxnet_voc_ft = os.path.join(self.mdxnet_models_dir, 'UVR-MDX-NET-Voc_FT.onnx')     
        vocals_path, instrumentals_path = run_mdx(self.mdx_model_params, output_dir, mdxnet_voc_ft, source_audio, denoise=True, keep_orig=True)

        progress(0.6, desc=f'Separating main vocals and backup vocals...')
        mdxnet_kara2 = os.path.join(self.mdxnet_models_dir, 'UVR_MDXNET_KARA_2.onnx')
        backup_vocals_path, main_vocals_path = run_mdx(self.mdx_model_params, output_dir, mdxnet_kara2, vocals_path, suffix='Backup', invert_suffix='Main', denoise=True)
        
        progress(0.6, desc=f'Separating reverb...')
        mdxnet_reverb = os.path.join(self.mdxnet_models_dir, 'Reverb_HQ_By_FoxJoy.onnx')
        _, main_vocals_dereverb_path = run_mdx(self.mdx_model_params, output_dir, mdxnet_reverb, main_vocals_path, invert_suffix='DeReverb', exclude_main=True, denoise=True)
            
        progress(1, desc=f'demixing complete')
                    
        self.fm.set_split("Instrumental.audio", instrumentals_path)
        self.fm.set_split("Vocals.audio", vocals_path)        
        self.fm.set_split("MainVocals.audio", main_vocals_path)    
        self.fm.set_split("BackupVocals.audio", backup_vocals_path)  
        self.fm.set_split("DereverbVocals.audio", main_vocals_dereverb_path)         
        
        return instrumentals_path, main_vocals_dereverb_path
        
            
    def _denoise_demucs(self, source_audio):
        _, extension = os.path.splitext(os.path.basename(source_audio))
        output_dir = os.path.dirname(source_audio)
        
        inst_audio_file, vocal_audio_file = demucs_split_file(source_audio, output_dir, 'htdemucs', extension[1:])
        self.fm.set_split("Instrumental.audio", inst_audio_file)
        self.fm.set_split("Vocals.audio", vocal_audio_file)

        return inst_audio_file, vocal_audio_file
