import os
import requests
import pysubs2

from pydub import AudioSegment
import gradio as gr

from app.abus_genuine import *
from app.abus_path import *
from app.abus_ffmpeg import *
from app.abus_text import *
from app.abus_nlp_spacy import *
from app.abus_audio import *
from app.abus_config import get_minimax_api_key

import structlog
logger = structlog.get_logger()


# Verified MiniMax TTS voice IDs
MINIMAX_VOICES = {
    "English_Graceful_Lady": "English_Graceful_Lady",
    "English_Insightful_Speaker": "English_Insightful_Speaker",
    "English_Radiant_Girl": "English_radiant_girl",
    "English_Persuasive_Man": "English_Persuasive_Man",
    "English_Lucky_Robot": "English_Lucky_Robot",
    "Wise_Woman": "Wise_Woman",
    "Cute_Boy": "cute_boy",
    "Lovely_Girl": "lovely_girl",
    "Friendly_Person": "Friendly_Person",
    "Inspirational_Girl": "Inspirational_girl",
    "Deep_Voice_Man": "Deep_Voice_Man",
    "Sweet_Girl": "sweet_girl",
}

MINIMAX_MODELS = {
    "speech-2.8-hd": "speech-2.8-hd",
    "speech-2.8-turbo": "speech-2.8-turbo",
}


class MiniMaxTTS:
    def __init__(self, model="speech-2.8-hd"):
        self.api_key = get_minimax_api_key()
        self.api_url = "https://api.minimax.io/v1/t2a_v2"
        self.model = model

    def generate_audio(self, text, voice_id, output_file, rate=0, volume=0, pitch=0):
        speed = 1.0 + (rate / 100.0)
        speed = max(0.5, min(2.0, speed))

        vol = 1.0 + (volume / 100.0)
        vol = max(0.1, min(2.0, vol))

        pitch_val = max(-12, min(12, int(pitch / 50)))

        payload = {
            "model": self.model,
            "text": text,
            "voice_setting": {
                "voice_id": voice_id,
                "speed": speed,
                "vol": vol,
                "pitch": pitch_val,
            },
            "audio_setting": {
                "format": "mp3",
            },
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=60)
            response.raise_for_status()
            result = response.json()

            base_resp = result.get("base_resp", {})
            if base_resp.get("status_code", 0) != 0:
                logger.warning(f"[abus_tts_minimax.py] generate_audio - API error: {base_resp.get('status_msg', 'unknown')}")
                return False

            audio_hex = result.get("data", {}).get("audio", "")
            if not audio_hex:
                logger.warning("[abus_tts_minimax.py] generate_audio - empty audio in response")
                return False

            audio_bytes = bytes.fromhex(audio_hex)
            with open(output_file, "wb") as f:
                f.write(audio_bytes)

            success, msg = self._validate_file(output_file)
            if success:
                logger.debug(f"[abus_tts_minimax.py] generate_audio - synthesized for: {text[:50]}")
                return True
            else:
                logger.warning(f"[abus_tts_minimax.py] generate_audio - validation failed: {msg}")
                return False

        except requests.exceptions.RequestException as e:
            logger.warning(f"[abus_tts_minimax.py] generate_audio - request error: {e}")
            return False

    def request_tts(self, line, output_file, voice_id, semitones, speed_factor, volume_factor, audio_format):
        output_voice_file = os.path.join(path_dubbing_folder(), path_new_filename(ext=".mp3"))
        line = AbusText.normalize_text(line)
        if len(line) < 1:
            logger.warning("[abus_tts_minimax.py] request_tts - error: no line")
            return False

        logger.debug(f'[abus_tts_minimax.py] request_tts - line = {line}')

        if not self.generate_audio(line, voice_id, output_voice_file, rate=speed_factor, volume=volume_factor, pitch=semitones):
            logger.warning("[abus_tts_minimax.py] request_tts - error: API returns False")
            return False

        trimed_voice_file = path_add_postfix(output_voice_file, "_trimed")
        AbusAudio.trim_silence_file(output_voice_file, trimed_voice_file)

        ffmpeg_to_stereo(trimed_voice_file, output_file)

        try:
            os.remove(output_voice_file)
            os.remove(trimed_voice_file)
        except Exception as e:
            logger.error(f"[abus_tts_minimax.py] request_tts - error: {e}")
            return False

        return True

    def srt_to_voice(self, subtitle_file, output_file, voice_id, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        tts_subtitle_file = path_add_postfix(subtitle_file, f"-{voice_id}", ".srt")

        AbusSpacy.process_subtitle_for_tts(subtitle_file, tts_subtitle_file)

        segments_folder = path_tts_segments_folder(subtitle_file)
        full_subs = pysubs2.load(tts_subtitle_file, encoding="utf-8")
        subs = full_subs

        combined_audio = AudioSegment.empty()
        for i in progress.tqdm(range(len(subs)), desc='Generating...'):
            line = subs[i]
            next_line = subs[i + 1] if i < len(subs) - 1 else None

            if i == 0:
                silence = AudioSegment.silent(duration=line.start)
                combined_audio += silence

            tts_segment_file = os.path.join(segments_folder, f'tts_{i + 1}.{audio_format}')
            tts_result = self.request_tts(line.text, tts_segment_file, voice_id, semitones, speed_factor, volume_factor, audio_format)

            if tts_result == False:
                if next_line:
                    silence = AudioSegment.silent(duration=next_line.start - line.start)
                    combined_audio += silence
                continue

            combined_audio += AudioSegment.from_file(tts_segment_file)

            if next_line and len(combined_audio) < next_line.start:
                silence_length = next_line.start - len(combined_audio)
                silence = AudioSegment.silent(duration=silence_length)
                combined_audio += silence
            elif next_line:
                next_line.start = len(combined_audio)
                next_line.end = next_line.start + (next_line.end - next_line.start)

        combined_audio.export(output_file, format=audio_format)
        cmd_delete_file(tts_subtitle_file)

    def text_to_voice(self, text, output_file, voice_id, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        segments_folder = path_tts_segments_folder(output_file)

        use_punctuation = AbusText.has_punctuation_marks(text)
        lines = AbusText.split_into_sentences(text, use_punctuation)

        combined_audio = AudioSegment.empty()
        for i in progress.tqdm(range(len(lines)), desc='Generating...'):
            tts_segment_file = os.path.join(segments_folder, f'tts_{i + 1:06}.{audio_format}')
            tts_result = self.request_tts(lines[i], tts_segment_file, voice_id, semitones, speed_factor, volume_factor, audio_format)
            if tts_result == False:
                continue
            combined_audio += AudioSegment.from_file(tts_segment_file)

        combined_audio.export(output_file, format=audio_format)

    def infer(self, text, output_file, voice_id, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        logger.debug(f'[abus_tts_minimax.py] infer - text = {text}')

        subtitle_file = None
        if AbusText.is_subtitle_format(text):
            subs = pysubs2.SSAFile.from_string(text)
            subtitle_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{subs.format}"))
            subs.save(subtitle_file)

        if subtitle_file:
            self.srt_to_voice(subtitle_file, output_file, voice_id, semitones, speed_factor, volume_factor, audio_format, progress)
        else:
            self.text_to_voice(text, output_file, voice_id, semitones, speed_factor, volume_factor, audio_format, progress)

    def _validate_file(self, file_path):
        if not os.path.exists(file_path):
            return False, "File does not exist."

        if not os.path.isfile(file_path):
            return False, "The path is not a file."

        file_size = os.path.getsize(file_path)
        if file_size <= 0:
            return False, "File size is not greater than 0."

        return True, "File is valid."
