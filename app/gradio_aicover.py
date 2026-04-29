import json

from src.config import UserConfig
from app.abus_downloader import *
from app.abus_path import *
from app.abus_ffmpeg import *

from app.abus_demucs import *
from app.abus_mdx import *
from app.abus_genuine import *
from app.abus_files import *
from app.abus_aicover import *

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()



class GradioAICover:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        
        self.fm = FileManager()
        self.downloader = YoutubeDownloader()        
                
        self.voice_model_path = os.path.join(os.getcwd(), 'model', 'rvc-voice')
        self.mdxnet_models_dir = os.path.join(os.getcwd(), 'model', 'mdxnet-model')
        with open(os.path.join(self.mdxnet_models_dir, 'model_data.json')) as infile:
            self.mdx_model_params = json.load(infile)

    def open_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def open_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    
    def open_model_folder(self):
        cmd_open_explorer(self.voice_model_path)   

    
    def get_voice_models(self):
        voice_models = path_subfolders(self.voice_model_path)
        if len(voice_models) == 0:
            voice_models = ['No voice model']
        return voice_models    
    
    def update_voice_models(self):
        voice_models = self.get_voice_models()
        return gr.update(choices=voice_models, value=voice_models[0])


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
                            
            # denoise
            self._denoise()

            return self.fm.get_split("Source.video"), self.fm.get_split("Source.audio"), self.fm.get_all_files()
        except Exception as e:
            logger.error(f"[gradio_rvc.py] upload_source - Error transcribing file: {e}")
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
        
    
    def _denoise(self):
        progress = gr.Progress()
        
        output_dir = os.path.dirname(self.source_file)  
            
        progress(0.2, desc=f'Separating vocals and instrumental...')
        mdxnet_voc_ft = os.path.join(self.mdxnet_models_dir, 'UVR-MDX-NET-Voc_FT.onnx')     
        vocals_path, instrumentals_path = run_mdx(self.mdx_model_params, output_dir, mdxnet_voc_ft, self.fm.get_split("Source.audio"), denoise=True, keep_orig=True)

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
    
    
    def make_cover(self, rvc_voice,
            pitch_change, pitch_change_all=0,
            index_rate=0.5, filter_radius=3, rms_mix_rate=0.25, protect=0.33,
            main_vocal_gain = 0, backup_vocal_gain = 0, inst_gain = 0,
            reverb_rm_size=0.15, reverb_wet=0.2, reverb_dry=0.8, reverb_damping=0.7):
        self.user_config.set("rvc_voice", rvc_voice)
        self.user_config.set("pitch_change", pitch_change)
        self.user_config.set("pitch_change_all", pitch_change_all)
        self.user_config.set("index_rate", index_rate)
        self.user_config.set("filter_radius", filter_radius)
        self.user_config.set("rms_mix_rate", rms_mix_rate)
        self.user_config.set("protect", protect)
        self.user_config.set("main_vocal_gain", main_vocal_gain)
        self.user_config.set("backup_vocal_gain", backup_vocal_gain)
        self.user_config.set("inst_gain", inst_gain)
        self.user_config.set("reverb_rm_size", reverb_rm_size)
        self.user_config.set("reverb_wet", reverb_wet)
        self.user_config.set("reverb_dry", reverb_dry)
        self.user_config.set("reverb_damping", reverb_damping)             
        
        try:
            cover_audio_file = self._pipeline(rvc_voice,
                                            pitch_change, pitch_change_all,
                                            index_rate, filter_radius, rms_mix_rate, protect,
                                            main_vocal_gain, backup_vocal_gain, inst_gain,
                                            reverb_rm_size, reverb_wet, reverb_dry, reverb_damping)
            self.fm.set_cover(f'{rvc_voice}.audio', cover_audio_file) 
            
            cover_video_file = path_add_postfix(self.source_file, f"({rvc_voice} Ver)-{int(time.time())}")
            if self.has_video:
                ffmpeg_replace_audio(self.source_file, cover_audio_file, cover_video_file)
                self.fm.set_cover(f'{rvc_voice}.video', cover_video_file)                

            # return video, audio, files
            if(ffmpeg_browser_compatible(cover_video_file)):
                return cover_video_file, cover_audio_file, self.fm.get_all_files()
            else:
                return None, cover_audio_file, self.fm.get_all_files()        
        except Exception as e:
            logger.error(f"[gradio_rvc.py] make_cover - Error transcribing file: {e}")
            gr.Warning(f'{e}')
            return None, None, None
    
    
    def _pipeline(self, rvc_voice,
            pitch_change, pitch_change_all=0,
            index_rate=0.5, filter_radius=3, rms_mix_rate=0.25, protect=0.33,
            main_vocal_gain = 0, backup_vocal_gain = 0, inst_gain = 0,
            reverb_rm_size=0.15, reverb_wet=0.2, reverb_dry=0.8, reverb_damping=0.7):
        
        source_audio_file = self.fm.get_split("Source.audio")
        output_dir = os.path.dirname(self.source_file)
        output_format = self.user_config.get("audio_format", "flac")
        
       
        # if not os.path.exists(ai_vocals_path):
        crepe_hop_length=128
        pitch_change = pitch_change * 12 + pitch_change_all
        main_vocals_dereverb_path = self.fm.get_split("DereverbVocals.audio")

        
        # mono
        ai_vocals_path = os.path.join(output_dir, f'{os.path.splitext(os.path.basename(source_audio_file))[0]}_{rvc_voice}_p{pitch_change}_i{index_rate}_fr{filter_radius}_rms{rms_mix_rate}_pro{protect}_rmvpe.wav')
        rvc_change_voice(main_vocals_dereverb_path, ai_vocals_path, rvc_voice, pitch_change, 'rmvpe', index_rate, filter_radius, rms_mix_rate, protect, crepe_hop_length)        
        
        # vocal effect
        ai_vocals_effect_path = path_add_postfix(ai_vocals_path, "_effect")
        rvc_add_effects(ai_vocals_path, ai_vocals_effect_path, reverb_rm_size, reverb_wet, reverb_dry, reverb_damping)
        
        # instrumental & backup vocal
        instrumentals_path = self.fm.get_split("Instrumental.audio")
        backup_vocals_path = self.fm.get_split("BackupVocals.audio")

        if pitch_change_all != 0:
            instrumental_pitch_audio = path_add_postfix(self.fm.get_split("Instrumental.audio"), f'_p{pitch_change_all}', ".wav")
            rvc_shift_pitch(self.fm.get_split("Instrumental.audio"), instrumental_pitch_audio, pitch_change_all)
            instrumentals_path = instrumental_pitch_audio
            
            backup_pitch_audio = path_add_postfix(self.fm.get_split("BackupVocals.audio"), f'_p{pitch_change_all}', ".wav")
            rvc_shift_pitch(self.fm.get_split("BackupVocals.audio"), backup_pitch_audio, pitch_change_all)
            backup_vocals_path = backup_pitch_audio


        timestamp = int(time.time())
        cover_audio_file = path_add_postfix(source_audio_file, f"({rvc_voice} Ver)-{timestamp}", f'.{output_format}')
        rvc_combine_audio([ai_vocals_effect_path, backup_vocals_path, instrumentals_path], cover_audio_file, main_vocal_gain, backup_vocal_gain, inst_gain, output_format)
        return cover_audio_file        

    def gradio_default_rvc(self):
        return [0, 0, 
                0.5, 3, 0.25, 0.33, 
                0, 0, 0,
                0.15, 0.2, 0.8, 0.7]
