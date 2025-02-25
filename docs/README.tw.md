<!--
    title: Voice-Pro：終極AI語音轉換和多語言翻譯工具
    description: 強大的AI驅動Web應用程式，用於YouTube影片處理、語音識別、翻譯和多語言支援的文字到語音轉換
    keywords: AI語音轉換, YouTube翻譯, 字幕生成, 語音轉文字, 文字轉語音, 語音克隆, 多語言翻譯, ElevenLabs替代品
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AI多媒體處理軟體
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

# Voice-Pro: 終極AI語音轉換和多語言翻譯工具 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md) ∙ [Deutsch](README.deu.md) ∙ [Español](README.spa.md) ∙ [Português](README.por.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

## 🎙️ 強大的AI驅動Web應用程式，用於YouTube影片處理、語音識別、翻譯和多語言支援的文字到語音轉換

Voice-Pro是一款革新多媒體內容製作的先進網頁應用程式。它將YouTube影片下載、音訊分離、語音辨識、翻譯和文字轉語音(TTS)整合到一個強大的工具中，為創作者、研究人員和多語言專家提供理想的解決方案。

- 🔊 頂級語音辨識：**Whisper**、**Faster-Whisper**、**Whisper-Timestamped**
- 🎤 零樣本聲音克隆：**F5-TTS**、**E2-TTS**、**CosyVoice**
- 📢 多語言文字轉語音：**Edge-TTS**、**kokoro**
- 🎥 YouTube處理和音訊提取：**yt-dlp**
- 🌍 100多種語言即時翻譯：**Deep-Translator**
- 🔇 專業級人聲分離：**UVR5**
- 🔥 AI翻唱製作：**RVC**

作為**ElevenLabs**的強大替代方案，Voice-Pro為播客主持人、開發者和創作者提供進階語音解決方案。

## ⚠️ 注意事項
- Voice-Pro已更新至**v2.x**版本（Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0）
- 🆓 免費試用版支援最長**60秒**的媒體處理
- 🔥 新增**AI翻唱**功能
- 🎤 新增**CosyVoice**和**kokoro**支援
- ⏳ 首次執行時需下載**CozyVoice2-0.5B (9GB)**，根據網路速度可能需要1小時以上
- 🎧 聲音克隆用的語音樣本將持續更新
- **提示：**
  - 從 v1.x 升級到 v2.x：**不可能**。因此，建議刪除 installer_files 資料夾並執行最新版本的 start.bat。
  - 從 v2.x 升級到 v2.x：**可能**。下載最新程式碼後，執行 update.bat。
  - 首次使用者：請參考以下安裝方法。
  - 問題解決：在大多數情況下，刪除 **installer_files** 資料夾並依序執行 configure.bat 和 start.bat 即可解決問題。


## 🚄 示範

### `配音工作室`標籤頁：轉錄、翻譯和TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c" width="100%" style="max-width: 720px;" controls muted aria-describedby="studio-demo-description"></video>
  <p id="studio-demo-description">工作室標籤頁的綜合媒體處理工作流程示範：從YouTube影片下載到AI語音分離、Whisper自動字幕、多語言翻譯，再到使用F5-TTS進行專業配音的一站式媒體轉換過程。</p>
</div>

### `F5-TTS-Multi`標籤頁：播客製作
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls muted aria-describedby="tts-demo-description"></video>
  <p id="tts-demo-description">F5-TTS的創新AI聲音克隆技術示範：精確模仿馬克·祖克柏和伊隆·馬斯克的真實聲音，創建全新內容的進階語音轉換技術展示。</p>
</div>

### `AI翻唱`標籤頁
<div aria-labelledby="ai-cover-description">
  <video src="https://github.com/user-attachments/assets/88a47ab1-a18b-4779-97c8-7c1da84f5fc3" width="100%" style="max-width: 720px;" controls muted aria-describedby="ai-cover-description"></video>
  <p id="ai-cover-description">製作川普版本的IU《Cupid》、金光石《想念的人》、《士兵的信》。</p>
</div>

### `即時翻譯`標籤頁：即時辨識和翻譯
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls muted aria-describedby="translate-demo-description"></video>
  <p id="translate-demo-description">即時多語言翻譯功能示範：即時擷取BBC新聞內容，產生即時字幕，並立即翻譯成其他語言的創新多語言媒體處理過程。</p>
</div>

## ⭐ 主要功能

### 1. 配音工作室
- YouTube影片下載和音訊提取
- 使用**MDX-Net**和**Demucs**進行語音分離
- 支援100多種語言的語音辨識和翻譯

### 2. 語音技術
- **語音轉文字：** **Whisper**、**Faster-Whisper**、**Whisper-Timestamped**
- **文字轉語音：**
  - **Edge-TTS**：支援100多種語言，400多種聲音
  - **E2-TTS**、**F5-TTS**、**CosyVoice**：零樣本克隆
  - **kokoro**：在HuggingFace TTS Arena中排名第二
- 🔥 **AI翻唱（語音轉語音）：** 使用**UVR5**移除人聲，使用**RVC**進行變聲

### 3. 即時翻譯
- 即時語音辨識
- 即時多語言翻譯
- 可自訂音訊輸入

## 🤖 網頁介面

### `配音工作室`標籤頁
- 整合中心：YouTube下載、降噪、字幕、翻譯、TTS
- 支援所有ffmpeg相容格式
- 輸出選項：WAV、FLAC、MP3
- 支援100多種語言的字幕和辨識
- 可調節TTS的速度、音量、音調
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.tw.png?raw=true" alt="多語言語音轉換和字幕生成網頁介面"/></p>

### `Whisper字幕`標籤頁
- 專用字幕：90多種語言
- 影片整合字幕顯示
- 單字級醒目提示和降噪選項

### `翻譯`標籤頁
- 100多種語言翻譯
- 支援字幕檔案（ASS、SSA、SRT等）
- 即時語音辨識和翻譯
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="即時語音辨識和翻譯網頁介面"/></p>

### `語音生成`標籤頁
- 選項：**Edge-TTS**、**F5-TTS**、**CosyVoice**、**kokoro**
- 使用名人聲音製作播客和多語言支援
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="使用語音克隆技術製作播客的網頁介面"/></p>

### 🔥 `AI翻唱`標籤頁
- 人聲移除：**MDX-Net**、**Demucs**
- 語音變調：**RVC**
- AI聲音可從[Discord AI Hub](https://discord.com/channels/1159260121998827560/@home)下載或發郵件至<abus.aikorea@gmail.com>請求
<p align="center"><img style="width: 90%; height: 90%" src="images/ai_cover.png?raw=true" alt="使用語音克隆技術製作播客的網頁介面"/></p>

## 💻 系統需求
- **作業系統：** Windows 10/11（64位元）※不支援Linux/Mac
- **顯示卡：** 支援CUDA 12.4的NVIDIA顯示卡（建議）
- **顯示記憶體：** 4GB以上（建議8GB以上）
- **記憶體：** 4GB以上
- **儲存空間：** 20GB以上可用空間
- **網路：** 必需

## 📀 安裝

使用**configure.bat**和**start.bat**輕鬆安裝Voice-Pro。

### 1. 準備套件
- 從[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)下載最新發布版本（**Source code (zip)**）
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. 安裝和執行
1. 🚀 **configure.bat**
   - 安裝git、ffmpeg、CUDA（使用NVIDIA GPU時）
   - 首次執行一次；需要網路，可能需要1小時以上
   - 不要關閉命令視窗
2. 🚀 **start.bat**
   - 執行Voice-Pro網頁介面
   - 首次執行時安裝相依性（可能需要1小時以上）
   - 如果出現問題，刪除**installer_files**後重新執行

### 3. 更新
- 🚀 **update.bat**：更新Python環境（比重新安裝更快）

### 4. 解除安裝
- 執行**uninstall.bat**或刪除資料夾（可攜式安裝）

## ❓使用技巧

#### 瀏覽器沒有自動啟動時
- 關閉Windows命令視窗，重新執行start.bat，或
- 直接啟動瀏覽器，在網址列輸入Windows命令視窗顯示的網址（例如**http://127.0.0.1:7892**）

#### 出現CUDA記憶體不足錯誤時
- 在Windows工作管理員-效能標籤中檢查GPU記憶體狀態
- 將降噪等級設定為0或1。降噪等級2需要8GB以上的GPU記憶體
- 將計算類型設定為int類型。float類型品質更好但需要更多GPU記憶體

#### 如何提高字幕品質？
- 字幕品質通常隨著使用更大的Whisper模型而提高，但並不總是如此。large > medium > small > base > tiny
- 在計算類型中，float類型效能更好。int類型透過模型量化降低GPU使用量並提高速度，但效能較差
- 提高降噪等級可以更多地去除背景音，只將剩餘的語音用於語音辨識。但不總是能保證更好的結果

## 📢 注意事項

Windows Defender可能會顯示不受信任應用程式的警告，並阻止Voice-Pro繼續執行。
如果SmartScreen安全等級設定為「警告」，請點選「更多資訊」後點選「仍要執行」。
如果SmartScreen設定為「阻止」等級，則沒有可以執行安裝的按鈕。在這種情況下，開啟start.bat檔案的屬性，勾選「解除封鎖」，套用變更後重新執行start.bat檔案。

<p align="center">
  <img style="width: 40%; height: 40%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  

如果Windows Defender錯誤地將批次檔案識別為特洛伊木馬，這通常被稱為「誤判」。要解決這個問題，可以採取以下步驟：

1. 檔案例外處理：可以在Windows Defender中設定特定檔案或程序跳過安全檢查。請按照以下步驟操作：
   * 點選「開始」按鈕，進入「設定」
   * 點選「更新與安全性」
   * 選擇「Windows安全性」，進入「病毒與威脅防護」
   * 點選「管理病毒與威脅防護設定」
   * 在「病毒與威脅防護設定」中選擇「新增或移除排除項目」
   * 選擇「檔案或資料夾」，找到相關批次檔案並新增為例外

2. 暫時停用Windows Defender：這可以作為臨時解決方案。但使用此方法時，請注意電腦可能會暴露於其他威脅中。

3. 向防毒軟體回報問題：如果您確信該檔案不是特洛伊木馬，可以向Microsoft回報為誤判。Microsoft會審查後採取必要的措施。


## 🚨 通知
- 此儲存庫提供 Voice-Pro 的**免費試用版**。
- Voice-Pro 的免費試用版允許您處理長達 **60 秒**的媒體。
- Voice-Pro 的正式版本可透過 ABUS 官方網站 (<https://abuskorea.imweb.me>) 購買。


## ☕ 貢獻
- 如果您想參與並幫助我們進行此專案，請隨時建立一個 [Issues](https://github.com/abus-aikorea/voice-pro/issues)。
- 如果出現問題，請提交一個 [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) 以改進此專案。
- 歡迎任何類型的貢獻。
- 有關購買、商業夥伴關係、技術調整、投資和其他相關事宜的諮詢，請透過電子郵件 (<abus.aikorea@gmail.com>) 與我們聯繫。
- 如果您喜歡這個專案，請給這個儲存庫加星號。我們將非常感謝。 ⭐⭐⭐
- 您可以在這裡透過捐贈支持 Voice-Pro：

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)


## 📬 聯絡方式
- 電子郵件：<abus.aikorea@gmail.com>
- 主頁（韓語）：<https://abuskorea.imweb.me>
- Amazon：[US](https://www.amazon.com/dp/B0DBR69JPL) | [Japan](https://www.amazon.co.jp/dp/B0DBVRJ542) | [Singapore](https://www.amazon.sg/dp/B0DCGKL8R4) | [UAE](https://www.amazon.ae/dp/B0DCGKM7FF)
- 韓國Naver：[軟體](https://smartstore.naver.com/abus/products/10385660040) | [解決方案](https://smartstore.naver.com/abus/products/10298346364)

## 👍 YouTube
- [產品資訊](https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [卡拉OK：流行音樂](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)

## 🙏 鳴謝
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

## ©️ 版權資訊
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)