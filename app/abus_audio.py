from pydub import AudioSegment
from pydub.silence import detect_leading_silence


import structlog
logger = structlog.get_logger()


class AbusAudio():
    def __init__(self):
        pass

    @staticmethod
    def move_subtitle_start_preserve_duration(subtitle_event, start_ms):
        duration = max(0, subtitle_event.end - subtitle_event.start)
        subtitle_event.start = start_ms
        subtitle_event.end = subtitle_event.start + duration
    
    
    @staticmethod
    def shirink(input_file, duration):
        audio = AudioSegment.from_file(input_file)
        return audio, 0
    
        # diff = len(audio) - duration
        # if diff > 0 and duration > 0:
            # new_speed = min(diff/duration + 1.0, 1.5)
            # new_frame_rate = int(audio.frame_rate * new_speed)
            # changed_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_frame_rate})
            # changed_audio = changed_audio.set_frame_rate(audio.frame_rate)
            # changed_audio.export(input_file)
            # audio = changed_audio
            
        #     return audio, 0
        # else:
        #     return audio, diff*(-1)
        
        
        
    @staticmethod    
    def trim_silence_audio(audio_segment, start_silence_threshold=-50.0, end_silence_threshold=-50.0, chunk_size=10, padding_duration=100):
        """
        오디오 세그먼트의 시작과 끝 부분의 무음을 제거합니다.
        
        :param audio_segment: 입력 파일 경로 또는 AudioSegment 객체
        :param start_silence_threshold: 시작 부분 무음으로 간주할 dBFS 임계값
        :param end_silence_threshold: 끝부분 무음으로 간주할 dBFS 임계값
        :param chunk_size: 분석할 청크의 크기(밀리초)
        :param padding_duration: 결과 오디오 끝에 추가할 패딩(밀리초)
        :return: 무음이 제거된 AudioSegment 객체
        """
        # 입력이 파일 경로인 경우 AudioSegment로 변환
        if isinstance(audio_segment, str):
            audio = AudioSegment.from_file(audio_segment)
        else:
            audio = audio_segment
            
        def detect_first_sound_index(asg, threshold=-50.0, chunk_size=10):
            """시작 부분의 첫 번째 소리 인덱스를 찾습니다."""
            for i in range(0, len(asg), chunk_size):
                chunk = asg[i:i + chunk_size]
                if chunk.dBFS > threshold and chunk.dBFS != float('-inf'):
                    return i
            return len(asg)  # 모두 무음이면 전체 길이 반환

        def detect_last_sound_index(asg, threshold=-50.0, chunk_size=10):
            """끝 부분의 마지막 소리 인덱스를 찾습니다."""
            reversed_audio = asg.reverse()
            for i in range(0, len(reversed_audio), chunk_size):
                chunk = reversed_audio[i:i + chunk_size]
                if chunk.dBFS > threshold and chunk.dBFS != float('-inf'):
                    return len(asg) - (i + chunk_size)
            return 0  # 모두 무음이면 0 반환

        # 시작과 끝 부분의 무음 인덱스 탐지
        start_index = detect_first_sound_index(audio, start_silence_threshold, chunk_size)
        end_index = detect_last_sound_index(audio, end_silence_threshold, chunk_size)

        # 무음 구간 제거
        trimmed_audio = audio[start_index:end_index]

        # 패딩 추가
        if padding_duration > 0:
            padding = AudioSegment.silent(duration=padding_duration)
            result_audio = trimmed_audio + padding
        else:
            result_audio = trimmed_audio
        
        return result_audio

    @staticmethod
    def trim_silence_file(input_file, output_file, start_silence_threshold=-50.0, end_silence_threshold=-50.0, chunk_size=10, padding_duration=100):
        """
        입력 파일의 무음을 제거하고 출력 파일로 저장합니다.
        
        :param input_file: 입력 오디오 파일 경로
        :param output_file: 출력 오디오 파일 경로
        :param start_silence_threshold: 시작 부분 무음 임계값
        :param end_silence_threshold: 끝 부분 무음 임계값
        :param chunk_size: 분석 청크 크기
        :param padding_duration: 패딩 길이
        """
        audio = AbusAudio.trim_silence_audio(input_file, start_silence_threshold, end_silence_threshold, chunk_size, padding_duration)
        audio.export(output_file)
