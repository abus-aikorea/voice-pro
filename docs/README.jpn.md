<!--
    title: Voice-Pro: 究極のAI音声変換および多言語翻訳ツール
    description: YouTubeビデオ処理、音声認識、翻訳、多言語サポートテキスト音声変換のための強力なAIベースWebアプリケーション
    keywords: AI音声変換, YouTube翻訳, 字幕生成, 音声テキスト変換, テキスト音声変換, 音声クローン, 多言語翻訳, ElevenLabs代替
    author: ABUS
    version: 4.0.0
    last-updated: 2026-07-13
    product-type: AIマルチメディア処理ソフトウェア
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, CosyVoice, kokoro, uv
    license: LGPL
-->

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">最高のAI音声認識、翻訳、多言語ダビングソリューション 🚀</i>
</p>

<h4 align="center">
  <a href="https://deepwiki.com/abus-aikorea/voice-pro">
    <img alt="Ask DeepWiki.com" src="https://deepwiki.com/badge.svg" style="height: 20px;">
  </a>
  <a href="https://www.youtube.com/channel/UCbCBWXuVbk-OBp9T4H5JjAA">
    <img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube" style="height: 20px;">
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
  </a> ∙ 
  <a href="README.fas.md">
    <img src="https://flagcdn.com/16x12/ir.png" alt="Iran Flag" style="vertical-align: middle;"> فارسی
  </a>
</p>

Voice-Proは、マルチメディアコンテンツ制作に革新をもたらす最先端のウェブアプリです。YouTube動画のダウンロード、音声分離、音声認識、翻訳、テキストから音声への変換（TTS）を1つの強力なツールに統合し、クリエイター、研究者、多言語専門家にとって理想的なソリューションを提供します。

- 🔊 トップレベルの音声認識: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 ゼロショット音声クローニング: **F5-TTS**, **E2-TTS**, **CosyVoice** (**Fun-CosyVoice3** を含む — 韓国語ほか8言語に対応)
- 📢 多言語テキスト読み上げ: **Edge-TTS**, **kokoro** (独自のキーで **Azure TTS** も利用可能 — 下記の「Azureサービス」セクションを参照)
- 🎥 YouTube処理およびオーディオ抽出: **yt-dlp**
- 🌍 100以上の言語に対応した即時翻訳: **Deep-Translator** (独自のキーで **Azure Translator** も利用可能)


**ElevenLabs**の強力な代替として、Voice-Proはポッドキャスター、開発者、クリエイターに先進的な音声ソリューションを提供します。

## ⚠️ 注意事項
- [WeConnect](https://www.wctokyoseoul.com)の開発作業により、Voice-Proの開発およびアップデートは当分の間不可能です。
- すべてのVoice-Proコードを公開し、完全無料に変更しました。Voice-Proは現在、誰でも自由に配布および変更できます。
- NVIDIA GPUを搭載したWindows環境で正常に動作します。Mac、Linuxでの動作は確認していません。
- ご要望は、[![GitHub Issues](https://img.shields.io/github/issues/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/issues)  または [![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions)  ページに残してください。
- **トラブルシューティング**: ほとんどの場合、`installer_files`フォルダを削除してから`start.bat`を再実行することで問題が解決します（クリーン再インストールは数分で完了し、`model/`にダウンロード済みのAIモデルは保持されます）。エラーはWebUIに、閉じるまで表示され続ける赤いトーストとして表示されます。



## 📰 ニュースと履歴

<details open>
<summary>version 4.0</summary>

- ⚡ **インストーラーをMiniconda/pipから[uv](https://docs.astral.sh/uv/)に移行** — コミット済みの`uv.lock`から、劇的に高速で完全に再現可能なインストールを実現。すべて（uv、Python、パッケージ）は`installer_files/`内に収まります。
- 🐍 ランタイムをアップグレード: **Python 3.12、Torch 2.8.0+cu128（RTX 50シリーズ対応）、Gradio 6.20**。
- 🎙️ 最新のASRスタック: **faster-whisper 1.2.1**（large-v3-turbo、distil-large-v3.5）、openai-whisper 20250625、whisper-timestamped 1.15.9。whisperXは削除されました（その依存関係のピン留めがGradio 6へのアップグレードを妨げていたため。既存の設定はfaster-whisperにフォールバックします）。
- 🗣️ 最新のTTSスタック: **F5-TTS 1.1.21**、kokoro 0.9.4、edge-tts 7.x、および再ベンダリングされた**CosyVoice**（アップストリームmain）。
- 🇰🇷 新しいオプションのTTSモデル: **Fun-CosyVoice3-0.5B** — 韓国語を含む9言語に対応。CosyVoiceタブで選択可能（初回使用時に公式HFリポジトリからダウンロード）。
- 🧹 CUDA ToolkitとVisual Studio Build Toolsは**不要になりました** — すべての依存関係はビルド済みwheelで提供され、PyTorchにはCUDAランタイムが同梱されています。
- 🛡️ **制限のある企業PC**にも優しい設計: 管理者権限は不要 — ffmpegがインストールされていない場合は`start.bat`がポータブル版**ffmpeg**を自動ダウンロードし、Whisperモデルのダウンロードは転送の中断・破損後に自己修復し、無料のGoogleエンドポイントがネットワークでレート制限された場合は翻訳が自動的にバックオフ付きでリトライします（失敗した行は報告され、原文が保持されます）。
- 🚨 **エラーがWebUIに表示されるようになりました**: すべての失敗は、閉じるまで画面に残る赤いエラートーストとして表示され（以前は見逃しやすい10秒間の警告でした）、よくある原因（ffmpegの欠落、メディア未登録など）については対処方法が分かるメッセージが表示されます。
- 🖥️ UI: **Gradio 6**に移行（全タブがフル幅レイアウト、字幕トラックをビデオプレーヤー内に直接表示）。
- 🧽 `uninstall.bat`は管理者権限が不要になり、強制再起動もしなくなりました。`uninstall.bat silent`で無人実行が可能です。

</details>

<details>
<summary>version 3.2</summary>

- 私たちは過去数ヶ月間、[WeConnect](https://www.wctokyoseoul.com)の開発に集中していたため、Voice-Proを全く管理できませんでした。 
- すべてのVoice-Proコードをオープンソース化することを決定しました。
- Voice-Proは完全無料で、Windows、Mac、Linuxをサポートしています。
- [WeConnect](https://www.wctokyoseoul.com)はグローバルな文化交流のためのアプリケーションです。
- 世界中の人々とつながり、意味のある文化交流、言語学習、国際的な友情を築くことができます。

<p align="center">
    <img src="images/Hotpot 0.png?raw=true" alt="ScreenShot 0" width="18%"/>
    <img src="images/Hotpot 1.png?raw=true" alt="ScreenShot 1" width="18%"/>
    <img src="images/Hotpot 2.png?raw=true" alt="ScreenShot 2" width="18%"/>
    <img src="images/Hotpot 3.png?raw=true" alt="ScreenShot 3" width="18%"/>
    <img src="images/Hotpot 4.png?raw=true" alt="ScreenShot 4" width="18%"/>
</p>

</details>

<details>
<summary>version 3.1</summary>

- 🪄 **F5-TTS** のファインチューニングされたモデルのサポート
- 🌍 対応言語
  - <img src="https://flagcdn.com/16x12/us.png" alt="United Kingdom Flag" style="vertical-align: middle;"> English & <img src="https://flagcdn.com/16x12/cn.png" alt="China Flag" style="vertical-align: middle;"> Chinese: <a href="https://huggingface.co/SWivid/F5-TTS/tree/main/F5TTS_v1_Base"> SWivid/F5-TTS_v1 </a> 
  - <img src="https://flagcdn.com/16x12/fi.png" alt="Spain Flag" style="vertical-align: middle;"> Finnish: <a href="https://huggingface.co/AsmoKoskinen/F5-TTS_Finnish_Model"> AsmoKoskinen/F5-TTS_Finnish_Model </a> 
  - <img src="https://flagcdn.com/16x12/fr.png" alt="Spain Flag" style="vertical-align: middle;"> French: <a href="https://huggingface.co/RASPIAUDIO/F5-French-MixedSpeakers-reduced"> RASPIAUDIO/F5-French-MixedSpeakers-reduced </a> 
  - <img src="https://flagcdn.com/16x12/in.png" alt="Spain Flag" style="vertical-align: middle;"> Hindi: <a href="https://huggingface.co/SPRINGLab/F5-Hindi-24KHz"> SPRINGLab/F5-Hindi-24KHz </a>  
  - <img src="https://flagcdn.com/16x12/it.png" alt="Spain Flag" style="vertical-align: middle;"> Italian: <a href="https://huggingface.co/alien79/F5-TTS-italian"> alien79/F5-TTS-italian </a>  
  - <img src="https://flagcdn.com/16x12/jp.png" alt="Spain Flag" style="vertical-align: middle;"> Japanese: <a href="https://huggingface.co/Jmica/F5TTS/tree/main/JA_21999120"> Jmica/F5TTS/JA_21999120 </a>  
  - <img src="https://flagcdn.com/16x12/ru.png" alt="Spain Flag" style="vertical-align: middle;"> Russian: <a href="https://huggingface.co/hotstone228/F5-TTS-Russian"> hotstone228/F5-TTS-Russian </a> 
  - <img src="https://flagcdn.com/16x12/es.png" alt="Spain Flag" style="vertical-align: middle;"> Spanish: <a href="https://huggingface.co/jpgallegoar/F5-Spanish"> jpgallegoar/F5-Spanish </a> 
  
</details>

<details>
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

## ⭐ 主な機能

### 1. ダビングスタジオ
- YouTube動画のダウンロードとオーディオ抽出
- **Demucs**による音声分離
- 音声認識と翻訳のための100以上の言語に対応

### 2. 音声技術
- **音声からテキストへ:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
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
- **OS:** Windows 10/11（64ビット）、Linux、Mac（Apple Silicon）
- **GPU:** 最新のドライバー（570以上推奨。RTX 50シリーズ対応）を備えたNVIDIA GPU。CUDA Toolkitのインストールは不要です。
- **VRAM:** 4GB以上（8GB以上推奨）
- **RAM:** 4GB以上
- **ストレージ:** 20GB以上の空き容量
- **インターネット:** 必須

## 📀 インストール

**configure.bat**と**start.bat**でVoice-Proを簡単にインストールできます（Mac/Linuxではconfigure.shとstart.shを使用）。

### 1. パッケージ準備
- [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)から最新リリースをダウンロード（**Source code (zip)**）
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. インストールと実行
1. 🚀 **configure.bat**（オプション）
   - gitとffmpegをシステム全体にセットアップ（CUDA Toolkit / Visual Studioは不要になりました）
   - 管理者権限が必要。初回のみ実行
   - 管理者権限がない場合はスキップ可能 — **start.bat**がポータブル版ffmpegを自動ダウンロードします
2. 🚀 **start.bat**
   - Voice-ProウェブUIを起動
   - 初回実行時にuvとPython 3.12をダウンロードし、ロックファイルからすべての依存関係をインストールした後（数時間ではなく数分）、AIモデル（約10GB — ここが時間のかかる部分）をダウンロード
   - GPU/CPUは自動検出。`GPU_CHOICE`環境変数（`G`=NVIDIA、`C`=CPU）または`installer_files\gpu_choice.txt`の削除で上書き可能
   - 問題発生時は**installer_files**を削除後に再実行

### 3. アップデート
- 🚀 **update.bat**: Python環境をコミット済みのロックファイルへ正確に再同期します（高速）

### 4. アンインストール
- **uninstall.bat**実行、またはフォルダ削除（ポータブルインストール）
- 管理者権限は不要。無人削除には`silent`を追加（`uninstall.bat silent`）
- 削除されるのは`installer_files`フォルダのみ — `model/`と`workspace/`フォルダは保持されます


## 🔑 Azureサービス（オプション、.env）

デフォルトでは、Voice-Proは**無料**のサービスを使用します。翻訳にはDeep-Translator（Googleの無料ウェブエンドポイント）、音声合成にはEdge-TTSです。独自の**Microsoft Azure**サブスクリプションをお持ちの場合は、両方をAzure APIに切り替えることができます。

1. プロジェクトルートで`.env.example`を`.env`にコピーします:
   ```bash
   copy .env.example .env     # Windows
   cp .env.example .env       # Mac/Linux
   ```
2. Azureの資格情報を入力します:
   ```ini
   # Azure Speech Service (TTS)
   AZURE_SPEECH_KEY=your_azure_speech_key_here
   AZURE_SPEECH_REGION=eastus

   # Azure Translator Service
   AZURE_TRANSLATOR_KEY=your_azure_translator_key_here
   AZURE_TRANSLATOR_ENDPOINT=https://your-translator-resource.cognitiveservices.azure.com/
   AZURE_TRANSLATOR_REGION=eastus
   ```
3. Voice-Proを再起動します。有効なキーは起動時に自動的に検出され、翻訳は**Azure Translator**に切り替わり、音声生成の最初のタブが**Azure-TTS**になります。

**どのような場合に設定する価値がありますか？**
- 🏢 **企業/制限のあるネットワーク**: セキュリティアプライアンスが無料の`translate.google.com`エンドポイントをレート制限またはブロックすることが多く、長い字幕翻訳が遅くなったり失敗したりします。Voice-Proはバックオフ付きでリトライし、失敗した行は原文を保持します（失敗数を示す警告が表示されます）が、Azure Translatorを使えばこの問題を完全に回避できます。
- 🗣️ より高品質で一貫性のあるTTS音声と、より高いレート制限。
- `.env`をバージョン管理にコミット**しないでください** — あなたの秘密キーが含まれています。


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
- [WeConnect](https://www.wctokyoseoul.com)の開発作業により、当分の間Voice-Proのアップデートはありません。
- すべてのVoice-Proコードを公開しました。完全無料で使用できます。
- [WeConnect](https://www.wctokyoseoul.com)は、グローバルな文化交流のためのコミュニケーションプラットフォームです。





<br />

## ⏳ 字幕作成、翻訳、TTSのためのSaaSプラットフォーム

以下の表は、字幕作成、翻訳、テキスト音声変換（TTS/ダビング）機能をサポートするSaaSプラットフォームをまとめたものです。コストは2025年4月15日時点の最新価格データに基づき、60分の韓国語ビデオを字幕生成、英語翻訳、英語ダビング処理することを含めて計算されています。

| プラットフォーム | 字幕作成 | 翻訳 | TTS/ダビング | 60分ビデオ処理コスト (USD, 約) | 主な特徴 |
| --- | --- | --- | --- | --- | --- |
| **[Maestra](https://maestra.ai)** | ✅ | ✅ | ✅ | $23.70 | 125以上の言語、リアルタイム字幕、SEOキーワード抽出、15分無料トライアル。 |
| **[Kapwing](https://www.kapwing.com)** | ✅ | ✅ | ✅ | $30\~$40 (Proプラン、分単位) | AI字幕、100以上の言語翻訳、自動リップシンクダビング、無料ティア提供。 |
| **[VEED.IO](https://www.veed.io)** | ✅ | ✅ | ❌ | $24\~$36 (Proプラン、部分処理) | 99.9%正確な字幕、Instagram最適化字幕、直感的なエディター。 |
| **[HappyScribe](https://happyscribe.com)** | ✅ | ✅ | ✅ | $36\~$48 (従量制) | 120以上の言語、プロの校正オプション、セキュア、会議文字起こし。 |
| **[Sonix](https://sonix.ai)** | ✅ | ✅ | ✅ | $30\~$40 (Standardプラン) | 54以上の言語、30分無料文字起こし、YouTube/Zoom統合。 |
| **[Descript](https://descript.com)** | ✅ | ✅ | ✅ | $36\~$48 (Creatorプラン) | テキストベース編集、Overdub TTS、フィラー単語除去、1時間無料文字起こし。 |
| **[AppTek](https://apptek.ai)** | ✅ | ✅ | ✅ | カスタム価格 (要問い合わせ) | メディア特化、カスタムモデル、メタデータ生成、クラウドベースWorkbench。 |
| **[Transkriptor](https://transkriptor.com)** | ✅ | ✅ | ❌ | $12\~$18 (従量制) | 100以上の言語、YouTubeリンク文字起こし、99%正確度、シンプルなエディター。 |

### コスト計算詳細

- **[Maestra](https://maestra.ai)**: Premiumプラン ($158/月、1200クレジット)。60分ビデオ：字幕60クレジット + 翻訳60クレジット + ダビング60クレジット = 180クレジット。コスト = (180/1200) \* $158 = $23.70。
- **[Kapwing](https://www.kapwing.com)**: Proプラン (\~$24/月、制限付き分数)。字幕+翻訳+ダビングで分あたり$0.50\~$0.67と推定 (分単位価格トレンドに基づく)。60分コスト：$30\~$40。正確な価格は要確認。
- **[VEED.IO](https://www.veed.io)**: Proプラン (\~$24/月)。字幕+翻訳で分あたり$0.40\~$0.60と推定。TTSなし、部分処理。60分コスト：$24\~$36。veed.ioで確認。
- **[HappyScribe](https://happyscribe.com)**: 従量制 (文字起こし分あたり\~$0.20、翻訳$0.20、ダビング$0.20)。60分コスト：$36\~$48 (結合サービスを仮定)。happyscribe.comで確認。
- **[Sonix](https://sonix.ai)**: Standardプラン (文字起こし時間あたり\~$10、翻訳/ダビング追加)。合計分あたり$0.50\~$0.67と推定。60分コスト：$30\~$40。sonix.aiで確認。
- **[Descript](https://descript.com)**: Creatorプラン (\~$24/月、制限付き時間)。字幕+翻訳+ダビングで分あたり$0.60\~$0.80と推定。60分コスト：$36\~$48。descript.comで確認。
- **[AppTek](https://apptek.ai)**: 企業向けカスタム価格。公開分単位料金なし。apptek.aiに問い合わせ。
- **[Transkriptor](https://transkriptor.com)**: 従量制 (文字起こし分あたり$0.05\~$0.10、翻訳同等)。TTSなし、部分処理。60分コスト：$12\~$18。transkriptor.comで確認。

### 注記

- **60分ビデオ処理コスト**: コストは60分の韓国語ビデオの字幕、英語翻訳、英語ダビング（可能な場合）を処理することを前提とした近似値です。TTS非対応プラットフォーム（例：VEED.IO、Transkriptor）は部分処理コストを反映。
- **言語サポート**: ほとんどのプラットフォームは韓国語と英語をサポート。特定言語の対応状況は各ウェブサイトで確認。
- **ユースケース**:
  - メディア/エンターテインメント: AppTek, Maestra
  - ソーシャルメディア: Kapwing, VEED.IO
  - ポッドキャスト/インタビュー: Sonix, Descript
  - Eラーニング/グローバルコンテンツ: Transkriptor, HappyScribe
- **価格更新**: プラン変更やプロモーションにより価格が変動する場合があります。最新情報は公式ウェブサイトで確認。
- 貢献や特定ユースケースの提案のために、このリポジトリでイシューを開くか、プルリクエストを提出してください！


<br />

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
- Homepage (Korean): <https://www.wctokyoseoul.com>



## 🙏 クレジット
* Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>
* edge-TTS: <https://github.com/rany2/edge-tts>
* F5-TTS: <https://github.com/SWivid/F5-TTS.git>
* openai-whisper: <https://github.com/openai/whisper>
* faster-whisper: <https://github.com/SYSTRAN/faster-whisper>
* whisper-timestamped: <https://github.com/linto-ai/whisper-timestamped>
* CosyVoice: <https://github.com/FunAudioLLM/CosyVoice>
* kokoro: <https://github.com/hexgrad/kokoro>
* Deep-Translator: <https://github.com/nidhaloff/deep-translator>
* spaCy: <https://github.com/explosion/spaCy>

## ©️ 著作権情報
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://www.wctokyoseoul.com)