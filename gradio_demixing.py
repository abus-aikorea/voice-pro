from src.config import UserConfig
from app.abus_demucs import *
from app.abus_mdx import *
from app.abus_genuine import *
from app.abus_files import *
from app.abus_hf import AbusHuggingFace

from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()


class GradioDemixing:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        
        self.fm = FileManager()
        self.downloader = YoutubeDownloader()

        self.mdxnet_models_dir = os.path.join(os.getcwd(), 'model', 'mdxnet-model')
        with open(os.path.join(self.mdxnet_models_dir, 'model_data.json')) as infile:
            self.mdx_model_params = json.load(infile) 
    
    
    def open_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def open_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    
    def open_model_folder(self):
        cmd_open_explorer(self.mdxnet_models_dir)        

    
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
            logger.error(f"[gradio_demixing.py] upload_source - Error transcribing file: {e}")
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
        remote_models = AbusHuggingFace.hf_demixing_names(has_local_file=False)
        
        local_dropdown = gr.Dropdown(label=i18n("MDX Models"), choices=local_models, value=self.user_config.get("demixing_model", "htdemucs"))
        remote_dropdown = gr.Dropdown(label=i18n("MDX Models"), choices=remote_models, value=None)
        return local_dropdown, remote_dropdown 

    # return Video, Audio, Video, Audio, File
    def demixing(self,
                 demixing_model, audio_format):
        self.user_config.set("demixing_model", demixing_model)
        self.user_config.set("demixing_audio_format", audio_format)
        
        try:
            self._demixing(demixing_model, audio_format)            
            return self.fm.get_split("Instrumental.video"), self.fm.get_split("Instrumental.audio"), self.fm.get_split("Vocals.video"), self.fm.get_split("Vocals.audio"), self.fm.get_all_files()
        except Exception as e:
            logger.error(f"[gradio_demixing.py] demixing - Error transcribing file: {e}")
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
            
            inst_audio_file = os.path.join(path_workspace_subfolder(input_audio_file), file_name + f"_{demixing_model}_main." + audio_format)
            vocal_audio_file = os.path.join(path_workspace_subfolder(input_audio_file), file_name + f"_{demixing_model}_invert." + audio_format)
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
            
            
    def show_model_info(self, demixing_model):
        model = AbusHuggingFace.hf_get_from_name(demixing_model)
        if model:
            return gr.Textbox(label=i18n("Model information"), value=model.download_info(), interactive=False)
        else:
            return gr.Textbox(label=i18n("Model information"), value=i18n("Select a model to download"), interactive=False)
                
    
    # return Dropdown, Dropdown, Textbox
    def download_model(self,
                       demixing_model):
        # local_dropdown, remote_dropdown = self.update_demixing_models()
        model = AbusHuggingFace.hf_get_from_name(demixing_model)
        if model == None:
            return gr.Textbox(label=i18n("Download Status"), value=i18n("Download Error"), interactive=False)
        
        if model.download():
            return gr.Textbox(label=i18n("Download Status"), value=i18n("OK - Please refresh models"), interactive=False)
        else:
            return gr.Textbox(label=i18n("Download Status"), value=i18n("Download Error"), interactive=False)
