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



## 🎙️ 高度なAI搭載マルチメディア処理ツール | Whisper音声認識WebUI

Voice-Proは、マルチメディアコンテンツ処理を革新するために設計された最先端のAIベースのウェブアプリケーションです。YouTubeビデオのダウンロード、音声分離、音声認識、翻訳、テキスト読み上げなどの包括的な機能を提供し、コンテンツ作成者、研究者、多言語コミュニケーションの専門家のためのオールインワンソリューションを提供します。

- 🔊 最先端の音声認識（Whisper、Faster-Whisper、Whisper-Timestamped）
- 🎤 F5-TTSおよびE2-TTSによるゼロショット音声クローニング
- 🎥 YouTubeビデオ処理と音声抽出
- 🔇 プロフェッショナルな音声分離（UVR5技術）
- 📢 多言語テキスト読み上げ（Edge-TTS）
- 🌍 100以上の言語での即時翻訳

コンテンツ作成者、ポッドキャスター、研究者、開発者に最適 | AIマルチメディアソリューション



## 🚄 実行画面

* `Studio`タブ : 文字起こし、翻訳、音声合成
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description">
   </video>
  <p id="studio-demo-description">
Voice-Proのスタジオタブによる包括的なメディア処理ワークフローのデモ：YouTubeビデオのダウンロードからAIベースの音声分離、Whisper自動字幕生成、多言語翻訳、F5-TTSを使用したプロフェッショナルな吹き替えまでの、ワンストップメディア変換プロセスを実演します。
  </p>
</div>

* `TTS` タブ : F5-TTSを利用したポッドキャスト制作
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted" 
   aria-describedby="tts-demo-description">
   </video>
  <p id="tts-demo-description">
F5-TTSの革新的なAIボイスクローニング技術のデモンストレーション：Mark ZuckerbergとElon Muskの実際の声を正確に模倣し、全く新しいコンテンツを生成する先進的な音声変換技術を紹介します。
  </p>
</div>

* `Live Translation` tab : リアルタイム音声認識と翻訳
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1"
  width="100%" 
  style="max-width: 720px;" 
  controls="controls" 
  muted="muted"
  aria-describedby="translate-demo-description">
  </video>
  <p id="translate-demo-description">
Voice-Proのリアルタイム多言語翻訳機能のデモ：YouTubeのBBCニュースコンテンツをAIベースの音声認識技術で即座にキャプチャし、リアルタイムで字幕を生成し、他の言語にすぐに翻訳する革新的な多言語メディア処理プロセスを実演します。
  </p>
</div> 


## ⭐ 主な機能と特徴

### 1. 包括的なスタジオタブ
- **YouTubeビデオ処理**: 複数の形式で音声をダウンロードおよび抽出
- **音声分離**: MDX-NetおよびDemucsを使用した高度なノイズ除去
- **多言語サポート**: 
  - 100以上の言語に対する音声認識
  - カスタマイズ可能な字幕生成
  - 100以上の言語に対する翻訳機能

### 2. 高度な音声技術
- **音声-テキスト (STT)**: 
  - Whisper統合
  - Faster-Whisper サポート
  - Whisper-timestamped 機能
- **テキスト-音声 (TTS)**: 
  - 400以上の音声に対応するEdge-TTS
  - ゼロショット音声クローニングが可能なF5-TTS
  - セレブリティ音声生成

### 3. リアルタイム翻訳
- 即時音声認識
- 多言語翻訳
- 設定可能な音声入力ソース


## ⭐ WebUI

* `Studio`タブ
  - YouTubeダウンローダ、ノイズ除去、字幕、翻訳、TTS統合環境で提供
  - ffmpegがサポートするすべてのビデオ/オーディオフォーマットが利用可能
  - 出力オーディオフォーマット（wav、flac、mp3）選択可能
  - 100言語の音声認識、字幕生成
  - PC性能に合わせた字幕生成オプションを選択可能(Whisper Model & Compute Type)
  - 100以上の言語への翻訳とTTSによる音声生成
  - オリジナル映像のBGMと効果音を多言語映像でもそのまま維持
  - TTS音声の速度、音量、ピッチ調整をサポート
  
<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt="多言語音声変換および字幕生成ウェブUIインターフェース"/>
</p>  


* `Whisper字幕`タブ
  - 字幕作成専用タブ。 90以上の言語をサポート
  - 映像とともに生成された字幕表示
  - World-Level Highlight機能を提供
  - Denoise機能を提供(1-Demucs、2-MDXNet)

* `翻訳`タブ
  - 翻訳専用タブ。 100以上の言語をサポート
  - 字幕ファイル（ass、ssa、srt、mpl2、tmp、vtt、microdvd、json）をサポート
  - テキスト直接入力も可能
  - アップロードしたファイルの言語を自動的に検出

* `TTS`タブ
  - Edge-TTS と F5-TTS がサポートされています。
  - Edge-TTS は100以上の言語と400以上の声をサポートしています。
  - ピッチ、ボリューム、スピードを調整できます。
  - F5-TTS はゼロショットボイスクローンをサポートしています。
  - Celeb Voice を使ってポッドキャストを制作できます。

<p align="center">
  <img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="ボイスクローニング技術を活用したポッドキャスト制作WebUI"/>
</p>  


* `Live Translation`タブ
  - リアルタイム音声認識＆翻訳サポート
  - Mic、Speakerなどのオーディオ入力ソースを選択可能
  - キャプチャされたオーディオ、認識された字幕、翻訳された字幕保存機能を提供

<p align="center">
  <img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="リアルタイム音声認識と翻訳のためのWebUI"/>
</p>  


* `Batch`タブ
  - 大量のファイルのバッチ処理
  - 字幕、翻訳、TTS


## 💻 実行環境
* OS: Windows 10/11（64ビット）**※ LinuxとMac OSはサポートされていません。**
* GPU: CUDA 12.1をサポートする**NVIDIA**グラフィックカードを推奨。
* VRAM: 4GB以上。8GB以上を推奨。
* RAM: 4GB以上
* HDD: インストール時に少なくとも20GBの空き容量が必要
* インターネット接続が必要（インストールと翻訳作業）


## 📀 インストール

Voice-Proはワンクリックで簡単にインストールできます。🚀**configure.bat**と🚀**start.bat**を実行するだけです。

### ステップ1. パッケージの準備
  + [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)から最新リリース（**Source code (zip)**）をクローンまたはダウンロードします。
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### ステップ2. プログラムのインストールと実行
1. 🚀 `configure.bat`を実行
   - Windows上にgit、ffmpeg、CUDA（NVIDIAのGPUを使用する場合）をインストールします。
   - 初回のみ実行する必要があります。
   - インターネット接続が必要で、システムによっては1時間以上かかる場合があります。
   - インストール中はWindows-Commandウィンドウを絶対に閉じないでください。
2. 🚀 `start.bat`を実行
   - Voice-Proを起動します。Web-UIが自動的に実行されます。
   - 初回実行時は、まずVoice-Proがインストールされます。
   - インターネット接続が必要で、システムによっては1時間以上かかる場合があります。
   - インストール中はWindows-Commandウィンドウを絶対に閉じないでください。
   - インストール中に問題が発生した場合は、**installer_files**フォルダを削除し、start.batを再度実行してください。

### ステップ3. プログラムのアンインストール
* `uninstall.bat`を実行:
  - **installer_files**フォルダを削除します。
  - Windows上にインストールされたffmpeg、git、CUDAパッケージを削除します（選択した場合）。
* Voice-Proは標準で**ポータブル**インストールです。プログラムをアンインストールするには、インストールフォルダを削除するだけで十分です。


## ❓ヒントとコツ

#### ブラウザが自動的に起動しない場合
- Windows-Commandウィンドウを閉じて、start.batを再度実行してください。
- ブラウザを直接起動し、Windows-Commandウィンドウに表示されているアドレス（例：**http://127.0.0.1:7892**）をアドレスバーに入力してください。

#### CUDA Out-Of-Memoryエラーが発生した場合
- WindowsタスクマネージャーのパフォーマンスタブでGPUメモリの状態を確認してください。
- ノイズ除去レベルを0または1に設定してください。ノイズ除去レベル2には少なくとも8GBのGPUメモリが必要です。
- Compute Typeをintタイプに設定してください。floatタイプは品質が良いですが、より多くのGPUメモリを必要とします。

#### 字幕の品質を向上させるには？
- 字幕の品質は、より大きなWhisperモデルで向上する傾向がありますが、必ずしもそうではありません。large > medium > small > base > tiny
- Compute Typeの中では、floatタイプのパフォーマンスが良いです。intタイプはモデル量子化によってGPU使用量を減らし、速度を上げるモデルです。一方で、パフォーマンスは低下します。
- ノイズ除去レベルを上げると、より多くのバックグラウンドサウンドが除去され、残った音声のみが音声認識に使用されます。必ずしも良い結果を保証するものではありません。

## 📢 注意

Windows Defenderは信頼できないアプリケーションに関する警告を表示し、Voice-Proのさらなる実行を許可しない場合があります。
SmartScreenのセキュリティレベルが「警告」に設定されている場合は、「詳細情報」をクリックし、その後「続行」をクリックしてください。
SmartScreenが「ブロック」に設定されている場合、インストールを実行するボタンは表示されません。この場合、start.batファイルのプロパティを開き、「ブロック解除」をチェックし、変更を適用してからstart.batを再度実行してください。

<p align="center">
  <img style="width: 60%; height: 60%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  

Windows Defenderがバッチファイルを誤ってトロイの木馬と認識した場合、これは「誤検出」と呼ばれることがよくあります。この問題を解決するには、以下の手順を行うことができます：

1. ファイルの例外処理：Windows Defenderで、特定のファイルやプロセスをセキュリティスキャンの対象から除外するように設定できます。そのためには、以下の手順に従ってください：
   * 「スタート」ボタンをクリックし、「設定」に進みます。
   * 「更新とセキュリティ」をクリックします。
   * 「Windowsセキュリティ」を選択し、「ウイルスと脅威の防止」に進みます。
   * 「ウイルスと脅威の防止の設定を管理する」をクリックします。
   * 「ウイルスと脅威の防止の設定」で「除外を追加または削除」を選択します。
   * 「ファイルまたはフォルダー」を選択し、問題のバッチファイルを見つけて例外として追加します。
2. Windows Defenderを一時的に無効にする：これは一時的な解決策かもしれません。ただし、この方法を使用する場合は、コンピューターが他の脅威にさらされる可能性があるため、注意が必要です。
3. 問題をアンチウイルスソフトウェアに報告する：ファイルがトロイの木馬でないことが確実な場合、誤検出としてMicrosoftに報告することができます。Microsoftはこれをレビューし、必要な対応を取ります。


## ☕ 通知
- このリポジトリは、Voice-Proの**無料トライアル**を提供しています。 
- 無料トライアルには**使用制限が30分**あります。これは、実行後30分経過すると、Web UIを使用できなくなることを意味します。 
- これは、処理できるメディアの長さに制限があることを意味するものではなく、進行中のタスクを停止するものでもありません。アクションボタンをクリックできなくなるだけです。 
- 少し不便かもしれませんが、再度使用するには、プログラムを閉じて再起動するだけです。 
- 以前の作業結果はワークスペースフォルダに保持されます。 
- Voice-Proの公式バージョンは、ABUS公式ウェブサイト(<https://abuskorea.imweb.me>)で購入できます。
- また、Buy Me a Coffee ☕を通じてサポートしていただければ、感謝の意を込めて、最大1か月分の使用バウチャーを提供いたします。 (<https://github.com/abus-aikorea/voice-pro/discussions/10#discussioncomment-11527327>)
- 購入、ビジネスパートナーシップ、調整、投資などに関する問い合わせは、メール(<abus.aikorea@gmail.com>)にてお願いいたします。



## 📬 お問い合わせ
* メール: <abus.aikorea@gmail.com>
* ホームページ(韓国語): <https://abuskorea.imweb.me>
* Amazon(アメリカ): <https://www.amazon.com/dp/B0DBR69JPL>
* Amazon(日本): <https://www.amazon.co.jp/dp/B0DBVRJ542>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKL8R4>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGKM7FF>
* 네이버 스마트스토어 (S/W): <https://smartstore.naver.com/abus/products/10385660040>
* 네이버 스마트스토어 (솔루션): <https://smartstore.naver.com/abus/products/10298346364>


## 👍 YouTube
* 商品説明: <https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq>
* ホームカラオケ (Pop): <https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6>
* ホームカラオケ (K-Pop): <https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8>
* ホームカラオケ (J-Pop): <https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq>
  

## 🙏 Credits
* Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>
* edge-TTS: <https://github.com/rany2/edge-tts>
* F5-TTS: <https://github.com/SWivid/F5-TTS.git>
* openai-whisper: <https://github.com/openai/whisper>
* faster-whisper: <https://github.com/SYSTRAN/faster-whisper>
* whisper-timestamped: <https://github.com/linto-ai/whisper-timestamped>


## ©️ 著作権
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)
