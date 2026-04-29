
import json
# import asyncio

from src.config import UserConfig
from app.abus_downloader import *
from app.abus_path import *
from app.abus_ffmpeg import *

from app.abus_demucs import *
from app.abus_mdx import *
from app.abus_genuine import *
from app.abus_files import *

from app.abus_rvc import *


import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()


class GradioRVC:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        
        self.fm = FileManager()

        self.downloader = YoutubeDownloader()
        self.rvc = RVC()
     
        self.mdxnet_models_dir = os.path.join(os.getcwd(), 'model', 'mdxnet-model')
        with open(os.path.join(self.mdxnet_models_dir, 'model_data.json')) as infile:
            self.mdx_model_params = json.load(infile)
            
            
    def gradio_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def gradio_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    
                       
    # return Video, Audio, File    
    def gradio_upload_source(self, 
                      file_obj, mic_file, youtube_url: str, video_quality: str, audio_format: str):
        self.user_config.set("video_quality", video_quality)
        self.user_config.set("audio_format", audio_format) 

        try:
            logger.debug(f'upload_source: file_obj={file_obj}, mic_file={mic_file}, youtube_url={youtube_url}')          
            self.fm = FileManager()           
            if self._upload(file_obj, mic_file, youtube_url, video_quality, audio_format) == False:
                return None, None, None
                            
            source_audio = self.fm.get_split("Source.audio")           
            if(self.has_video and ffmpeg_browser_compatible(self.source_file)):
                return self.source_file, source_audio, self.fm.get_all_files()
            else:
                return None, source_audio, self.fm.get_all_files()
        except Exception as e:
            logger.error(f"[GradioRVC] gradio_upload_source - Error transcribing file: {e}")
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
                           
    
    def gradio_voices(self):
        return self.rvc.get_voices()

    
    def gradio_rvc_dubbing(self, rvc_voice, rvc_f0_up_key, 
                           rvc_filter_radius = 3, rvc_index_rate = 0.3, rvc_rms_mix_rate = 1, rvc_protect = 0.23, rvc_hop_length = 256, rvc_clean_strength = 0.2, audio_format: str = "mp3"):
        self.user_config.set("audio_format", audio_format)
        self.user_config.set("rvc_voice", rvc_voice)
        self.user_config.set("rvc_f0_up_key", rvc_f0_up_key)
        self.user_config.set("rvc_filter_radius", rvc_filter_radius)     
        self.user_config.set("rvc_index_rate", rvc_index_rate)
        self.user_config.set("rvc_rms_mix_rate", rvc_rms_mix_rate)     
        self.user_config.set("rvc_protect", rvc_protect)     
        self.user_config.set("rvc_hop_length", rvc_hop_length)     
        self.user_config.set("rvc_clean_strength", rvc_clean_strength)  

        try:
            denoise_level = 1
            source_audio_file = self.fm.get_split("Source.audio")
            denoise_inst_path, denoise_vocal_path = self._denoise(source_audio_file, denoise_level)
            
                        
            aidub_audio_file = path_add_postfix(source_audio_file, f"_{rvc_voice}")
            self.rvc.call_infer_pipeline(denoise_vocal_path, aidub_audio_file, rvc_voice, rvc_f0_up_key, rvc_filter_radius, rvc_index_rate, rvc_rms_mix_rate, rvc_protect, rvc_hop_length, rvc_clean_strength, audio_format)
            
            mixed_audio_file = path_add_postfix(source_audio_file, f"_mixed_{rvc_voice}")
            ffmpeg_mix_audio(aidub_audio_file, denoise_inst_path, mixed_audio_file, 12, 6, audio_format)
            
            # aidub_audio_volume_file = path_add_postfix(source_audio_file, f"_{rvc_voice}_volume")
            # ffmpeg_volume_control(aidub_audio_file, aidub_audio_volume_file, 12)
            
            if self.has_video:
                source_video_file = self.fm.get_split("Source.video")
                aidub_video_file = path_add_postfix(source_video_file, f"_{rvc_voice}")
                
                ffmpeg_replace_audio(source_video_file, mixed_audio_file, aidub_video_file)
                return aidub_video_file, mixed_audio_file, self.fm.get_all_files()
            else:
                return None, mixed_audio_file, self.fm.get_all_files()       

        except Exception as e:
            logger.error(f"[GradioRVC] gradio_rvc_dubbing - Error transcribing file: {e}")
            gr.Warning(f'{e}')
            return None, None, None     
        
        
       
    def gradio_default(self):
        return [0, 3, 0.3, 1, 0.23, 256, 0.2]


    def gradio_update_voice(self):
        voices = self.rvc.get_voices()
        if len(voices) > 0:
            return gr.update(choices=voices, value=voices[0])
        else:
            return gr.update(choices=voices, value=None)
    
    def gradio_voice_folder(self):
        rvc_voice_folder = os.path.join(os.getcwd(), 'model', 'rvc-voice')
        cmd_open_explorer(rvc_voice_folder)       

