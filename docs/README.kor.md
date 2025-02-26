<!--
    title: Voice-Pro: 궁극의 AI 음성 변환 및 다국어 번역 도구
    description: 유튜브 비디오 처리, 음성 인식, 번역, 다국어 지원 텍스트 음성 변환을 위한 강력한 AI 기반 웹 애플리케이션
    keywords: AI 음성 변환, 유튜브 번역, 자막 생성, 음성 텍스트 변환, 텍스트 음성 변환, 음성 복제, 다국어 번역, ElevenLabs 대체
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AI 멀티미디어 처리 소프트웨어
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

# Voice-Pro: 궁극의 AI 음성 변환 및 다국어 번역 도구 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md) ∙ [Deutsch](README.deu.md) ∙ [Español](README.spa.md) ∙ [Português](README.por.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

## 🎙️ 유튜브 비디오 처리, 음성 인식, 번역, 다국어 지원 텍스트 음성 변환을 위한 강력한 AI 기반 웹 애플리케이션

Voice-Pro는 멀티미디어 콘텐츠 제작을 혁신하는 최첨단 웹 앱입니다. YouTube 비디오 다운로드, 음성 분리, 음성 인식, 번역, 텍스트-음성 변환(TTS)을 하나의 강력한 도구로 통합하여 창작자, 연구자, 다국어 전문가에게 이상적인 솔루션을 제공합니다.

- 🔊 최고 수준의 음성 인식: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 제로샷 음성 복제: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 다국어 텍스트-음성 변환: **Edge-TTS**, **kokoro**
- 🎥 YouTube 처리 및 오디오 추출: **yt-dlp**
- 🌍 100개 이상 언어 즉시 번역: **Deep-Translator**
- 🔇 전문가 수준의 보컬 분리: **UVR5**
- 🔥 AI 커버 제작: **RVC**

**ElevenLabs**의 강력한 대안으로, Voice-Pro는 팟캐스터, 개발자, 창작자들에게 고급 음성 솔루션을 제공합니다.

## ⚠️ 주의사항
- Voice-Pro가 **v2.x**로 업데이트 되었습니다 (Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0)
- 🆓 무료 체험판은 최대 **60초** 분량의 미디어를 지원합니다.
- 🔥 **AI 커버** 기능이 추가 되었습니다.
- 🎤 **CosyVoice** 및 **kokoro** 지원이 추가되었습니다.
- ⏳ 첫 실행 시 **CozyVoice2-0.5B (9GB)** 를 다운로드합니다. 네트워크 속도에 따라 1시간 이상 소요될 수 있음
- 🎧 음성 복제용 보이스 샘플은 지속적으로 업데이트 될 예정입니다.
- **안내:**
  - v1.x 에서 v2.x 로 업그레이드: **불가능**. 따라서, installer_files 폴더 삭제 후, 최신 버전의 start.bat 실행 권장.
  - v2.x 에서 v2.x 로 업그레이드: **가능**. 최신 코드를 다운로드 받은 후, update.bat 실행.
  - 처음 사용자: 아래 설치방법을 참고하세요.
  - 문제해결: 대부분의 경우, **installer_files** 폴더 삭제 후, configure.bat 와 start.bat 를 차례로 실행하면 해결 됩니다.


## 🚄 데모

### `더빙 스튜디오` 탭: 전사, 번역 및 TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c" width="100%" style="max-width: 720px;" controls muted aria-describedby="studio-demo-description"></video>
  <p id="studio-demo-description">스튜디오 탭의 종합 미디어 처리 워크플로우 데모: YouTube 비디오 다운로드부터 AI 기반 음성 분리, Whisper 자동 자막, 다국어 번역, F5-TTS를 사용한 전문 더빙까지 원스톱 미디어 변환 과정을 보여줍니다.</p>
</div>

### `F5-TTS-Multi` 탭: 팟캐스트 제작
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls muted aria-describedby="tts-demo-description"></video>
  <p id="tts-demo-description">F5-TTS의 혁신적인 AI 음성 복제 기술 데모: 마크 저커버그와 일론 머스크의 실제 목소리를 정밀하게 모방하여 완전히 새로운 콘텐츠를 만드는 고급 음성 변환 기술을 보여줍니다.</p>
</div>

### `AI 커버` 탭
<div aria-labelledby="ai-cover-description">
  <video src="https://github.com/user-attachments/assets/88a47ab1-a18b-4779-97c8-7c1da84f5fc3" width="100%" style="max-width: 720px;" controls muted aria-describedby="ai-cover-description"></video>
  <p id="ai-cover-description">트럼프 버전의 IU 'Cupid', 김광석 '그리운 사람', '이병의 편지'를 제작합니다.</p>
</div>

### `실시간 번역` 탭: 실시간 인식 및 번역
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls muted aria-describedby="translate-demo-description"></video>
  <p id="translate-demo-description">실시간 다국어 번역 기능 데모: BBC 뉴스 콘텐츠를 즉시 캡처하고, 실시간 자막을 생성하며, 즉시 다른 언어로 번역하는 혁신적인 다국어 미디어 처리 과정을 보여줍니다.</p>
</div>



## ⭐ 주요 기능

### 1. 더빙 스튜디오
- YouTube 비디오 다운로드 및 오디오 추출
- **MDX-Net** 및 **Demucs**를 이용한 음성 분리
- 100개 이상의 언어에 대한 음성 인식 및 번역 지원

### 2. 음성 기술
- **음성-텍스트:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- **텍스트-음성 변환:**
  - **Edge-TTS**: 100개 이상 언어, 400개 이상 목소리
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: 제로샷 복제
  - **kokoro**: HuggingFace TTS Arena에서 2위
- 🔥 **AI 커버 (음성-음성):** **UVR5**로 보컬 제거, **RVC**로 변조

### 3. 실시간 번역
- 즉각적인 음성 인식
- 실시간 다국어 번역
- 사용자 지정 가능한 오디오 입력



## 🤖 웹UI

### `더빙 스튜디오` 탭
- 통합 허브: YouTube 다운로드, 소음 제거, 자막, 번역, TTS
- ffmpeg 호환 형식 모두 지원
- 출력 옵션: WAV, FLAC, MP3
- 100개 이상 언어에 대한 자막 및 인식
- 속도, 볼륨, 피치 조절 가능한 TTS
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt="다국어 음성 변환 및 자막 생성 웹UI 인터페이스"/></p>

### `Whisper 자막` 탭
- 자막 전용: 90개 이상 언어
- 비디오와 통합된 자막 표시
- 단어 단위 하이라이트 및 소음 제거 옵션

### `번역` 탭
- 100개 이상 언어 번역
- 자막 파일 지원 (ASS, SSA, SRT 등)
- 실시간 음성 인식 및 번역
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="실시간 음성 인식 및 번역 웹UI"/></p>

### `음성 생성` 탭
- 옵션: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- 유명인 목소리로 팟캐스트 및 다국어 지원
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="음성 복제 기술을 활용한 팟캐스트 제작 웹UI"/></p>

### 🔥 `AI 커버` 탭
- 보컬 제거: **MDX-Net**, **Demucs**
- 음성 변조: **RVC**
- AI 목소리는 [Discord AI Hub](https://discord.com/channels/1159260121998827560/@home)에서 다운로드하거나 <abus.aikorea@gmail.com>으로 요청
<p align="center"><img style="width: 90%; height: 90%" src="images/ai_cover.png?raw=true" alt="음성 복제 기술을 활용한 팟캐스트 제작 웹UI"/></p>



## 🎤✨ 참조 음성

- 추가하고 싶은 음성은 [Issues](https://github.com/abus-aikorea/voice-pro/issues/50) 페이지에서 요청해 주세요. 

### English

<table>
  <tr>
    <td align="center"><img src="celebrities30s/English/Andrew Bustamante.jpg" width="150"><br>Andrew Bustamante</td>
    <td align="center"><img src="celebrities30s/English/Andrew Huberman.jpg" width="150"><br>Andrew Huberman</td>
    <td align="center"><img src="celebrities30s/English/Avi Loeb.jpg" width="150"><br>Avi Loeb</td>
    <td align="center"><img src="celebrities30s/English/Ben Shapiro.jpg" width="150"><br>Ben Shapiro</td>
    <td align="center"><img src="celebrities30s/English/Brett Johnson.jpg" width="150"><br>Brett Johnson</td>
    <td align="center"><img src="celebrities30s/English/Brian Keating.jpg" width="150"><br>Brian Keating</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Coffeezilla.jpg" width="150"><br>Coffeezilla</td>
    <td align="center"><img src="celebrities30s/English/Dan Carlin.jpg" width="150"><br>Dan Carlin</td>
    <td align="center"><img src="celebrities30s/English/David Buss.jpg" width="150"><br>David Buss</td>
    <td align="center"><img src="celebrities30s/English/David Fravor.jpg" width="150"><br>David Fravor</td>
    <td align="center"><img src="celebrities30s/English/David Kipping.jpg" width="150"><br>David Kipping</td>
    <td align="center"><img src="celebrities30s/English/Dennis Whyte.jpg" width="150"><br>Dennis Whyte</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Donald Hoffman.jpg" width="150"><br>Donald Hoffman</td>
    <td align="center"><img src="celebrities30s/English/Donald Trump.jpg" width="150"><br>Donald Trump</td>
    <td align="center"><img src="celebrities30s/English/Douglas Murray.jpg" width="150"><br>Douglas Murray</td>
    <td align="center"><img src="celebrities30s/English/Duncan Trussell.jpg" width="150"><br>Duncan Trussell</td>
    <td align="center"><img src="celebrities30s/English/Elon Musk.jpg" width="150"><br>Elon Musk</td>
    <td align="center"><img src="celebrities30s/English/Garry Nolan.jpg" width="150"><br>Garry Nolan</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Jack Barsky.jpg" width="150"><br>Jack Barsky</td>
    <td align="center"><img src="celebrities30s/English/James Sexton.jpg" width="150"><br>James Sexton</td>
    <td align="center"><img src="celebrities30s/English/Jeff Bezos.jpg" width="150"><br>Jeff Bezos</td>
    <td align="center"><img src="celebrities30s/English/Joe Rogan.jpg" width="150"><br>Joe Rogan</td>
    <td align="center"><img src="celebrities30s/English/John Mearsheimer.jpg" width="150"><br>John Mearsheimer</td>
    <td align="center"><img src="celebrities30s/English/Jordan Peterson.jpg" width="150"><br>Jordan Peterson</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Kanye 'Ye' West.jpg" width="150"><br>Kanye 'Ye' West</td>
    <td align="center"><img src="celebrities30s/English/Mark Zuckerberg.jpg" width="150"><br>Mark Zuckerberg</td>
    <td align="center"><img src="celebrities30s/English/Michael Levin.jpg" width="150"><br>Michael Levin</td>
    <td align="center"><img src="celebrities30s/English/Michael Saylor.jpg" width="150"><br>Michael Saylor</td>
    <td align="center"><img src="celebrities30s/English/Michio Kaku.jpg" width="150"><br>Michio Kaku</td>
    <td align="center"><img src="celebrities30s/English/MrBeast.jpg" width="150"><br>MrBeast</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Nick Lane.jpg" width="150"><br>Nick Lane</td>
    <td align="center"><img src="celebrities30s/English/Paul Rosolie.jpg" width="150"><br>Paul Rosolie</td>
    <td align="center"><img src="celebrities30s/English/Ryan Graves.jpg" width="150"><br>Ryan Graves</td>
    <td align="center"><img src="celebrities30s/English/Sam Altman.jpg" width="150"><br>Sam Altman</td>
    <td align="center"><img src="celebrities30s/English/Sam Harris.jpg" width="150"><br>Sam Harris</td>
    <td align="center"><img src="celebrities30s/English/Stephen Wolfram.jpg" width="150"><br>Stephen Wolfram</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Tucker Carlson.jpg" width="150"><br>Tucker Carlson</td>
    <td align="center"><img src="celebrities30s/English/Vitalik Buterin.jpg" width="150"><br>Vitalik Buterin</td>
    <td align="center"><img src="celebrities30s/English/Yuval Harari.jpg" width="150"><br>Yuval Harari</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>


### Chinese

<table>
  <tr>
    <td align="center"><img src="celebrities30s/Chinese/Dilraba Dilmurat.jpg" width="150"><br>迪丽热巴 (Dílì Rèbā)</td>
    <td align="center"><img src="celebrities30s/Chinese/Jolin Tsai.jpg" width="150"><br>蔡依林 (Cài Yīlín)</td>
    <td align="center"><img src="celebrities30s/Chinese/Kris Wu.jpg" width="150"><br>吴亦凡 (Wú Yìfán)</td>
    <td align="center"><img src="celebrities30s/Chinese/Li Yifeng.jpg" width="150"><br>李易峰 (Lǐ Yìfēng)</td>
    <td align="center"><img src="celebrities30s/Chinese/Yang Mi.jpg" width="150"><br>杨幂 (Yáng Mì)</td>
    <td align="center"><img src="celebrities30s/Chinese/Zhao Liying.jpg" width="150"><br>赵丽颖 (Zhào Lìyǐng)</td>
  </tr>
</table>

### Korean

<table>
  <tr>
    <td align="center"><img src="celebrities30s/Korean/BTS Jin.jpg" width="150"><br>BTS 진 (Jin)</td>
    <td align="center"><img src="celebrities30s/Korean/BTS RM.jpg" width="150"><br>BTS RM</td>
    <td align="center"><img src="celebrities30s/Korean/IU.jpg" width="150"><br>IU (아이유)</td>
    <td align="center"><img src="celebrities30s/Korean/LeeByungHun.jpg" width="150"><br>이병헌</td>
    <td align="center"><img src="celebrities30s/Korean/LeeJungJae.jpg" width="150"><br>이정재</td>
    <td align="center"><img src="celebrities30s/Korean/YouJaeSuk.jpg" width="150"><br>유재석</td>
  </tr>
</table>

### Japanese

<table>
  <tr>
    <td align="center"><img src="celebrities30s/Japanese/Ayase Haruka.jpg" width="150"><br>綾瀬はるか (Ayase Haruka)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>



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
  <img style="width: 40%; height: 40%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
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


## 🚨 공지
- 이 저장소는 Voice-Pro의 **무료 체험판**을 제공합니다.
- Voice-Pro의 무료 체험판 버전은 최대 **60초**의 미디어를 처리할 수 있습니다.
- Voice-Pro의 공식 버전은 ABUS 공식 웹사이트(<https://abuskorea.imweb.me>)를 통해 구매할 수 있습니다.


## ☕ 기여
- 이 프로젝트에 참여하고 저희를 돕고 싶으시다면, 언제든지 [Issues](https://github.com/abus-aikorea/voice-pro/issues)를 생성해주세요.
- 문제가 발생하면, 이 프로젝트를 개선하기 위해 [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls)를 제출해주세요.
- 모든 유형의 기여를 환영합니다.
- 구매, 비즈니스 파트너십, 기술 튜닝, 투자 및 기타 관련 문의는 이메일(<abus.aikorea@gmail.com>)로 문의해주세요.
- 이 프로젝트가 마음에 드시면, 이 저장소에 별표를 눌러주세요. 저희에게 매우 큰 도움이 될 것입니다. ⭐⭐⭐
- 여기에서 기부를 통해 Voice-Pro를 후원할 수 있습니다.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)



## 📬 연락처
- 이메일: <abus.aikorea@gmail.com>
- 홈페이지 (한국어): <https://abuskorea.imweb.me>
- Amazon: [US](https://www.amazon.com/dp/B0DBR69JPL) | [Japan](https://www.amazon.co.jp/dp/B0DBVRJ542) | [Singapore](https://www.amazon.sg/dp/B0DCGKL8R4) | [UAE](https://www.amazon.ae/dp/B0DCGKM7FF)
- 네이버: [소프트웨어](https://smartstore.naver.com/abus/products/10385660040) | [솔루션](https://smartstore.naver.com/abus/products/10298346364)

## 👍 YouTube
- [제품 정보](https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [가라오케: 팝](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)


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

## ©️ 저작권 정보
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)

