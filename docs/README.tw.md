# Voice-Pro: The best gradio web-ui for transcription, translation and text-to-speech 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/voice-pro)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases )


**Voice-Pro是最佳的轉錄、翻譯和文字轉語音的gradio網頁界面。** 它可以一鍵安裝。使用Miniconda創建虛擬環境，完全獨立於Windows系統運行（完全便攜）。支持實時轉錄和翻譯，以及批處理模式。

- **YouTube下載器**：您可以下載YouTube視頻並提取音頻（mp3、wav、flac）。
- **人聲分離**：使用UVR5支持的MDX-Net和Meta開發的Demucs引擎進行語音分離。
- **STT**：支持使用Whisper、Faster-Whisper和whisper-timestamped進行語音轉文字。
- **翻譯器**：Google翻譯。短文翻譯，字幕文件翻譯。
- **TTS**：文字轉語音。Edge-TTS。zero-shot語音克隆的E2和F5-TTS。
- 我們免費提供Celeb聲音。試著製作自己的播客。您可以在F5-TTS標籤中查看。


### ☕ 通知
- 該倉庫提供 Voice-Pro 的**免費試用**。 
- 免費試用有**30分鐘的使用限制**。這意味著運行後30分鐘後，您將無法再使用Web界面。 
- 這並不意味著處理媒體的長度有限制，也不會停止正在進行的任務。您只是無法再點擊操作按鈕。 
- 可能會有點不便，但要再次使用，只需關閉程序並重新啟動。 
- 先前的工作結果保存在工作空間文件夾中。 
- Voice-Pro的官方版本可以通過ABUS官方網站(<https://abuskorea.imweb.me>)購買。
- 此外，如果您通過Buy Me a Coffee ☕支持我們，我們將作為感謝，為您提供最多一個月的使用憑證。 (<https://github.com/abus-aikorea/voice-pro/discussions/10#discussioncomment-11527327>)
- 關於購買、商業合作、調整、投資等方面的咨詢，請通過電子郵件(<abus.aikorea@gmail.com>)與我們聯繫。


### 🚄 運行畫面

* `TTS` tab : Podcast Production using F5-TTS
<video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls="controls" muted="muted"></video>

* `Studio` tab : Transcription, Translation & Text-to-Speech
<video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c" width="100%" style="max-width: 720px;" controls="controls" muted="muted"></video>

* `Live Translation` tab : 即時語音辨識和翻譯
<video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls="controls" muted="muted"></video>




## ⭐ 主要功能

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
  <img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt=""/>
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
  <img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt=""/>
</p>  


* `Live Translation`標籤頁
  - 支持實時語音識別和翻譯
  - 選擇麥克風、揚聲器等音頻輸入源
  - 提供保存捕獲的音頻、識別的字幕和翻譯的字幕的功能

<p align="center">
  <img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt=""/>
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
- 直接運行瀏覽器並在地址欄輸入Windows命令窗口中顯示的地址（例如**http://127.0.0.1:7892**）。

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
