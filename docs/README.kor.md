<!--
    title: Voice-Pro: 궁극의 AI 음성 변환 및 다국어 번역 도구
    description: 유튜브 비디오 처리, 음성 인식, 번역, 다국어 지원 텍스트 음성 변환을 위한 강력한 AI 기반 웹 애플리케이션
    keywords: AI 음성 변환, 유튜브 번역, 자막 생성, 음성 텍스트 변환, 텍스트 음성 변환, 음성 복제, 다국어 번역, ElevenLabs 대체
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AI 멀티미디어 처리 소프트웨어
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, WhisperX, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->


<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">최고의 AI 음성인식, 번역 및 다국어 더빙 솔루션 🚀</i>
</p>

<h4 align="center">
  <a href="https://deepwiki.com/abus-aikorea/voice-pro">
    <img alt="Ask DeepWiki.com" src="https://devin.ai/assets/deepwiki-badge.png" style="height: 20px;">
  </a>
  <a href="https://www.youtube.com/channel/UCbCBWXuVbk-OBp9T4H5JjAA">
    <img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube" style="height: 20px;">
  </a>
  <a href="https://www.amazon.com/dp/B0F1LQZ42T">
    <img src="https://img.shields.io/badge/Amazon-f90.svg?style=flat-square&logo=amazon&logoColor=white" alt="Amazon" style="height: 20px;">
  </a>
  <a href="https://r17wvy-t2.myshopify.com">
    <img src="https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white" alt="Shopify" style="height: 20px;">
  </a>
    <a href="https://www.buymeacoffee.com/abus">
    <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
  </a>
  <a href="https://github.com/abus-aikorea/voice-pro/releases">
    <img src="https://img.shields.io/github/v/release/abus-aikorea/voice-pro" alt="release" style="height: 20px;">
  </a>
  <a href="https://github.com/abus-aikorea/voice-pro/stargazers">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/abus-aikorea/voice-pro">
  </a>  
</h4>

<p align="center">
    <img src="images/main_page_crop.kor.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />


## 🎙️ 음성 인식, 번역 및 더빙을 위한 AI 기반 웹 애플리케이션

<p>  
  <a href="README.kor.md">
    <img src="https://flagcdn.com/16x12/kr.png" alt="South Korea Flag" style="vertical-align: middle;"> 한국어
  </a> ∙ 
  <a href="README.eng.md">
    <img src="https://flagcdn.com/16x12/us.png" alt="United Kingdom Flag" style="vertical-align: middle;"> English
  </a> ∙ 
  <a href="README.zh.md">
    <img src="https://flagcdn.com/16x12/cn.png" alt="China Flag" style="vertical-align: middle;"> 中文简体
  </a> ∙ 
  <a href="README.tw.md">
    <img src="https://flagcdn.com/16x12/tw.png" alt="Taiwan Flag" style="vertical-align: middle;"> 中文繁體
  </a> ∙ 
  <a href="README.jpn.md">
    <img src="https://flagcdn.com/16x12/jp.png" alt="Japan Flag" style="vertical-align: middle;"> 日本語
  </a> ∙ 
  <a href="README.deu.md">
    <img src="https://flagcdn.com/16x12/de.png" alt="Germany Flag" style="vertical-align: middle;"> Deutsch
  </a> ∙ 
  <a href="README.spa.md">
    <img src="https://flagcdn.com/16x12/es.png" alt="Spain Flag" style="vertical-align: middle;"> Español
  </a> ∙ 
  <a href="README.por.md">
    <img src="https://flagcdn.com/16x12/pt.png" alt="Portugal Flag" style="vertical-align: middle;"> Português
  </a>
</p>


Voice-Pro는 멀티미디어 콘텐츠 제작을 혁신하는 최첨단 웹 앱입니다. YouTube 비디오 다운로드, 음성 분리, 음성 인식, 번역, 텍스트-음성 변환(TTS)을 하나의 강력한 도구로 통합하여 창작자, 연구자, 다국어 전문가에게 이상적인 솔루션을 제공합니다.

- 🔊 최고 수준의 음성 인식: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- 🎤 제로샷 음성 복제: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 다국어 텍스트-음성 변환: **Edge-TTS**, **kokoro** (유료 버전에는 **Azure TTS** 포함)
- 🎥 YouTube 처리 및 오디오 추출: **yt-dlp**
- 🌍 100개 이상의 언어에 대한 즉시 번역: **Deep-Translator** (유료 버전에는 **Azure Translator** 포함)


**ElevenLabs**의 강력한 대안으로, Voice-Pro는 팟캐스터, 개발자, 창작자들에게 고급 음성 솔루션을 제공합니다.


## ⚠️ 주의 사항
- **v2.x에서 v3.x로 업그레이드**: 불가능합니다. `installer_files` 폴더를 삭제하고 최신 버전의 `start.bat`를 실행하는 것을 권장합니다.
- **v3.x에서 v3.x로 업그레이드**: 가능합니다. 최신 코드를 다운로드한 후 `update.bat`를 실행하세요.
- **최초 사용자**: 아래 설치 지침을 참조하세요.
- **문제 해결**: 대부분의 경우, `installer_files` 폴더를 삭제한 후 `configure.bat`를 실행하고 이어서 `start.bat`를 실행하면 문제가 해결됩니다.
- 🎁 **무료 활성화 키 요청**: 활성화 키를 받으려면 이 [Google 설문지](https://forms.gle/anMSmsR5dH9wxE6N6)을 작성해 주세요. 활성화 키는 이메일 주소당 하나로 제한됩니다.
- 🏆 **추가 활성화 키 요청**: Voice-Pro를 사용하여 멋진 콘텐츠를 만드세요. [![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions)에서 게시물 링크를 공유해 주세요. 여러분의 기여에 기꺼이 보답하겠습니다.


## 📰 뉴스 및 히스토리

<details open>
<summary>version 3.1</summary>

- 🪄 **F5-TTS**의 미세 조정 모델 지원
- 🌍 지원 언어 (한국어는 없음 ㅠㅠㅠ)
  - <img src="https://flagcdn.com/16x12/us.png" alt="United Kingdom Flag" style="vertical-align: middle;"> English & <img src="https://flagcdn.com/16x12/cn.png" alt="China Flag" style="vertical-align: middle;"> Chinese: <a href="https://huggingface.co/SWivid/F5-TTS/tree/main/F5TTS_v1_Base"> SWivid/F5-TTS_v1 </a> 
  - <img src="https://flagcdn.com/16x12/fi.png" alt="Spain Flag" style="vertical-align: middle;"> Finnish: <a href="https://huggingface.co/AsmoKoskinen/F5-TTS_Finnish_Model"> AsmoKoskinen/F5-TTS_Finnish_Model </a> 
  - <img src="https://flagcdn.com/16x12/fr.png" alt="Spain Flag" style="vertical-align: middle;"> French: <a href="https://huggingface.co/RASPIAUDIO/F5-French-MixedSpeakers-reduced"> RASPIAUDIO/F5-French-MixedSpeakers-reduced </a> 
  - <img src="https://flagcdn.com/16x12/in.png" alt="Spain Flag" style="vertical-align: middle;"> Hindi: <a href="https://huggingface.co/SPRINGLab/F5-Hindi-24KHz"> SPRINGLab/F5-Hindi-24KHz </a>  
  - <img src="https://flagcdn.com/16x12/it.png" alt="Spain Flag" style="vertical-align: middle;"> Italian: <a href="https://huggingface.co/alien79/F5-TTS-italian"> alien79/F5-TTS-italian </a>  
  - <img src="https://flagcdn.com/16x12/jp.png" alt="Spain Flag" style="vertical-align: middle;"> Japanese: <a href="https://huggingface.co/Jmica/F5TTS/tree/main/JA_21999120"> Jmica/F5TTS/JA_21999120 </a>  
  - <img src="https://flagcdn.com/16x12/ru.png" alt="Spain Flag" style="vertical-align: middle;"> Russian: <a href="https://huggingface.co/hotstone228/F5-TTS-Russian"> hotstone228/F5-TTS-Russian </a> 
  - <img src="https://flagcdn.com/16x12/es.png" alt="Spain Flag" style="vertical-align: middle;"> Spanish: <a href="https://huggingface.co/jpgallegoar/F5-Spanish"> jpgallegoar/F5-Spanish </a> 
  
</details>

<details open>
<summary>버전 3.0</summary>

- 🔥 **AI Cover** 기능이 제거되었습니다.  
- 🚀 **m-bain/whisperX** 지원이 추가되었습니다.  

</details>

<details>
<summary>버전 2.0</summary>

- 🐍 Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0으로 제작되었습니다.  
- 🆓 무료 체험은 최대 **60초** 길이의 미디어를 지원합니다.  
- 🔥 **AI Cover** 기능이 추가되었습니다.  
- 🎤 **CosyVoice** 및 **kokoro** 지원이 도입되었습니다.  
- ⏳ 초기 실행 시 **CozyVoice2-0.5B (9GB)**를 다운로드하며, 네트워크 속도에 따라 1시간 이상 걸릴 수 있습니다.  
- 🎧 음성 복제를 위한 음성 샘플은 지속적으로 업데이트됩니다.  
- 📝 문장별 자연스러운 번역 및 TTS를 위해 **spaCy**가 추가되었습니다.  
- ☁️ 구독 버전은 **Microsoft Azure** 번역기 및 TTS를 포함합니다.  
- 🏪 구독 버전은 구독 기간 동안 **무제한 사용** (60초 제한 없음)을 제공하며, [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com)에서 구매할 수 있습니다.  

</details>

## 🎥 YouTube Showcase

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/scC5CicZ6G0" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/scC5CicZ6G0/hqdefault.jpg" alt="Demo Video 1" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Demo for Voice-Pro (v2.0)</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/Wfo7vQCD4no" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/Wfo7vQCD4no/hqdefault.jpg" alt="Demo Video 2" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">F5-TTS: Voice Cloning</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/GOzCDj4MCpo" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/GOzCDj4MCpo/hqdefault.jpg" alt="Demo Video 3" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Live Transcription & Translation</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/YdAq80wjtuQ" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/YdAq80wjtuQ/hqdefault.jpg" alt="Demo Video 4" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Multi-Lingual Voice Cloning: Korean - German</span>
      </a>
    </td>
  </tr>
  <tr>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/Tu2okoHY174" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/Tu2okoHY174/hqdefault.jpg" alt="Demo Video 5" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Multi-Lingual Voice Cloning: English - Korean</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/dWCEwO56_7Y" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/dWCEwO56_7Y/hqdefault.jpg" alt="Demo Video 6" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Multi-Lingual Voice Cloning: Korean - Japanese</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/HXomwoKS3V4" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/HXomwoKS3V4/hqdefault.jpg" alt="Demo Video 7" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">NVIDIA RTX Video Super-Resolution</span>
      </a>
    </td>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/lZK7pLJBHb4" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/lZK7pLJBHb4/hqdefault.jpg" alt="Demo Video 8" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">AI Karaoke</span>
      </a>
    </td>
  </tr>
  <tr>
    <td style="padding: 10px; border: none;" align="center">
      <a href="https://youtu.be/Co70lh95EsQ" style="text-decoration: none; color: inherit;">
        <img src="https://img.youtube.com/vi/Co70lh95EsQ/hqdefault.jpg" alt="Demo Video 5" width="240" height="135" style="border-radius: 4px;">
        <br>
        <span style="font-size: 16px; font-weight: 600; color: #0f0f0f; line-height: 1.2;">Multi-Lingual Voice Cloning: English - Korean</span>
      </a>
    </td>
  </tr>    
</table>




## ⭐ 주요 기능

### 1. 더빙 스튜디오
- YouTube 비디오 다운로드 및 오디오 추출
- **Demucs**를 사용한 음성 분리
- 음성 인식 및 번역을 위한 100개 이상의 언어 지원

### 2. 음성 기술
- **음성을 텍스트로:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- **텍스트를 음성으로:** 
  - **Edge-TTS**: 100개 이상의 언어, 400개 이상의 음성
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: 제로샷 클로닝
  - **kokoro**: HuggingFace TTS 아레나에서 2위

### 3. 실시간 번역
- 즉각적인 음성 인식
- 실시간 다국어 번역
- 사용자 정의 가능한 오디오 입력



## 🤖 웹UI

### `더빙 스튜디오` 탭
- 통합 허브: YouTube 다운로드, 소음 제거, 자막, 번역, TTS
- ffmpeg 호환 형식 모두 지원
- 출력 옵션: WAV, FLAC, MP3
- 100개 이상 언어에 대한 자막 및 인식
- 속도, 볼륨, 피치 조절 가능한 TTS
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.kor.jpg?raw=true" alt="다국어 음성 변환 및 자막 생성 웹UI 인터페이스"/></p>

### `Whisper 자막` 탭
- 자막 전용: 90개 이상 언어
- 비디오와 통합된 자막 표시
- 단어 단위 하이라이트 및 소음 제거 옵션

### `번역` 탭
- 100개 이상 언어 번역
- 자막 파일 지원 (ASS, SSA, SRT 등)
- 실시간 음성 인식 및 번역
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.jpg?raw=true" alt="실시간 음성 인식 및 번역 웹UI"/></p>

### `음성 생성` 탭
- 옵션: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- 유명인 목소리로 팟캐스트 및 다국어 지원
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.jpg?raw=true" alt="음성 복제 기술을 활용한 팟캐스트 제작 웹UI"/></p>


## 🎤✨ 참조 음성

- 추가하고 싶은 음성은 [Issues](https://github.com/abus-aikorea/voice-pro/issues/50) 페이지에서 요청해 주세요. 

<details>
<summary>
English
</summary> <br />

<table>
  <tr>
    <td align="center"><img src="celebrities30sREADME/English/Andrew Bustamante.jpg" width="150"><br>Andrew Bustamante</td>
    <td align="center"><img src="celebrities30sREADME/English/Andrew Huberman.jpg" width="150"><br>Andrew Huberman</td>
    <td align="center"><img src="celebrities30sREADME/English/Avi Loeb.jpg" width="150"><br>Avi Loeb</td>
    <td align="center"><img src="celebrities30sREADME/English/Ben Shapiro.jpg" width="150"><br>Ben Shapiro</td>
    <td align="center"><img src="celebrities30sREADME/English/Brett Johnson.jpg" width="150"><br>Brett Johnson</td>
    <td align="center"><img src="celebrities30sREADME/English/Brian Keating.jpg" width="150"><br>Brian Keating</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30sREADME/English/Coffeezilla.jpg" width="150"><br>Coffeezilla</td>
    <td align="center"><img src="celebrities30sREADME/English/Dan Carlin.jpg" width="150"><br>Dan Carlin</td>
    <td align="center"><img src="celebrities30sREADME/English/David Buss.jpg" width="150"><br>David Buss</td>
    <td align="center"><img src="celebrities30sREADME/English/David Fravor.jpg" width="150"><br>David Fravor</td>
    <td align="center"><img src="celebrities30sREADME/English/David Kipping.jpg" width="150"><br>David Kipping</td>
    <td align="center"><img src="celebrities30sREADME/English/Dennis Whyte.jpg" width="150"><br>Dennis Whyte</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30sREADME/English/Donald Hoffman.jpg" width="150"><br>Donald Hoffman</td>
    <td align="center"><img src="celebrities30sREADME/English/Donald Trump.jpg" width="150"><br>Donald Trump</td>
    <td align="center"><img src="celebrities30sREADME/English/Douglas Murray.jpg" width="150"><br>Douglas Murray</td>
    <td align="center"><img src="celebrities30sREADME/English/Duncan Trussell.jpg" width="150"><br>Duncan Trussell</td>
    <td align="center"><img src="celebrities30sREADME/English/Elon Musk.jpg" width="150"><br>Elon Musk</td>
    <td align="center"><img src="celebrities30sREADME/English/Garry Nolan.jpg" width="150"><br>Garry Nolan</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30sREADME/English/Jack Barsky.jpg" width="150"><br>Jack Barsky</td>
    <td align="center"><img src="celebrities30sREADME/English/James Sexton.jpg" width="150"><br>James Sexton</td>
    <td align="center"><img src="celebrities30sREADME/English/Jeff Bezos.jpg" width="150"><br>Jeff Bezos</td>
    <td align="center"><img src="celebrities30sREADME/English/Joe Rogan.jpg" width="150"><br>Joe Rogan</td>
    <td align="center"><img src="celebrities30sREADME/English/John Mearsheimer.jpg" width="150"><br>John Mearsheimer</td>
    <td align="center"><img src="celebrities30sREADME/English/Jordan Peterson.jpg" width="150"><br>Jordan Peterson</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30sREADME/English/Kanye 'Ye' West.jpg" width="150"><br>Kanye 'Ye' West</td>
    <td align="center"><img src="celebrities30sREADME/English/Mark Zuckerberg.jpg" width="150"><br>Mark Zuckerberg</td>
    <td align="center"><img src="celebrities30sREADME/English/Michael Levin.jpg" width="150"><br>Michael Levin</td>
    <td align="center"><img src="celebrities30sREADME/English/Michael Saylor.jpg" width="150"><br>Michael Saylor</td>
    <td align="center"><img src="celebrities30sREADME/English/Michio Kaku.jpg" width="150"><br>Michio Kaku</td>
    <td align="center"><img src="celebrities30sREADME/English/MrBeast.jpg" width="150"><br>MrBeast</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30sREADME/English/Nick Lane.jpg" width="150"><br>Nick Lane</td>
    <td align="center"><img src="celebrities30sREADME/English/Paul Rosolie.jpg" width="150"><br>Paul Rosolie</td>
    <td align="center"><img src="celebrities30sREADME/English/Ryan Graves.jpg" width="150"><br>Ryan Graves</td>
    <td align="center"><img src="celebrities30sREADME/English/Sam Altman.jpg" width="150"><br>Sam Altman</td>
    <td align="center"><img src="celebrities30sREADME/English/Sam Harris.jpg" width="150"><br>Sam Harris</td>
    <td align="center"><img src="celebrities30sREADME/English/Stephen Wolfram.jpg" width="150"><br>Stephen Wolfram</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30sREADME/English/Tucker Carlson.jpg" width="150"><br>Tucker Carlson</td>
    <td align="center"><img src="celebrities30sREADME/English/Vitalik Buterin.jpg" width="150"><br>Vitalik Buterin</td>
    <td align="center"><img src="celebrities30sREADME/English/Yuval Harari.jpg" width="150"><br>Yuval Harari</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
</details>


<details>
<summary>
Chinese
</summary> <br />

<table>
  <tr>
    <td align="center"><img src="celebrities30sREADME/Chinese/Dilraba Dilmurat.jpg" width="150"><br>迪丽热巴 (Dílì Rèbā)</td>
    <td align="center"><img src="celebrities30sREADME/Chinese/Jolin Tsai.jpg" width="150"><br>蔡依林 (Cài Yīlín)</td>
    <td align="center"><img src="celebrities30sREADME/Chinese/Kris Wu.jpg" width="150"><br>吴亦凡 (Wú Yìfán)</td>
    <td align="center"><img src="celebrities30sREADME/Chinese/Li Yifeng.jpg" width="150"><br>李易峰 (Lǐ Yìfēng)</td>
    <td align="center"><img src="celebrities30sREADME/Chinese/Yang Mi.jpg" width="150"><br>杨幂 (Yáng Mì)</td>
    <td align="center"><img src="celebrities30sREADME/Chinese/Zhao Liying.jpg" width="150"><br>赵丽颖 (Zhào Lìyǐng)</td>
  </tr>
</table>
</details>


<details>
<summary>
Korean
</summary> <br />

<table>
  <tr>
    <td align="center"><img src="celebrities30sREADME/Korean/BTS Jin.jpg" width="150"><br>BTS 진 (Jin)</td>
    <td align="center"><img src="celebrities30sREADME/Korean/BTS RM.jpg" width="150"><br>BTS RM</td>
    <td align="center"><img src="celebrities30sREADME/Korean/IU.jpg" width="150"><br>IU (아이유)</td>
    <td align="center"><img src="celebrities30sREADME/Korean/LeeByungHun.jpg" width="150"><br>이병헌</td>
    <td align="center"><img src="celebrities30sREADME/Korean/LeeJungJae.jpg" width="150"><br>이정재</td>
    <td align="center"><img src="celebrities30sREADME/Korean/YouJaeSuk.jpg" width="150"><br>유재석</td>
  </tr>
</table>
</details>


<details>
<summary>
Japanese
</summary> <br />

<table>
  <tr>
    <td align="center"><img src="celebrities30sREADME/Japanese/Ayase Haruka.jpg" width="150"><br>綾瀬はるか (Ayase Haruka)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
</details>
<br />


## 💻 시스템 요구사항
- **OS:** Windows 10/11 (64비트) ※ Linux/Mac 미지원
- **GPU:** CUDA 12.4 지원 NVIDIA (권장)
- **VRAM:** 4GB 이상 (8GB 이상 권장)
- **RAM:** 4GB 이상
- **저장소:** 20GB 이상 여유 공간
- **인터넷:** 필수



## 📀 설치

**configure.bat** 및 **start.bat**으로 Voice-Pro를 쉽게 설치하세요.

### 1. 패키지 준비
- [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)에서 최신 릴리스 다운로드 (**Source code (zip)**)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. 설치 및 실행
1. 🚀 **configure.bat**
   - git, ffmpeg, CUDA 설치 (NVIDIA GPU 사용 시)
   - 최초 1회 실행; 인터넷 필요, 1시간 이상 소요 가능
   - 명령 창 닫지 않기
2. 🚀 **start.bat**
   - Voice-Pro 웹UI 실행
   - 첫 실행 시 의존성 설치 (1시간 이상 소요 가능)
   - 문제 발생 시 **installer_files** 삭제 후 재실행

### 3. 업데이트
- 🚀 **update.bat**: Python 환경 갱신 (재설치보다 빠름)

### 4. 제거
- **uninstall.bat** 실행 또는 폴더 삭제 (휴대용 설치)



## ❓사용팁

#### Browser가 자동으로 실행되지 않는 경우
- Windows-Commnad 창을 종료하고, start.bat 을 다시 실행하거나
- Browser를 직접 실행하고, Windows-Command 창에 표시된 주소(예, **http://127.0.0.1:7870** )를 주소창에 입력합니다.

#### CUDA Out-Of-Memory 오류가 발생하는 경우
- 윈도우 작업관리자 - 성능 탭에서 GPU 메모리 상태를 확인하세요. 
- Denoise 레벨을 0 또는 1 로 설정하세요. Denoise 레벨 2 는 8GB 이상의 GPU 메모리를 필요로 합니다.
- Compute Type 을 int 타입으로 설정하세요. float 타입의 품질이 더 좋지만 더 많은 GPU 메모리를 요구합니다.

#### 자막의 품질을 높이려면?
- 자막의 품질은 더 큰 Whisper 모델을 사용할 수록 좋아지는 경향은 있지만, 꼭 그런것은 아닙니다. large >  medium > small > base > tiny 
- Compute Type 중에서는 float 타입의 성능이 좋습니다. int 타입은 모델 양자화를 통해 GPU사용량을 낮추고 속도를 높인 모델입니다. 반면, 성능은 떨어집니다. 
- Denoise 레벨을 높이면 배경음을 더 많이 제거하고, 남아있는 보이스만 음성인식에 사용하게 됩니다. 항상 좋은 결과를 보장하지는 않습니다.



## 🚨 공지
- 이 저장소는 Voice-Pro의 **무료 체험판**을 제공합니다.
- Voice-Pro의 무료 체험판 버전은 최대 **60초**의 미디어를 처리할 수 있습니다.
- Subscription 버전은 Microsoft Azure TTS 와 Translator 를 지원합니다. [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com) 에서 구매하세요..

<table>
  <tr>
    <th></th>
    <th>Trial Version</th>
    <th>☕Contributor Version</th>
    <th>Subscription Version</th>
  </tr>
  <tr>
    <th>Media Length Limit</th>
    <td>60 seconds</td>
    <td>Unlimited</td>
    <td>Unlimited</td>
  </tr>
  <tr>
    <th>Translation Service</th>
    <td>Google Translate (Open Source)</td>
    <td>Google Translate (Open Source)</td>
    <td>Azure Translate (Microsoft)</td>
  </tr>
  <tr>
    <th>Text-to-Speech Service</th>
    <td>Edge TTS (Open Source)</td>
    <td>Edge TTS (Open Source)</td>
    <td>Azure TTS (Microsoft)</td>
  </tr>
</table>


<br />

## ⏳ 자막 제작, 번역, TTS를 위한 SaaS 플랫폼

아래 표는 자막 제작, 번역, 텍스트-음성 변환(TTS/더빙) 기능을 지원하는 SaaS 플랫폼을 정리한 것입니다. 비용은 2025년 4월 15일 기준 최신 가격 데이터를 바탕으로, 60분 분량의 한국어 영상에 대해 자막 생성, 영어 번역, 영어 더빙 처리를 포함하여 계산되었습니다.

| 플랫폼 | 자막 제작 | 번역 | TTS/더빙 | 60분 영상 처리 비용 (USD, 약) | 주요 기능 |
| --- | --- | --- | --- | --- | --- |
| **[Maestra](https://maestra.ai)** | ✅ | ✅ | ✅ | $23.70 | 125+ 언어, 실시간 자막, SEO 키워드 추출, 15분 무료 체험. |
| **[Kapwing](https://www.kapwing.com)** | ✅ | ✅ | ✅ | $30\~$40 (Pro 플랜, 분당) | AI 자막, 100+ 언어 번역, 자동 립싱크 더빙, 무료 티어 제공. |
| **[VEED.IO](https://www.veed.io)** | ✅ | ✅ | ❌ | $24\~$36 (Pro 플랜, 부분 처리) | 99.9% 정확도 자막, 인스타그램 최적화 자막, 직관적인 편집기. |
| **[HappyScribe](https://happyscribe.com)** | ✅ | ✅ | ✅ | $36\~$48 (종량제) | 120+ 언어, 전문 교정 옵션, 보안, 회의 전사. |
| **[Sonix](https://sonix.ai)** | ✅ | ✅ | ✅ | $30\~$40 (Standard 플랜) | 54+ 언어, 30분 무료 전사, YouTube/Zoom 통합. |
| **[Descript](https://descript.com)** | ✅ | ✅ | ✅ | $36\~$48 (Creator 플랜) | 텍스트 기반 편집, Overdub TTS, 필러 단어 제거, 1시간 무료 전사. |
| **[AppTek](https://apptek.ai)** | ✅ | ✅ | ✅ | 맞춤 가격 (문의) | 미디어 특화, 맞춤 모델, 메타데이터 생성, 클라우드 기반 Workbench. |
| **[Transkriptor](https://transkriptor.com)** | ✅ | ✅ | ❌ | $12\~$18 (종량제) | 100+ 언어, YouTube 링크 전사, 99% 정확도, 간단한 편집기. |

### 비용 계산 상세

- **[Maestra](https://maestra.ai)**: Premium 플랜 ($158/월, 1200 크레딧). 60분 영상: 자막 60 크레딧 + 번역 60 크레딧 + 더빙 60 크레딧 = 180 크레딧. 비용 = (180/1200) \* $158 = $23.70.
- **[Kapwing](https://www.kapwing.com)**: Pro 플랜 (\~$24/월, 제한된 분량). 자막+번역+더빙 분당 $0.50\~$0.67 추정 (분당 가격 트렌드 기반). 60분 비용: $30\~$40. 정확한 가격은 확인 필요.
- **[VEED.IO](https://www.veed.io)**: Pro 플랜 (\~$24/월). 자막+번역 분당 $0.40\~$0.60 추정. TTS 없음, 부분 처리. 60분 비용: $24\~$36. veed.io에서 확인.
- **[HappyScribe](https://happyscribe.com)**: 종량제 (전사 분당 \~$0.20, 번역 $0.20, 더빙 $0.20). 60분 비용: $36\~$48 (결합 서비스 가정). happyscribe.com에서 확인.
- **[Sonix](https://sonix.ai)**: Standard 플랜 (전사 시간당 \~$10, 번역/더빙 추가). 총 분당 $0.50\~$0.67 추정. 60분 비용: $30\~$40. sonix.ai에서 확인.
- **[Descript](https://descript.com)**: Creator 플랜 (\~$24/월, 제한된 시간). 자막+번역+더빙 분당 $0.60\~$0.80 추정. 60분 비용: $36\~$48. descript.com에서 확인.
- **[AppTek](https://apptek.ai)**: 기업용 맞춤 가격. 공개 분당 요금 없음. apptek.ai로 문의.
- **[Transkriptor](https://transkriptor.com)**: 종량제 (전사 분당 $0.05\~$0.10, 번역 유사). TTS 없음, 부분 처리. 60분 비용: $12\~$18. transkriptor.com에서 확인.

### 참고

- **60분 영상 처리 비용**: 비용은 60분 한국어 영상의 자막, 영어 번역, 영어 더빙(가능한 경우)을 처리하는 것을 가정하며, 근사치입니다. TTS 미지원 플랫폼(예: VEED.IO, Transkriptor)은 부분 처리 비용을 반영.
- **언어 지원**: 대부분 플랫폼은 한국어와 영어를 지원. 특정 언어 지원 여부는 각 웹사이트에서 확인.
- **사용 사례**:
  - 미디어/엔터테인먼트: AppTek, Maestra
  - 소셜 미디어: Kapwing, VEED.IO
  - 팟캐스트/인터뷰: Sonix, Descript
  - E-러닝/글로벌 콘텐츠: Transkriptor, HappyScribe
- **가격 업데이트**: 플랜 변경이나 프로모션으로 가격이 변동될 수 있음. 최신 정보는 공식 웹사이트에서 확인.
- 기여나 특정 사용 사례 추천을 위해 이 저장소에서 이슈를 열거나 풀 리퀘스트를 제출하세요!


<br />



## ☕ 기여

안녕하세요, 저는 Voice-Pro 팀의 David입니다.
저희 팀은 업계 최고의 AI 기술을 발굴하여 누구나 쉽고 편리하게 사용할 수 있도록 제공하고 있습니다.
저희는 설립된 지 1년밖에 되지 않은 한국의 작은 스타트업입니다. 여러분과 다른 창작자들이 훌륭한 콘텐츠를 제작할 수 있도록 열심히 노력하고 있습니다.
여러분의 ⭐⭐⭐⭐⭐ 리뷰는 저희 비즈니스가 여러분과 함께 성장하는 데 큰 도움이 됩니다. 저희 작은 팀을 지원해 주시면 감사하겠습니다.

감사합니다,
ABUS 고객 서비스

- 이 프로젝트에 참여하고 저희를 돕고 싶으시다면, 언제든지 [Issues](https://github.com/abus-aikorea/voice-pro/issues)를 생성해주세요.
- 문제가 발생하면, 이 프로젝트를 개선하기 위해 [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls)를 제출해주세요.
- 모든 유형의 기여를 환영합니다.
- 구매, 비즈니스 파트너십, 기술 튜닝, 투자 및 기타 관련 문의는 이메일(<abus.aikorea@gmail.com>)로 문의해주세요.
- 이 프로젝트가 마음에 드시면, 이 저장소에 별표를 눌러주세요. 저희에게 매우 큰 도움이 될 것입니다. ⭐⭐⭐
- 기부를 통해 Voice-Pro를 후원할 수 있습니다.   
</a>
  <a href="https://www.buymeacoffee.com/abus">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
</a>




## 📬 연락처
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- 유료버전 구매매: [Shopify (Global)](https://r17wvy-t2.myshopify.com), [Naver (Korean)](https://smartstore.naver.com/abus)



## 🙏 Credits
* Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>
* edge-TTS: <https://github.com/rany2/edge-tts>
* F5-TTS: <https://github.com/SWivid/F5-TTS.git>
* openai-whisper: <https://github.com/openai/whisper>
* faster-whisper: <https://github.com/SYSTRAN/faster-whisper>
* whisper-timestamped: <https://github.com/linto-ai/whisper-timestamped>
* whisperX: <https://github.com/m-bain/whisperX>
* CosyVoice: <https://github.com/FunAudioLLM/CosyVoice>
* kokoro: <https://github.com/hexgrad/kokoro>
* Deep-Translator: <https://github.com/nidhaloff/deep-translator>
* spaCy: <https://github.com/explosion/spaCy>

## ©️ 저작권 정보
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)

