import os
import sys
from pathlib import Path
import random
import requests


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

matcha_dir = os.path.join(parent_dir, 'third_party', 'Matcha-TTS')
sys.path.append(matcha_dir)


import platform
import torch
import gradio as gr
from src.config import UserConfig

import src.ui as ui
from src.i18n.i18n import I18nAuto
i18n = I18nAuto()

import structlog
import logging

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("fairseq").setLevel(logging.WARNING)
logging.getLogger("azure.core").setLevel(logging.WARNING)
logging.getLogger("faster_whisper").setLevel(logging.DEBUG)

logging.getLogger('matplotlib').setLevel(logging.WARNING)


level = os.environ.get("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, level)
structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.DEBUG)
)
logger = structlog.get_logger()


from app.abus_genuine import *
from app.tab_gulliver import gulliver_tab
from app.tab_subtitle import subtitle_tab
from app.tab_tts_edge import tts_edge_tab
from app.tab_tts_f5_single import tts_f5_single_tab
from app.tab_tts_f5_multi import tts_f5_multi_tab
from app.tab_tts_cosyvoice import tts_cosyvoice_tab
from app.tab_tts_kokoro import tts_kokoro_tab
from app.tab_tts_minimax import tts_minimax_tab
from app.tab_translate import translate_tab
from app.tab_live_translate import live_translate_tab
from app.tab_vsr import vsr_tab
from app.tab_aicover import aicover_tab
from app.tab_demixing import demixing_tab
from app.tab_tts_rvc import tts_rvc_tab
from app.tab_rvc import rvc_tab
from app.tab_batch_tts import batch_tts_tab


##############################################################################################
# Gradio
##############################################################################################    


def create_ui(user_config: UserConfig):
    # css/js strings
    css = ui.css
    js = ui.js

    with gr.Blocks(title='Voice Gulliver', css=css, theme=ui.theme) as gradio_interface:
        gr.HTML(f'<center><h6>{i18n("")}</h6></center>')
        
        with gr.Tab(i18n("Dubbing Studio")):
            gulliver_tab(user_config)
            
        with gr.Tab(i18n("Whisper subtitles")):
            subtitle_tab(user_config)            
            
        with gr.Tab(i18n("Translation")):
            with gr.Tabs():
                with gr.Tab(i18n("VOD")):
                    translate_tab(user_config)
                with gr.Tab(i18n("Live")):
                    live_translate_tab(user_config)
            
        with gr.Tab(i18n("Speech Generation")):
            with gr.Tabs():
                tab_name = i18n('Azure-TTS') if azure_text_api_working() else i18n('Edge-TTS')
                with gr.Tab(tab_name):
                    tts_edge_tab(user_config)
                with gr.Tab(i18n("F5-TTS (Single)")):
                    tts_f5_single_tab(user_config)
                with gr.Tab(i18n("F5-TTS (Multi)")):
                    tts_f5_multi_tab(user_config)                   
                with gr.Tab(i18n("CosyVoice")):
                    tts_cosyvoice_tab(user_config)                           
                with gr.Tab(i18n("kokoro")):
                    tts_kokoro_tab(user_config)
                with gr.Tab(i18n("MiniMax")):
                    tts_minimax_tab(user_config)

        with gr.Tab(i18n("AI Cover")):
            with gr.Tabs():                      
                with gr.Tab(i18n("Cover Studio")):
                    aicover_tab(user_config)                                    
                with gr.Tab(i18n("Demixing")):
                    demixing_tab(user_config)              

        with gr.Tab(i18n("Batch processing")):
            batch_tts_tab(user_config)

        with gr.Tab(i18n("RVC")):
            rvc_tab(user_config)
                                 
        with gr.Tab(i18n("TTS + RVC")):
            tts_rvc_tab(user_config)
            
        with gr.Tab(i18n("NVIDIA RTX")):
            vsr_tab(user_config) 
            
        create_app_footer()    

        gradio_interface.load(None, None, None, js="() => document.getElementsByTagName('body')[0].classList.add('dark')")
        gradio_interface.load(None, None, None, js=f"() => {{{js}}}")
                    
        
    gradio_interface.launch(
        share=False,
        server_name=None, 
        server_port=7860,
        inbrowser=True
    )
    
def create_app_footer():
    gradio_version = gr.__version__
    python_version = platform.python_version()
    torch_version = torch.__version__

    footer_items = ["🔊 [voice-gulliver](https://github.com/abus-aikorea/voice-gulliver)"]
    footer_items.append(f"python: `{python_version}`")
    footer_items.append(f"torch: `{torch_version}`")
    footer_items.append(f"gradio: `{gradio_version}`")

    genuine = "activated version"
    footer_items.append(f"{genuine}")

    gr.Markdown(
        " | ".join(footer_items),
        elem_classes=["no-translate"],
    )


