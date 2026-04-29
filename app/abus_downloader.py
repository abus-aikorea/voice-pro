import os
import platform
import gradio as gr
from yt_dlp import YoutubeDL
from yt_dlp.postprocessor import PostProcessor

from app.abus_path import cmd_rename_file, path_shorten

import structlog
logger = structlog.get_logger()


class FilenameCollectorPP(PostProcessor):
    def __init__(self):
        super(FilenameCollectorPP, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information["filepath"])
        return [], information
    

class ExceededMaximumDuration(Exception):
    def __init__(self, videoDuration, maxDuration, message):
        self.videoDuration = videoDuration
        self.maxDuration = maxDuration
        super().__init__(message)    
    
    
class YoutubeDownloader:
    def __init__(self):
        self.progress = gr.Progress()         
        
    def validate_path(self, path):
        try:
            shortened_path = path_shorten(path)
            cmd_rename_file(path, shortened_path)
        except ValueError as e:
            shortened_path = path
            logger.error(f"validate_path - Error: {e}")    

        return shortened_path
        
        
    def dl_progress_hook(self, d):
        if ('status' not in d):
            return
        if ('total_bytes' not in d) and ('total_bytes_estimate' not in d):
            return
        
        try:
            total_bytes = d["total_bytes"] if 'total_bytes' in d else (d["total_bytes_estimate"] if 'total_bytes_estimate' in d else 0)     
            downloaded_bytes = d["downloaded_bytes"]
            
            if d["status"] == "downloading" and total_bytes > 0:
                self.progress(int(downloaded_bytes / total_bytes * 100) / 100.0, desc="YouTube Downloader")
        except Exception as e:
            logger.error(f"[abus_downloader.py] dl_progress_hook - An error occurred: {e}")

   
    def yt_download(self, url: str, download_folder: str, quality: str = "good", maxDuration: int = None):       
        ydl_opts = {}
        ydl_opts['keepvideo'] = False
        ydl_opts['progress_hooks'] = [self.dl_progress_hook]
        ydl_opts['playlist_items'] = '1'
        
        # Enable Node.js JS runtime for YouTube challenge solving
        # (yt-dlp 2026+ only enables Deno by default)
        ydl_opts['js_runtimes'] = {'node': {}}
        ydl_opts['remote_components'] = ['ejs:github']
        
        # User Agent 설정 추가
        ydl_opts['http_headers'] = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }        
        
        system = platform.system()
        if system == "Linux":
            cookiefile_path = os.path.join(os.getcwd(), 'cookies.txt')
            ydl_opts['cookiefile'] = cookiefile_path
                
        
        if quality == "best":
            ydl_opts['format'] = 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/bestvideo[ext=webm][vcodec^=vp9]+bestaudio[ext=webm]/best'
        elif quality == "good":            
            ydl_opts['format'] = 'bestvideo[ext=mp4][vcodec^=avc1][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][vcodec^=avc1][height<=1080]/best'
        elif quality == "low":
            ydl_opts['format'] = 'bestvideo[ext=mp4][vcodec^=avc1][height<=720]+bestaudio[ext=m4a]/best[ext=mp4][vcodec^=avc1][height<=720]/best'

        ydl_opts['outtmpl'] = download_folder + '/%(title)s.f%(format_id)s.%(ext)s'

        filename_collector = FilenameCollectorPP()
        with YoutubeDL(ydl_opts) as ydl:
            # Extract metadata once, then download from the same result
            # to avoid redundant HTTP requests and rate-limiting
            info = ydl.extract_info(url, download=False)
            
            if maxDuration and maxDuration > 0:
                entries = "entries" in info and info["entries"] or [info]
                total_duration = 0

                # Compute total duration
                for entry in entries:
                    total_duration += float(entry["duration"])

                if total_duration >= maxDuration:
                    raise ExceededMaximumDuration(videoDuration=total_duration, maxDuration=maxDuration, message="Video is too long")

            ydl.add_post_processor(filename_collector)
            ydl.process_ie_result(info, download=True)

        if len(filename_collector.filenames) <= 0:
            raise Exception("Cannot download " + url)
        
        
        valid_path = self.validate_path(filename_collector.filenames[0])
        return valid_path
                

                