import re


def timeformat_srt(time):
    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    seconds = time - hours * 3600 - minutes * 60
    milliseconds = (time - int(time)) * 1000
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{int(milliseconds):03d}"


def timeformat_vtt(time):
    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    seconds = time - hours * 3600 - minutes * 60
    milliseconds = (time - int(time)) * 1000
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{int(milliseconds):03d}"


def write_file(subtitle, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(subtitle)


def get_srt(segments):
    output = ""
    for i, segment in enumerate(segments):
        output += f"{i + 1}\n"
        output += f"{timeformat_srt(segment['start'])} --> {timeformat_srt(segment['end'])}\n"
        if segment['text'].startswith(' '):
            segment['text'] = segment['text'][1:]
        output += f"{segment['text']}\n\n"
    return output


def get_srt_wordlevel(segments):
    output = ""
    i = 0
    for segment in segments:
        for word in segment['words']:
            i += 1
            output += f"{i}\n"
            output += f"{timeformat_srt(word.start)} --> {timeformat_srt(word.end)}\n"
            
            striped = word.word.strip()
            highlighted = f'<font color=\"#0e556a\"><b><u>{striped}</u></b></font>'
            line = segment['text'].replace(striped, highlighted)

            output += f"{line}\n\n"    
    return output


def get_vtt(segments):
    output = "WEBVTT\n\n"
    for i, segment in enumerate(segments):
        output += f"{i + 1}\n"
        output += f"{timeformat_vtt(segment['start'])} --> {timeformat_vtt(segment['end'])}\n"
        if segment['text'].startswith(' '):
            segment['text'] = segment['text'][1:]
        output += f"{segment['text']}\n\n"
    return output

def get_vtt_block(segments, start_idx=1):
    output = ""
    for i, segment in enumerate(segments):
        output += f"{i + start_idx}\n"
        output += f"{timeformat_vtt(segment['start'])} --> {timeformat_vtt(segment['end'])}\n"
        if segment['text'].startswith(' '):
            segment['text'] = segment['text'][1:]
        output += f"{segment['text']}\n\n"
    return output




def get_txt(segments):
    output = ""
    for i, segment in enumerate(segments):
        if segment['text'].startswith(' '):
            segment['text'] = segment['text'][1:]
        output += f"{segment['text']}\n"
    return output


def parse_srt(file_path):
    """Reads SRT file and returns as dict"""
    with open(file_path, 'r', encoding='utf-8') as file:
        srt_data = file.read()

    data = []
    blocks = srt_data.split('\n\n')

    for block in blocks:
        if block.strip() != '':
            lines = block.strip().split('\n')
            index = lines[0]
            timestamp = lines[1]
            sentence = ' '.join(lines[2:])

            data.append({
                "index": index,
                "timestamp": timestamp,
                "sentence": sentence
            })
    return data


def parse_vtt(file_path):
    """Reads WebVTT file and returns as dict"""
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        webvtt_data = file.read()

    data = []
    blocks = webvtt_data.split('\n\n')

    # The magic is uppercase in the standard; retain support for old exports.
    # Only the first block is a header, since cue IDs can also start with WEBVTT.
    if blocks and re.match(r'^(?:WEBVTT|WebVTT)(?:[ \t].*)?(?:\n|$)', blocks[0]):
        blocks = blocks[1:]

    for block in blocks:
        if block.strip() != '':
            lines = block.strip().split('\n')
            index = lines[0]
            timestamp = lines[1]
            sentence = ' '.join(lines[2:])

            data.append({
                "index": index,
                "timestamp": timestamp,
                "sentence": sentence
            })

    return data


def get_serialized_srt(dicts):
    output = ""
    for dic in dicts:
        output += f'{dic["index"]}\n'
        output += f'{dic["timestamp"]}\n'
        output += f'{dic["sentence"]}\n\n'
    return output


def get_serialized_vtt(dicts):
    output = "WEBVTT\n\n"
    for dic in dicts:
        output += f'{dic["index"]}\n'
        output += f'{dic["timestamp"]}\n'
        output += f'{dic["sentence"]}\n\n'
    return output



import time

def safe_filename(name):
    return f'{name}-{int(time.time())}'
    # from app import _args
    # INVALID_FILENAME_CHARS = r'[<>:"/\\|?*\x00-\x1f]'
    # safe_name = re.sub(INVALID_FILENAME_CHARS, '_', name)
    # if not _args.colab:
    #     return safe_name
    # # Truncate the filename if it exceeds the max_length (20)
    # if len(safe_name) > 20:
    #     file_extension = safe_name.split('.')[-1]
    #     if len(file_extension) + 1 < 20:
    #         truncated_name = safe_name[:20 - len(file_extension) - 1]
    #         safe_name = truncated_name + '.' + file_extension
    #     else:
    #         safe_name = safe_name[:20]
    # return safe_name
