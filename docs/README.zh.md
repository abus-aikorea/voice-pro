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


## 🎙️ 先进的AI驱动多媒体处理工具 | Whisper语音识别WebUI

Voice-Pro是一款旨在革新多媒体内容处理的尖端AI驱动的Web应用程序。通过提供YouTube视频下载、语音分离、语音识别、翻译和文本转语音等全面功能，为内容创作者、研究者和多语言通信专业人士提供了一站式解决方案。

- 🔊 尖端语音识别（Whisper、Faster-Whisper、Whisper-Timestamped）
- 🎤 使用F5-TTS和E2-TTS进行零样本语音克隆
- 🎥 YouTube视频处理和音频提取
- 🔇 专业语音分离（UVR5技术）
- 📢 多语言文本转语音（Edge-TTS）
- 🌍 跨100多种语言的即时翻译

为内容创作者、播客制作者、研究者和开发者打造 | AI多媒体解决方案


## 🚄 运行画面

* `Studio` tab : Transcription, Translation & Text-to-Speech
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description">
   </video>
  <p id="studio-demo-description">
Voice-Pro工作室选项卡的全面媒体处理工作流程演示：从YouTube视频下载到基于AI的语音分离、Whisper自动字幕生成、多语言翻译，再到使用F5-TTS进行专业配音的一站式媒体转换过程的展示。
  </p>
</div>

* `TTS` tab : Podcast Production using F5-TTS
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted" 
   aria-describedby="tts-demo-description">
   </video>
  <p id="tts-demo-description">
F5-TTS创新的AI语音克隆技术演示：展示了精确模仿Mark Zuckerberg和Elon Musk真实声音，从而创建全新内容的先进语音转换技术。
  </p>
</div>

* `Live Translation` tab : 实时语音识别和翻译
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1"
  width="100%" 
  style="max-width: 720px;" 
  controls="controls" 
  muted="muted"
  aria-describedby="translate-demo-description">
  </video>
  <p id="translate-demo-description">
Voice-Pro实时多语言翻译功能演示：展示了一个创新的多语言媒体处理过程，通过AI语音识别技术即时捕获YouTube BBC新闻内容，实时生成字幕，并立即将其翻译成其他语言。
  </p>
</div> 


## ⭐ 主要功能和特点

### 1. 全面的工作室标签
- **YouTube视频处理**：以多种格式下载和提取音频
- **语音分离**：使用MDX-Net和Demucs进行高级降噪
- **多语言支持**： 
  - 支持100多种语言的语音识别
  - 具有可自定义选项的字幕创建
  - 支持100多种语言的翻译功能

### 2. 高级语音技术
- **语音转文字（STT）**： 
  - Whisper集成
  - Faster-Whisper支持
  - Whisper-timestamped功能
- **文字转语音（TTS）**： 
  - 具有400多种语音的Edge-TTS
  - 支持零样本语音克隆的F5-TTS
  - 名人语音生成

### 3. 实时翻译
- 即时语音识别
- 多语言翻译
- 可配置的音频输入源



## ⭐ WebUI

* `Studio`标签页
  - 提供YouTube下载器、噪音去除、字幕、翻译和TTS的集成环境
  - 支持所有ffmpeg支持的视频/音频格式
  - 可选择输出音频格式（wav、flac、mp3）
  - 支持100种语言的语音识别和字幕创建
  - 选择适合PC性能的字幕创建选项（Whisper模型和计算类型）
  - 翻译成100多种语言并通过TTS生成语音
  - 原始视频的背景音乐和音效在多语言视频中保持不变
  - 支持TTS语音速度、音量和音调调整

<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt="多语言语音转换和字幕生成Web UI界面"/>
</p>  

* `Whisper Caption`标签页
  - 专用于创建字幕的标签页。支持90多种语言
  - 显示与视频一起创建的字幕
  - 提供单词级高亮功能
  - 提供降噪功能（1-Demucs、2-MDXNet）

* `Translate`标签页
  - 专用于翻译的标签页。支持100多种语言
  - 支持字幕文件（ass、ssa、srt、mpl2、tmp、vtt、microdvd、json）
  - 也可以直接输入文本
  - 自动检测上传文件的语言

* `TTS`标签页
  - 支持 Edge-TTS 和 F5-TTS。
  - Edge-TTS 支持超過 100 種語言和 400 種以上的聲音。
  - 可以調整音高、音量和速度。
  - F5-TTS 支持零樣本語音克隆。
  - 可以使用 Celeb Voice 製作播客。

<p align="center">
  <img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="使用语音克隆技术的播客制作Web界面"/>
</p>  


* `Live Translation`标签页
  - 支持实时语音识别和翻译
  - 选择麦克风、扬声器等音频输入源
  - 提供保存捕获的音频、识别的字幕和翻译的字幕的功能

<p align="center">
  <img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="用于实时语音识别和翻译的WebUI"/>
</p>  


* `Batch`标签页
  - 大量文件的批处理
  - 字幕、翻译、TTS

## 💻 执行环境
* 操作系统：Windows 10/11（64位）**※不支持Linux和Mac OS。**
* GPU：推荐支持CUDA 12.1的**NVIDIA**显卡。
* VRAM：4GB或以上。推荐8GB或以上。
* RAM：4GB或以上
* 硬盘：安装时至少需要20GB的可用空间
* 需要网络连接（安装和翻译工作）

## 📀 安装

Voice-Pro可以轻松地一键安装。只需运行🚀**configure.bat**和🚀**start.bat**即可。

### 步骤1. 准备包
  + 从[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/)克隆或下载最新版本（**Source code (zip)**）。

```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 步骤2. 安装和运行程序
1. 🚀 运行`configure.bat`
   - 在Windows上安装git、ffmpeg和CUDA（如果使用NVIDIA GPU）。
   - 只需要在第一次运行时执行。
   - 需要网络连接，根据系统情况可能需要一个多小时。
   - 安装过程中切勿关闭Windows命令窗口。
2. 🚀 运行`start.bat`
   - 启动Voice-Pro。网页界面将自动运行。
   - 首次运行时，会先安装Voice-Pro。
   - 需要网络连接，根据系统情况可能需要一个多小时。
   - 安装过程中切勿关闭Windows命令窗口。
   - 如果安装过程中出现问题，请删除**installer_files**文件夹并再次运行start.bat。

### 步骤3. 卸载程序
* 运行`uninstall.bat`：
  - 删除**installer_files**文件夹。
  - 删除安装在Windows上的ffmpeg、git和CUDA包（如果选择）。
* Voice-Pro默认为**便携式**安装。要卸载程序，只需删除安装文件夹即可。

## ❓ 提示和技巧

#### 如果浏览器没有自动运行
- 关闭Windows命令窗口并再次运行start.bat。
- 直接运行浏览器并在地址栏输入Windows命令窗口中显示的地址（例如 **http://127.0.0.1:7892**）。

#### 如果出现CUDA内存不足错误
- 在Windows任务管理器的性能选项卡中检查GPU内存状态。
- 将降噪级别设置为0或1。降噪级别2至少需要8GB的GPU内存。
- 将计算类型设置为int类型。float类型质量更好，但需要更多GPU内存。

#### 如何提高字幕质量？
- 字幕质量通常随着更大的Whisper模型而提高，但并非总是如此。large > medium > small > base > tiny
- 在计算类型中，float类型性能较好。int类型是通过模型量化减少GPU使用并提高速度的模型。另一方面，性能会下降。
- 如果增加降噪级别，将会去除更多背景声音，只使用剩余的声音进行语音识别。这并不总是保证好的结果。

## 📢 注意

Windows Defender 可能会发出有关不受信任的应用程序的警告，并禁止进一步执行 Voice-Pro。
如果 SmartScreen 的安全级别设置为“警告”，只需点击“更多信息”，然后点击“仍然要运行”。
如果 SmartScreen 设置为“阻止”级别，则不会有按钮来运行安装。在这种情况下，打开 start.bat 文件的属性，检查“解除阻止”，应用更改后再次运行 start.bat。

<p align="center">
  <img style="width: 60%; height: 60%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  

当Windows Defender错误地将批处理文件识别为特洛伊木马时，这通常被称为"误报"。要解决这个问题，您可以按照以下步骤操作：

1. 文件例外处理：在Windows Defender中，您可以设置某些文件或进程跳过安全扫描。要做到这一点，请按照以下步骤：
   * 点击"开始"按钮并进入"设置"。
   * 点击"更新与安全"。
   * 选择"Windows安全中心"并进入"病毒和威胁防护"。
   * 点击"管理病毒和威胁防护设置"。
   * 在"病毒和威胁防护设置"中选择"添加或删除排除项"。
   * 选择"文件或文件夹"，找到相关的批处理文件并将其添加为例外。
2. 暂时禁用Windows Defender：这可能是一个临时解决方案。但是，使用此方法时必须小心，因为它可能会使您的计算机暴露于其他威胁中。
3. 向防病毒软件报告问题：如果您确定该文件不是特洛伊木马，可以将其作为误报向Microsoft报告。Microsoft将审查此问题并采取必要的行动。


## ☕ 通知
- 该仓库提供 Voice-Pro 的**免费试用**。 
- 免费试用有**30分钟的使用限制**。这意味着运行后30分钟后，您将无法再使用Web界面。 
- 这并不意味着处理媒体的长度有限制，也不会停止正在进行的任务。您只是无法再点击操作按钮。 
- 可能会有点不便，但要再次使用，只需关闭程序并重新启动。 
- 先前的工作结果保存在工作空间文件夹中。 
- Voice-Pro的官方版本可以通过ABUS官方网站(<https://abuskorea.imweb.me>)购买。
- 此外，如果您通过Buy Me a Coffee ☕支持我们，我们将作为感谢，为您提供最多一个月的使用凭证。 (<https://github.com/abus-aikorea/voice-pro/discussions/10#discussioncomment-11527327>)
- 关于购买、商业合作、调整、投资等方面的咨询，请通过电子邮件(<abus.aikorea@gmail.com>)与我们联系。



## 📬 联系我们
* 电子邮件：<abus.aikorea@gmail.com>
* 主页（韩语）：<https://abuskorea.imweb.me>
* 亚马逊（美国）：<https://www.amazon.com/dp/B0DBR69JPL>
* 亚马逊（日本）：<https://www.amazon.co.jp/dp/B0DBVRJ542>
* 亚马逊（新加坡）：<https://www.amazon.sg/dp/B0DCGKL8R4>
* 亚马逊（阿联酋）：<https://www.amazon.ae/dp/B0DCGKM7FF>
* Naver智能商店（S/W）：<https://smartstore.naver.com/abus/products/10385660040>
* Naver智能商店（解决方案）：<https://smartstore.naver.com/abus/products/10298346364>

## 👍 YouTube
* 产品信息：<https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq>
* 家庭卡拉OK（流行音乐）：<https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6>
* 家庭卡拉OK（K-Pop）：<https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8>
* 家庭卡拉OK（J-Pop）：<https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq>


## 🙏 鸣谢
* Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>
* edge-TTS: <https://github.com/rany2/edge-tts>
* F5-TTS: <https://github.com/SWivid/F5-TTS.git>
* openai-whisper: <https://github.com/openai/whisper>
* faster-whisper: <https://github.com/SYSTRAN/faster-whisper>
* whisper-timestamped: <https://github.com/linto-ai/whisper-timestamped>

## ©️ 版权
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)
