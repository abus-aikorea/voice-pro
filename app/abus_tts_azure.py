import pysubs2

from pydub import AudioSegment
import gradio as gr

from app.abus_genuine import *
from app.abus_path import *
from app.abus_ffmpeg import *
from app.abus_text import *
from app.abus_nlp_spacy import *
from app.abus_audio import *
from app.abus_config import get_azure_speech_key, get_azure_speech_region

import azure.cognitiveservices.speech as speechsdk

import structlog
logger = structlog.get_logger()


class AzureTTS:
    def __init__(self):
        speech_key = get_azure_speech_key()
        service_region = get_azure_speech_region()
        self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        

    def speech_synthesis_get_available_voices(self):
        """gets the available voices list."""

        # Creates a speech synthesizer.
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=None)

        logger.debug("Enter a locale in BCP-47 format (e.g. en-US) that you want to get the voices of, or enter empty to get voices in all locales.")
        try:
            text = input()
        except EOFError:
            pass

        result = speech_synthesizer.get_voices_async(text).get()
        # Check result
        if result.reason == speechsdk.ResultReason.VoicesListRetrieved:
            logger.debug('Voices successfully retrieved, they are:')
            for voice in result.voices:
                print(voice.name)
        elif result.reason == speechsdk.ResultReason.Canceled:
            print("Speech synthesis canceled; error details: {}".format(result.error_details))
    
    # Voice styles and roles
    # https://learn.microsoft.com/ko-kr/azure/ai-services/speech-service/speech-synthesis-markup-voice
    # https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#voice-styles-and-roles
    def generate_audio(self, text, voice, output_file, rate=0, volume=0, pitch=0):
        rate_options = f'+{rate}%' if rate>=0 else f'{rate}%'
        volume_options = f'+{volume}%' if volume>=0 else f'{volume}%'
        pitch_options = f'+{pitch}Hz' if pitch>= 0 else f'{pitch}Hz'
        
        self.speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio48Khz192KBitRateMonoMp3)     # Riff48Khz16BitMonoPcm   
        audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
               
        # SSML을 사용하여 prosody 설정
        logger.debug(f'voice = {voice}')
        ssml = f"""
        <speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" version="1.0" xml:lang="en-US">
            <voice name="{voice}">
                <prosody rate="{rate_options}" volume="{volume_options}" pitch="{pitch_options}">
                    {text}
                </prosody>
            </voice>
        </speak>
        """
        result = synthesizer.speak_ssml_async(ssml).get()
        
        # Checks result.
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            success, msg = self._validate_file(output_file)
            if True == success:
                logger.debug("Speech synthesized to speaker for text [{}]".format(text))
                return True
            else:
                logger.warning(f"Speech synthesis for '{text}' failed. reason: {msg}")
                return False
                
        
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            logger.debug("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
            logger.warning("Did you update the subscription info?")
            return False

    
    
    def request_tts(self, line: str, output_file: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format):
        # Audio48Khz192KBitRateMonoMp3
        output_voice_file = os.path.join(path_dubbing_folder(), path_new_filename(ext = ".mp3"))
        line = AbusText.normalize_text(line)
        if len(line) < 1:
            logger.warning(f"[abus_tts_azure.py] request_tts - error: no line")
            return False
        
        logger.debug(f'[abus_tts_azure.py] request_tts - line = {line}')
        
        if False == self.generate_audio(line, voice_name, output_voice_file, rate=speed_factor, volume=volume_factor, pitch=semitones):
            logger.warning(f"[abus_tts_azure.py] request_tts - error: API returns False")
            return False
                
        trimed_voice_file = path_add_postfix(output_voice_file, "_trimed")
        AbusAudio.trim_silence_file(output_voice_file, trimed_voice_file)
        
        ffmpeg_to_stereo(trimed_voice_file, output_file)
        
        try:
            os.remove(output_voice_file)
            os.remove(trimed_voice_file)
        except Exception as e:
            logger.error(f"[abus_tts_azure.py] request_tts - error: {e}")
            return False
        
        return True
    
    
    def srt_to_voice(self, subtitle_file: str, output_file: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        tts_subtitle_file = path_add_postfix(subtitle_file, f"-{voice_name}", ".srt")
        
        # AbusText.process_subtitle_for_tts(subtitle_file, tts_subtitle_file)
        AbusSpacy.process_subtitle_for_tts(subtitle_file, tts_subtitle_file)
  

        segments_folder = path_tts_segments_folder(subtitle_file)
        full_subs = pysubs2.load(tts_subtitle_file, encoding="utf-8")
        subs = full_subs
        
        combined_audio = AudioSegment.empty()
        for i in progress.tqdm(range(len(subs)), desc='Generating...'):
            line = subs[i]
            next_line = subs[i+1] if i < len(subs)-1 else None
            
            if i == 0:
                silence = AudioSegment.silent(duration=line.start)
                combined_audio += silence   

            tts_segment_file = os.path.join(segments_folder, f'tts_{i+1}.{audio_format}')
            tts_result = self.request_tts(line.text, tts_segment_file, voice_name, semitones, speed_factor, volume_factor, audio_format)

            if tts_result == False:
                if next_line:
                    silence = AudioSegment.silent(duration=next_line.start-line.start)
                    combined_audio += silence
                continue        
            
            combined_audio += AudioSegment.from_file(tts_segment_file)

            if next_line and len(combined_audio) < next_line.start:
                silence_length = next_line.start - len(combined_audio)
                silence = AudioSegment.silent(duration=silence_length)
                combined_audio += silence
            elif next_line:
                AbusAudio.move_subtitle_start_preserve_duration(next_line, len(combined_audio))
                
        combined_audio.export(output_file, format=audio_format)
        cmd_delete_file(tts_subtitle_file)                        
          

    def text_to_voice(self, text: str, output_file: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        segments_folder = path_tts_segments_folder(output_file)  
        
        use_punctuation = AbusText.has_punctuation_marks(text)
        lines = AbusText.split_into_sentences(text, use_punctuation)
        lines = lines
        
        combined_audio = AudioSegment.empty() 
        for i in progress.tqdm(range(len(lines)), desc='Generating...'):
            tts_segment_file = os.path.join(segments_folder, f'tts_{i+1:06}.{audio_format}')    
            tts_result = self.request_tts(lines[i], tts_segment_file, voice_name, semitones, speed_factor, volume_factor, audio_format)
            if tts_result == False:
                continue
            combined_audio += AudioSegment.from_file(tts_segment_file)
            
        combined_audio.export(output_file, format=audio_format)


    def infer(self, text: str, output_file: str, voice_name: str, semitones, speed_factor, volume_factor, audio_format, progress=gr.Progress()):
        logger.debug(f'[abus_tts_azure.py] infer - text = {text}')
        
        subtitle_file = None
        if AbusText.is_subtitle_format(text):
            subs = pysubs2.SSAFile.from_string(text)
            subtitle_file = os.path.join(path_dubbing_folder(), path_new_filename(f".{subs.format}"))
            subs.save(subtitle_file)        
        
        if subtitle_file:  
            self.srt_to_voice(subtitle_file, output_file, voice_name, semitones, speed_factor, volume_factor, audio_format, progress)
        else:
            self.text_to_voice(text, output_file, voice_name, semitones, speed_factor, volume_factor, audio_format, progress)
        
    
    def _validate_file(self, file_path):
        # Check file existence
        if not os.path.exists(file_path):
            return False, "File does not exist."
        
        if not os.path.isfile(file_path):
            return False, "The path is not a file."

        # Check file size
        file_size = os.path.getsize(file_path)
        if file_size <= 0:
            return False, "File size is not greater than 0."

        return True, "File is valid."
