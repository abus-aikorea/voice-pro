<!--
    title: Voice-Pro: 究極のAI音声変換および多言語翻訳ツール
    description: YouTubeビデオ処理、音声認識、翻訳、多言語サポートテキスト音声変換のための強力なAIベースWebアプリケーション
    keywords: AI音声変換, YouTube翻訳, 字幕生成, 音声テキスト変換, テキスト音声変換, 音声クローン, 多言語翻訳, ElevenLabs代替
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AIマルチメディア処理ソフトウェア
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, WhisperX, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">最高のAI音声認識、翻訳、多言語ダビングソリューション 🚀</i>
</p>

<h4 align="center">
  <a href="https://www.youtube.com/channel/UCbCBWXuVbk-OBp9T4H5JjAA">
    <img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube" style="height: 20px;">
  </a>
  <a href="https://www.amazon.co.jp/dp/B0F1LQZ42T">
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
    <img src="images/main_page_crop.jpn.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />


## 🎙️ 音声認識、翻訳、ダビングのためのAI搭載ウェブアプリケーション


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

Voice-Proは、マルチメディアコンテンツ制作に革新をもたらす最先端のウェブアプリです。YouTube動画のダウンロード、音声分離、音声認識、翻訳、テキストから音声への変換（TTS）を1つの強力なツールに統合し、クリエイター、研究者、多言語専門家にとって理想的なソリューションを提供します。

- 🔊 トップレベルの音声認識: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- 🎤 ゼロショット音声クローニング: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 多言語テキスト読み上げ: **Edge-TTS**, **kokoro** (有料版には **Azure TTS** が含まれます)
- 🎥 YouTube処理およびオーディオ抽出: **yt-dlp**
- 🌍 100以上の言語に対応した即時翻訳: **Deep-Translator** (有料版には **Azure Translator** が含まれます)


**ElevenLabs**の強力な代替として、Voice-Proはポッドキャスター、開発者、クリエイターに先進的な音声ソリューションを提供します。

## ⚠️ 注意事項
- **v2.xからv3.xへのアップグレード**: 不可能です。`installer_files`フォルダを削除し、最新バージョンの`start.bat`を実行することをお勧めします。
- **v3.xからv3.xへのアップグレード**: 可能です。最新コードをダウンロードした後、`update.bat`を実行してください。
- **初めてのユーザー**: 以下のインストール手順を参照してください。
- **トラブルシューティング**: ほとんどの場合、`installer_files`フォルダを削除し、`configure.bat`を実行した後に`start.bat`を実行することで問題が解決します。
- 🎁 **無料アクティベーションキー申請**: アクティベーションキーを受け取るには、この[Google フォーム](https://forms.gle/anMSmsR5dH9wxE6N6)を記入してください。アクティベーションキーはメールアドレスごとに1つに制限されています。
- 🏆 **追加アクティベーションキー申請**: Voice-Proを使用して素晴らしいコンテンツを作成してください。[![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions)で投稿のリンクを共有してください。皆様の貢献に喜んで報酬をお贈りします。



## 📰 ニュースと履歴

<details open>
<summary>バージョン 3.0</summary>

- 🔥 **AI Cover**機能が削除されました。  
- 🚀 **m-bain/whisperX**のサポートが追加されました。  

</details>

<details>
<summary>バージョン 2.0</summary>

- 🐍 Python 3.10.15、Torch 2.5.1+cu124、Gradio 5.14.0で構築されました。  
- 🆓 無料トライアルは最大**60秒**のメディアをサポートします。  
- 🔥 **AI Cover**機能が追加されました。  
- 🎤 **CosyVoice**および**kokoro**のサポートが導入されました。  
- ⏳ 初回実行時に**CozyVoice2-0.5B (9GB)**をダウンロードし、ネットワーク速度によっては1時間以上かかる場合があります。  
- 🎧 ボイスクローニング用のボイスサンプルは継続的に更新されます。  
- 📝 文ごとの自然な翻訳とTTSのために**spaCy**が追加されました。  
- ☁️ サブスクリプション版には**Microsoft Azure**の翻訳およびTTSが含まれます。  
- 🏪 サブスクリプション版は期間中の**無制限使用**（60秒制限なし）を提供し、[![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com)で購入可能です。  

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
</table>

## ⭐ 主な機能

### 1. ダビングスタジオ
- YouTube動画のダウンロードとオーディオ抽出
- **Demucs**による音声分離
- 音声認識と翻訳のための100以上の言語に対応

### 2. 音声技術
- **音声からテキストへ:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- **テキストから音声へ:** 
  - **Edge-TTS**: 100以上の言語、400以上の声
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: ゼロショットクローニング
  - **kokoro**: HuggingFace TTSアリーナで2位

### 3. リアルタイム翻訳
- 即時音声認識
- その場での多言語翻訳
- カスタマイズ可能なオーディオ入力

## 🤖 ウェブUI

### `ダビングスタジオ`タブ
- 統合ハブ: YouTubeダウンロード、ノイズ除去、字幕、翻訳、TTS
- ffmpeg互換フォーマットすべて対応
- 出力オプション: WAV, FLAC, MP3
- 100以上の言語での字幕と認識
- 速度、ボリューム、ピッチ調整可能なTTS
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.jpn.jpg?raw=true" alt="多言語音声変換および字幕生成ウェブUIインターフェース"/></p>

### `Whisper字幕`タブ
- 字幕専用: 90以上の言語
- ビデオと統合された字幕表示
- 単語単位のハイライトとノイズ除去オプション

### `翻訳`タブ
- 100以上の言語翻訳
- 字幕ファイル対応（ASS、SSA、SRTなど）
- リアルタイム音声認識と翻訳
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.jpg?raw=true" alt="リアルタイム音声認識および翻訳ウェブUI"/></p>

### `音声生成`タブ
- オプション: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- 有名人声でのポッドキャストと多言語サポート
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.jpg?raw=true" alt="音声クローニング技術を活用したポッドキャスト制作ウェブUI"/></p>



## 🎤✨ 参照音声

- 追加したい音声はIssuesページでリクエストしてください。[Issues](https://github.com/abus-aikorea/voice-pro/issues/50)


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




## 💻 システム要件
- **OS:** Windows 10/11（64ビット） ※ Linux/Mac非対応
- **GPU:** CUDA 12.4対応NVIDIA（推奨）
- **VRAM:** 4GB以上（8GB以上推奨）
- **RAM:** 4GB以上
- **ストレージ:** 20GB以上の空き容量
- **インターネット:** 必須

## 📀 インストール

**configure.bat**と**start.bat**でVoice-Proを簡単にインストールできます。

### 1. パッケージ準備
- [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)から最新リリースをダウンロード（**Source code (zip)**）
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. インストールと実行
1. 🚀 **configure.bat**
   - git、ffmpeg、CUDAをインストール（NVIDIA GPU使用時）
   - 初回のみ実行。インターネット必要、1時間以上かかる場合あり
   - コマンドウィンドウを閉じない
2. 🚀 **start.bat**
   - Voice-ProウェブUIを起動
   - 初回実行時に依存関係をインストール（1時間以上かかる場合あり）
   - 問題発生時は**installer_files**を削除後再実行

### 3. アップデート
- 🚀 **update.bat**: Python環境を更新（再インストールより高速）

### 4. アンインストール
- **uninstall.bat**実行、またはフォルダ削除（ポータブルインストール）

## ❓ 使用のヒント

#### ブラウザが自動起動しない場合
- Windowsコマンドウィンドウを閉じ、**start.bat**を再実行するか
- ブラウザを直接起動し、コマンドウィンドウに表示されるアドレス（例: **http://127.0.0.1:7870**）を入力

#### CUDAメモリ不足エラーが出る場合
- Windowsタスクマネージャーの「パフォーマンス」タブでGPUメモリを確認
- ノイズ除去レベルを0または1に設定（レベル2は8GB以上のGPUメモリが必要）
- 計算タイプをintに設定（floatは品質が高いがGPUメモリを多く使用）

#### 字幕の品質を向上させるには？
- 大きなWhisperモデルほど字幕品質が向上する傾向あり（large > medium > small > base > tiny）、ただし必ずしもそうではない
- 計算タイプではfloatが優れた性能を発揮。intはモデル量子化でGPU使用量を減らし速度を向上させるが、性能は低下
- ノイズ除去レベルを上げると背景音が除去され、残った音声のみが認識に使用されるが、常に良い結果を保証するわけではない


## 🚨 お知らせ
- このリポジトリはVoice-Proの**無料トライアル**を提供します。
- Voice-Proの無料トライアル版では、最大**60秒**のメディアを処理できます。
- サブスクリプションバージョンは、Microsoft Azure TTSとTranslatorをサポートしています。[![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com)で購入してください。

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

## ☕ 貢献

こんにちは、Voice-Proチームのデイビッドです。
私たちのチームは、業界最高の人工知能技術を発掘し、誰でも簡単かつ便利に利用できるように提供しています。
私たちは創業からわずか1年の韓国の小さなスタートアップです。皆様や他のクリエイターが素晴らしいコンテンツを制作できるよう、日々努力しています。

あなたの⭐⭐⭐⭐⭐レビューは、私たちのビジネスが皆様と共に成長する上で非常に役立ちますので、ぜひご協力をお願いいたします。私たちの小さなチームを支援してください。

ありがとうございます。
ABUSカスタマーサービス

- このプロジェクトに参加して協力したい場合は、お気軽に[Issues](https://github.com/abus-aikorea/voice-pro/issues)を作成してください。
- 問題が発生した場合は、このプロジェクトを改善するために[Pull requests](https://github.com/abus-aikorea/voice-pro/pulls)を提出してください。
- どのような貢献も歓迎します。
- 購入、ビジネスパートナーシップ、技術チューニング、投資、その他の関連事項に関するお問い合わせは、メール(<abus.aikorea@gmail.com>)でお問い合わせください。
- このプロジェクトが気に入ったら、このリポジトリに星を付けてください。大変感謝いたします。 ⭐⭐⭐
- こちらから寄付でVoice-Proを支援できます。    
</a>
  <a href="https://www.buymeacoffee.com/abus">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
</a>


## 📬 連絡先
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- 有料版購入: [Shopify (Global)](https://r17wvy-t2.myshopify.com), [Naver (Korean)](https://smartstore.naver.com/abus)



## 🙏 クレジット
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

## ©️ 著作権情報
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)