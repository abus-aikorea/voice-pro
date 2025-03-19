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

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">最佳AI語音識別、翻譯和多語言配音解決方案 🚀</i>
</p>

<h4 align="center">
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
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 20px;">
  </a>  
  <a href="https://github.com/abus-aikorea/voice-pro/releases">
    <img src="https://img.shields.io/github/v/release/abus-aikorea/voice-pro" alt="release" style="height: 20px;">
  </a>
</h4>

<p align="center">
    <img src="images/main_page_crop.tw.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />


## 🎙️ 為語音識別、翻譯和配音設計的AI驅動網絡應用程序


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

Voice-Pro是一款革新多媒體內容製作的先進網頁應用程式。它將YouTube影片下載、音訊分離、語音辨識、翻譯和文字轉語音(TTS)整合到一個強大的工具中，為創作者、研究人員和多語言專家提供理想的解決方案。

- 🔊 頂級語音辨識：**Whisper**、**Faster-Whisper**、**Whisper-Timestamped**
- 🎤 零樣本聲音克隆：**F5-TTS**、**E2-TTS**、**CosyVoice**
- 📢 多語言文字轉語音：**Edge-TTS**、**kokoro**
- 🎥 YouTube處理和音訊提取：**yt-dlp**
- 🌍 100多種語言即時翻譯：**Deep-Translator**
- 🔇 專業級人聲分離：**UVR5**
- 🔥 AI翻唱製作：**RVC**

作為**ElevenLabs**的強大替代方案，Voice-Pro為播客主持人、開發者和創作者提供進階語音解決方案。

## ⚠️ 請注意
  - 從v1.x升級到v2.x：**不可能**。因此，建議刪除installer_files資料夾，然後運行最新版本的**start.bat**。
  - 從v2.x升級到v2.x：**可能**。下載最新代碼後，運行**update.bat**。
  - 首次使用者：請參考以下安裝方法。
  - 問題解決：在大多數情況下，刪除**installer_files**資料夾後，依次運行**configure.bat**和**start.bat**即可解決。

## 📰 新聞與歷史
- Voice-Pro已更新至**v2.x**（Python 3.10.15，Torch 2.5.1+cu124，Gradio 5.14.0）
- 🆓 免費試用版支持最長**60秒**的媒體。
- 🔥 添加了**AI翻唱**功能。
- 🎤 添加了對**CosyVoice**和**kokoro**的支持。
- ⏳ 首次運行將下載**CozyVoice2-0.5B（9GB）**。根據網絡速度，可能需要1小時以上。
- 🎧 用於語音克隆的語音樣本將持續更新。
- 引入了**spaCy**用於自然的句子級翻譯和TTS。
- ☁️ 訂閱版支持**Microsoft Azure**的**Translator**和**TTS**。
- 🏪 訂閱版在訂閱期限內提供**無限使用**（無60秒限制），可通過[**Shopify**](https://r17wvy-t2.myshopify.com/zh-hant)購買。


## ▶️ 示範

### `配音工作室`標籤頁：轉錄、翻譯和TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/1cf084a4-3286-4055-86d2-238ed179560e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description2">
  </video>   
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
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.tw.jpg?raw=true" alt="多語言語音轉換和字幕生成網頁介面"/></p>

### `Whisper字幕`標籤頁
- 專用字幕：90多種語言
- 影片整合字幕顯示
- 單字級醒目提示和降噪選項

### `翻譯`標籤頁
- 100多種語言翻譯
- 支援字幕檔案（ASS、SSA、SRT等）
- 即時語音辨識和翻譯
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.jpg?raw=true" alt="即時語音辨識和翻譯網頁介面"/></p>

### `語音生成`標籤頁
- 選項：**Edge-TTS**、**F5-TTS**、**CosyVoice**、**kokoro**
- 使用名人聲音製作播客和多語言支援
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.jpg?raw=true" alt="使用語音克隆技術製作播客的網頁介面"/></p>

### 🔥 `AI翻唱`標籤頁
- 人聲移除：**MDX-Net**、**Demucs**
- 語音變調：**RVC**
- AI聲音可從[Discord AI Hub](https://discord.com/channels/1159260121998827560/@home)下載或發郵件至<abus.aikorea@gmail.com>請求
<p align="center"><img style="width: 90%; height: 90%" src="images/ai_cover.jpg?raw=true" alt="使用語音克隆技術製作播客的網頁介面"/></p>



## 🎤✨ 參考聲音

- 請在Issues頁面上請求想添加的聲音。[Issues](https://github.com/abus-aikorea/voice-pro/issues/50)


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
- 直接啟動瀏覽器，在網址列輸入Windows命令視窗顯示的網址（例如**http://127.0.0.1:7870**）

#### 出現CUDA記憶體不足錯誤時
- 在Windows工作管理員-效能標籤中檢查GPU記憶體狀態
- 將降噪等級設定為0或1。降噪等級2需要8GB以上的GPU記憶體
- 將計算類型設定為int類型。float類型品質更好但需要更多GPU記憶體

#### 如何提高字幕品質？
- 字幕品質通常隨著使用更大的Whisper模型而提高，但並不總是如此。large > medium > small > base > tiny
- 在計算類型中，float類型效能更好。int類型透過模型量化降低GPU使用量並提高速度，但效能較差
- 提高降噪等級可以更多地去除背景音，只將剩餘的語音用於語音辨識。但不總是能保證更好的結果



## 🚨 通知
- 此儲存庫提供 Voice-Pro 的**免費試用版**。
- Voice-Pro 的免費試用版允許您處理長達 **60 秒**的媒體。
- 訂閱版本支援 Microsoft Azure TTS 和 Translator。請在 [Shopify](https://r17wvy-t2.myshopify.com/zh-hant) 上購買。


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

## ☕ 貢獻

您好，我是Voice-Pro團隊的戴維。
我們的團隊致力於發掘業內頂尖的人工智慧技術，並提供給大家，讓大家都能輕鬆便捷地使用。
我們是一家剛成立一年的韓國小型創業公司。我們努力工作，旨在幫助您和其他創作者製作出色的內容。

您的⭐⭐⭐⭐⭐評價對我們的業務與您共同成長至關重要，我們對此深表感謝。請您支持我們這個小團隊。

謝謝，
ABUS客戶服務


- 如果您想參與並幫助我們進行此專案，請隨時建立一個 [Issues](https://github.com/abus-aikorea/voice-pro/issues)。
- 如果出現問題，請提交一個 [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) 以改進此專案。
- 歡迎任何類型的貢獻。
- 有關購買、商業夥伴關係、技術調整、投資和其他相關事宜的諮詢，請透過電子郵件 (<abus.aikorea@gmail.com>) 與我們聯繫。
- 如果您喜歡這個專案，請給這個儲存庫加星號。我們將非常感謝。 ⭐⭐⭐
- 您可以在這裡透過捐贈支持 Voice-Pro：

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)


## 📬 聯絡方式
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- Naver (Korean): [30-day subscription](https://smartstore.naver.com/abus/products/11308510267)
- Shopify (Global): [30-day subscription](https://r17wvy-t2.myshopify.com/zh-hant)

## 👍 YouTube
- [PlayList](https://www.youtube.com/watch?v=Tu2okoHY174&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
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
* CosyVoice: <https://github.com/FunAudioLLM/CosyVoice>
* kokoro: <https://github.com/hexgrad/kokoro>
* Deep-Translator: <https://github.com/nidhaloff/deep-translator>
* spaCy: <https://github.com/explosion/spaCy>

## ©️ 版權資訊
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)