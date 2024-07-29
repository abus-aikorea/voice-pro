# Voice-Gulliver

🌍 [韓国語](README.kor.md) ∙ [English](README.eng.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/voice-gulliver)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-gulliver)](https://github.com/abus-aikorea/voice-gulliver/releases )

The best gradio web-ui for asr, translation and tts. Easy one click installation. Fully portable.


## はじめに
* ボイスガリバーは**字幕、翻訳、ダビング**統合ソリューションです。 
* ボイスガリバーで映像に多言語字幕を追加してみてください。グローバル進出安心！
* 朝毎にワールドニュースを視聴していますか？では、ライブ翻訳機能をご利用ください。 YouTubeで見たまさに、リアルタイム翻訳をサポートします。
* ボイスガリバーは、UVR5が提供する**ボーカルリムーバー**とMetaの**Demucs**エンジンを搭載しています。 
* ボイスガリバーは**OpenAI Whisper**と**Microsoft Azure AI**を使用します。      
* ボイスガリバーは**ワンクリック**で簡単にインストールでき、Gradio Web-UIを提供します。 
* 最高レベルの**On-Device AI Voice**技術を体験してください。


## 主な機能

* `VOD`タブ
  - YouTubeダウンローダ、ノイズ除去、字幕、翻訳、ダビング統合環境で提供
  - ffmpegがサポートするすべてのビデオ/オーディオフォーマットが利用可能
  - 出力オーディオフォーマット（wav、flac、mp3）選択可能
  - 100言語の音声認識、字幕生成
  - PC性能に合わせた字幕生成オプションを選択可能(Whisper Model & Compute Type)
  - オリジナル映像のBGMと効果音をダビング映像でもそのまま維持
  - ダビング音声の速度、音量、ピッチ調整をサポート  
  
<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt=""/>
</p>  


* `Live`タブ
  - リアルタイム音声認識＆翻訳サポート
  - Mic、Speakerなどのオーディオ入力ソースを選択可能
  - キャプチャされたオーディオ、認識された字幕、翻訳された字幕保存機能を提供

* `Batch`タブ
  - 大量のファイルをバッチ処理

* `Garage`タブ
  - 字幕ファイルをアップロードし、翻訳して吹き替えることができます。
  - AIによって自動生成された字幕を校正する必要がある場合に便利です。
  - サポートされている字幕形式: '.ass'、'.ssa'、'.srt'、'.mpl2'、'.tmp'、'.vtt'、'.microdvd'、'.json'


## 特徴
* YouTube動画（mp4、webm）をダウンロードし、オーディオファイル（mp3、wav、flac）として保存できます。
* ノイズ除去＆ボーカル分離により、音声認識の精度を高めることができます。 **MDX-Net**とMetaの**Demucs**を利用します。
* **ワンクリックインストール**。一度インストールすると、追加料金なしで**永続**として使用できます。 （※Freeバージョンは利用時間**30分制限**あり）
* **Web-UI**を提供します。 Google Chromeブラウザをお勧めします。


## 実行環境
* OS：Windows 10/11（64bits）**※Linux、Mac OSはサポートしていません。**
* CPU：Intelプロセッサ2GHz以上（または同等の互換性）
* RAM：4GB以上
* HDD：インストール中に少なくとも20 GBの空き容量
* GPU: CUDA 12.1をサポートする**NVIDIA**グラフィックカードを推奨。 VRAM 4GB以上。 8GB以上を推奨。
* インターネット接続が必要（インストールおよび翻訳作業）


## インストールと実行

### step 1. パッケージの準備
* A.有料バージョン
    + USBに含まれる圧縮ファイル（**voice-gulliver-x.zip**）をコンピュータの適切な場所に解凍する
    + またはすでに解凍されているフォルダ（**voice-gulliver-x**）をコンピュータの適切な場所にコピーする

* B. 無料版
  + [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-gulliver)](https://github.com/abus-aikorea/voice-gulliver/ releases) から最新リリース (**Source code (zip)**) ダウンロード後に解凍 
  + または、git cloneでソースコードをダウンロードする
    
``` bash
git clone https://github.com/abus-aikorea/voice-gulliver.git
```

### step 2. プログラムのインストールと実行
1. `configure.bat`の実行
   - WindowsにffmpegとCUDA（NVIDIA GPUを使用している場合）をインストールします。
   - 最初の1回だけ実行するだけです。
2. `start.bat`の実行
   - Voice-Gulliverを起動します。 Web-UIが自動的に起動します。
   - 最初の実行時には、Voice-Gulliverのインストール作業を先に進めます。
   - Voice-Gulliverインストールはインターネット接続を必要とし、システムによってはインストールに1時間以上かかることがあります。
   - インストール中は絶対にWindowsコマンドウィンドウを終了しないでください。
   - インストール中に問題が発生した場合は、installer_filesフォルダを削除してstart.batを再実行してください。



### 実行画面

https://github.com/abus-aikorea/voice-gulliver/assets/161691694/bb7dd2f2-9863-49e3-bd3e-59b0b8315fca



### step 3. プログラムの削除
* `uninstall.bat`実行：
  - installer_filesフォルダを削除します。
  - Windowsにインストールしたffmepg、CUDAパッケージを削除します（選択した場合）

* Voice-Gulliverは**ポータブル**インストールがデフォルトです。プログラムの削除は、インストールフォルダを削除するだけで十分です。


## ヒントとコツ

#### Browserが自動的に実行されない場合
- Windows-Commnadウィンドウを終了し、start.batを再実行するか、
- ブラウザを直接実行し、Windowsコマンドウィンドウに表示されているアドレス（例：**http://127.0.0.1:7892**）をアドレスウィンドウに入力します。

#### CUDA Out-Of-Memoryエラーが発生した場合
- Windowsタスクマネージャ - [パフォーマンス]タブでGPUメモリの状態を確認します。 
- Denoiseレベルを0または1に設定します。 Denoiseレベル2は8GB以上のGPUメモリを必要とします。
- Compute Type を int 型に設定します。 floatタイプの品質は良いですが、より多くのGPUメモリが必要です。

#### 字幕の品質を向上させるには？
- 字幕の品質は、より大きなWhisperモデルを使用するほど良くなる傾向がありますが、必ずしもそうではありません。 large > medium > small > base > tiny 
- Compute Typeの中では、floatタイプのパフォーマンスが良いです。 int型はモデル量子化によりGPU使用量を下げ、スピードを高めたモデルです。一方、パフォーマンスは低下します。 
- Denoiseレベルを上げると背景音をより多く除去し、残っているボイスだけ音声認識に使用するようになります。常に良い結果を保証するわけではありません。




## 注意事項
Windows Defenderが誤ってバッチファイルをトロイの木馬として認識している場合、これはしばしば「False Positive」と呼ばれます。この問題を解決するには、次の手順を実行できます。

1. ファイル例外処理：Windows Defenderでは、特定のファイルまたはプロセスがセキュリティチェックをスキップするように設定できます。これを行うには、以下の手順に従ってください

   * 「スタート」ボタンをクリックして「設定」に進みます。
   * [アップデートとセキュリティ]をクリックしてください。
   * 「Windowsセキュリティ」を選択し、「ウイルスと脅威の保護」に進みます。
   * [ウイルスと脅威の保護設定の管理]をクリックしてください。
   * 「ウイルスと脅威の保護設定」で「例外を追加」を選択してください。
   * 「ファイルまたはフォルダ」を選択し、問題のバッチファイルを見つけて例外として追加します。
2.  Windows Defender をしばらく無効にする: この方法は一時的な解決策になります。ただし、この方法を使用すると、コンピュータが他の脅威にさらされる可能性があるため、注意が必要です。

3. ワクチンソフトウェアに問題を提起: ファイルがトロイの木馬ではないという確信があれば、マイクロソフトに False Positive として情報を提供できます。マイクロソフトはこれを確認した後、必要な措置を講じます。


## 製品お問い合わせ
* メール: <abus.aikorea@gmail.com>
* ホームページ(韓国語): <https://abuskorea.imweb.me>
* 네이버 스마트스토어 (S/W): <https://smartstore.naver.com/abus/products/10385660040>
* 네이버 스마트스토어 (솔루션): <https://smartstore.naver.com/abus/products/10298346364>
* Amazon(アメリカ): <https://www.amazon.com/dp/B0D5H8Z4FL>
* Amazon(日本): <https://www.amazon.co.jp/dp/B0CTHT2JH3>


## YouTube
* 商品説明: <https://youtu.be/heEN4UIQLjc>
* 自動字幕・翻訳: <https://youtu.be/uQ14hoEiI4c?si=Io9K_vIDYyeu9Z8_>
* ホームカラオケ: <https://youtube.com/playlist?list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq&si=B4S8HJr8gmeAw8hw>


## Credits
* FacebookResearch Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>


## 著作権
  <img src="images/AbUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)
