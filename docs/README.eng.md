<!-- 
    title: Voice-Pro: Ultimate AI Voice Conversion and Multilingual Translation Tool
    description: Powerful AI-powered web application for YouTube video processing, speech recognition, translation, and text-to-speech with multilingual support
    keywords: AI voice conversion, YouTube translation, subtitle generation, speech-to-text, text-to-speech, voice cloning, multilingual translation, ElevenLabs Alternative 
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AI Multimedia Processing Software
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->



# Voice-Pro: Ultimate AI Voice Conversion and Multilingual Translation Tool 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)∙ [Deutsch](README.deu.md)∙ [Español](README.spa.md)∙ [Português](README.por.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases )


## 🎙️ Powerful AI-powered web application for YouTube video processing, speech recognition, translation, and text-to-speech with multilingual support

Voice-Pro is a state-of-the-art web app that transforms multimedia content creation. It integrates YouTube video downloading, voice separation, speech recognition, translation, and text-to-speech into a single, powerful tool for creators, researchers, and multilingual professionals.
- 🔊 Top-tier speech recognition: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 Zero-shot voice cloning: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 Multilingual text-to-speech: **Edge-TTS**, **kokoro**
- 🎥 YouTube processing & audio extraction: **yt-dlp**
- 🌍 Instant translation for 100+ languages: **Deep-Translator**
- 🔇 Pro-grade vocal isolation: **UVR5**
- 🔥 AI cover creation: **RVC**

A robust alternative to **ElevenLabs**, Voice-Pro empowers podcasters, developers, and creators with advanced voice solutions.

## ⚠️ Heads-Up
- Now updated to **v2.x** (Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0)
- 🆓 Free trial processes up to **60 seconds** of media
- 🔥 New **AI Cover** feature added
- 🎤 **CosyVoice** and **kokoro** now supported
- ⏳ Initial launch downloads **CozyVoice2-0.5B (9GB)**—may take over an hour based on your network
- 🎧 Celebrity voice options for cloning expanding regularly
- **Guidance:**
  - Upgrade from v1.x to v2.x: **Impossible**. Therefore, it is recommended to delete the installer_files folder and run the latest version of start.bat.
  - Upgrade from v2.x to v2.x: **Possible**. Download the latest code and run update.bat.
  - First-time users: Please refer to the installation instructions below.
  - Troubleshooting: In most cases, deleting the **installer_files** folder and running configure.bat and start.bat sequentially will solve the problem.


## 🚄 Demos

### `Dubbing Studio` Tab: Transcription, Translation & TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description">
   </video>
  <p id="studio-demo-description">
Studio Tab's comprehensive media processing workflow demo: Demonstrates a one-stop media transformation process from YouTube video download to AI-based voice separation, automatic Whisper subtitles, multilingual translation, and professional dubbing using F5-TTS.
  </p>
</div>

### `F5-TTS-Multi` Tab: Podcast Creation
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted" 
   aria-describedby="tts-demo-description">
   </video>
  <p id="tts-demo-description">
Demonstration of F5-TTS's innovative AI voice cloning technology: Showcasing advanced voice conversion technology that precisely mimics the actual voices of Mark Zuckerberg and Elon Musk to create entirely new content.
  </p>
</div>

### `AI Cover` Tab
<div aria-labelledby="ai-cover-description">
  <video src="https://github.com/user-attachments/assets/88a47ab1-a18b-4779-97c8-7c1da84f5fc3"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted" 
   aria-describedby="ai-cover-description">
   </video>
  <p id="ai-cover-description">
Make a Trump version of IU's 'Cupid', Kim Kwang-seok's 'I Miss You', and 'Private's Letter'.
  </p>
</div>


### `Live Translation` Tab: Real-Time Recognition & Translation
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1"
  width="100%" 
  style="max-width: 720px;" 
  controls="controls" 
  muted="muted"
  aria-describedby="translate-demo-description">
  </video>
  <p id="translate-demo-description">
Demonstration of real-time multilingual translation feature: Showcasing an innovative multilingual media processing process that instantly captures BBC news content, generates subtitles in real-time, and immediately translates them into other languages.
  </p>
</div> 



## ⭐ Key Features

### 1. Dubbing Studio
- YouTube video downloads & audio extraction
- Voice separation with **MDX-Net** & **Demucs**
- Supports 100+ languages for speech recognition & translation

### 2. Speech Technologies
- **Speech-to-Text:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- **Text-to-Speech:** 
  - **Edge-TTS**: 100+ languages, 400+ voices
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: Zero-shot cloning
  - **kokoro**: Ranked #2 in HuggingFace TTS Arena
- 🔥 **AI Cover (Speech-to-Speech):** Vocal removal via **UVR5**, modulation with **RVC**

### 3. Real-Time Translation
- Instant speech recognition
- Multilingual translation on the fly
- Customizable audio inputs



## 🤖 WebUI

### `Dubbing Studio` Tab
- All-in-one hub: YouTube downloads, noise removal, subtitles, translation, & TTS
- Supports all ffmpeg-compatible formats
- Output options: WAV, FLAC, MP3
- Subtitles & recognition for 100+ languages
- TTS with speed, volume, & pitch controls
  
<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.eng.png?raw=true" alt="Multilingual Voice Conversion and Subtitle Generation Web UI Interface"/>
</p>  


### `Whisper Caption` Tab
- Subtitle-focused: 90+ languages
- Video-integrated subtitle display
- Word-level highlighting & denoise options

### `Translate` Tab
- Translation for 100+ languages
- Supports subtitle files (ASS, SSA, SRT, etc.)
- Real-time voice recognition & translation

<p align="center">
  <img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="WebUI for Real-Time Speech Recognition and Translation"/>
</p>  

### `Speech Generation` Tab
- Options: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- Celeb voice podcasts & multilingual support

<p align="center">
  <img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="Podcast Production WebUI Using Voice-Cloning Technology"/>
</p>  

### 🔥 `AI Cover` Tab
- Vocal removal: **MDX-Net**, **Demucs**
- Voice modulation: **RVC**
- Download AI voices from [Discord AI Hub](https://discord.com/channels/1159260121998827560/@home) or request via <abus.aikorea@gmail.com>

<p align="center">
  <img style="width: 90%; height: 90%" src="images/ai_cover.png?raw=true" alt="Podcast Production WebUI Using Voice-Cloning Technology"/>
</p>  



## 💻 System Requirements
- **OS:** Windows 10/11 (64-bit) ※ Linux/Mac unsupported
- **GPU:** NVIDIA with CUDA 12.4 (recommended)
- **VRAM:** 4GB+ (8GB+ preferred)
- **RAM:** 4GB+
- **Storage:** 20GB+ free space
- **Internet:** Required



## 📀 Installation

Install Voice-Pro with ease using **configure.bat** and **start.bat**.


### 1. Get the Package

  + Clone or download the latest release (**Source code (zip)**) from  [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```
  

### 2. Install & Run
1. 🚀 **configure.bat**
   - Sets up git, ffmpeg, and CUDA (if NVIDIA GPU)
   - Run once; takes 1+ hour with internet
   - Don’t close the command window
2. 🚀 **start.bat**
   - Launches Voice-Pro WebUI
   - First run installs dependencies (1+ hour)
   - Retry after deleting **installer_files** if issues arise

### 3. Update
- 🚀 **update.bat**: Refreshes Python environment (faster than reinstall)

### 4. Uninstall
- Run **uninstall.bat** or delete the folder (portable install)


## ❓Tips & Tricks

#### If Browser does not run automatically
- Close the Windows-Commnad window and run start.bat again.
- Run the browser directly and enter the address displayed in the Windows-Command window (e.g. **http://127.0.0.1:7892**) in the address bar.

#### If a CUDA Out-Of-Memory error occurs
- Check the GPU memory status in Windows Task Manager - Performance tab. 
- Set the Denoise level to 0 or 1. Denoise level 2 requires at least 8GB of GPU memory.
- Set Compute Type to int type. The float type has better quality, but requires more GPU memory.

#### How to improve the quality of subtitles?
- The quality of subtitles tends to improve with larger Whisper models, but this is not necessarily the case. large > medium > small > base > tiny 
- Among compute types, float type has good performance. The int type is a model that reduces GPU usage and increases speed through model quantization. On the other hand, performance decreases. 
- If you increase the denoise level, more background sounds will be removed, and only the remaining voice will be used for voice recognition. It does not always guarantee good results.
  

## 📢 caution

Windows Defender may give a warning about untrusted application and disallow further execution of Voice-Pro.
If SmartScreen security level is set to "Warn", just click "More info" and then click "Run anyway". 
If SmartScreen is set to level "Block" there will be no button to run the installation. In this case, open the properties of the start.bat file, and check "Unblock", apply the change and run the start.bat again.

<p align="center">
  <img style="width: 40%; height: 40%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  


When Windows Defender mistakenly recognizes a batch file as a Trojan, this is often called a 'False Positive'. To solve this problem, you can go through the following steps:

1. File exception handling: In Windows Defender, you can set certain files or processes to skip security scanning. To do this, follow the steps below:
   * Click the ‘Start’ button and go to ‘Settings’.
   * Click ‘Update & Security’.
   * Select ‘Windows Security’ and go to ‘Virus & threat protection’.
   * Click ‘Manage Virus & Threat Protection Settings’.
   * Select 'Add exception' in 'Virus & threat protection settings'.
   * Select 'File or Folder', find the batch file in question and add it as an exception.
2. Temporarily disable Windows Defender: This may be a temporary solution. However, you must be careful when using this method as it may expose your computer to other threats.
3. Report the problem to anti-virus software: If you are sure that the file is not a Trojan horse, you can report it to Microsoft as a False Positive. Microsoft will review this and take any necessary action.


## 🚨 Notice
- This repository offers a **free trial** of Voice-Pro. 
- The free trial version of Voice-Pro allows you to process up to **60 seconds** of media.
- The official version of Voice-Pro can be purchased through the ABUS official website (<https://abuskorea.imweb.me>)


## ☕ Contributions
- If you want to participate in and help us with this project, feel free to create an [Issues](https://github.com/abus-aikorea/voice-pro/issues) 
- If something goes wrong, please submit a [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) to improve this project.
- Any type of contribution is welcome.
- For inquiries related to purchases, business partnerships, technical tuning, investments, and other matters, please contact us by email. (<abus.aikorea@gmail.com>)."
- If you like this project, please star this repository. We would greatly appreciate it. ⭐⭐⭐
- You can support Voice-Pro with a donation here:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)



## 📬 Contact
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- Amazon: [US](https://www.amazon.com/dp/B0DBR69JPL) | [Japan](https://www.amazon.co.jp/dp/B0DBVRJ542) | [Singapore](https://www.amazon.sg/dp/B0DCGKL8R4) | [UAE](https://www.amazon.ae/dp/B0DCGKM7FF)
- Naver: [Software](https://smartstore.naver.com/abus/products/10385660040) | [Solution](https://smartstore.naver.com/abus/products/10298346364)

## 👍 YouTube
- [Product Info](https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [Karaoke: Pop](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)

## 🙏 Credits
* Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>
* edge-TTS: <https://github.com/rany2/edge-tts>
* F5-TTS: <https://github.com/SWivid/F5-TTS.git>
* openai-whisper: <https://github.com/openai/whisper>
* faster-whisper: <https://github.com/SYSTRAN/faster-whisper>
* whisper-timestamped: <https://github.com/linto-ai/whisper-timestamped>
* RVC-Project: <https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI>
* UVR5: <https://github.com/Anjok07/ultimatevocalremovergui>
* CosyVoice: <https://github.com/FunAudioLLM/CosyVoice>
* kokoro: <https://github.com/hexgrad/kokoro>
* Deep-Translator: <https://github.com/nidhaloff/deep-translator>



## ©️ Copyright
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)

