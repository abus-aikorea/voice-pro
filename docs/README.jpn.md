<!--
    title: Voice-Pro: 究極のAI音声変換および多言語翻訳ツール
    description: YouTubeビデオ処理、音声認識、翻訳、多言語サポートテキスト音声変換のための強力なAIベースWebアプリケーション
    keywords: AI音声変換, YouTube翻訳, 字幕生成, 音声テキスト変換, テキスト音声変換, 音声クローン, 多言語翻訳, ElevenLabs代替
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AIマルチメディア処理ソフトウェア
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

# Voice-Pro: 究極のAI音声変換＆多言語翻訳ツール 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md) ∙ [Deutsch](README.deu.md) ∙ [Español](README.spa.md) ∙ [Português](README.por.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

## 🎙️ YouTubeビデオ処理、音声認識、翻訳、多言語サポートテキスト音声変換のための強力なAIベースWebアプリケーション

Voice-Proは、マルチメディアコンテンツ制作に革新をもたらす最先端のウェブアプリです。YouTube動画のダウンロード、音声分離、音声認識、翻訳、テキストから音声への変換（TTS）を1つの強力なツールに統合し、クリエイター、研究者、多言語専門家にとって理想的なソリューションを提供します。

- 🔊 最高レベルの音声認識: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 ゼロショット音声クローニング: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 多言語テキスト音声変換: **Edge-TTS**, **kokoro**
- 🎥 YouTube処理＆オーディオ抽出: **yt-dlp**
- 🌍 100以上の言語での即時翻訳: **Deep-Translator**
- 🔇 プロ級ボーカル分離: **UVR5**
- 🔥 AIカバー作成: **RVC**

**ElevenLabs**の強力な代替として、Voice-Proはポッドキャスター、開発者、クリエイターに先進的な音声ソリューションを提供します。

## ⚠️ 注意事項
- Voice-Proは**v2.x**にアップデートされました（Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0）
- 🆓 無料体験版は最大**60秒**のメディア処理に対応
- 🔥 **AIカバー**機能が追加されました
- 🎤 **CosyVoice**と**kokoro**のサポートが追加されました
- ⏳ 初回起動時に**CozyVoice2-0.5B (9GB)**をダウンロードします。ネットワーク速度によっては1時間以上かかる場合があります
- 🎧 音声クローニング用のボイスサンプルは継続的に更新予定
- **ご案内:**
  - v1.x から v2.x へのアップグレード: **不可能**. したがって、installer_files フォルダを削除し、最新バージョンの start.bat を実行することを推奨します。
  - v2.x から v2.x へのアップグレード: **可能**. 最新のコードをダウンロードした後、update.bat を実行します。
  - 初めてのユーザー: 以下のインストール方法を参照してください。
  - トラブルシューティング: ほとんどの場合、**installer_files** フォルダを削除し、configure.bat と start.bat を順番に実行すると解決します。


## 🚄 デモ

### `ダビングスタジオ`タブ: 文字起こし、翻訳、TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c" width="100%" style="max-width: 720px;" controls muted aria-describedby="studio-demo-description"></video>

  <video src="https://github.com/user-attachments/assets/1cf084a4-3286-4055-86d2-238ed179560e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description2">
   </video>
     
  <p id="studio-demo-description">スタジオタブの総合的なメディア処理ワークフローデモ: YouTube動画のダウンロードからAIによる音声分離、Whisper自動字幕、多言語翻訳、F5-TTSを使用したプロフェッショナルなダビングまで、一貫したメディア変換プロセスを紹介します。</p>
</div>

### `F5-TTS-Multi`タブ: ポッドキャスト制作
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls muted aria-describedby="tts-demo-description"></video>
  <p id="tts-demo-description">F5-TTSの革新的なAI音声クローニング技術デモ: マーク・ザッカーバーグやイーロン・マスクの実際の声を精密に模倣し、まったく新しいコンテンツを作成する高度な音声変換技術を披露します。</p>
</div>

### `AIカバー`タブ
<div aria-labelledby="ai-cover-description">
  <video src="https://github.com/user-attachments/assets/88a47ab1-a18b-4779-97c8-7c1da84f5fc3" width="100%" style="max-width: 720px;" controls muted aria-describedby="ai-cover-description"></video>
  <p id="ai-cover-description">トランプバージョンのIU『Cupid』、キム・グァンソク『恋しい人』、『二等兵の手紙』を制作します。</p>
</div>

### `リアルタイム翻訳`タブ: リアルタイム認識と翻訳
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls muted aria-describedby="translate-demo-description"></video>
  <p id="translate-demo-description">リアルタイム多言語翻訳機能デモ: BBCニュースコンテンツを即座にキャプチャし、リアルタイムで字幕を生成、他の言語に即時翻訳する革新的な多言語メディア処理プロセスを紹介します。</p>
</div>

## ⭐ 主な機能

### 1. ダビングスタジオ
- YouTube動画ダウンロード＆オーディオ抽出
- **MDX-Net**および**Demucs**による音声分離
- 100以上の言語での音声認識と翻訳をサポート

### 2. 音声技術
- **音声からテキスト:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- **テキストから音声:**
  - **Edge-TTS**: 100以上の言語、400以上の声
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: ゼロショットクローニング
  - **kokoro**: HuggingFace TTS Arenaで2位
- 🔥 **AIカバー（音声から音声）:** **UVR5**でボーカル除去、**RVC**で変調

### 3. リアルタイム翻訳
- 即時音声認識
- リアルタイム多言語翻訳
- カスタマイズ可能なオーディオ入力

## 🤖 ウェブUI

### `ダビングスタジオ`タブ
- 統合ハブ: YouTubeダウンロード、ノイズ除去、字幕、翻訳、TTS
- ffmpeg互換フォーマットすべて対応
- 出力オプション: WAV, FLAC, MP3
- 100以上の言語での字幕と認識
- 速度、ボリューム、ピッチ調整可能なTTS
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.jpn.png?raw=true" alt="多言語音声変換および字幕生成ウェブUIインターフェース"/></p>

### `Whisper字幕`タブ
- 字幕専用: 90以上の言語
- ビデオと統合された字幕表示
- 単語単位のハイライトとノイズ除去オプション

### `翻訳`タブ
- 100以上の言語翻訳
- 字幕ファイル対応（ASS、SSA、SRTなど）
- リアルタイム音声認識と翻訳
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="リアルタイム音声認識および翻訳ウェブUI"/></p>

### `音声生成`タブ
- オプション: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- 有名人声でのポッドキャストと多言語サポート
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="音声クローニング技術を活用したポッドキャスト制作ウェブUI"/></p>

### 🔥 `AIカバー`タブ
- ボーカル除去: **MDX-Net**, **Demucs**
- 音声変調: **RVC**
- AIボイスは[Discord AI Hub](https://discord.com/channels/1159260121998827560/@home)でダウンロード、または<abus.aikorea@gmail.com>にリクエスト
<p align="center"><img style="width: 90%; height: 90%" src="images/ai_cover.png?raw=true" alt="音声クローニング技術を活用したポッドキャスト制作ウェブUI"/></p>




## 🎤✨ 参照音声

- 追加したい音声はIssuesページでリクエストしてください。[Issues](https://github.com/abus-aikorea/voice-pro/issues/50)

### English

<table>
  <tr>
    <td align="center"><img src="celebrities30s/English/Andrew Bustamante.jpg" width="150"><br>Andrew Bustamante</td>
    <td align="center"><img src="celebrities30s/English/Andrew Huberman.jpg" width="150"><br>Andrew Huberman</td>
    <td align="center"><img src="celebrities30s/English/Avi Loeb.jpg" width="150"><br>Avi Loeb</td>
    <td align="center"><img src="celebrities30s/English/Ben Shapiro.jpg" width="150"><br>Ben Shapiro</td>
    <td align="center"><img src="celebrities30s/English/Brett Johnson.jpg" width="150"><br>Brett Johnson</td>
    <td align="center"><img src="celebrities30s/English/Brian Keating.jpg" width="150"><br>Brian Keating</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Coffeezilla.jpg" width="150"><br>Coffeezilla</td>
    <td align="center"><img src="celebrities30s/English/Dan Carlin.jpg" width="150"><br>Dan Carlin</td>
    <td align="center"><img src="celebrities30s/English/David Buss.jpg" width="150"><br>David Buss</td>
    <td align="center"><img src="celebrities30s/English/David Fravor.jpg" width="150"><br>David Fravor</td>
    <td align="center"><img src="celebrities30s/English/David Kipping.jpg" width="150"><br>David Kipping</td>
    <td align="center"><img src="celebrities30s/English/Dennis Whyte.jpg" width="150"><br>Dennis Whyte</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Donald Hoffman.jpg" width="150"><br>Donald Hoffman</td>
    <td align="center"><img src="celebrities30s/English/Donald Trump.jpg" width="150"><br>Donald Trump</td>
    <td align="center"><img src="celebrities30s/English/Douglas Murray.jpg" width="150"><br>Douglas Murray</td>
    <td align="center"><img src="celebrities30s/English/Duncan Trussell.jpg" width="150"><br>Duncan Trussell</td>
    <td align="center"><img src="celebrities30s/English/Elon Musk.jpg" width="150"><br>Elon Musk</td>
    <td align="center"><img src="celebrities30s/English/Garry Nolan.jpg" width="150"><br>Garry Nolan</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Jack Barsky.jpg" width="150"><br>Jack Barsky</td>
    <td align="center"><img src="celebrities30s/English/James Sexton.jpg" width="150"><br>James Sexton</td>
    <td align="center"><img src="celebrities30s/English/Jeff Bezos.jpg" width="150"><br>Jeff Bezos</td>
    <td align="center"><img src="celebrities30s/English/Joe Rogan.jpg" width="150"><br>Joe Rogan</td>
    <td align="center"><img src="celebrities30s/English/John Mearsheimer.jpg" width="150"><br>John Mearsheimer</td>
    <td align="center"><img src="celebrities30s/English/Jordan Peterson.jpg" width="150"><br>Jordan Peterson</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Kanye 'Ye' West.jpg" width="150"><br>Kanye 'Ye' West</td>
    <td align="center"><img src="celebrities30s/English/Mark Zuckerberg.jpg" width="150"><br>Mark Zuckerberg</td>
    <td align="center"><img src="celebrities30s/English/Michael Levin.jpg" width="150"><br>Michael Levin</td>
    <td align="center"><img src="celebrities30s/English/Michael Saylor.jpg" width="150"><br>Michael Saylor</td>
    <td align="center"><img src="celebrities30s/English/Michio Kaku.jpg" width="150"><br>Michio Kaku</td>
    <td align="center"><img src="celebrities30s/English/MrBeast.jpg" width="150"><br>MrBeast</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Nick Lane.jpg" width="150"><br>Nick Lane</td>
    <td align="center"><img src="celebrities30s/English/Paul Rosolie.jpg" width="150"><br>Paul Rosolie</td>
    <td align="center"><img src="celebrities30s/English/Ryan Graves.jpg" width="150"><br>Ryan Graves</td>
    <td align="center"><img src="celebrities30s/English/Sam Altman.jpg" width="150"><br>Sam Altman</td>
    <td align="center"><img src="celebrities30s/English/Sam Harris.jpg" width="150"><br>Sam Harris</td>
    <td align="center"><img src="celebrities30s/English/Stephen Wolfram.jpg" width="150"><br>Stephen Wolfram</td>
  </tr>
  <tr>
    <td align="center"><img src="celebrities30s/English/Tucker Carlson.jpg" width="150"><br>Tucker Carlson</td>
    <td align="center"><img src="celebrities30s/English/Vitalik Buterin.jpg" width="150"><br>Vitalik Buterin</td>
    <td align="center"><img src="celebrities30s/English/Yuval Harari.jpg" width="150"><br>Yuval Harari</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>


### Chinese

<table>
  <tr>
    <td align="center"><img src="celebrities30s/Chinese/Dilraba Dilmurat.jpg" width="150"><br>迪丽热巴 (Dílì Rèbā)</td>
    <td align="center"><img src="celebrities30s/Chinese/Jolin Tsai.jpg" width="150"><br>蔡依林 (Cài Yīlín)</td>
    <td align="center"><img src="celebrities30s/Chinese/Kris Wu.jpg" width="150"><br>吴亦凡 (Wú Yìfán)</td>
    <td align="center"><img src="celebrities30s/Chinese/Li Yifeng.jpg" width="150"><br>李易峰 (Lǐ Yìfēng)</td>
    <td align="center"><img src="celebrities30s/Chinese/Yang Mi.jpg" width="150"><br>杨幂 (Yáng Mì)</td>
    <td align="center"><img src="celebrities30s/Chinese/Zhao Liying.jpg" width="150"><br>赵丽颖 (Zhào Lìyǐng)</td>
  </tr>
</table>

### Korean

<table>
  <tr>
    <td align="center"><img src="celebrities30s/Korean/BTS Jin.jpg" width="150"><br>BTS 진 (Jin)</td>
    <td align="center"><img src="celebrities30s/Korean/BTS RM.jpg" width="150"><br>BTS RM</td>
    <td align="center"><img src="celebrities30s/Korean/IU.jpg" width="150"><br>IU (아이유)</td>
    <td align="center"><img src="celebrities30s/Korean/LeeByungHun.jpg" width="150"><br>이병헌</td>
    <td align="center"><img src="celebrities30s/Korean/LeeJungJae.jpg" width="150"><br>이정재</td>
    <td align="center"><img src="celebrities30s/Korean/YouJaeSuk.jpg" width="150"><br>유재석</td>
  </tr>
</table>

### Japanese

<table>
  <tr>
    <td align="center"><img src="celebrities30s/Japanese/Ayase Haruka.jpg" width="150"><br>綾瀬はるか (Ayase Haruka)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>


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

## 📢 注意事項

Windows DefenderがVoice-Proを信頼できないアプリとして警告し、実行を制限する場合があります。
- **SmartScreen「警告」設定:** 「詳細情報」をクリックし、「それでも実行」を選択
- **SmartScreen「ブロック」設定:** **start.bat**のプロパティで「ブロック解除」をチェックし、再実行
<p align="center"><img style="width: 40%; height: 40%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/></p>

Windows Defenderがバッチファイルをトロイの木馬と誤認識する場合、これは「偽陽性（False Positive）」と呼ばれることが多いです。解決策は以下の通りです。
1. **ファイル例外処理:**
   - 「スタート」ボタンをクリックし、「設定」に移動
   - 「更新とセキュリティ」をクリック
   - 「Windowsセキュリティ」から「ウイルスと脅威の防止」に進む
   - 「ウイルスと脅威の防止設定の管理」をクリック
   - 「ウイルスと脅威の防止設定」で「例外の追加」を選択
   - 「ファイルまたはフォルダ」を選び、対象のバッチファイルを追加
2. **Windows Defenderの一時無効化:** 一時的な解決策。ただし、他の脅威にさらされる可能性があるため注意が必要
3. **アンチウイルスソフトへの報告:** ファイルが安全と確信できる場合、Microsoftに偽陽性として報告可能。Microsoftが確認後対応


## 🚨 お知らせ
- このリポジトリはVoice-Proの**無料トライアル**を提供します。
- Voice-Proの無料トライアル版では、最大**60秒**のメディアを処理できます。
- Voice-Proの公式バージョンは、ABUS公式サイト(<https://abuskorea.imweb.me>)から購入できます。

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
- このプロジェクトに参加して協力したい場合は、お気軽に[Issues](https://github.com/abus-aikorea/voice-pro/issues)を作成してください。
- 問題が発生した場合は、このプロジェクトを改善するために[Pull requests](https://github.com/abus-aikorea/voice-pro/pulls)を提出してください。
- どのような貢献も歓迎します。
- 購入、ビジネスパートナーシップ、技術チューニング、投資、その他の関連事項に関するお問い合わせは、メール(<abus.aikorea@gmail.com>)でお問い合わせください。
- このプロジェクトが気に入ったら、このリポジトリに星を付けてください。大変感謝いたします。 ⭐⭐⭐
- こちらから寄付でVoice-Proを支援できます。

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)


## 📬 連絡先
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- Naver: [30-day subscription](https://smartstore.naver.com/abus/products/11308510267)

## 👍 YouTube
- [製品情報](https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [カラオケ: ポップ](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)

## 🙏 クレジット
- Demucs: <https://github.com/facebookresearch/demucs>
- yt-dlp: <https://github.com/yt-dlp/yt-dlp>
- gradio: <https://github.com/gradio-app/gradio>
- edge-TTS: <https://github.com/rany2/edge-tts>
- F5-TTS: <https://github.com/SWivid/F5-TTS.git>
- openai-whisper: <https://github.com/openai/whisper>
- faster-whisper: <https://github.com/SYSTRAN/faster-whisper>
- whisper-timestamped: <https://github.com/linto-ai/whisper-timestamped>
- RVC-Project: <https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI>
- UVR5: <https://github.com/Anjok07/ultimatevocalremovergui>

## ©️ 著作権情報
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)