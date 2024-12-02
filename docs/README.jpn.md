# Voice-Pro: The best gradio web-ui for transcription, translation and text-to-speech 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/voice-pro)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases )



**Voice-Proは、文字起こし、翻訳、テキスト読み上げのための最高のgradio WebUIです。** ワンクリックで簡単にインストールできます。Minicondaを使用して仮想環境を作成し、Windowsシステムとは完全に分離して実行します（完全にポータブル）。リアルタイムの文字起こしと翻訳、およびバッチモードをサポートしています。

- **YouTubeダウンローダー**: YouTubeの動画をダウンロードし、音声を抽出できます（mp3、wav、flac）。
- **ボーカルリムーバー**: UVR5でサポートされているMDX-NetとMetaが開発したDemucsエンジンを使用して音声分離を行います。
- **STT**: Whisper、Faster-Whisper、whisper-timestampedを使用して音声からテキストへの変換をサポートします。
- **翻訳**: Google翻訳を使用します。短文翻訳、字幕ファイル翻訳。
- **TTS**: テキスト読み上げ。Edge-TTS。ゼロショット音声クローンをサポートするE2とF5-TTS。
- Celebボイスを無料で提供しています。自分のポッドキャストを作成してみましょう。F5-TTSタブで確認できます。

### 🚄 実行画面

* `TTS` タブ : F5-TTSを利用したポッドキャスト制作
<video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls="controls" muted="muted"></video>

* `Studio`タブ : 文字起こし、翻訳、音声合成
<video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c" width="100%" style="max-width: 720px;" controls="controls" muted="muted"></video>

* `Live Translation` tab : リアルタイム音声認識と翻訳
<video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls="controls" muted="muted"></video>



## ⭐ 主な機能

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
  <img style="width: 90%; height: 90%" src="images/main_page.jpn.png?raw=true" alt=""/>
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
  <img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt=""/>
</p>  


* `Live Translation`タブ
  - リアルタイム音声認識＆翻訳サポート
  - Mic、Speakerなどのオーディオ入力ソースを選択可能
  - キャプチャされたオーディオ、認識された字幕、翻訳された字幕保存機能を提供

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
