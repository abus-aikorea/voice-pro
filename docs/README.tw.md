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

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases )


## 🎙️ 先進的AI驅動多媒體處理工具 | Whisper語音識別WebUI

Voice-Pro是一款旨在革新多媒體內容處理的尖端AI驅動的Web應用程式。通過提供YouTube視頻下載、語音分離、語音識別、翻譯和文字轉語音等全面功能，為內容創作者、研究者和多語言通信專業人士提供了一站式解決方案。

- 🔊 尖端語音識別 (**Whisper**, **Faster-Whisper**, **Whisper-Timestamped**)
- 🎤 使用**F5-TTS**和**E2-TTS**進行零樣本語音克隆
- 🎥 YouTube視頻處理和音頻提取
- 🔇 專業語音分離（**UVR5**技術）
- 📢 多語言文字轉語音（**Edge-TTS**）
- 🌍 跨100多種語言的即時翻譯

Voice-Pro為**ElevenLabs**提供了一個現實的替代方案，滿足尋求先進文本轉語音解決方案的內容創作者、播客、研究人員和開發者的需求。


## 🚄 運行畫面

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
Voice-Pro工作室分頁的全面媒體處理工作流程示範：從YouTube視頻下載到基於AI的語音分離、Whisper自動字幕生成、多語言翻譯，再到使用F5-TTS進行專業配音的一站式媒體轉換過程的展示。
  </p>
</div>

* `TTS` tab : Podcast Production using F5-TTS
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted" 
   aria-describedby="tts-demo-description">
   </video>
  <p id="tts-demo-description">
F5-TTS創新的AI語音克隆技術示範：展示了精確模仿Mark Zuckerberg和Elon Musk真實聲音，從而創建全新內容的先進語音轉換技術。
  </p>
</div>

* `Live Translation` tab : 即時語音辨識和翻譯
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1"
  width="100%" 
  style="max-width: 720px;" 
  controls="controls" 
  muted="muted"
  aria-describedby="translate-demo-description">
  </video>
  <p id="translate-demo-description">
Voice-Pro即時多語言翻譯功能示範：展示了一個創新的多語言媒體處理過程，通過AI語音識別技術即時捕獲YouTube BBC新聞內容，即時生成字幕，並立即將其翻譯成其他語言。
  </p>
</div> 

## ⭐ 主要功能和特點

### 1. 全面的工作室標籤
- **YouTube視頻處理**：以多種格式下載和提取音頻
- **語音分離**：使用MDX-Net和Demucs進行高級降噪
- **多語言支持**： 
  - 支持100多種語言的語音識別
  - 具有可自定義選項的字幕創建
  - 支持100多種語言的翻譯功能

### 2. 高級語音技術
- **語音轉文字（STT）**： 
  - Whisper集成
  - Faster-Whisper支持
  - Whisper-timestamped功能
- **文字轉語音（TTS）**： 
  - 具有400多種語音的Edge-TTS
  - 支持零樣本語音克隆的F5-TTS
  - 名人語音生成

### 3. 即時翻譯
- 即時語音識別
- 多語言翻譯
- 可配置的音頻輸入源



## ⭐ WebUI

* `Studio`標籤頁
  - 提供YouTube下載器、噪音去除、字幕、翻譯和TTS的集成環境
  - 支持所有ffmpeg支持的視頻/音頻格式
  - 可選擇輸出音頻格式（wav、flac、mp3）
  - 支持100種語言的語音識別和字幕創建
  - 選擇適合PC性能的字幕創建選項（Whisper模型和計算類型）
  - 翻譯成100多種語言並通過TTS生成語音
  - 原始視頻的背景音樂和音效在多語言視頻中保持不變
  - 支持TTS語音速度、音量和音調調整

<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt="多語言語音轉換和字幕生成Web UI介面"/>
</p>  

* `Whisper Caption`標籤頁
  - 專用於創建字幕的標籤頁。支持90多種語言
  - 顯示與視頻一起創建的字幕
  - 提供單詞級高亮功能
  - 提供降噪功能（1-Demucs、2-MDXNet）

* `Translate`標籤頁
  - 專用於翻譯的標籤頁。支持100多種語言
  - 支持字幕文件（ass、ssa、srt、mpl2、tmp、vtt、microdvd、json）
  - 也可以直接輸入文本
  - 自動檢測上傳文件的語言

* `TTS`標籤頁
  - 支持 Edge-TTS 和 F5-TTS。
  - Edge-TTS 支持超过 100 种语言和 400 种以上的声音。
  - 可以调整音高、音量和速度。
  - F5-TTS 支持零样本语音克隆。
  - 可以使用 Celeb Voice 制作播客。

<p align="center">
  <img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="使用語音克隆技術的播客製作Web介面"/>
</p>  


* `Live Translation`標籤頁
  - 支持實時語音識別和翻譯
  - 選擇麥克風、揚聲器等音頻輸入源
  - 提供保存捕獲的音頻、識別的字幕和翻譯的字幕的功能

<p align="center">
  <img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="用於即時語音識別和翻譯的WebUI"/>
</p>  

* `Batch`標籤頁
  - 大量文件的批處理
  - 字幕、翻譯、TTS

## 💻 執行環境
* 操作系統：Windows 10/11（64位）**※不支持Linux和Mac OS。**
* GPU：推薦支持CUDA 12.1的**NVIDIA**顯卡。
* VRAM：4GB或以上。推薦8GB或以上。
* RAM：4GB或以上
* 硬碟：安裝時至少需要20GB的可用空間
* 需要網絡連接（安裝和翻譯工作）

## 📀 安裝

Voice-Pro可以輕鬆地一鍵安裝。只需運行🚀**configure.bat**和🚀**start.bat**即可。

### 步驟1. 準備包

  + 從[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)克隆或下載最新版本（**Source code (zip)**）。

```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 步驟2. 安裝和運行程序
1. 🚀 運行`configure.bat`
   - 在Windows上安裝git、ffmpeg和CUDA（如果使用NVIDIA GPU）。
   - 只需要在第一次運行時執行。
   - 需要網絡連接，根據系統情況可能需要一個多小時。
   - 安裝過程中切勿關閉Windows命令窗口。
2. 🚀 運行`start.bat`
   - 啟動Voice-Pro。網頁界面將自動運行。
   - 首次運行時，會先安裝Voice-Pro。
   - 需要網絡連接，根據系統情況可能需要一個多小時。
   - 安裝過程中切勿關閉Windows命令窗口。
   - 如果安裝過程中出現問題，請刪除**installer_files**文件夾並再次運行start.bat。

### 步驟3. 卸載程序
* 運行`uninstall.bat`：
  - 刪除**installer_files**文件夾。
  - 刪除安裝在Windows上的ffmpeg、git和CUDA包（如果選擇）。
* Voice-Pro默認為**便攜式**安裝。要卸載程序，只需刪除安裝文件夾即可。

## ❓ 提示和技巧

#### 如果瀏覽器沒有自動運行
- 關閉Windows命令窗口並再次運行start.bat。
- 直接運行瀏覽器並在地址欄輸入Windows命令窗口中顯示的地址（例如 **http://127.0.0.1:7892**）。

#### 如果出現CUDA內存不足錯誤
- 在Windows任務管理器的性能選項卡中檢查GPU內存狀態。
- 將降噪級別設置為0或1。降噪級別2至少需要8GB的GPU內存。
- 將計算類型設置為int類型。float類型質量更好，但需要更多GPU內存。

#### 如何提高字幕質量？
- 字幕質量通常隨著更大的Whisper模型而提高，但並非總是如此。large > medium > small > base > tiny
- 在計算類型中，float類型性能較好。int類型是通過模型量化減少GPU使用並提高速度的模型。另一方面，性能會下降。
- 如果增加降噪級別，將會去除更多背景聲音，只使用剩餘的聲音進行語音識別。這並不總是保證好的結果。

## 📢 注意

Windows Defender 可能會發出有關不受信任的應用程式的警告，並禁止進一步執行 Voice-Pro。
如果 SmartScreen 的安全級別設置為「警告」，只需點擊「更多資訊」，然後點擊「仍然要執行」。
如果 SmartScreen 設置為「阻止」級別，則不會有按鈕來運行安裝。在這種情況下，打開 start.bat 文件的屬性，檢查「解除封鎖」，應用更改後再次運行 start.bat。

<p align="center">
  <img style="width: 60%; height: 60%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  

當Windows Defender錯誤地將批處理文件識別為特洛伊木馬時，這通常被稱為"誤報"。要解決這個問題，您可以按照以下步驟操作：

1. 文件例外處理：在Windows Defender中，您可以設置某些文件或進程跳過安全掃描。要做到這一點，請按照以下步驟：
   * 點擊"開始"按鈕並進入"設置"。
   * 點擊"更新與安全"。
   * 選擇"Windows安全中心"並進入"病毒和威脅防護"。
   * 點擊"管理病毒和威脅防護設置"。
   * 在"病毒和威脅防護設置"中選擇"添加或刪除排除項"。
   * 選擇"文件或文件夾"，找到相關的批處理文件並將其添加為例外。
2. 暫時禁用Windows Defender：這可能是一個臨時解決方案。但是，使用此方法時必須小心，因為它可能會使您的計算機暴露於其他威脅中。
3. 向防病毒軟件報告問題：如果您確定該文件不是特洛伊木馬，可以將其作為誤報向Microsoft報告。Microsoft將審查此問題並採取必要的行動。



## ☕ 通知
- 該倉庫提供 Voice-Pro 的**免費試用**。 
- 免費試用有**30分鐘的使用限制**。這意味著運行後30分鐘後，您將無法再使用Web界面。 
- 這並不意味著處理媒體的長度有限制，也不會停止正在進行的任務。您只是無法再點擊操作按鈕。 
- 可能會有點不便，但要再次使用，只需關閉程序並重新啟動。 
- 先前的工作結果保存在工作空間文件夾中。 
- Voice-Pro的官方版本可以通過ABUS官方網站(<https://abuskorea.imweb.me>)購買。
- 此外，如果您通過Buy Me a Coffee ☕支持我們，我們將作為感謝，為您提供最多一個月的使用憑證。 (<https://github.com/abus-aikorea/voice-pro/discussions/10#discussioncomment-11527327>)
- 關於購買、商業合作、調整、投資等方面的咨詢，請通過電子郵件(<abus.aikorea@gmail.com>)與我們聯繫。



## 📬 聯繫我們
* 電子郵件：<abus.aikorea@gmail.com>
* 主頁（韓語）：<https://abuskorea.imweb.me>
* 亞馬遜（美國）：<https://www.amazon.com/dp/B0DBR69JPL>
* 亞馬遜（日本）：<https://www.amazon.co.jp/dp/B0DBVRJ542>
* 亞馬遜（新加坡）：<https://www.amazon.sg/dp/B0DCGKL8R4>
* 亞馬遜（阿聯酋）：<https://www.amazon.ae/dp/B0DCGKM7FF>
* Naver智能商店（S/W）：<https://smartstore.naver.com/abus/products/10385660040>
* Naver智能商店（解決方案）：<https://smartstore.naver.com/abus/products/10298346364>

## 👍 YouTube
* 產品資訊：<https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq>
* 家庭卡拉OK（流行音樂）：<https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6>
* 家庭卡拉OK（K-Pop）：<https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8>
* 家庭卡拉OK（J-Pop）：<https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq>


## 🙏 鳴謝
* Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>
* edge-TTS: <https://github.com/rany2/edge-tts>
* F5-TTS: <https://github.com/SWivid/F5-TTS.git>
* openai-whisper: <https://github.com/openai/whisper>
* faster-whisper: <https://github.com/SYSTRAN/faster-whisper>
* whisper-timestamped: <https://github.com/linto-ai/whisper-timestamped>

## ©️ 版權
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)
