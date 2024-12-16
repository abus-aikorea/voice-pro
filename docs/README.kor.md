<!-- 
    title: Voice-Pro: AI Voice Conversion and Translation Solution
    description: Powerful AI-powered web application for YouTube video processing, speech recognition, translation, and text-to-speech with multilingual support
    keywords: AI voice conversion, YouTube translation, subtitle generation, speech-to-text, text-to-speech, voice cloning, multilingual translation
    author: ABUS
    version: 1.6.7
    last-updated: 2024-12-16
    product-type: AI Multimedia Processing Software
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2, F5-TTS, YouTube Downloader, Demucs, MDX-Net
    license: LGPL
-->

# Voice-Pro: Ultimate AI Voice Conversion and Multilingual Translation Tool 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases )


## 🎙️ AI 기반 멀티미디어 처리 도구 | Whisper 음성 인식 WebUI

Voice-Pro는 멀티미디어 콘텐츠 처리를 위해 설계된 최첨단 AI 기반 웹 애플리케이션입니다. YouTube 동영상 다운로드, 음성 분리, 음성 인식, 번역 및 텍스트-음성 변환 등 포괄적인 기능을 제공하여 콘텐츠 제작자, 연구자 및 다국어 커뮤니케이션 전문가를 위한 원스톱 솔루션을 제공합니다.

- 🔊 최첨단 음성 인식 (Whisper, Faster-Whisper, Whisper-Timestamped)
- 🎤 F5-TTS 및 E2-TTS를 이용한 제로샷 음성 클로닝
- 🎥 YouTube 동영상 처리 및 오디오 추출
- 🔇 전문적인 보컬 분리 (UVR5 기술)
- 📢 다국어 텍스트-음성 변환 (Edge-TTS)
- 🌍 100개 이상 언어의 즉각적인 번역

콘텐츠 제작자, 팟캐스터, 연구자 및 개발자를 위한 완벽한 도구 | AI 멀티미디어 솔루션


## 🚄 실행 화면

* `Studio` tab : Transcription, Translation & Text-to-Speech
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description">
   </video>
  <p id="studio-demo-description">
Studio Tab의 미디어 처리 워크플로우 데모: YouTube 동영상 다운로드부터 AI 기반 음성 분리, Whisper 자동 자막 생성, 다국어 번역, 그리고 F5-TTS를 활용한 전문적인 더빙 제작까지의 원스톱 미디어 트랜스포메이션 과정을 시연합니다.
  </p>
</div>

* `TTS` tab : F5-TTS를 이용한 Podcast 제작
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted" 
   aria-describedby="tts-demo-description">
   </video>
  <p id="tts-demo-description">
F5-TTS의 혁신적인 AI 보이스 클로닝 기술을 활용한 팟캐스트 제작 시연: Mark Zuckerberg와 Elon Musk의 실제 음성을 정밀하게 모방하여 완전히 새로운 콘텐츠를 생성하는 첨단 음성 변환 기술을 보여줍니다.
  </p>
</div>

* `Live Translation` tab : 실시간 음성인식 및 번역
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1"
  width="100%" 
  style="max-width: 720px;" 
  controls="controls" 
  muted="muted"
  aria-describedby="translate-demo-description">
  </video>
  <p id="translate-demo-description">
실시간 다국어 번역 기능 데모: YouTube의 BBC 뉴스 콘텐츠를 AI 기반 음성 인식 기술로 즉각 캡처하고, 실시간으로 자막을 생성하며 다른 언어로 즉시 번역하는 혁신적인 다국어 미디어 처리 과정을 실연합니다.
  </p>
</div> 

## ⭐ 주요 기능 및 특징

### 1. 스튜디오 탭
- **YouTube 동영상 처리**: 다양한 형식으로 오디오 다운로드 및 추출
- **음성 분리**: MDX-Net 및 Demucs를 사용한 고급 노이즈 제거
- **다국어 지원**: 
  - 100개 이상 언어에 대한 음성 인식
  - 사용자 정의 가능한 자막 생성
  - 100개 이상 언어에 대한 번역 기능

### 2. 고급 음성 기술
- **음성-텍스트 (STT)**: 
  - Whisper 통합
  - Faster-Whisper 지원
  - Whisper-timestamped 지원
- **텍스트-음성 변환 (TTS)**: 
  - 400개 이상의 음성을 지원하는 Edge-TTS
  - 제로샷 음성 클로닝이 가능한 F5-TTS
  - 유명인 음성 생성

### 3. 실시간 번역
- 리얼타임 음성 인식
- 실시간 다국어 번역
- 구성 가능한 오디오 입력 소스

## ⭐ WebUI

* `Studio` 탭
  - YouTube 다운로더, 노이즈 제거, 자막, 번역, TTS 통합환경으로 제공
  - ffmpeg 이 지원하는 모든 비디오/오디오 포맷 사용 가능
  - 출력 오디오 포맷(wav, flac, mp3) 선택가능
  - 100개 언어에 대한 음성 인식, 자막 생성
  - PC 성능에 맞는 자막 생성 옵션 선택 가능 (Whisper Model & Compute Type)
  - 100여개 언어로 번역 및 TTS 를 통한 음성 생성
  - 원본 영상의 BGM 과 효과음을 다국어 영상에서도 그대로 유지
  - TTS 음성의 속도, 음량, 피치 조절 지원  
  
<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt="다국어 음성 변환 및 자막 생성 웹 UI 인터페이스"/>
</p>  

* `Whisper 자막` 탭
  - 자막 생성 전용 탭. 90여개 언어 지원
  - 영상과 함께 생성된 자막 표시
  - World-Level Highlight 기능 제공
  - Denoise 기능 제공 (1-Demucs, 2-MDXNet)

* `번역` 탭
  - 번역 전용 탭. 100여개 언어 지원
  - 자막파일(ass, ssa, srt, mpl2, tmp, vtt, microdvd, json) 지원
  - 텍스트 직접 입력도 가능
  - 업로드한 파일의 언어를 자동으로 감지

* `TTS` 탭
  - Edge-TTS 와 F5-TTS 를 지원합니다.
  - Edge-TTS 는 100 개 이상의 언어, 400개 이상의 보이스를 지원합니다.
  - Pitch, Volume, Speed 조절이 가능합니다.
  - F5-TTS 는 Zero-Shot Voice Cloning 을 지원합니다.
  - Celeb Voice 를 이용하여 PodCast 를 제작할 수 있습니다.

<p align="center">
  <img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="Voice-Cloning 기술을 이용한 Podcast 제작 WebUI"/>
</p>  


* `Live Translation` 탭
  - 실시간 음성 인식 & 번역 지원
  - Mic, Speaker 등의 오디오 입력소스 선택 가능
  - 캡처된 오디오, 인식된 자막, 번역된 자막 저장 기능 제공

<p align="center">
  <img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="실시간 음성 인식 및 번역을 위한 WebUI"/>
</p>  


* `Batch` 탭
  - 대량의 파일에 대한 일괄 처리
  - 자막, 번역, TTS
 


## 💻 실행환경
* OS : Windows 10/11 (64bits) **※ Linux, Mac OS는 지원하지 않습니다.**
* GPU: CUDA 12.1을 지원하는 **NVIDIA** 그래픽 카드 권장. 
* VRAM: 4GB 이상. 8GB이상 권장.
* RAM: 4GB 이상
* HDD: 설치 중 최소 20GB의 여유 공간
* 인터넷 연결 필요(설치 및 번역 작업)


## 📀 설치와 실행

Voice-Pro 는 one click 설치를 지원합니다. 🚀**configure.bat** 와 🚀**start.bat** 를 순서대로 실행하세요.

### step 1. 패키지 준비

  + Clone or download the latest release (**Source code (zip)**) from  [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)

```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### step 2. 프로그램 설치 및 실행
1. 🚀 `configure.bat` 실행
   - Windows에 ffmpeg, git 과 CUDA(NVIDIA GPU를 사용하는 경우)를 설치합니다. 
   - 최초 1회만 실행하면 됩니다.
   - 인터넷 연결을 필요로하며, 시스템에 따라 설치에 1시간 이상 소요될 수 있음.
   - 설치 중에는 절대 Windows-Command 창을 종료하지 마세요.
2. 🚀 `start.bat` 실행
   - Voice-Pro 를 시작합니다. Web-UI가 자동으로 실행됩니다. 
   - 최초 실행시에는 Voice-Pro 설치 작업을 먼저 진행합니다. 
   - Voice-Pro 설치는 인터넷 연결을 필요로 하며, 시스템에 따라 설치에 1시간 이상이 소요될 수 있습니다. 
   - 설치 중에는 절대 Windows-Command 창을 종료하지 마세요.
   - 설치중 문제가 발생한 경우, installer_files 폴더를 삭제하고 start.bat를 다시 실행하세요.


### step 3. 프로그램 제거
* `uninstall.bat` 실행: 
  - installer_files 폴더를 제거합니다. 
  - Windows 에 설치한 ffmepg, CUDA 패키지를 제거합니다(선택할 경우)
* Voice-Pro는 **포터블** 설치가 기본입니다. 프로그램의 제거는 설치 폴더를 삭제하는 것으로 충분합니다.



## ❓사용팁

#### Browser가 자동으로 실행되지 않는 경우
- Windows-Commnad 창을 종료하고, start.bat 을 다시 실행하거나
- Browser를 직접 실행하고, Windows-Command 창에 표시된 주소(예, **http://127.0.0.1:7892** )를 주소창에 입력합니다.

#### CUDA Out-Of-Memory 오류가 발생하는 경우
- 윈도우 작업관리자 - 성능 탭에서 GPU 메모리 상태를 확인하세요. 
- Denoise 레벨을 0 또는 1 로 설정하세요. Denoise 레벨 2 는 8GB 이상의 GPU 메모리를 필요로 합니다.
- Compute Type 을 int 타입으로 설정하세요. float 타입의 품질이 더 좋지만 더 많은 GPU 메모리를 요구합니다.

#### 자막의 품질을 높이려면?
- 자막의 품질은 더 큰 Whisper 모델을 사용할 수록 좋아지는 경향은 있지만, 꼭 그런것은 아닙니다. large >  medium > small > base > tiny 
- Compute Type 중에서는 float 타입의 성능이 좋습니다. int 타입은 모델 양자화를 통해 GPU사용량을 낮추고 속도를 높인 모델입니다. 반면, 성능은 떨어집니다. 
- Denoise 레벨을 높이면 배경음을 더 많이 제거하고, 남아있는 보이스만 음성인식에 사용하게 됩니다. 항상 좋은 결과를 보장하지는 않습니다.




## 📢 주의사항

Windows Defender가 신뢰할 수 없는 애플리케이션에 대한 경고를 표시하고 Voice-Pro의 추가 실행을 허용하지 않을 수 있습니다.
SmartScreen 보안 수준이 "경고"로 설정되어 있다면 "More info"를 클릭한 후 "어쨌든 실행"을 클릭하세요.
SmartScreen이 "차단" 수준으로 설정되어 있으면 설치를 실행할 수 있는 버튼이 없습니다. 이 경우, start.bat 파일의 속성을 열고 "차단 해제"를 체크한 후 변경 사항을 적용하고 다시 start.bat 파일을 실행하세요.

<p align="center">
  <img style="width: 60%; height: 60%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  


Windows Defender가 실수로 batch 파일을 트로이 목마로 인식하는 경우, 이는 종종 'False Positive'라고 불립니다. 이런 문제를 해결하기 위해서는 다음과 같은 과정을 거칠 수 있습니다.

1. 파일 예외 처리: Windows Defender에서 특정 파일이나 프로세스가 보안 검사를 건너뛰도록 설정할 수 있습니다. 이를 위해 아래의 단계를 따르세요.
   * '시작' 버튼을 클릭하고 '설정'으로 이동하세요.
   * '업데이트 및 보안'을 클릭하세요.
   * 'Windows 보안'을 선택하고 '바이러스 및 위협 보호'로 이동하세요.
   * '바이러스 및 위협 보호 설정 관리'를 클릭하세요.
   * '바이러스 및 위협 보호 설정'에서 '예외 추가'를 선택하세요.
   * '파일 또는 폴더'를 선택하고, 문제의 batch 파일을 찾아 예외로 추가하세요.
2. Windows Defender를 잠시 비활성화: 이 방법은 임시적인 해결책이 될 수 있습니다. 하지만 이 방법을 사용할 경우, 컴퓨터가 다른 위협에 노출될 수 있으므로 주의가 필요합니다.
3. 백신 소프트웨어에 문제 제보: 만약 파일이 트로이 목마가 아니라는 확신이 있다면, Microsoft에 False Positive로 제보할 수 있습니다. Microsoft는 이를 검토한 후 필요한 조치를 취할 것입니다.


## ☕ 공지
- 이 저장소는 Voice-Pro의 **무료 체험판**을 제공합니다. 
- 무료 체험판은 **30분의 사용 제한**이 있습니다. 즉, 실행 후 30분이 경과하면 웹 UI를 더 이상 사용할 수 없습니다. 
- 이는 처리할 수 있는 미디어의 길이에 제한이 있다는 의미가 아니며, 진행 중인 작업을 중단하지도 않습니다. 액션 버튼을 더 이상 클릭할 수 없을 뿐입니다. 
- 약간 불편할 수 있지만, 다시 사용하려면 프로그램을 닫고 다시 시작하면 됩니다. 
- 이전 작업 결과는 workspace 폴더에 유지됩니다. 
- Voice-Pro의 공식 버전은 ABUS 공식 웹사이트(<https://abuskorea.imweb.me>)에서 구매할 수 있습니다.
- 또한, Buy Me a Coffee ☕를 통해 지원해 주시면 감사의 표시로 최대 한 달간 사용할 수 있는 이용권을 제공해 드립니다. (<https://github.com/abus-aikorea/voice-pro/discussions/10#discussioncomment-11527327>)
- 구매, 사업 제휴, 기능추가, 투자 등과 관련된 문의 사항은 이메일(<abus.aikorea@gmail.com>)로 연락 바랍니다.


## 📬 제품 문의
* 이메일 문의: <abus.aikorea@gmail.com>
* 홈페이지: <https://abuskorea.imweb.me>
* Amazon(US): <https://www.amazon.com/dp/B0DBR69JPL>
* Amazon(Japan): <https://www.amazon.co.jp/dp/B0DBVRJ542>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKL8R4>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGKM7FF>
* 네이버 스마트스토어 (S/W): <https://smartstore.naver.com/abus/products/10385660040>
* 네이버 스마트스토어 (솔루션): <https://smartstore.naver.com/abus/products/10298346364>


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


## ©️ 저작권 정보
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)

