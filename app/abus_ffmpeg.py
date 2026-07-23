import os
import subprocess
import json
import ffmpeg
import shutil
import gradio as gr
import re
from typing import Optional

import structlog
logger = structlog.get_logger()



def ffmpeg_replace_audio(input_path: str, audio_path: str, output_path: str, progress = gr.Progress(), shortest: bool = True):
    _, file_extension = os.path.splitext(os.path.basename(input_path))
    shortest_option = " -shortest" if shortest else ""
    
    if file_extension == ".mp4":
        command = f'ffmpeg -y -i "{input_path}" -i "{audio_path}" -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac{shortest_option} "{output_path}" -nostdin'
    elif file_extension == ".webm":
        command = f'ffmpeg -y -i "{input_path}" -i "{audio_path}" -c:v copy -map 0:v:0 -map 1:a:0 -c:a libopus{shortest_option} "{output_path}" -nostdin'
    else:
        command = f'ffmpeg -y -i "{input_path}" -i "{audio_path}" -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac{shortest_option} "{output_path}" -nostdin'        
        
    logger.debug(f'[abus:ffmpeg_replace_audio] {command}')
    os.system(command)
    return output_path


def ffmpeg_extract_audio(input_path: str, output_path: str, audio_format: str = "wav"):  
    encoding_options = "-acodec pcm_s16le -ar 48000 -b:a 320k -ac 2"
    if audio_format=="flac":
        encoding_options = "-acodec flac -ar 48000 -compression_level 0 -ac 2"
    elif audio_format=="mp3":
        encoding_options = "-f mp3 -qscale:a 0 -ar 48000 -ac 2"    # -ar 48000 -ab 320k
    elif audio_format=="ogg":
        encoding_options = "-acodec libvorbis -ar 48000 -b:a 320k -ac 2"
      
    command = f'ffmpeg -y -i "{input_path}" -vn {encoding_options} "{output_path}" -nostdin'    
    logger.debug(f'[abus:ffmpeg_extract_audio] {command}')
    os.system(command)  
    return output_path    


def ffmpeg_codec_type(input_path: str):
    has_video = False
    has_audio = False
    
    
    # 입력 파일 존재 확인
    if not os.path.exists(input_path):
        logger.error(f'[abus:ffmpeg_codec_type] Input file not found: {input_path}')
        return has_audio, has_video
    
    # ffprobe 존재 확인
    ffprobe_path = shutil.which('ffprobe')
    if not ffprobe_path:
        logger.error('[abus:ffmpeg_codec_type] ffprobe not found in system PATH')
        return has_audio, has_video    
    
    # 명령어를 리스트로 구성
    input_path_encoded = input_path.encode('utf-8')  # 파일명 UTF-8로 인코딩
    command = [
        'ffprobe',
        '-loglevel', 'error',
        '-show_entries', 'stream=codec_type',
        '-of', 'json',
        input_path_encoded
    ]
    logger.debug(f'[abus:ffmpeg_codec_type] command = {command}')
    
    try:       
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8',  # UTF-8 인코딩 명시
            check=True  # 에러 발생 시 CalledProcessError 발생
        )
        
        logger.debug(f'[abus:ffmpeg_codec_type] result.stdout = {result.stdout}')
        data = json.loads(result.stdout)
        
        if "streams" in data:
            for stream in data["streams"]:
                if stream["codec_type"] == "video":
                    has_video = True
                elif stream["codec_type"] == "audio":
                    has_audio = True
                    
    except subprocess.CalledProcessError as e:
        logger.error(f'[abus:ffmpeg_codec_type] ffprobe execution failed: {e.stderr}')
    except json.JSONDecodeError as e:
        logger.error(f'[abus:ffmpeg_codec_type] JSON parsing error: {e}')
    except Exception as e:
        logger.error(f'[abus:ffmpeg_codec_type] Unexpected error: {str(e)}')
    
    return has_audio, has_video


def ffmpeg_browser_compatible(input_path):
    # 입력 파일 존재 확인
    if not os.path.exists(input_path):
        logger.error(f'[abus:ffmpeg_browser_compatible] Input file not found: {input_path}')
        return False
    
    # ffprobe 존재 확인
    ffprobe_path = shutil.which('ffprobe')
    if not ffprobe_path:
        logger.error('[abus:ffmpeg_browser_compatible] ffprobe not found in system PATH')
        return False    
    
    # 명령어를 리스트로 구성
    input_path_encoded = input_path.encode('utf-8')  # 파일명 UTF-8로 인코딩
    command = [
        "ffprobe",
        "-v", "quiet",  # 필요에 따라 -v error 등으로 변경 가능
        "-print_format", "json",
        "-show_streams",
        "-show_format",
        input_path_encoded  # 인코딩된 경로 사용
    ]
    logger.debug(f'[abus:ffmpeg_browser_compatible] command = {command}')
            
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8',  # UTF-8 인코딩 명시
            check=True  # 에러 발생 시 CalledProcessError 발생
        )

        logger.debug(f'[abus:ffmpeg_browser_compatible] result.stdout = {result.stdout}')
        probe = json.loads(result.stdout)

        video_info = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        audio_info = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)

        if not video_info or not audio_info:  # video 또는 audio stream이 없는 경우
            logger.warning(f"[abus:ffmpeg_browser_compatible] No video or audio stream found in {input_path}")
            return False

        fmt = probe['format']['format_long_name']
        vcodec = video_info['codec_name']
        acodec = audio_info['codec_name']
        logger.debug(f'ffmpeg_info: {fmt}, {vcodec}, {acodec}')

        # 브라우저 호환성 확인
        if (vcodec == 'h264' and acodec == 'aac') or ((vcodec == 'vp8' or vcodec == 'vp9') and (acodec == 'opus' or acodec == 'vorbis')):
            logger.debug(f'[abus:ffmpeg_browser_compatible] ffmpeg_browser_compatible: YES')
            return True
        else:
            logger.debug(f'[abus:ffmpeg_browser_compatible] ffmpeg_browser_compatible: NO')
            return False

    except subprocess.CalledProcessError as e:
        logger.error(f"[abus:ffmpeg_browser_compatible] - Error occurred: {e}")
        logger.error(f"[abus:ffmpeg_browser_compatible] - stderr output: {e.stderr}")
        return False
    except json.JSONDecodeError as e:
        logger.error(f"[abus:ffmpeg_browser_compatible] - Error occurred: Invalid JSON output from ffmpeg: {e}")
        logger.error(f"[abus:ffmpeg_browser_compatible] - ffmpeg output: {result.stdout if 'result' in locals() else 'N/A'}") # ffmpeg 출력을 로깅
        return False
    except Exception as e:
        logger.error(f"[abus:ffmpeg_browser_compatible] - Error occurred: {e}")
        return False

    
# audio_gain1, audio_gain2: decibel 
def ffmpeg_mix_audio(audio_path1: str, audio_path2: str, output_path: str, audio_gain1: float, audio_gain2:float, audio_format: str = "flac"):   
    volume1 = f"{audio_gain1}dB"
    volume2 = f"{audio_gain2}dB"
    
    filter_complex = f'[0:a]volume={volume1}[a0];[1:a]volume={volume2}[a1];[a0][a1]amix=inputs=2:duration=longest'
    
    encoding_options = "-c:a pcm_s16le -ar 48000 -b:a 320k -ac 2"
    if audio_format=="flac":
        encoding_options = "-c:a flac -ar 48000 -compression_level 0 -ac 2"
    elif audio_format=="mp3":
        encoding_options = "-c:a libmp3lame -qscale:a 0 -ar 48000 -ac 2"      # -ar 48000 -ab 320k
    elif audio_format=="ogg":
        encoding_options = "-c:a libvorbis -ar 48000 -b:a 320k -ac 2"    
    
    command = f'ffmpeg -y -i "{audio_path1}" -i "{audio_path2}" -filter_complex "{filter_complex}" {encoding_options} "{output_path}" -nostdin'
    logger.debug(f'[abus:ffmpeg_mix_audio] {command}')
    os.system(command)



def ffmpeg_convert_audio(input_path: str, output_path: str, audio_format: str):
    encoding_options = "-c:a pcm_s16le -ar 48000 -b:a 320k -ac 2"
    if audio_format=="flac":
        encoding_options = "-c:a flac -ar 48000 -compression_level 0 -ac 2"
    elif audio_format=="mp3":
        encoding_options = "-c:a libmp3lame -qscale:a 0 -ar 48000 -ac 2"      # -ar 48000 -ab 320k
    elif audio_format=="ogg":
        encoding_options = "-c:a libvorbis -ar 48000 -b:a 320k -ac 2"
        
    command = f'ffmpeg -y -i "{input_path}" {encoding_options} "{output_path}" -nostdin'             
    logger.debug(f'[abus:ffmpeg_convert_audio] {command}')
    os.system(command)



def ffmpeg_to_mono(input_path: str, left_path: str, right_path: str, audio_format: str = "wav"):
    filter_complex = "[0:a]channelsplit=channel_layout=stereo[left][right]"
    
    encoding_options = "-c:a pcm_s16le -ar 48000 -b:a 320k"
    if audio_format=="flac":
        encoding_options = "-c:a flac -ar 48000 -compression_level 0"
    elif audio_format=="mp3":
        encoding_options = "-c:a libmp3lame -qscale:a 0 -ar 48000"    # -ar 48000 -ab 320k
    elif audio_format=="ogg":
        encoding_options = "-c:a libvorbis -ar 48000 -b:a 320k"    

    command = f'ffmpeg -y -i "{input_path}" -filter_complex "{filter_complex}" -map "[left]" {encoding_options} "{left_path}" -map "[right]" {encoding_options} "{right_path}"'
    logger.debug(f'[abus:ffmpeg_to_mono] {command}')
    os.system(command)



def ffmpeg_to_stereo(left_path, right_path, stereo_path):
    file_name, file_extension = os.path.splitext(os.path.basename(stereo_path))
    ext = file_extension.lower()
    
    
    filter_complex = "[0:a][1:a]join=inputs=2:channel_layout=stereo[a]"
    # filter_complex = "[0:a][1:a]amerge=inputs=2[a]"
    
    encoding_options = "-c:a pcm_s16le -ar 48000 -b:a 320k -ac 2"
    if ext==".flac":
        encoding_options = "-c:a flac -ar 48000 -compression_level 0 -ac 2"
    elif ext==".mp3":
        encoding_options = "-c:a libmp3lame -qscale:a 0 -ar 48000 -ac 2"    # -ar 48000 -ab 320k
    elif ext==".ogg":
        encoding_options = "-c:a libvorbis -ar 48000 -b:a 320k -ac 2"        
    
    command = f'ffmpeg -y -i "{left_path}" -i "{right_path}" -filter_complex "{filter_complex}" -map "[a]" {encoding_options} "{stereo_path}"'
    logger.debug(f'[abus:ffmpeg_to_stereo] {command}')
    os.system(command)
    return True


def ffmpeg_to_stereo(mono_path, stereo_path):
    file_name, file_extension = os.path.splitext(os.path.basename(stereo_path))
    ext = file_extension.lower()    
    
    encoding_options = "-c:a pcm_s16le -ar 48000 -b:a 320k -ac 2"
    if ext==".flac":
        encoding_options = "-c:a flac -ar 48000 -compression_level 0 -ac 2"
    elif ext==".mp3":
        encoding_options = "-c:a libmp3lame -qscale:a 0 -ar 48000 -ac 2"    # -ar 48000 -ab 320k
    elif ext==".ogg":
        encoding_options = "-c:a libvorbis -ar 48000 -b:a 320k -ac 2"        
    
    command = f'ffmpeg -y -i "{mono_path}" {encoding_options} "{stereo_path}"'
    logger.debug(f'[abus:ffmpeg_to_stereo] {command}')
    os.system(command)
    return True

# audio_gain: decibel 
def ffmpeg_volume_control(input_path: str, output_path: str, audio_gain: float):
    volume = f"{audio_gain}dB"
    encoding_options = f'-filter:a "volume={volume}"'
        
    command = f'ffmpeg -y -i "{input_path}" {encoding_options} "{output_path}" -nostdin'             
    logger.debug(f'[abus:ffmpeg_volume_control] {command}')
    os.system(command)
    
    
def ffmpeg_trim_seconds(input_path: str, output_path: str, seconds: float):
    command = f'ffmpeg -y -ss 00:00:00 -i "{input_path}" -t {seconds} -c copy "{output_path}"'
    logger.debug(f'[abus:ffmpeg_trim_seconds] {command}')
    os.system(command)
    return True


def ffmpeg_video_resolution(input_path):
    # 입력 파일 존재 확인
    if not os.path.exists(input_path):
        logger.error(f'[abus:ffmpeg_video_resolution] Input file not found: {input_path}')
        return None
    
    # ffprobe 존재 확인
    ffprobe_path = shutil.which('ffprobe')
    if not ffprobe_path:
        logger.error('[abus:ffmpeg_video_resolution] ffprobe not found in system PATH')
        return None
    

    # 명령어를 리스트로 구성
    input_path_encoded = input_path.encode('utf-8')  # 파일명 UTF-8로 인코딩    
    command = [
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height',
        input_path_encoded
    ]
    logger.debug(f'[abus:ffmpeg_video_resolution] command = {command}')
            
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8',  # UTF-8 인코딩 명시
            check=True  # 에러 발생 시 CalledProcessError 발생
        )
        
        # JSON 파싱
        logger.debug(f'[abus:ffmpeg_video_resolution] result.stdout = {result.stdout}')
        data = json.loads(result.stdout)
        
        # 비디오 스트림 정보 추출
        if 'streams' in data and len(data['streams']) > 0:
            stream = data['streams'][0]
            width = stream.get('width')
            height = stream.get('height')
            return (width, height)
            
        return None
        
    except Exception as e:
        logger.error(f"[abus:ffmpeg_video_resolution] Unexpected error: {str(e)}")
        return None
    
    
def ffmpeg_get_fps(input_path):
    # 입력 파일 존재 확인
    if not os.path.exists(input_path):
        logger.error(f'[abus:ffmpeg_get_fps] Input file not found: {input_path}')
        return 0
    
    input_path_encoded = input_path.encode('utf-8')  # 파일명 UTF-8로 인코딩    
    command = ['ffmpeg', 
               '-i', 
               input_path_encoded
               ]
    logger.debug(f'[abus:ffmpeg_get_fps] command = {command}')        
    
    try:
        result = subprocess.run(command, 
                                capture_output=True,
                                text=True,
                                encoding='utf-8',  # UTF-8 인코딩 명시
                                check=True  # 에러 발생 시 CalledProcessError 발생
                            )                                
        
        logger.debug(f'[abus:ffmpeg_get_fps] result.stdout = {result.stdout}')
        fps_match = re.search(r'(\d+\.?\d*) fps', result.stdout)
        if fps_match:
            return float(fps_match.group(1))
        else:
            raise ValueError(f"FPS information not found in {input_path}")
            
    except Exception as e:
        logger.error(f"[abus:ffmpeg_get_fps] Unexpected error: {str(e)}")
        return 0    
    
    
def ffmpeg_change_fps(input_path, output_path, target_fps):
    if not os.path.exists(input_path):
        logger.error(f'[abus:ffmpeg_change_fps] Input file not found: {input_path}')
        return False
    
    input_path_encoded = input_path.encode('utf-8')  # 파일명 UTF-8로 인코딩
    output_path_encoded = output_path.encode('utf-8')  # 파일명 UTF-8로 인코딩
    command = [
        'ffmpeg',
        '-y',  # 기존 파일 덮어쓰기 옵션 추가
        '-i', input_path_encoded,
        '-r', str(target_fps),
        '-c:v', 'libx264',
        '-crf', '18',
        '-preset', 'slow',
        '-c:a', 'copy',
        output_path_encoded
    ]
    logger.debug(f'[abus:ffmpeg_change_fps] command = {command}')
        
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8',  # UTF-8 인코딩 명시
            check=True  # 에러 발생 시 CalledProcessError 발생
        )
        logger.debug(f'[abus:ffmpeg_change_fps] result.stdout = {result.stdout}')
                
        logger.info(f"Successfully changed FPS of {input_path} to {target_fps}")
        return True
        
    except Exception as e:
        logger.error(f"[abus:ffmpeg_change_fps] Unexpected error: {str(e)}")
        return False    


def ffmpeg_get_duration(input_path):
    if not os.path.exists(input_path):
        logger.error(f'[abus:ffmpeg_get_duration] Input file not found: {input_path}')
        return 0

    input_path_encoded = input_path.encode('utf-8')  # 파일명 UTF-8로 인코딩
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        input_path_encoded
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8',  # UTF-8 인코딩 명시
            check=True  # 에러 발생 시 CalledProcessError 발생
        )
        logger.debug(f'[abus:ffmpeg_media_duration] result.stdout = {result.stdout}')        
        duration = float(result.stdout)
        return duration

    except Exception as e:
        logger.error(f"[abus:ffmpeg_media_duration] Unexpected error: {str(e)}")
        return 0



def ffmpeg_compress_video(
    input_path: str, 
    output_path: str, 
    target_size_mb: Optional[int] = None,
    crf: int = 23,
    preset: str = 'medium'
    ) -> bool:
    """
    비디오 파일을 압축합니다.
    
    Args:
        input_path (str): 입력 비디오 파일 경로
        output_path (str, optional): 출력 비디오 파일 경로. 
                                    지정하지 않으면 입력 파일 이름에 '_compressed' 추가
        target_size_mb (int, optional): 원하는 최대 파일 크기 (MB)
        crf (int): 압축 품질 조절 (0-51, 낮을수록 고품질. 디폴트 23)
        preset (str): 압축 속도와 효율성 조절 (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)
    
    Returns:
        bool: 압축 성공 여부
    """
    if not os.path.exists(input_path):
        logger.error(f'[abus:ffmpeg_compress_video] Input file not found: {input_path}')
        return False
    
    input_path_encoded = input_path.encode('utf-8')  # 파일명 UTF-8로 인코딩
    output_path_encoded = output_path.encode('utf-8')  # 파일명 UTF-8로 인코딩

    # 기본 FFmpeg 압축 명령어
    command = [
        'ffmpeg', 
        '-y',  # 기존 파일 덮어쓰기
        '-i', input_path_encoded,
        '-vcodec', 'libx264',  # H.264 비디오 코덱
        '-acodec', 'aac',  # AAC 오디오 코덱
        '-crf', str(crf),  # 압축 품질 (0-51)
        '-preset', preset,  # 압축 속도/효율성
        '-pix_fmt', 'yuv420p',  # 호환성을 위한 픽셀 포맷
    ]

    try:
        # 목표 파일 크기가 지정된 경우
        if target_size_mb:
            # 현재 파일 크기 확인
            original_size = os.path.getsize(input_path) / (1024 * 1024)  # MB 단위
            
            # 목표 크기에 따라 CRF 값 동적 조정
            if original_size > target_size_mb:
                # 대략적인 CRF 조정 로직 (실제 결과는 다를 수 있음)
                adjust_factor = original_size / target_size_mb
                new_crf = min(max(int(crf * adjust_factor), 0), 51)
                command[command.index('-crf') + 1] = str(new_crf)
                logger.info(f"Adjusted CRF to {new_crf} for target size {target_size_mb}MB")
        
        # 최종 출력 경로 추가
        command.append(output_path_encoded)
        logger.debug(f'[abus:ffmpeg_compress_video] command = {command}')        
        
        # FFmpeg 실행
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8',  # UTF-8 인코딩 명시
            check=True  # 에러 발생 시 CalledProcessError 발생
        )
        logger.debug(f'[abus:ffmpeg_compress_video] result.stdout = {result.stdout}')
        
        # 압축 결과 로깅
        original_size = os.path.getsize(input_path) / (1024 * 1024)
        compressed_size = os.path.getsize(output_path) / (1024 * 1024)
        
        logger.info(f"Compression complete:")
        logger.info(f"Original size: {original_size:.2f} MB")
        logger.info(f"Compressed size: {compressed_size:.2f} MB")
        logger.info(f"Size reduction: {(1 - compressed_size/original_size)*100:.2f}%")
        return True
    
    except Exception as e:
        logger.error(f"[abus:ffmpeg_compress_video] - Error occurred: {e}")
        return False   
