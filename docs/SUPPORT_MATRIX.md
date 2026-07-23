# Support Matrix

This page summarizes what Voice-Pro supports today and where results depend on
the selected model, operating system, or service credentials.

## Platforms

| Platform | Status | Notes |
| --- | --- | --- |
| Windows 10/11 | Primary | Best-tested path. Use `configure.bat` once, then `start.bat`. NVIDIA GPU mode uses PyTorch CUDA wheels; CUDA Toolkit is not required. |
| Linux | Best effort | Use `configure.sh`, then `start.sh`. CPU mode works without NVIDIA. GPU mode requires a recent NVIDIA driver; driver version 570 or newer is recommended for RTX 50-series / Blackwell GPUs. |
| macOS Apple Silicon | Best effort CPU | Use `configure.sh`, then `start.sh`. NVIDIA GPU mode is not available. Some model downloads and native audio dependencies can still vary by macOS version. |
| macOS Intel | Not recommended | PyTorch no longer ships all required wheels for Intel macOS in the current stack. |
| Docker | CPU image | See [Docker setup](DOCKER.md). GPU Docker images need a separate CUDA runtime design. |

## Language Coverage

| Workflow | Coverage | Notes |
| --- | --- | --- |
| ASR | Multilingual | Whisper, faster-whisper, and whisper-timestamped support many languages. Accuracy depends on the model size and source audio quality. |
| Translation | 100+ languages | Deep Translator is available by default. Azure Translator is used when Azure credentials are configured. |
| Edge TTS | 100+ languages / 400+ voices | Includes requested languages such as Arabic, Indonesian, Italian, and Turkish through Microsoft neural voices. |
| F5 / E2 TTS | Model-dependent | Built-in configs include English/Chinese, Finnish, French, Hindi, Italian, Japanese, Russian, and Spanish models. For native Spanish output, choose `jpgallegoar/F5-Spanish`; for Italian, choose `alien79/F5-TTS-italian`. |
| CosyVoice | Model-dependent | `CosyVoice2-0.5B` and `Fun-CosyVoice3-0.5B` cover different language sets. Cross-lingual quality depends heavily on reference audio and prompt text. |
| Kokoro | Voice-pack-dependent | Available languages are the languages shipped in the downloaded Kokoro sample pack. |
| RVC | Voice-model-dependent | RVC changes speaker timbre after a TTS pass. It does not add target-language phoneme knowledge by itself. |

## Choosing a TTS Path

- Use Edge TTS first when you need broad language coverage, including Arabic,
  Indonesian, Italian, and Turkish.
- Use F5-TTS when you need voice cloning and a matching target-language model is
  available.
- Use CosyVoice cross-lingual mode when the speaker reference matters more than
  strict native pronunciation, then compare with a target-language F5 model.
- Use RVC after TTS when you already have a good target-language speech result
  and only want to transfer timbre.

## Known Limits

- A voice reference recorded in one language can sound accented in another
  language. Prefer a target-language model or reference when native pronunciation
  matters.
- Very long translated speech may exceed the source video duration. Shorten the
  translation, increase TTS speed, or use a workflow that preserves the full
  dubbed audio.
- macOS and Linux support are community/best-effort paths; Windows remains the
  primary tested platform.
