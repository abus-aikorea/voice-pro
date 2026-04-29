import os
import sys
from pathlib import Path
import shutil
import subprocess
import hashlib
import datetime
import time
from datetime import datetime
import re

import structlog
logger = structlog.get_logger()


def sanitize_filename(filename):
    filename = filename.strip()
    
    # 플랫폼별 금지 문자 체크
    import platform
    system = platform.system()
    
    if system == 'Windows':
        invalid_chars = r'[<>:"/\\|?*\x00-\x1f]'
    elif system == 'Darwin':  # macOS
        invalid_chars = r'[/\x00]'
    else:  # Linux
        invalid_chars = r'[/\x00]'
    
    filename = re.sub(invalid_chars, '', filename)
    
    # macOS/Linux에서 금지된 파일명 (., .. 등)
    if filename in ['.', '..']:
        filename = '_' + filename
    
    return filename

def shorten_string(title, max_length = 64):
    title = title.strip()
    
    if len(title) > max_length:
        shortened = f"{title[:max_length//2]}...{title[-(max_length//2-3):]}"
        return shortened
    else:
        return title



def path_shorten(file_path, max_path=None):
    import platform
    system = platform.system()
    
    # 플랫폼별 기본 최대 경로 길이
    if max_path is None:
        if system == 'Windows':
            max_path = 260  # Windows 기본 제한
        else:
            max_path = 4096  # Linux/macOS 일반 제한
    
    folder_path = os.path.dirname(file_path)    
    folder_path_length = len(folder_path)
    
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    sanitized_filename = sanitize_filename(file_name)

    # 파일 이름에 사용할 수 있는 최대 길이 계산
    max_filename = min(max_path - folder_path_length - 8, 128)
    if max_filename < 6:  # 최소한 "a...a.ext" 형태는 되어야 함
        raise ValueError("Path is too long")
    
    # 파일 이름 축약
    shortened_filename = shorten_string(sanitized_filename, 128)
    shortened_file = f"{shortened_filename}{file_extension}"
    new_path = os.path.join(folder_path, shortened_file)
    return new_path
    


def path_add_postfix(file_path: str, postfix: str, ext: str = ""):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    if ext == "":
        new_file_name = f"{file_name}{postfix}{file_extension}"
    else:
        new_file_name = f"{file_name}{postfix}{ext}"
        
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
    return new_file_path

def path_change_ext(file_path: str, ext: str = ".flac"):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    new_file_name = f"{file_name}{ext}"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
    return new_file_path


def path_model_folder():
    script_dir = os.getcwd()
    model_folder = os.path.join(script_dir, 'model')
    # logger.debug(f'[abus_path.py] path_model_folder: {model_folder}')
    
    if not os.path.exists(model_folder):
        os.makedirs(model_folder, exist_ok=True)
    return model_folder
  

def path_workspace_folder():
    script_dir = os.getcwd()
    workspace_folder = os.path.join(script_dir, 'workspace')
    logger.debug(f'[abus_path.py] path_workspace_folder: {workspace_folder}')
    
    if not os.path.exists(workspace_folder):
        os.makedirs(workspace_folder, exist_ok=True)
    return workspace_folder
    
def path_gradio_folder():
    script_dir = os.getcwd()
    gradio_folder = os.path.join(script_dir, 'installer_files', 'gradio')
    logger.debug(f'[abus_path.py] path_gradio_folder: {gradio_folder}')
    
    if not os.path.exists(gradio_folder):
        os.makedirs(gradio_folder, exist_ok=True)
    return gradio_folder

def path_youtube_folder():
    workspace_folder = path_workspace_folder()
    youtube_folder = os.path.join(workspace_folder, 'youtube')
    logger.debug(f'[abus_path.py] path_youtube_folder: {youtube_folder}')
    
    if not os.path.exists(youtube_folder):
        os.makedirs(youtube_folder, exist_ok=True)
    return youtube_folder


def path_live_folder():
    workspace_folder = path_workspace_folder()
    live_folder = os.path.join(workspace_folder, 'live')
    logger.debug(f'[abus_path.py] path_live_folder: {live_folder}')
    
    if not os.path.exists(live_folder):
        os.makedirs(live_folder, exist_ok=True)
    return live_folder


def path_translate_folder():
    workspace_folder = path_workspace_folder()
    translate_folder = os.path.join(workspace_folder, 'translate')
    logger.debug(f'[abus_path.py] path_translate_folder: {translate_folder}')
    
    if not os.path.exists(translate_folder):
        os.makedirs(translate_folder, exist_ok=True)
    return translate_folder

def path_dubbing_folder():
    workspace_folder = path_workspace_folder()
    dubbing_folder = os.path.join(workspace_folder, 'dubbing')
    logger.debug(f'[abus_path.py] path_dubbing_folder: {dubbing_folder}')
    
    if not os.path.exists(dubbing_folder):
        os.makedirs(dubbing_folder, exist_ok=True)
    return dubbing_folder

def path_new_filename(ext: str = ".wav", format: str = "%Y%m%d-%H%M%S"):
    filename = f'{path_time_string(format)}{ext}'
    return filename

# def path_cache_folder(title: str = "abus"):
#     return os.path.join(Path.home(), ".cache", title)

# def path_appdata_roaming_folder(title: str = "aicover"):
#     return os.path.join(os.getenv('APPDATA'), "ABUS", title)

# def path_appdata_local_temp_folder(title: str = ""):
#     return os.path.join(os.getenv('LOCALAPPDATA'), "Temp", title)


def path_subfolders(folder_path: str):
    directories = []
    if not os.path.exists(folder_path):
        return directories
    
    contents = os.listdir(folder_path)
    for item in contents:
        if os.path.isdir(os.path.join(folder_path, item)):
            directories.append(item)
    return directories


def path_subfile(folder_path: str, ext: str = ".pth"):
    if not os.path.exists(folder_path):
        return None
    
    contents = os.listdir(folder_path)
    for item in contents:
        file_name, file_extension = os.path.splitext(os.path.basename(item))
        if file_extension == ext:
            return os.path.join(folder_path, item)
    return None

def path_av_subfiles(folder_path: str):
    audio_exts = ['.mp3', '.aac', '.wav', '.ogg', '.flac', '.m4a', '.opus']
    video_exts = ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.webm', '.wmv', '.mpeg', '.mpg']    
    av_exts = audio_exts + video_exts
    
    files = []
    if not os.path.exists(folder_path):
        return files    
    
    
    contents = os.listdir(folder_path)
    for item in contents:
        file_name, file_extension = os.path.splitext(os.path.basename(item))
        if file_extension.lower() in av_exts:
            av_file = os.path.join(folder_path, item)
            files.append(av_file)
    return files
        

def path_get_hash(file_path, length=12):
    hash_obj = hashlib.md5()
    
    # extension 제외한 부분만 사용
    path_without_extension = os.path.splitext(file_path)[0]
    hash_obj.update(path_without_extension.encode('utf-8'))
    hash_value = hash_obj.hexdigest()
    return hash_value[:length]

def path_time_string(format = "%Y%m%d-%H%M%S"):
    formatted_time = datetime.now().strftime(format)
    return formatted_time


def path_workspace_subfolder(file_path: str):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    
    # hash = path_get_hash(file_name)
    formatted_time = path_time_string()
   
    # folder_name = f'[{formatted_time}] {file_name[:36]}-{hash}'
    shortened_filename = shorten_string(file_name, 32)
    folder_name = f'[{formatted_time}] {shortened_filename}'

    workspace_folder = path_workspace_folder()
    
    sub_folder = os.path.join(workspace_folder, folder_name)
    logger.debug(f'[abus_path.py] path_workspace_subfolder - {sub_folder}')
    
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder, exist_ok=True)
    return sub_folder    


def path_rvc_segments_folder(subtitle_path: str):
    formatted_time = path_time_string()
    folder_path = os.path.dirname(subtitle_path)
    segments_folder = os.path.join(folder_path, f"[{formatted_time}] rvc_segments")
    if not os.path.exists(segments_folder):
        os.makedirs(segments_folder, exist_ok=True)
    return segments_folder

def path_tts_segments_folder(subtitle_path: str):
    formatted_time = path_time_string()
    folder_path = os.path.dirname(subtitle_path)
    segments_folder = os.path.join(folder_path, f"[{formatted_time}] tts_segments")
    if not os.path.exists(segments_folder):
        os.makedirs(segments_folder, exist_ok=True)
    return segments_folder
    
def path_xtts_segments_folder(subtitle_path: str):
    formatted_time = path_time_string()
    folder_path = os.path.dirname(subtitle_path)
    segments_folder = os.path.join(folder_path, f"[{formatted_time}] xtts_segments")
    if not os.path.exists(segments_folder):
        os.makedirs(segments_folder, exist_ok=True)
    return segments_folder
    

def cmd_copy_files(from_files: list, dest_directory: str) -> list:
    to_files = []
    for from_file in from_files:
        from_file_name = os.path.basename(from_file)
        try:
            # 크로스 플랫폼 파일 복사
            if not os.path.exists(dest_directory):
                os.makedirs(dest_directory, exist_ok=True)
            
            if os.path.isdir(from_file):
                # 디렉토리인 경우
                dest_path = os.path.join(dest_directory, from_file_name)
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                shutil.copytree(from_file, dest_path)
                to_file = dest_path
            else:
                # 파일인 경우
                to_file = os.path.join(dest_directory, from_file_name)
                shutil.copy2(from_file, to_file)
            
            logger.debug(f'[abus_path.py] cmd_copy_files: {from_file} -> {to_file}')
            to_files.append(to_file)
        except Exception as e:
            logger.error(f"[abus_path.py] cmd_copy_files - Error copying {from_file}: {e}")
            # 오류가 발생해도 계속 진행
            to_file = os.path.join(dest_directory, from_file_name)
            to_files.append(to_file)
    return to_files
        
def cmd_copy_file_to(from_file: str, to_directory: str):
    from_file_name = os.path.basename(from_file)
    to_file = os.path.join(to_directory, from_file_name)
    
    try:
        if not os.path.exists(to_directory):
            os.makedirs(to_directory, exist_ok=True)
        
        shutil.copy(from_file, to_file)
        logger.debug(f'[abus_path.py] cmd_copy_file_to: {from_file} -> {to_file}')
    except Exception as e:
        logger.error(f"[abus_path.py] cmd_copy_file_to - Error: {e}")
    return to_file  
        
def cmd_copy_file(from_file: str, to_file: str):
    try:        
        shutil.copy(from_file, to_file)
        logger.debug(f'[abus_path.py] cmd_copy_file: {from_file} -> {to_file}')
    except Exception as e:
        logger.error(f"[abus_path.py] cmd_copy_file - Error: {e}")
    return to_file          
        
def cmd_move_file_to(from_file: str, to_directory: str):
    from_file_name = os.path.basename(from_file)
    to_file = os.path.join(to_directory, from_file_name)
    shutil.move(from_file, to_file)
    return to_file


def cmd_rename_file(original_path: str, new_path: str):
    directory, new_filename = os.path.split(new_path)
    if os.path.exists(new_path):
        logger.debug(f'[abus_path.py] cmd_rename_file: already exist {new_path}')
        return new_path    
    
    try:
        shutil.move(original_path, new_path)
    except Exception as e:
        logger.error(f"[abus_path.py] cmd_rename_file - Error: {e}")    
    
    return new_path

def cmd_safe_rename(original_path, new_path):
    directory, new_filename = os.path.split(new_path)
    if os.path.exists(new_path):
        base, extension = os.path.splitext(new_filename)
        counter = 1
        while True:
            new_filename = f"{base}_{counter}{extension}"
            new_path = os.path.join(directory, new_filename)
            if not os.path.exists(new_path):
                break
            counter += 1
    shutil.move(original_path, new_path)
    return new_path
   
def cmd_delete_file(target_file):
    if target_file is None:
        logger.error("[abus_path.py] cmd_delete_file - target_file is None")
        return "Target file is None"
        
    try:
        os.remove(target_file)  # Delete file
        logger.debug(f'[abus_path.py] cmd_delete_file: {target_file} deleted')
        return None  # Deletion successful
    except FileNotFoundError:
        logger.error(f"[abus_path.py] cmd_delete_file - File not found: {target_file}")
        return f"File not found: {target_file}"
    except PermissionError:
        logger.error(f"[abus_path.py] cmd_delete_file - Permission denied: {target_file}")
        return f"Permission denied to delete: {target_file}"
    except Exception as e:
        logger.error(f"[abus_path.py] cmd_delete_file - Error: {e}")
        return f"Error during file deletion: {e}"
        
def cmd_open_explorer(path='.'):
    logger.debug(f'[abus_path.py] cmd_open_explorer: {path}')
    import platform
    system = platform.system()
    
    try:
        if system == 'Windows':
            subprocess.run(['explorer', path], check=True)
        elif system == 'Darwin':  # macOS
            subprocess.run(['open', path], check=True)
        elif system == 'Linux':
            subprocess.run(['xdg-open', path], check=True)
        else:
            print(f"Unsupported platform: {system}")
    except subprocess.CalledProcessError:
        print("Error opening file explorer.")
    except FileNotFoundError:
        print(f"File explorer command not found on {system}.")
        
def cmd_select_folder(default_path='.'):
    import platform
    system = platform.system()
    
    try:
        if system == 'Windows':
            # PowerShell 사용 (기존 코드 유지)
            command = 'powershell -NoProfile -Command "Add-Type -AssemblyName System.windows.forms; $folderBrowser = New-Object System.Windows.Forms.FolderBrowserDialog; $null = $folderBrowser.ShowDialog(); if ($folderBrowser.SelectedPath) { $folderBrowser.SelectedPath }"'
            folder_path = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.PIPE).strip()
        elif system == 'Darwin':  # macOS
            # osascript 사용
            abs_path = os.path.abspath(default_path)
            script = f'tell application "Finder" to return POSIX path of (choose folder with prompt "Select folder" default location POSIX file "{abs_path}")'
            folder_path = subprocess.check_output(['osascript', '-e', script], text=True).strip()
        elif system == 'Linux':
            # zenity 또는 kdialog 사용
            folder_path = None
            try:
                folder_path = subprocess.check_output(['zenity', '--file-selection', '--directory', '--title=Select folder'], text=True).strip()
            except FileNotFoundError:
                try:
                    folder_path = subprocess.check_output(['kdialog', '--getexistingdirectory', default_path], text=True).strip()
                except FileNotFoundError:
                    # 폴백: 터미널 입력
                    folder_path = input(f"Enter folder path (default: {default_path}): ").strip() or default_path
        else:
            # 알 수 없는 플랫폼: 터미널 입력 사용
            folder_path = input(f"Enter folder path (default: {default_path}): ").strip() or default_path
        
        return folder_path or default_path
    except subprocess.CalledProcessError as e:
        logger.error(f"[abus_path.py] cmd_select_folder - Command failed: {e}")
        return default_path
    except Exception as e:
        logger.error(f"[abus_path.py] cmd_select_folder - Error: {e}")
        sys.stderr.flush()
        return default_path


def gradio_file_path(file_obj):
    """Safely extract a file path from a Gradio file component input.
    
    In Gradio 4/5, gr.File(type='filepath') returns a NamedString (str subclass
    with .name). gr.Audio(type='filepath') returns a plain str. This helper
    handles all cases robustly, including legacy file-like objects.
    """
    if file_obj is None:
        return None
    if isinstance(file_obj, str):
        return file_obj
    if hasattr(file_obj, 'name'):
        return file_obj.name
    return str(file_obj)
        
