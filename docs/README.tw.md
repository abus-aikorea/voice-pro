# Voice-Pro

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/voice-pro)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

用於轉錄、翻譯和文字轉語音的最佳 gradio 網頁界面。一鍵安裝簡便。完全可攜。

## 簡介
* Voice-Pro 是一個整合了**字幕、翻譯和文字轉語音**的解決方案。
* 使用 Voice-Pro 為您的影片添加多語言字幕和多語言音訊。讓全球市場擴展成為可能！
* 您每天早晨都看世界新聞嗎？那麼，試試使用即時翻譯功能。它支援即時翻譯，就像您在 YouTube 上看到的那樣。
* Voice-Pro 配備了 UVR5 提供的**人聲移除器**和 Meta 的 **Demucs** 引擎。
* Voice-Pro 使用 **OpenAI Whisper** 和免費的**開源翻譯器**以及**開源文字轉語音**。
* Voice-Pro 可以透過**一鍵**輕鬆安裝，並提供 Gradio 網頁界面。
* 體驗最高水準的**設備端 AI 語音**技術。

### 運行畫面

https://github.com/user-attachments/assets/27b4e79c-7b29-4efd-80c3-5757fa5f71e4



## 主要功能

* `Studio` 標籤頁
  - 提供 YouTube 下載器、降噪、字幕、翻譯和文字轉語音的整合環境
  - 支援所有 ffmpeg 可用的影片/音訊格式
  - 可選擇輸出音訊格式（wav、flac、mp3）
  - 支援 100 種語言的語音識別和字幕建立
  - 選擇適合 PC 效能的字幕建立選項（Whisper 模型和計算類型）
  - 翻譯成 100 多種語言，並透過文字轉語音生成語音
  - 多語言影片中保留原始影片的背景音樂和音效
  - 支援調整文字轉語音的語速、音量和音調

<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.eng.png?raw=true" alt=""/>
</p>  

* `Whisper Caption` 標籤頁
  - 專門用於建立字幕的標籤頁。支援 90 多種語言
  - 顯示與影片一起建立的字幕
  - 提供單詞級高亮功能
  - 提供降噪功能（1-Demucs，2-MDXNet）

* `Translate` 標籤頁
  - 專門用於翻譯的標籤頁。支援 100 多種語言
  - 支援字幕檔案（ass、ssa、srt、mpl2、tmp、vtt、microdvd、json）
  - 也可以直接輸入文字
  - 自動檢測上傳檔案的語言

* `TTS` 標籤頁
  - 專門用於文字轉語音的標籤頁。支援 100 多種語言和 400 種聲音
  - 支援字幕檔案（ass、ssa、srt、mpl2、tmp、vtt、microdvd、json）
  - 也可以直接輸入文字
  - 自動檢測上傳檔案的語言
  - 可調節音調、音量和語速

* `Live Translation` 標籤頁
  - 支援即時語音識別和翻譯
  - 選擇音訊輸入源，如麥克風、揚聲器等
  - 提供儲存捕獲的音訊、識別的字幕和翻譯的字幕的功能

* `Batch` 標籤頁
  - 批次處理大量檔案
  - 字幕、翻譯、文字轉語音

## 特點
* 您可以下載 YouTube 影片（mp4、webm）並將其儲存為音訊檔案（mp3、wav、flac）。
* 透過去除噪音和分離人聲，可以提高語音識別的準確性。使用 **MDX-Net** 和 Meta 的 **Demucs**。
* 透過 AI 語音識別提供自動字幕建立、機器翻譯和文字轉語音功能。
* 您可以輕鬆製作多語言影片。
* **一鍵安裝**。安裝後，無需額外費用即可**永久**使用。（※ 免費版有 **30 分鐘**使用時間限制）
* 提供**網頁界面**。推薦使用 Google Chrome 瀏覽器。

## 執行環境
* 作業系統：Windows 10/11（64位）**※ 不支援 Linux 和 Mac OS。**
* CPU：Intel 處理器 2GHz 或更高（或同等相容處理器）
* 記憶體：4GB 或更多
* 硬碟：安裝時至少需要 20GB 的可用空間
* 顯示卡：推薦支援 CUDA 12.1 的 **NVIDIA** 顯示卡。顯示記憶體 4GB 或更多，建議 8GB 或更多。
* 需要網際網路連線（用於安裝和翻譯工作）

## 安裝和執行

### 步驟 1. 準備套件
* A. 付費版
    + 將 USB 中包含的壓縮檔（**voice-pro-x.zip**）解壓到電腦上的適當位置。
    + 或者，將已解壓的資料夾（**voice-pro-x**）複製到電腦上的適當位置。

* B. 免費版
  + 從 [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) 下載並解壓最新版本（**Source code (zip)**）
  + 或者，使用 git clone 下載原始碼
    
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 步驟 2. 安裝和執行程式
1. 執行 `configure.bat`
   - 在 Windows 上安裝 ffmpeg 和 CUDA（如果使用 NVIDIA GPU）。
   - 您只需要在第一次執行時執行此操作。
2. 執行 `start.bat`
   - 啟動 Voice-Pro。網頁界面將自動執行。
   - 首次執行時，會先安裝 Voice-Pro。
   - Voice-Pro 安裝需要網際網路連線，根據系統情況，安裝可能需要一個多小時。
   - 安裝過程中切勿關閉 Windows 命令視窗。
   - 如果安裝過程中出現問題，請刪除 installer_files 資料夾並重新執行 start.bat。


### 步驟 3. 解除安裝程式
* 執行 `uninstall.bat`：
  - 刪除 installer_files 資料夾。
  - 刪除在 Windows 上安裝的 ffmpeg 和 CUDA 套件（如果選擇）

* Voice-Pro 預設為**可攜式**安裝。要解除安裝程式，刪除安裝資料夾即可。

## 技巧與竅門

#### 如果瀏覽器沒有自動執行
- 關閉 Windows 命令視窗並重新執行 start.bat。
- 直接執行瀏覽器，並在網址列中輸入 Windows 命令視窗中顯示的網址（例如 **http://127.0.0.1:7892**）。

#### 如果出現 CUDA 記憶體不足錯誤
- 在 Windows 工作管理員 - 效能標籤中檢查 GPU 記憶體狀態。
- 將降噪級別設定為 0 或 1。降噪級別 2 需要至少 8GB 的 GPU 記憶體。
- 將計算類型設定為 int 類型。float 類型品質更好，但需要更多 GPU 記憶體。

#### 如何提高字幕品質？
- 字幕品質往往隨著更大的 Whisper 模型而提高，但並非總是如此。large > medium > small > base > tiny 
- 在計算類型中，float 類型效能較好。int 類型是透過模型量化來減少 GPU 使用並提高速度的模型。然而，效能會降低。
- 如果增加降噪級別，會去除更多背景聲音，只使用剩餘的語音進行語音識別。這並不總是保證好的結果。

## 注意事項
當 Windows Defender 錯誤地將批次處理檔案識別為特洛伊木馬時，這通常被稱為「誤報」。要解決這個問題，您可以透過以下步驟：

1. 檔案例外處理：在 Windows Defender 中，您可以設定某些檔案或程序跳過安全掃描。操作如下：
   * 點擊「開始」按鈕，進入「設定」。
   * 點擊「更新和安全性」。
   * 選擇「Windows 安全性」，進入「病毒與威脅防護」。
   * 點擊「管理病毒與威脅防護設定」。
   * 在「病毒與威脅防護設定」中選擇「新增或移除排除項目」。
   * 選擇「檔案或資料夾」，找到相關的批次處理檔案並將其新增為例外。
2. 暫時停用 Windows Defender：這可能是一個暫時解決方案。但是，使用這種方法時必須小心，因為它可能會使您的電腦面臨其他威脅。
3. 向防毒軟體報告問題：如果您確定該檔案不是特洛伊木馬，可以將其報告給 Microsoft 作為誤報。Microsoft 將對此進行審查並採取必要的行動。

## 聯絡我們
* 電子郵件：<abus.aikorea@gmail.com>
* 主頁（韓語）：<https://abuskorea.imweb.me>
* Naver 智慧商店（軟體）：<https://smartstore.naver.com/abus/products/10385660040>
* Naver 智慧商店（解決方案）：<https://smartstore.naver.com/abus/products/10298346364>
* Coupang（韓國）：<https://www.coupang.com/vp/products/7875503674>
* Amazon（美國）：<https://www.amazon.com/dp/B0D5H8Z4FL>
* Amazon（日本）：<https://www.amazon.co.jp/dp/B0CTHT2JH3>

## YouTube
* 產品資訊：<https://youtu.be/heEN4UIQLjc>
* 自動字幕∙翻譯：<https://youtu.be/uQ14hoEiI4c?si=Io9K_vIDYyeu9Z8_>
* 家庭卡拉 OK：<https://youtube.com/playlist?list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6&si=TZBh5AFjcr7_dyiI>

## 鳴謝
* FacebookResearch Demucs：<https://github.com/facebookresearch/demucs>
* yt-dlp：<https://github.com/yt-dlp/yt-dlp>
* gradio：<https://github.com/gradio-app/gradio>

## 版權
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)
