import os
import sys
import platform

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


import gradio as gr
from src.config import UserConfig

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

from app.gradio_tts_minimax import *
from app.abus_tts_minimax import MINIMAX_VOICES, MINIMAX_MODELS


def tts_minimax_tab(user_config: UserConfig):
    tts = GradioMiniMaxTTS(user_config)
    subtitle_exts = ['.ass', '.ssa', '.srt', '.mpl2', '.tmp', '.vtt', '.microdvd', '.json']
    system = platform.system()

    voice_choices = list(MINIMAX_VOICES.keys())
    model_choices = list(MINIMAX_MODELS.keys())

    with gr.Row():
        with gr.Column(scale=4):
            with gr.Group():
                gr.HTML(f'<center><h4>{i18n("Voice")}</h4></center>')
                minimax_voice_dropdown = gr.Dropdown(
                    label=i18n("Voice"),
                    choices=voice_choices,
                    value=user_config.get("minimax_tts_voice", "English_Graceful_Lady"),
                )
                minimax_model_dropdown = gr.Dropdown(
                    label=i18n("Model"),
                    choices=model_choices,
                    value=user_config.get("minimax_tts_model", "speech-2.8-hd"),
                )

        with gr.Column(scale=8):
            with gr.Group():
                gr.HTML(f'<center><h4>{i18n("Script")}</h4></center>')
                dubbing_file_in = gr.File(
                    label=i18n("Subtitle File"),
                    type="filepath",
                    file_count="single",
                    file_types=subtitle_exts,
                )
                dubbing_text_in = gr.Textbox(
                    label=i18n("Source Text"),
                    interactive=True,
                    show_label=True,
                    max_lines=24,
                    show_copy_button=True,
                    placeholder=i18n("Placeholder for Source Text"),
                    lines=5,
                )
            with gr.Group():
                gr.HTML(f'<center><h4>{i18n("Synthesized voice")}</h4></center>')
                dubbing_audio = gr.Audio(label=i18n("Audio"), type="filepath", interactive=False)
                dubbing_file_out = gr.File(label=i18n("File"), type="filepath", file_count="single", interactive=False)
            with gr.Row():
                workspace_button = gr.Button(value=i18n("🗂️ Open workspace folder"), variant="secondary")
                temp_button = gr.Button(value=i18n("🗀 Open Temp folder"), variant="secondary")

        with gr.Column(scale=4):
            with gr.Group():
                gr.HTML(f'<center><h4>{i18n("Speech Generation")}</h4></center>')
                minimax_tts_speed = gr.Slider(
                    -100, 200,
                    value=user_config.get("minimax_tts_speed", 0),
                    step=1,
                    label=i18n("Speech rate"),
                    info="-100% ~ +200%",
                )
                audio_format_radio = gr.Radio(
                    label=i18n("Audio Format"),
                    choices=["wav", "flac", "mp3"],
                    value=user_config.get("audio_format", "mp3"),
                )
            with gr.Row():
                minimax_dubbing_button = gr.Button(value=i18n("Synthesis"), variant="primary")

    # Event handlers
    dubbing_file_in.upload(
        tts.gradio_upload_file,
        inputs=[dubbing_file_in],
        outputs=[dubbing_text_in],
    )

    workspace_button.click(tts.gradio_workspace_folder)
    temp_button.click(tts.gradio_temp_folder)

    minimax_dubbing_button.click(
        tts.gradio_tts_dubbing,
        inputs=[dubbing_text_in, minimax_voice_dropdown, minimax_model_dropdown, minimax_tts_speed, audio_format_radio],
        outputs=[dubbing_file_out, dubbing_audio],
    )
