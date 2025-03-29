<!--
    title: Voice-Pro：终极AI语音转换和多语言翻译工具
    description: 强大的AI驱动Web应用程序，用于YouTube视频处理、语音识别、翻译和多语言支持的文本到语音转换
    keywords: AI语音转换, YouTube翻译, 字幕生成, 语音转文本, 文本转语音, 语音克隆, 多语言翻译, ElevenLabs替代品
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AI多媒体处理软件
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, WhisperX, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">最佳AI语音识别、翻译和多语言配音解决方案 🚀</i>
</p>

<h4 align="center">
  <a href="https://www.youtube.com/channel/UCbCBWXuVbk-OBp9T4H5JjAA">
    <img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube" style="height: 20px;">
  </a>
  <a href="https://www.amazon.sg/dp/B0F1LQZ42T">
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
    <img src="images/main_page_crop.zh.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />

## 🎙️ 为语音识别、翻译和配音设计的AI驱动网络应用程序


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

Voice-Pro是一款革新多媒体内容制作的先进网页应用。它将YouTube视频下载、音频分离、语音识别、翻译和文本转语音(TTS)集成到一个强大的工具中，为创作者、研究人员和多语言专家提供理想的解决方案。

- 🔊 顶级语音识别: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- 🎤 零样本语音克隆: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 多语言文本转语音: **Edge-TTS**, **kokoro** (付费版包括 **Azure TTS**)
- 🎥 YouTube处理与音频提取: **yt-dlp**
- 🌍 超过100种语言的即时翻译: **Deep-Translator** (付费版包括 **Azure Translator**)


作为**ElevenLabs**的强大替代方案，Voice-Pro为播客主持人、开发者和创作者提供高级语音解决方案。

## ⚠️ 请注意
- **从v2.x升级到v3.x**: 不可能。我们建议删除`installer_files`文件夹并运行最新版本的`start.bat`。
- **从v3.x升级到v3.x**: 可以。下载最新代码后，运行`update.bat`。
- **首次用户**: 请参阅下面的安装说明。
- **故障排除**: 在大多数情况下，删除`installer_files`文件夹，然后依次运行`configure.bat`和`start.bat`即可解决问题。
- 🎁 **免费激活密钥请求**: 请填写此[Google 表单](https://forms.gle/anMSmsR5dH9wxE6N6)以获取您的激活密钥。激活密钥每个电子邮件地址限领一个。
- 🏆 **额外激活密钥请求**: 使用Voice-Pro创建精彩内容。请在[![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions)中分享您的帖子链接。我们将乐意奖励您的贡献。


## 📰 新闻与历史

<details open>
<summary>version 3.1</summary>

- 🪄 支持 **F5-TTS** 的微调模型
- 🌍 支持的语言
  - <img src="https://flagcdn.com/16x12/us.png" alt="United Kingdom Flag" style="vertical-align: middle;"> English & <img src="https://flagcdn.com/16x12/cn.png" alt="China Flag" style="vertical-align: middle;"> Chinese: <a href="https://huggingface.co/SWivid/F5-TTS/tree/main/F5TTS_v1_Base"> SWivid/F5-TTS_v1 </a> 
  - <img src="https://flagcdn.com/16x12/fi.png" alt="Spain Flag" style="vertical-align: middle;"> Finnish: <a href="https://huggingface.co/AsmoKoskinen/F5-TTS_Finnish_Model"> AsmoKoskinen/F5-TTS_Finnish_Model </a> 
  - <img src="https://flagcdn.com/16x12/fr.png" alt="Spain Flag" style="vertical-align: middle;"> French: <a href="https://huggingface.co/RASPIAUDIO/F5-French-MixedSpeakers-reduced"> RASPIAUDIO/F5-French-MixedSpeakers-reduced </a> 
  - <img src="https://flagcdn.com/16x12/in.png" alt="Spain Flag" style="vertical-align: middle;"> Hindi: <a href="https://huggingface.co/SPRINGLab/F5-Hindi-24KHz"> SPRINGLab/F5-Hindi-24KHz </a>  
  - <img src="https://flagcdn.com/16x12/it.png" alt="Spain Flag" style="vertical-align: middle;"> Italian: <a href="https://huggingface.co/alien79/F5-TTS-italian"> alien79/F5-TTS-italian </a>  
  - <img src="https://flagcdn.com/16x12/jp.png" alt="Spain Flag" style="vertical-align: middle;"> Japanese: <a href="https://huggingface.co/Jmica/F5TTS/tree/main/JA_21999120"> Jmica/F5TTS/JA_21999120 </a>  
  - <img src="https://flagcdn.com/16x12/ru.png" alt="Spain Flag" style="vertical-align: middle;"> Russian: <a href="https://huggingface.co/hotstone228/F5-TTS-Russian"> hotstone228/F5-TTS-Russian </a> 
  - <img src="https://flagcdn.com/16x12/es.png" alt="Spain Flag" style="vertical-align: middle;"> Spanish: <a href="https://huggingface.co/jpgallegoar/F5-Spanish"> jpgallegoar/F5-Spanish </a> 
  
</details>

<details open>
<summary>版本 3.0</summary>

- 🔥 **AI Cover**功能已移除。  
- 🚀 添加了对**m-bain/whisperX**的支持。  

</details>

<details>
<summary>版本 2.0</summary>

- 🐍 使用Python 3.10.15、Torch 2.5.1+cu124和Gradio 5.14.0构建。  
- 🆓 免费试用支持最长**60秒**的媒体。  
- 🔥 添加了**AI Cover**功能。  
- 🎤 引入了对**CosyVoice**和**kokoro**的支持。  
- ⏳ 首次运行时下载**CozyVoice2-0.5B (9GB)**，根据网络速度可能需要超过1小时。  
- 🎧 用于语音克隆的语音样本将持续更新。  
- 📝 添加了**spaCy**以实现自然逐句翻译和TTS。  
- ☁️ 订阅版本包括**Microsoft Azure**的翻译和TTS。  
- 🏪 订阅版本在订阅期间提供**无限制使用**（无60秒限制），可通过  [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com) 购买。  

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

## ⭐ 主要功能

### 1. 配音工作室
- YouTube视频下载与音频提取
- 使用**Demucs**进行声音分离
- 支持100多种语言的语音识别与翻译

### 2. 语音技术
- **语音转文本:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- **文本转语音:** 
  - **Edge-TTS**: 100多种语言，400多种声音
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: 零样本克隆
  - **kokoro**: 在HuggingFace TTS竞技场中排名第2

### 3. 实时翻译
- 即时语音识别
- 实时多语言翻译
- 可定制的音频输入



## 🤖 网页界面

### `配音工作室`标签页
- 集成中心：YouTube下载、降噪、字幕、翻译、TTS
- 支持所有ffmpeg兼容格式
- 输出选项：WAV、FLAC、MP3
- 支持100多种语言的字幕和识别
- 可调节TTS的速度、音量、音调
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.zh.jpg?raw=true" alt="多语言语音转换和字幕生成网页界面"/></p>

### `Whisper字幕`标签页
- 专用字幕：90多种语言
- 视频集成字幕显示
- 单词级高亮和降噪选项

### `翻译`标签页
- 100多种语言翻译
- 支持字幕文件（ASS、SSA、SRT等）
- 实时语音识别和翻译
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.jpg?raw=true" alt="实时语音识别和翻译网页界面"/></p>

### `语音生成`标签页
- 选项：**Edge-TTS**、**F5-TTS**、**CosyVoice**、**kokoro**
- 使用名人声音制作播客和多语言支持
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.jpg?raw=true" alt="使用语音克隆技术制作播客的网页界面"/></p>



## 🎤✨ 参考声音

- 请在Issues页面上请求想添加的声音。[Issues](https://github.com/abus-aikorea/voice-pro/issues/50)


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



## 💻 系统要求
- **操作系统：** Windows 10/11（64位）※不支持Linux/Mac
- **显卡：** 支持CUDA 12.4的NVIDIA显卡（推荐）
- **显存：** 4GB以上（推荐8GB以上）
- **内存：** 4GB以上
- **存储：** 20GB以上可用空间
- **网络：** 必需

## 📀 安装

使用**configure.bat**和**start.bat**轻松安装Voice-Pro。

### 1. 准备包
- 从[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)下载最新发布版本（**Source code (zip)**）
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. 安装和运行
1. 🚀 **configure.bat**
   - 安装git、ffmpeg、CUDA（使用NVIDIA GPU时）
   - 首次运行一次；需要网络，可能需要1小时以上
   - 不要关闭命令窗口
2. 🚀 **start.bat**
   - 运行Voice-Pro网页界面
   - 首次运行时安装依赖（可能需要1小时以上）
   - 如果出现问题，删除**installer_files**后重新运行

### 3. 更新
- 🚀 **update.bat**：更新Python环境（比重新安装更快）

### 4. 卸载
- 运行**uninstall.bat**或删除文件夹（便携式安装）

## ❓使用技巧

#### 浏览器没有自动启动时
- 关闭Windows命令窗口，重新运行start.bat，或
- 直接启动浏览器，在地址栏输入Windows命令窗口显示的地址（例如**http://127.0.0.1:7870**）

#### 出现CUDA内存不足错误时
- 在Windows任务管理器-性能标签中检查GPU内存状态
- 将降噪级别设置为0或1。降噪级别2需要8GB以上的GPU内存
- 将计算类型设置为int类型。float类型质量更好但需要更多GPU内存

#### 如何提高字幕质量？
- 字幕质量通常随着使用更大的Whisper模型而提高，但并不总是如此。large > medium > small > base > tiny
- 在计算类型中，float类型性能更好。int类型通过模型量化降低GPU使用量并提高速度，但性能较差
- 提高降噪级别可以更多地去除背景音，只将剩余的语音用于语音识别。但不总是能保证更好的结果



## 🚨 通知
- 此存储库提供 Voice-Pro 的**免费试用版**。
- Voice-Pro 的免费试用版允许您处理长达 **60 秒**的媒体。
- 订阅版本支持 Microsoft Azure TTS 和 Translator。请在 [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com) 上购买。

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

## ☕ 贡献

您好，我是Voice-Pro团队的戴维。
我们的团队致力于发掘业内顶尖的人工智能技术，并提供给所有人，让大家都能轻松便捷地使用。
我们是一家刚成立一年的韩国小型创业公司。我们努力工作，旨在帮助您和其他创作者制作出色的内容。

您的⭐⭐⭐⭐⭐评价对我们的业务与您共同成长至关重要，我们对此深表感谢。请您支持我们这个小团队。

谢谢，
ABUS客户服务

- 如果您想参与并帮助我们进行此项目，请随时创建一个 [Issues](https://github.com/abus-aikorea/voice-pro/issues)。
- 如果出现问题，请提交一个 [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) 以改进此项目。
- 欢迎任何类型的贡献。
- 有关购买、商业伙伴关系、技术调整、投资和其他相关事宜的咨询，请通过电子邮件 (<abus.aikorea@gmail.com>) 与我们联系。
- 如果您喜欢这个项目，请给这个存储库加星标。我们将非常感谢。 ⭐⭐⭐
- 您可以在这里通过捐赠支持 Voice-Pro：    
</a>
  <a href="https://www.buymeacoffee.com/abus">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
</a>




## 📬 联系方式
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- 付费版本购买: [Shopify (Global)](https://r17wvy-t2.myshopify.com), [Naver (Korean)](https://smartstore.naver.com/abus)



## 🙏 鸣谢
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

## ©️ 版权信息
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)   