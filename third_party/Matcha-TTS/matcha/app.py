import tempfile
from argparse import Namespace
from pathlib import Path

import gradio as gr
import soundfile as sf
import torch

from matcha.cli import (
    MATCHA_URLS,
    VOCODER_URLS,
    assert_model_downloaded,
    get_device,
    load_matcha,
    load_vocoder,
    process_text,
    to_waveform,
)
from matcha.utils.utils import get_user_data_dir, plot_tensor

LOCATION = Path(get_user_data_dir())

args = Namespace(
    cpu=False,
    model="matcha_vctk",
    vocoder="hifigan_univ_v1",
    spk=0,
)

CURRENTLY_LOADED_MODEL = args.model


def MATCHA_TTS_LOC(x):
    return LOCATION / f"{x}.ckpt"


def VOCODER_LOC(x):
    return LOCATION / f"{x}"


LOGO_URL = "https://shivammehta25.github.io/Matcha-TTS/images/logo.png"
RADIO_OPTIONS = {
    "Multi Speaker (VCTK)": {
        "model": "matcha_vctk",
        "vocoder": "hifigan_univ_v1",
    },
    "Single Speaker (LJ Speech)": {
        "model": "matcha_ljspeech",
        "vocoder": "hifigan_T2_v1",
    },
}

# Ensure all the required models are downloaded
assert_model_downloaded(MATCHA_TTS_LOC("matcha_ljspeech"), MATCHA_URLS["matcha_ljspeech"])
assert_model_downloaded(VOCODER_LOC("hifigan_T2_v1"), VOCODER_URLS["hifigan_T2_v1"])
assert_model_downloaded(MATCHA_TTS_LOC("matcha_vctk"), MATCHA_URLS["matcha_vctk"])
assert_model_downloaded(VOCODER_LOC("hifigan_univ_v1"), VOCODER_URLS["hifigan_univ_v1"])

device = get_device(args)

# Load default model
model = load_matcha(args.model, MATCHA_TTS_LOC(args.model), device)
vocoder, denoiser = load_vocoder(args.vocoder, VOCODER_LOC(args.vocoder), device)


def load_model(model_name, vocoder_name):
    model = load_matcha(model_name, MATCHA_TTS_LOC(model_name), device)
    vocoder, denoiser = load_vocoder(vocoder_name, VOCODER_LOC(vocoder_name), device)
    return model, vocoder, denoiser


def load_model_ui(model_type, textbox):
    model_name, vocoder_name = RADIO_OPTIONS[model_type]["model"], RADIO_OPTIONS[model_type]["vocoder"]

    global model, vocoder, denoiser, CURRENTLY_LOADED_MODEL  # pylint: disable=global-statement
    if CURRENTLY_LOADED_MODEL != model_name:
        model, vocoder, denoiser = load_model(model_name, vocoder_name)
        CURRENTLY_LOADED_MODEL = model_name

    if model_name == "matcha_ljspeech":
        spk_slider = gr.update(visible=False, value=-1)
        single_speaker_examples = gr.update(visible=True)
        multi_speaker_examples = gr.update(visible=False)
        length_scale = gr.update(value=0.95)
    else:
        spk_slider = gr.update(visible=True, value=0)
        single_speaker_examples = gr.update(visible=False)
        multi_speaker_examples = gr.update(visible=True)
        length_scale = gr.update(value=0.85)

    return (
        textbox,
        gr.update(interactive=True),
        spk_slider,
        single_speaker_examples,
        multi_speaker_examples,
        length_scale,
    )


@torch.inference_mode()
def process_text_gradio(text):
    output = process_text(1, text, device)
    return output["x_phones"][1::2], output["x"], output["x_lengths"]


@torch.inference_mode()
def synthesise_mel(text, text_length, n_timesteps, temperature, length_scale, spk):
    spk = torch.tensor([spk], device=device, dtype=torch.long) if spk >= 0 else None
    output = model.synthesise(
        text,
        text_length,
        n_timesteps=n_timesteps,
        temperature=temperature,
        spks=spk,
        length_scale=length_scale,
    )
    output["waveform"] = to_waveform(output["mel"], vocoder, denoiser)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        sf.write(fp.name, output["waveform"], 22050, "PCM_24")

    return fp.name, plot_tensor(output["mel"].squeeze().cpu().numpy())


def multispeaker_example_cacher(text, n_timesteps, mel_temp, length_scale, spk):
    global CURRENTLY_LOADED_MODEL  # pylint: disable=global-statement
    if CURRENTLY_LOADED_MODEL != "matcha_vctk":
        global model, vocoder, denoiser  # pylint: disable=global-statement
        model, vocoder, denoiser = load_model("matcha_vctk", "hifigan_univ_v1")
        CURRENTLY_LOADED_MODEL = "matcha_vctk"

    phones, text, text_lengths = process_text_gradio(text)
    audio, mel_spectrogram = synthesise_mel(text, text_lengths, n_timesteps, mel_temp, length_scale, spk)
    return phones, audio, mel_spectrogram


def ljspeech_example_cacher(text, n_timesteps, mel_temp, length_scale, spk=-1):
    global CURRENTLY_LOADED_MODEL  # pylint: disable=global-statement
    if CURRENTLY_LOADED_MODEL != "matcha_ljspeech":
        global model, vocoder, denoiser  # pylint: disable=global-statement
        model, vocoder, denoiser = load_model("matcha_ljspeech", "hifigan_T2_v1")
        CURRENTLY_LOADED_MODEL = "matcha_ljspeech"

    phones, text, text_lengths = process_text_gradio(text)
    audio, mel_spectrogram = synthesise_mel(text, text_lengths, n_timesteps, mel_temp, length_scale, spk)
    return phones, audio, mel_spectrogram


def main():
    description = """# 🍵 Matcha-TTS: A fast TTS architecture with conditional flow matching
    ### [Shivam Mehta](https://www.kth.se/profile/smehta), [Ruibo Tu](https://www.kth.se/profile/ruibo), [Jonas Beskow](https://www.kth.se/profile/beskow), [Éva Székely](https://www.kth.se/profile/szekely), and [Gustav Eje Henter](https://people.kth.se/~ghe/)
    We propose 🍵 Matcha-TTS, a new approach to non-autoregressive neural TTS, that uses conditional flow matching (similar to rectified flows) to speed up ODE-based speech synthesis. Our method:


    * Is probabilistic
    * Has compact memory footprint
    * Sounds highly natural
    * Is very fast to synthesise from


    Check out our [demo page](https://shivammehta25.github.io/Matcha-TTS). Read our [arXiv preprint for more details](https://arxiv.org/abs/2309.03199).
    Code is available in our [GitHub repository](https://github.com/shivammehta25/Matcha-TTS), along with pre-trained models.

    Cached examples are available at the bottom of the page.
    """

    with gr.Blocks(title="🍵 Matcha-TTS: A fast TTS architecture with conditional flow matching") as demo:
        processed_text = gr.State(value=None)
        processed_text_len = gr.State(value=None)

        with gr.Box():
            with gr.Row():
                gr.Markdown(description, scale=3)
                with gr.Column():
                    gr.Image(LOGO_URL, label="Matcha-TTS logo", height=50, width=50, scale=1, show_label=False)
                    html = '<br><iframe width="560" height="315" src="https://www.youtube.com/embed/xmvJkz3bqw0?si=jN7ILyDsbPwJCGoa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
                    gr.HTML(html)

        with gr.Box():
            radio_options = list(RADIO_OPTIONS.keys())
            model_type = gr.Radio(
                radio_options, value=radio_options[0], label="Choose a Model", interactive=True, container=False
            )

            with gr.Row():
                gr.Markdown("# Text Input")
            with gr.Row():
                text = gr.Textbox(value="", lines=2, label="Text to synthesise", scale=3)
                spk_slider = gr.Slider(
                    minimum=0, maximum=107, step=1, value=args.spk, label="Speaker ID", interactive=True, scale=1
                )

            with gr.Row():
                gr.Markdown("### Hyper parameters")
            with gr.Row():
                n_timesteps = gr.Slider(
                    label="Number of ODE steps",
                    minimum=1,
                    maximum=100,
                    step=1,
                    value=10,
                    interactive=True,
                )
                length_scale = gr.Slider(
                    label="Length scale (Speaking rate)",
                    minimum=0.5,
                    maximum=1.5,
                    step=0.05,
                    value=1.0,
                    interactive=True,
                )
                mel_temp = gr.Slider(
                    label="Sampling temperature",
                    minimum=0.00,
                    maximum=2.001,
                    step=0.16675,
                    value=0.667,
                    interactive=True,
                )

                synth_btn = gr.Button("Synthesise")

        with gr.Box():
            with gr.Row():
                gr.Markdown("### Phonetised text")
                phonetised_text = gr.Textbox(interactive=False, scale=10, label="Phonetised text")

        with gr.Box():
            with gr.Row():
                mel_spectrogram = gr.Image(interactive=False, label="mel spectrogram")

                # with gr.Row():
                audio = gr.Audio(interactive=False, label="Audio")

        with gr.Row(visible=False) as example_row_lj_speech:
            examples = gr.Examples(  # pylint: disable=unused-variable
                examples=[
                    [
                        "We propose Matcha-TTS, a new approach to non-autoregressive neural TTS, that uses conditional flow matching (similar to rectified flows) to speed up O D E-based speech synthesis.",
                        50,
                        0.677,
                        0.95,
                    ],
                    [
                        "The Secret Service believed that it was very doubtful that any President would ride regularly in a vehicle with a fixed top, even though transparent.",
                        2,
                        0.677,
                        0.95,
                    ],
                    [
                        "The Secret Service believed that it was very doubtful that any President would ride regularly in a vehicle with a fixed top, even though transparent.",
                        4,
                        0.677,
                        0.95,
                    ],
                    [
                        "The Secret Service believed that it was very doubtful that any President would ride regularly in a vehicle with a fixed top, even though transparent.",
                        10,
                        0.677,
                        0.95,
                    ],
                    [
                        "The Secret Service believed that it was very doubtful that any President would ride regularly in a vehicle with a fixed top, even though transparent.",
                        50,
                        0.677,
                        0.95,
                    ],
                    [
                        "The narrative of these events is based largely on the recollections of the participants.",
                        10,
                        0.677,
                        0.95,
                    ],
                    [
                        "The jury did not believe him, and the verdict was for the defendants.",
                        10,
                        0.677,
                        0.95,
                    ],
                ],
                fn=ljspeech_example_cacher,
                inputs=[text, n_timesteps, mel_temp, length_scale],
                outputs=[phonetised_text, audio, mel_spectrogram],
                cache_examples=True,
            )

        with gr.Row() as example_row_multispeaker:
            multi_speaker_examples = gr.Examples(  # pylint: disable=unused-variable
                examples=[
                    [
                        "Hello everyone! I am speaker 0 and I am here to tell you that Matcha-TTS is amazing!",
                        10,
                        0.677,
                        0.85,
                        0,
                    ],
                    [
                        "Hello everyone! I am speaker 16 and I am here to tell you that Matcha-TTS is amazing!",
                        10,
                        0.677,
                        0.85,
                        16,
                    ],
                    [
                        "Hello everyone! I am speaker 44 and I am here to tell you that Matcha-TTS is amazing!",
                        50,
                        0.677,
                        0.85,
                        44,
                    ],
                    [
                        "Hello everyone! I am speaker 45 and I am here to tell you that Matcha-TTS is amazing!",
                        50,
                        0.677,
                        0.85,
                        45,
                    ],
                    [
                        "Hello everyone! I am speaker 58 and I am here to tell you that Matcha-TTS is amazing!",
                        4,
                        0.677,
                        0.85,
                        58,
                    ],
                ],
                fn=multispeaker_example_cacher,
                inputs=[text, n_timesteps, mel_temp, length_scale, spk_slider],
                outputs=[phonetised_text, audio, mel_spectrogram],
                cache_examples=True,
                label="Multi Speaker Examples",
            )

        model_type.change(lambda x: gr.update(interactive=False), inputs=[synth_btn], outputs=[synth_btn]).then(
            load_model_ui,
            inputs=[model_type, text],
            outputs=[text, synth_btn, spk_slider, example_row_lj_speech, example_row_multispeaker, length_scale],
        )

        synth_btn.click(
            fn=process_text_gradio,
            inputs=[
                text,
            ],
            outputs=[phonetised_text, processed_text, processed_text_len],
            api_name="matcha_tts",
            queue=True,
        ).then(
            fn=synthesise_mel,
            inputs=[processed_text, processed_text_len, n_timesteps, mel_temp, length_scale, spk_slider],
            outputs=[audio, mel_spectrogram],
        )

        demo.queue().launch(share=True)


if __name__ == "__main__":
    main()
