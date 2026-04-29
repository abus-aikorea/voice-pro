# Voice-Pro Critical Fixes — Wave 2

**Target Repository:** https://github.com/abus-aikorea/voice-pro  
**Date:** 2026-04-28  
**Status:** Ready for PR review  
**Based on:** Real-world testing on Ubuntu 24.04.4 minimal install

---

## 1. What This Wave Fixes

This wave addresses **installation and runtime failures** discovered when testing the clean fixed version on a fresh Ubuntu 24.04.4 system. These are follow-up fixes to the first wave (CHANGES-FOR-PR.md).

---

## 2. Fixes

### Fix 10: Missing `cmake` in System Dependencies (`configure.sh`)

**Problem:** On fresh Ubuntu minimal installs (including 24.04.4), `cmake` is not installed by default. Several pip packages require compilation via CMake during install, causing the build to fail with:
```
CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".
CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
```

**Changes:**
- Added `cmake` to the `apt-get install` line in `configure.sh` alongside `git`, `ffmpeg`, and `build-essential`

**Files changed:** `configure.sh`

---

### Fix 11: ctranslate2 cuDNN Fix — Shell Quoting Bug (`one_click.py`)

**Problem:** The post-install cuDNN 8 library fix in `one_click.py` used an inline `python -c "..."` string with escaped quotes (`\"ctranslate2.libs\"`). When passed through `subprocess.run(cmd, shell=True)`, the shell interpreted the inner quotes and mangled the Python syntax, causing:
```python
SyntaxError: invalid syntax
libs = os.path.join(sp, ctranslate2.libs) if sp else ;
```

**Changes:**
- Replaced the inline `python -c` shell command with a temporary Python script file (`/tmp/fix_cudnn8.py`)
- The script is written to disk and executed directly, completely avoiding shell quoting issues

**Files changed:** `one_click.py`

---

### Fix 12: `torchaudio.AudioMetaData` Missing (`start-voice.py`)

**Problem:** `pyannote.audio` (a dependency of `whisperx`) expects `torchaudio.AudioMetaData` to be available at the top level (`torchaudio.AudioMetaData`). In some torchaudio builds — especially CPU wheels or certain CUDA configurations — this class is only accessible via `torchaudio.backend.common.AudioMetaData` and is not re-exported at the top level. This causes:
```
AttributeError: module 'torchaudio' has no attribute 'AudioMetaData'
```

**Changes:**
- Added a defensive monkey-patch in `start-voice.py` (alongside the existing Gradio 5.x patches)
- If `torchaudio.AudioMetaData` is missing, imports it from `torchaudio.backend.common` and attaches it
- Wrapped in `try/except` so it never crashes if the import path changes in future versions

**Files changed:** `start-voice.py`

---

### Fix 13: Outdated `yt-dlp` Pin (`requirements-voice-*.txt`)

**Problem:** Both `requirements-voice-gpu.txt` and `requirements-voice-cpu.txt` pinned `yt-dlp==2025.11.12`. This version is >5 months old and fails on modern YouTube due to SABR streaming and JS challenge changes.

**Changes:**
- Updated to `yt-dlp>=2026.3.17` in both requirements files

**Files changed:** `requirements-voice-gpu.txt`, `requirements-voice-cpu.txt`

---

## 3. Files Changed (Wave 2)

| File | Fix # | Description |
|---|---|---|
| `configure.sh` | 10 | Add `cmake` to apt dependencies |
| `one_click.py` | 11 | ctranslate2 cuDNN fix → temp script (avoids shell quoting) |
| `start-voice.py` | 12 | Monkey-patch `torchaudio.AudioMetaData` for pyannote.audio |
| `requirements-voice-gpu.txt` | 13 | `yt-dlp>=2026.3.17` |
| `requirements-voice-cpu.txt` | 13 | `yt-dlp>=2026.3.17` |

**Total:** 5 files changed, 0 files removed.

---

## 4. Combined Impact (Wave 1 + Wave 2)

| Metric | Wave 1 | Wave 2 | Total |
|---|---|---|---|
| Fixes | 9 | 4 | **13** |
| Files changed | 24 | 5 | **29** |
| Issues addressed | #76, #62, #60 | — | **3 upstream issues** |

---

## 5. Testing Environment

- **OS:** Ubuntu 24.04.4 LTS (minimal install)
- **Test path:** `./configure.sh` → `./start.sh`
- **Result:** All fixes verified — install completes, app launches, YouTube downloader works

---

## 6. Suggested PR Title for Wave 2

> **fix: cmake dependency, ctranslate2 shell quoting, torchaudio.AudioMetaData, and yt-dlp version**
>
> Follow-up fixes discovered during Ubuntu 24.04.4 testing: adds `cmake` to configure.sh, replaces inline shell script with temp file for ctranslate2 cuDNN fix, patches missing `torchaudio.AudioMetaData` for pyannote.audio compatibility, and updates yt-dlp pin to 2026.3.17+.
