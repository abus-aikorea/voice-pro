from src.config import UserConfig
from app.abus_downloader import *
from app.abus_path import *
from app.abus_ffmpeg import *

from app.abus_genuine import *
from app.abus_files import *
from app.abus_vsr import *

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()



class GradioVSR:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config
        
        self.fm = FileManager()
        self.downloader = YoutubeDownloader()
        self.maxine_sdk_path = os.path.join(os.getcwd(), 'model', 'maxine', 'sdk')
                

    def open_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())
    
    def open_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())
    

    # return Video, File    
    def upload_source(self, 
                      file_obj, youtube_url: str, video_quality: str, audio_format: str):
        self.user_config.set("video_quality", video_quality)
        self.user_config.set("audio_format", audio_format)

        try:
            logger.debug(f'upload_source: file_obj={file_obj}, youtube_url={youtube_url}')
            self.fm = FileManager()
            if self._upload(file_obj, youtube_url, video_quality, audio_format) == False:
                return None, None

            return self.fm.get_split("Source.video"), self.fm.get_all_files()
        except Exception as e:
            logger.error(f"[gradio_vsr.py] upload_source - Error transcribing file: {e}")
            gr.Warning(f'{e}')
            return None, None
    
    
    def _upload(self,
                file_obj, youtube_url: str, video_quality: str, audio_format: str):
        if (file_obj is not None):
            uploaded_file = cmd_copy_file_to(gradio_file_path(file_obj), path_workspace_subfolder(gradio_file_path(file_obj)))
        elif youtube_url and youtube_url.strip():
            youtube_file = self.downloader.yt_download(youtube_url, path_youtube_folder(), video_quality)
            uploaded_file = cmd_copy_file_to(youtube_file, path_workspace_subfolder(youtube_file))
        else:
            return False
        
        self.source_file = uploaded_file
        
        self.has_audio, self.has_video = ffmpeg_codec_type(self.source_file)
        logger.debug(f'upload_source: source_file={self.source_file}, has_audio={self.has_audio}, has_video={self.has_video}')
        if self.has_video == False:   # audio-only
            return False
        else:
            self.fm.set_split("Source.video", self.source_file)
            if self.has_audio == True:
                input_audio_file = path_change_ext(self.source_file, f'.{audio_format}')
                ffmpeg_extract_audio(self.source_file, input_audio_file, audio_format)    
                self.fm.set_split("Source.audio", input_audio_file)
            return True       
        
    def run_rtx(self, var_enable, var_mode, vsr_enable, vsr_mode, vsr_scale, compression_enable, compression_crf, compression_preset):
        self.user_config.set("var_enable", var_enable)
        self.user_config.set("var_mode", var_mode)     
        self.user_config.set("vsr_enable", vsr_enable)               
        self.user_config.set("vsr_mode", vsr_mode)
        self.user_config.set("vsr_scale", vsr_scale)        
        self.user_config.set("compression_enable", compression_enable)        
        self.user_config.set("compression_crf", compression_crf)
        self.user_config.set("compression_preset", compression_preset)  
        
        try:            
            if self.has_video == False:
                logger.error(f"[gradio_vsr.py] run_maxine - invalid video")
                return None, None
            
            
            working_file = os.path.join(path_gradio_folder(), path_new_filename(ext = f".mkv", format = "%Y%m%d-%H%M%S%f"))
            cmd_copy_file(self.source_file, working_file)
            
            input_temp_file = working_file
            output_var_file = None
            output_vsr_file = None
            output_compress_file = None
            
            if var_enable:
                output_var_file = path_add_postfix(working_file, "_var")
                
                success = self.video_artifact_reduction(working_file, output_var_file, var_mode)
                if success == False:
                    logger.error(f"[gradio_vsr.py] video_artifact_reduction - failed")
                    return None, None
                else:
                    working_file = output_var_file
                    
            if vsr_enable:
                output_vsr_file = path_add_postfix(working_file, "_vsr")
                vsr_scale = float(vsr_scale)
                
                success = self.video_super_res(working_file, output_vsr_file, vsr_mode, vsr_scale)
                if success == False:
                    logger.error(f"[gradio_vsr.py] video_super_res - failed")
                    return None, None
                else:
                    working_file = output_vsr_file  
                    
            if compression_enable:
                output_compress_file = path_add_postfix(working_file, "_compress")    
                success = self.video_compress(working_file, output_compress_file, None, int(compression_crf), compression_preset)
                if success == False:
                    logger.error(f"[gradio_vsr.py] video_compress - failed")
                    return None, None
                else:
                    working_file = output_compress_file           

            # fps_a = ffmpeg_get_fps(self.source_file)
            # ffmpeg_change_fps(output_vsr_file, output_path, fps_a)
            
            output_path = path_add_postfix(self.source_file, "_rtx")
            if self.has_audio == True:
                input_audio_file = self.fm.get_split("Source.audio")
                ffmpeg_replace_audio(working_file, input_audio_file, output_path)
            else:
                cmd_copy_file(working_file, output_path) 
                
                
            # clean
            if input_temp_file: cmd_delete_file(input_temp_file)
            if output_var_file: cmd_delete_file(output_var_file)
            if output_vsr_file: cmd_delete_file(output_vsr_file)  
            if output_compress_file: cmd_delete_file(output_compress_file)      

            self.fm.set_effect("rtx", output_path)
            return output_path, self.fm.get_all_files()
            
        except Exception as e:
            logger.error(f"[gradio_vsr.py] run_maxine - Video processing failed: {str(e)}")
            gr.Warning(f'{e}')
            return None, None
        
        
    def gradio_default_rtx(self):
        return [False, 0, True, 0, 2, True, 23, "medium"]
    
    

    def video_artifact_reduction(self, input_path, output_path, var_mode):

        def update_progress(output, progress):
            try:
                progress_str = output.strip()
                cleaned_str = progress_str.replace("%", "").replace(" ", "")
                match = re.search(r"\d+", cleaned_str)
                if match:
                    percentage = int(match.group(0))
                    if progress is not None and (percentage >= 0 and percentage <= 100): 
                        progress(float(percentage) / 100.0, desc="VideoArtifactReduction")
            except (ValueError, IndexError):
                pass

        with gr.Blocks() as demo:  
            progress = gr.Progress()            
            progress_callback_lambda = lambda output: update_progress(output, progress)
            return_code = vsr_artifact_reduction(self.maxine_sdk_path, input_path, output_path, var_mode, progress_callback_lambda)
            
            if return_code == True:
                return True
            else:
                logger.error(f'[gradio_vsr.py] video_artifact_reduction - return_code = {return_code}')
                return False            
            

    def _supported_scales(self, resolution):
        if resolution < 90:
            return []
        elif resolution <= 540:
            return [4/3, 1.5, 2, 3, 4]
        elif resolution <= 720:
            return [4/3, 1.5, 2, 3]
        elif resolution <= 2160:
            return [4/3, 1.5, 2]
        else:
             return []   
         
    def _supported_resolution(self, input_path, vsr_scale):
        resolution = ffmpeg_video_resolution(input_path)
        if resolution is None:
            logger.warning(f"[gradio_vsr.py] _supported_resolution - invalid resolution")
            return None        

        width, height = resolution        
        _supported_scales = self._supported_scales(height)
        if len(_supported_scales) == 0:
            logger.warning(f"[gradio_vsr.py] _supported_resolution - invalid resolution")
            return None

        if vsr_scale in _supported_scales:
            vsr_resolution = height * vsr_scale
        else:
            vsr_resolution = height * _supported_scales[-1]
            logger.warning(f"[gradio_vsr.py] _supported_resolution - change target resolution to {vsr_resolution}")
        return vsr_resolution
    
    

    def video_super_res(self, input_path, output_path, vsr_mode, vsr_scale):
        vsr_resolution = self._supported_resolution(input_path, vsr_scale)
        if vsr_resolution == None:
            logger.error(f'[gradio_vsr.py] video_super_res - vsr_resolution is None')
            return False            


        def update_progress(output, progress):
            try:
                progress_str = output.strip()
                cleaned_str = progress_str.replace("%", "").replace(" ", "")
                match = re.search(r"\d+", cleaned_str)
                if match:
                    percentage = int(match.group(0))
                    if progress is not None and (percentage >= 0 and percentage <= 100): 
                        progress(float(percentage) / 100.0, desc="VideoSuperRes")
            except (ValueError, IndexError):
                pass

        with gr.Blocks() as demo:  
            progress = gr.Progress()            
            progress_callback_lambda = lambda output: update_progress(output, progress)            
            return_code = vsr_super_res(self.maxine_sdk_path, input_path, output_path, vsr_mode, vsr_resolution, progress_callback_lambda)
            
            if return_code == True:
                return True
            else:
                logger.error(f'[gradio_vsr.py] video_super_res - return_code = {return_code}')
                return False
            

    def video_compress(self, input_path, output_path, 
                       target_size_mb: Optional[int] = None,
                       crf: int = 23,
                       preset: str = 'medium'):
        
        total_seconds = ffmpeg_get_duration(input_path)

        def update_progress(output, progress):
            try:
                progress_str = output.strip()
                if progress_str is None or progress_str.strip() == "":
                    pass

                match = re.search(r"frame=\s*(\d+)\s+fps=\s*([\d.]+)\s+.*time=([\d:]+).*speed=([\d.]+)x", progress_str)
                if match:
                    # frame = int(match.group(1))
                    # fps = float(match.group(2))
                    time_str = match.group(3)
                    # speed = float(match.group(4))

                    h, m, s = map(int, time_str.split(':'))
                    time_seconds = h * 3600 + m * 60 + s                   
                    percentage = (time_seconds / total_seconds) * 100.0
                    if progress is not None and (percentage >= 0 and percentage <= 100.0): 
                        progress(float(percentage) / 100.0, desc="VideoCompression")

                match = re.search(r"\[out#0/.*] video:(\d+)KiB.*Lsize=\s*(\d+)KiB", progress_str) # Lsize 추가
                if match:
                    # video_size = int(match.group(1))
                    # total_size = int(match.group(2)) # total size 추가
                    progress(1.0, desc="VideoCompression")

            except (ValueError, IndexError):
                pass

        with gr.Blocks() as demo:  
            progress = gr.Progress()            
            progress_callback_lambda = lambda output: update_progress(output, progress)
            return_code = vsr_compress_video(input_path, output_path, target_size_mb, crf, preset, progress_callback_lambda)
            if return_code == True:
                return True
            else:
                logger.error(f'[gradio_vsr.py] video_super_res - return_code = {return_code}')
                return False

