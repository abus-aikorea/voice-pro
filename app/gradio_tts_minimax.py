from src.config import UserConfig
from app.abus_path import *
from app.abus_tts_minimax import *
from app.abus_genuine import *
from app.abus_files import *

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
logger = structlog.get_logger()


class GradioMiniMaxTTS:
    def __init__(self, user_config: UserConfig):
        self.user_config = user_config

    def gradio_workspace_folder(self):
        cmd_open_explorer(path_workspace_folder())

    def gradio_temp_folder(self):
        cmd_open_explorer(path_gradio_folder())

    def gradio_upload_file(self, file_obj):
        if file_obj is not None:
            text = self._read_file(file_obj.name)
            return text
        return "No file uploaded"

    def gradio_tts_dubbing(self, text, voice_name, model_name, speed_factor, audio_format='mp3'):
        self.user_config.set("minimax_tts_speed", speed_factor)
        self.user_config.set("audio_format", audio_format)

        logger.debug(f'[gradio_tts_minimax.py] gradio_tts_dubbing - text = {text}, '
                     f'voice_name = {voice_name}, model_name = {model_name}, '
                     f'speed_factor = {speed_factor}, audio_format = {audio_format}')

        input_text = text
        logger.debug(f"[gradio_tts_minimax.py] gradio_tts_dubbing - input_text: {input_text}")

        try:
            voice_id = MINIMAX_VOICES.get(voice_name, voice_name)
            tts = MiniMaxTTS(model=model_name)

            if voice_id and input_text:
                aidub_audio_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{audio_format}"))
                tts.infer(input_text, aidub_audio_file, voice_id, 0, speed_factor, 0, audio_format)
                return aidub_audio_file, aidub_audio_file
            else:
                message = i18n("Error")
                gr.Warning(message)
                return None, None
        except Exception as e:
            logger.error(f"[gradio_tts_minimax.py] gradio_tts_dubbing - error: {e}")
            gr.Warning(f'{e}')
            return None, None

    def _read_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except UnicodeDecodeError:
            return "Error: The file is not a valid text file or uses an unsupported encoding."
        except IOError:
            return "Error: Unable to read the file."
