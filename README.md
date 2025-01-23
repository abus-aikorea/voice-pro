<!-- 
    title: Voice-Pro: Ultimate AI Voice Conversion and Multilingual Translation Tool
    description: Powerful AI-powered web application for YouTube video processing, speech recognition, translation, and text-to-speech with multilingual support
    keywords: AI voice conversion, YouTube translation, subtitle generation, speech-to-text, text-to-speech, voice cloning, multilingual translation, ElevenLabs Alternative 
    author: ABUS
    version: 1.6.7
    last-updated: 2024-12-16
    product-type: AI Multimedia Processing Software
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2, F5-TTS, YouTube Downloader, Demucs, MDX-Net
    license: LGPL
-->



# Voice-Pro: Ultimate AI Voice Conversion and Multilingual Translation Tool 🔊

🌍 [한국어](docs/README.kor.md) ∙ [English](docs/README.eng.md) ∙ [中文简体](docs/README.zh.md) ∙ [中文繁體](docs/README.tw.md) ∙ [日本語](docs/README.jpn.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases )


## 🎙️ Advanced AI-Powered Multimedia Processing Tool | Whisper Speech Recognition WebUI

Voice-Pro is a cutting-edge AI-powered web application designed to revolutionize multimedia content processing. With comprehensive features for YouTube video downloading, voice separation, speech recognition, translation, and text-to-speech, it offers an all-in-one solution for content creators, researchers, and multilingual communication professionals.

- 🔊 Cutting-edge Speech Recognition (**Whisper**, **Faster-Whisper**, **Whisper-Timestamped**)
- 🎤 Zero-Shot Voice Cloning with **F5-TTS** & **E2-TTS**
- 🎥 YouTube Video Processing & Audio Extraction
- 🔇 Professional Vocal Isolation (**UVR5** Technology)
- 📢 Multilingual Text-to-Speech (**Edge-TTS**)
- 🌍 Instant Translation Across 100+ Languages
- 🔥 Easily create **AI Cover** with **RVC** Technology

Voice-Pro offers a realistic alternative to **ElevenLabs**, catering to content creators, podcasters, researchers, and developers seeking advanced text-to-speech solutions.

## ⚠️ Attention
  - Voice-Pro has been updated to **v1.7.x**
  - It now supports the latest **yt-dlp** and **Gradio 5**
  - 🔥 **AI-Cover** creation feature has been added. 
  - Please refer to the guidance below.
    - Previous user: If you have updated Voice-Pro to v1.7.x, run **update.bat**. The Python virtual environment will be updated to the latest version.
    - First-time user: Refer to the Installation below. Simply run **configure.bat** and then **start.bat**



## 🚄 Run screen

* `Dubbing Studio` tab : Transcription, Translation & Text-to-Speech
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

* `F5-TTS-Multi` tab : Podcast Production using F5-TTS
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

* `AI Cover` tab : 
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




* `Live Translation` tab : Real-time Speech Recognition and Translation
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



## ⭐ Key Features and Capabilities

### 1. Comprehensive Studio Tab
- **YouTube Video Processing**: Download and extract audio in multiple formats
- **Voice Separation**: Advanced noise removal using MDX-Net and Demucs
- **Multilingual Support**: 
  - Speech recognition for 100+ languages
  - Subtitle creation with customizable options
  - Translation capabilities for over 100 languages

### 2. Advanced Speech Technologies
- **Speech-to-Text (STT)**: 
  - Whisper integration
  - Faster-Whisper support
  - Whisper-timestamped functionality
- **Text-to-Speech (TTS)**: 
  - Edge-TTS with 400+ voices
  - F5-TTS with zero-shot voice cloning
  - Celebrity voice generation
- 🔥 **Speech-to-Speech (RVC)**:
  - Equipped with **Vocal Remover** provided by UVR5 and **RVC** engine.
  - Provides voice modulation function. **RVC v2** is used.

### 3. Real-Time Translation
- Instant speech recognition
- Real-time Multilingual translation
- Configurable audio input sources



## 🤖 WebUI

* `Dubbing Studio` tab
  - Provides integrated environment for YouTube downloader, noise removal, subtitles, translation, and TTS
  - All video/audio formats supported by ffmpeg can be used
  - Selectable output audio format (wav, flac, mp3)
  - Speech recognition and subtitle creation for 100 languages
  - Select subtitle creation options suitable for PC performance (Whisper Model & Compute Type)
  - Translation into over 100 languages ​​and voice generation through TTS
  - The BGM and sound effects from the original video are maintained in the multilingual video.
  - Supports TTS voice speed, volume, and pitch adjustment
  
<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/main_page.kor.png?raw=true" alt="Multilingual Voice Conversion and Subtitle Generation Web UI Interface"/>
</p>  


* `Whisper Caption` tab
  - A tab dedicated to creating subtitles. Supports over 90 languages
  - Display subtitles created with the video
  - World-Level Highlight function provided
  - Denoise function provided (1-Demucs, 2-MDXNet)

* `Translate` tab
  - Dedicated tab for translation. Supports over 100 languages
  - Supports subtitle files (ass, ssa, srt, mpl2, tmp, vtt, microdvd, json)
  - Direct text input is also possible
  - Automatically detects the language of uploaded files

* `Speech` tab
  - Edge-TTS, F5-TTS and AI-Cover(RVC) are supported.
  - Edge-TTS tab
    - supports over 100 languages and more than 400 voices.
    - Pitch, Volume, and Speed can be adjusted.
  - F5-TTS tab
    - supports Zero-Shot Voice Cloning.
    - You can create podcasts using Celeb Voices.

<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/tts_f5_multi.png?raw=true" alt="Podcast Production WebUI Using Voice-Cloning Technology"/>
</p>  

  - 🔥 **AI-Cover** tab 
    - Provides vocal remover. Uses **MDX-Net** and **Demucs**.
    - Provides voice modulation function. **RVC v2** is used.
    - AI Voice can be downloaded from **Discord AI Hub** or, if necessary, **production request (abus.aikorea@gmail.com)**.
    - The length of video supported by the **trial** version is limited to **60 seconds.**

<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/ai_cover.png?raw=true" alt="Podcast Production WebUI Using Voice-Cloning Technology"/>
</p>  

  


* `Live Translation` tab
  - Real-time voice recognition & translation support
  - Select audio input source such as Mic, Speaker, etc.
  - Provides the ability to save captured audio, recognized subtitles, and translated subtitles

<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/live_translation_bbc.png?raw=true" alt="WebUI for Real-Time Speech Recognition and Translation"/>
</p>  

* `Batch` tab
  - Batch processing for large amounts of files
  - Subtitles, translation, TTS



## 💻 Execution environment
* OS: Windows 10/11 (64bits) **※ Linux and Mac OS are not supported.**
* GPU: **NVIDIA** graphics card supporting CUDA 12.1 recommended. 
* VRAM: 4GB or more. 8GB or more recommended.
* RAM: 4GB or more
* HDD: At least 20GB of free space during installation
* Internet connection required (installation and translation work)



## 📀 Installation

Voice-Pro can be easily installed with one click. Just run 🚀**configure.bat** and 🚀**start.bat**


### step 1. Package preparation

  + Clone or download the latest release (**Source code (zip)**) from  [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```
  

### step 2. Install and run the program
1. 🚀 Run `configure.bat`
   - Install git, ffmpeg and CUDA (if using NVIDIA GPU) on Windows. 
   - You only need to run it the first time.
   - An internet connection is required, and it may take over an hour depending on the system.
   - Never close the Windows-Command window during installation.
2. 🚀 Run `start.bat`
   - Start Voice-Pro. Web-UI will run automatically. 
   - When running for the first time, Voice-Pro is installed first. 
   - An internet connection is required, and it may take over an hour depending on the system. 
   - Never close the Windows-Command window during installation.
   - If a problem occurs during installation, delete the **installer_files** folder and run start.bat again.

### step 3. Update the program
* 🚀 Run `update.bat`:
  - Update the Python virtual environment installed in the **installer_files** folder.
  - It is much easier and faster than deleting the **installer_files** folder and reinstalling.
  - Recommended for existing users.

### step 4. Uninstall program
* Run `uninstall.bat`:
  - Remove the **installer_files** folder.
  - Remove ffmepg, git and CUDA packages installed on Windows (if selected)
* Voice-Pro has **portable** installation as standard. To uninstall the program, deleting the installation folder is sufficient.


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
  <img style="width: 60%; height: 60%" src="docs/images/windows_smartscreen_warning.png?raw=true" alt=""/>
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


## ☕ Notice
- This repository offers a **free trial** of Voice-Pro. 
- The free trial has a **usage limit of 30 minutes**. This means that once 30 minutes have elapsed after running, you will no longer be able to use the web UI. 
- It does not mean there is a limitation on the length of media that can be processed, nor does it stop ongoing tasks. You simply cannot click the action button anymore. 
- It may be a bit inconvenient, but to use it again, you just need to close the program and restart it. 
- Previous work results are maintained in the workspace folder. 
- But, There is a **60-second limit** for AI Cover creation.
- The official version of Voice-Pro can be purchased through the ABUS official website (<https://abuskorea.imweb.me>)
- Additionally, if you support us through Buy Me a Coffee ☕, we will give you a usage voucher for up to one month as a token of our gratitude. (<https://github.com/abus-aikorea/voice-pro/discussions/10#discussioncomment-11527327>)
-  For inquiries regarding purchases, business partnerships, tuning, investments, etc., please contact us via email (<abus.aikorea@gmail.com>)."



## 📬 Contact us
* e-mail: <abus.aikorea@gmail.com>
* homepage(Korean): <https://abuskorea.imweb.me>
* Amazon(US): <https://www.amazon.com/dp/B0DBR69JPL>
* Amazon(Japan): <https://www.amazon.co.jp/dp/B0DBVRJ542>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKL8R4>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGKM7FF>
* 네이버 스마트스토어 (S/W): <https://smartstore.naver.com/abus/products/10385660040>
* 네이버 스마트스토어 (Solution): <https://smartstore.naver.com/abus/products/10298346364>

## 👍 YouTube
* Product Information: <https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq>
* Home Karaoke (Pop): <https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6>
* Home Karaoke (K-Pop): <https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8>
* Home Karaoke (J-Pop): <https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq>
  


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



## ©️ Copyright
  <img src="docs/images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)

