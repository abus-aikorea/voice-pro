# Voice-Pro Critical Fixes — Pull Request Summary

**Target Repository:** https://github.com/abus-aikorea/voice-pro  
**Date:** 2026-04-27  
**Status:** Ready for PR review

---

## 1. What This PR Fixes

This PR addresses **runtime failures** that prevent Voice-Pro from being operational on modern systems. All changes are backward-compatible and additive — the original `./start.sh` launch path works exactly as before.

### Upstream Issues Addressed

| Issue | Title | Fix # | Note |
|---|---|---|---|
| [#76](https://github.com/abus-aikorea/voice-pro/issues/76) | `none_type not iterable` error | 3 | Gradio 5.x `Progress.tqdm()` returns `self` instead of iterable; patched in `start-voice.py` |
| [#62](https://github.com/abus-aikorea/voice-pro/issues/62) | Installation Error | 4 | `setuptools>=80` removed `pkg_resources`; `one_click.py` now pins `<70` and installs whisper without build isolation |
| [#60](https://github.com/abus-aikorea/voice-pro/issues/60) | Installation is too much trouble | 4, 6 | Installer reliability improved; GPU auto-detect removes manual config step |

> Issues **not** addressed by this PR: #61 (Azure SDK TranslatorCredential), #75/#74 (RTX 5070 sm_120 ctranslate2 kernel), #79 (azure-ai-translation-text 1.0.0+), #80 (demucs subprocess failure detection), #68 (missing demucs output files), #67 (Windows grep compatibility).

---

## 2. Critical Fixes

### Fix 1: YouTube Downloader (`app/abus_downloader.py`)

**Problem:** The built-in YouTube downloader fails on most videos because:
- `yt-dlp 2025.11.12` is >5 months old and cannot handle YouTube's current SABR streaming + JS challenges
- No JavaScript runtime is configured (yt-dlp 2026+ only enables Deno by default)
- Metadata is extracted twice per download, doubling HTTP requests and triggering rate limits

**Changes:**
- Updated `ydl_opts` with `js_runtimes: {'node': {}}` and `remote_components: ['ejs:github']`
- Replaced double extraction with single `extract_info(..., download=False)` + `process_ie_result(info, download=True)`

**Note:** `yt-dlp` itself must also be updated to `2026.3.17+` in the environment (done via pip in the conda env).

---

### Fix 2: VAD Model Path (`src/vad.py`)

**Problem:** The VAD constructor hardcodes `~/.cache/whisper-live/silero_vad.onnx` and ignores the project-local copy at `model/vad/silero_vad.onnx`. On fresh clones or systems without the cache, VAD fails immediately.

**Changes:**
- Constructor now checks `model/vad/silero_vad.onnx` (project-local) first
- Falls back to `~/.cache/whisper-live/silero_vad.onnx`
- Prints clear manual-sourcing instructions if neither is found

---

### Fix 3: Gradio 5.x Compatibility (`app/abus_path.py`, `app/gradio_*.py`, `start-voice.py`)

**Problem:** Gradio 5.x introduced breaking API changes:
- `gr.Progress.tqdm()` returns `self` instead of a wrapped iterable, causing `"NoneType object is not iterable"` errors (reported in upstream issue #76)
- `gr.File(type='filepath')` now returns a `NamedString` (str subclass with `.name`) instead of a plain str, while `gr.Audio(type='filepath')` still returns a plain str. Code using `file_obj.name` crashes when the input is a plain str.
- `FileData.model_validate()` rejects payloads with missing/None `meta` fields, causing upload failures.

**Changes:**
- Added `gradio_file_path(file_obj)` helper in `app/abus_path.py` that handles `str`, `NamedString`, and legacy file objects
- Updated **13 `app/gradio_*.py` files** to use `gradio_file_path(file_obj)` instead of `file_obj.name`
- Added monkey-patches in `start-voice.py` for `Progress.tqdm` (wraps with standard `tqdm`) and `FileData.model_validate` (injects default `meta` when missing)

**Files affected:**
`app/abus_path.py`, `app/gradio_aicover.py`, `app/gradio_asr.py`, `app/gradio_demixing.py`, `app/gradio_gulliver.py`, `app/gradio_kara.py`, `app/gradio_rvc.py`, `app/gradio_translate.py`, `app/gradio_tts_cosyvoice.py`, `app/gradio_tts_edge.py`, `app/gradio_tts_f5.py`, `app/gradio_tts_kokoro.py`, `app/gradio_tts_rvc.py`, `app/gradio_vsr.py`, `start-voice.py`

---

### Fix 4: Installer Build Fixes (`one_click.py`)

**Problem:** Fresh installs fail on modern Python environments because:
- `setuptools>=80` removed `pkg_resources`, breaking `openai-whisper` (sdist that imports `pkg_resources` during build)
- `openai-whisper` build isolation pulls in a newer setuptools that lacks `pkg_resources`
- `ctranslate2` bundles a renamed cuDNN 8 library but omits the split `.so` files (e.g., `libcudnn_ops_infer.so.8`) that it `dlopen`s at runtime, causing CUDA errors
- The inline `python -c` shell command for the ctranslate2 fix had quoting issues that caused `SyntaxError` on some shells

**Changes:**
- Pre-install `setuptools<70` and `wheel` before requirements
- Install `openai-whisper==20240930` with `--no-build-isolation`
- Post-install: write the cuDNN fix to a temp Python script file instead of an inline `python -c` string, avoiding shell quoting bugs

---

### Fix 5: cuDNN Version Bump (`requirements-voice-gpu.txt`)

**Problem:** `nvidia-cudnn-cu12==8.9.7.29` pins an old version that may conflict with newer PyTorch builds.

**Changes:**
- Relaxed to `nvidia-cudnn-cu12>=9.1.0.70`

---

### Fix 6: GPU Auto-Detection (`start.sh`, `update.sh`)

**Problem:** Users on fresh systems often forget to set `GPU_CHOICE`, causing the app to default to an incorrect mode or prompt interactively.

**Changes:**
- Added auto-detection: if `nvidia-smi` is available, set `GPU_CHOICE=G`; otherwise `GPU_CHOICE=C`

---

### Fix 7: Build Tool Dependencies (`configure.sh`)

**Problem:** Ubuntu minimal installs (and some fresh 24.04 setups) lack `cmake`, causing pip packages that require compilation to fail with `CMAKE_MAKE_PROGRAM is not set`.

**Changes:**
- Added `cmake` to the `apt-get install` line alongside `git`, `ffmpeg`, and `build-essential`

---

### Fix 8: torchaudio / pyannote.audio Compatibility (`start-voice.py`)

**Problem:** `pyannote.audio` (dependency of `whisperx`) expects `torchaudio.AudioMetaData` to be available at the top level. In some torchaudio builds (especially CPU wheels or certain CUDA builds), this class is not re-exported, causing `AttributeError: module 'torchaudio' has no attribute 'AudioMetaData'` on import.

**Changes:**
- Added monkey-patch in `start-voice.py`: if `torchaudio.AudioMetaData` is missing, import it from `torchaudio.backend.common` and attach it

---

### Fix 9: yt-dlp Version Pin (`requirements-voice-*.txt`)

**Problem:** `yt-dlp==2025.11.12` is too old for modern YouTube.

**Changes:**
- Relaxed to `yt-dlp>=2026.3.17` in both GPU and CPU requirements files

---

## 3. Files Changed

| File | Fix # | Description |
|---|---|---|
| `app/abus_downloader.py` | 1 | YouTube JS runtime + single extraction |
| `src/vad.py` | 2 | Local VAD path check first |
| `app/abus_path.py` | 3 | `gradio_file_path()` helper |
| `app/gradio_aicover.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_asr.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_demixing.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_gulliver.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_kara.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_rvc.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_translate.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_tts_cosyvoice.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_tts_edge.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_tts_f5.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_tts_kokoro.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_tts_rvc.py` | 3 | Use `gradio_file_path()` |
| `app/gradio_vsr.py` | 3 | Use `gradio_file_path()` |
| `start-voice.py` | 3, 8 | Monkey-patches for Gradio 5.x tqdm + FileData + torchaudio.AudioMetaData |
| `one_click.py` | 4 | setuptools, whisper, ctranslate2 cuDNN fixes (temp script) |
| `start.sh` | 6 | GPU auto-detect |
| `update.sh` | 6 | GPU auto-detect |
| `configure.sh` | 7 | Add `cmake` to apt dependencies |
| `requirements-voice-gpu.txt` | 5, 9 | cuDNN version bump + yt-dlp update |
| `requirements-voice-cpu.txt` | 9 | yt-dlp update |

**Total:** 24 files changed, 0 files removed.

---

## 4. Testing

| Test | Result |
|---|---|
| YouTube download (modern video with JS challenges) | ✅ Success |
| VAD initialization (fresh clone, no cache) | ✅ Success |
| Gradio file upload (audio + video inputs) | ✅ Success |
| Progress bar iteration (subtitle generation) | ✅ Success |
| Fresh install on Linux Mint 22.2 | ✅ Success |

---

## 5. Suggested PR Title

> **fix: YouTube downloader, VAD paths, Gradio 5.x compatibility, and installer build errors**
>
> Fixes yt-dlp JS runtime config for modern YouTube, adds project-local VAD fallback, resolves Gradio 5.x breaking changes (tqdm/FileData/file paths), and patches one_click.py for setuptools/pkg_resources and ctranslate2 cuDNN compatibility.
