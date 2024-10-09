# Voice-Pro

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/voice-pro)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

用于转录、翻译和文本转语音的最佳 gradio 网页界面。一键安装简便。完全便携。

## 简介
* Voice-Pro 是一个集成了**字幕、翻译和文本转语音**的解决方案。
* 使用 Voice-Pro 为您的视频添加多语言字幕和多语言音频。让全球市场扩展成为可能！
* 您每天早晨都看世界新闻吗？那么，试试使用实时翻译功能。它支持实时翻译，就像您在 YouTube 上看到的那样。
* Voice-Pro 配备了 UVR5 提供的**人声移除器**和 Meta 的 **Demucs** 引擎。
* Voice-Pro 使用 **OpenAI Whisper** 和免费的**开源翻译器**以及**开源文本转语音**。
* Voice-Pro 可以通过**一键**轻松安装，并提供 Gradio 网页界面。
* 体验最高水平的**设备端 AI 语音**技术。

## 主要功能

* `Studio` 标签页
  - 提供 YouTube 下载器、降噪、字幕、翻译和文本转语音的集成环境
  - 支持所有 ffmpeg 可用的视频/音频格式
  - 可选择输出音频格式（wav、flac、mp3）
  - 支持 100 种语言的语音识别和字幕创建
  - 选择适合 PC 性能的字幕创建选项（Whisper 模型和计算类型）
  - 翻译成 100 多种语言，并通过文本转语音生成语音
  - 多语言视频中保留原始视频的背景音乐和音效
  - 支持调整文本转语音的语速、音量和音调

<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.eng.png?raw=true" alt=""/>
</p>  

* `Whisper Caption` 标签页
  - 专门用于创建字幕的标签页。支持 90 多种语言
  - 显示与视频一起创建的字幕
  - 提供单词级高亮功能
  - 提供降噪功能（1-Demucs，2-MDXNet）

* `Translate` 标签页
  - 专门用于翻译的标签页。支持 100 多种语言
  - 支持字幕文件（ass、ssa、srt、mpl2、tmp、vtt、microdvd、json）
  - 也可以直接输入文本
  - 自动检测上传文件的语言

* `TTS` 标签页
  - 专门用于文本转语音的标签页。支持 100 多种语言和 400 种声音
  - 支持字幕文件（ass、ssa、srt、mpl2、tmp、vtt、microdvd、json）
  - 也可以直接输入文本
  - 自动检测上传文件的语言
  - 可调节音调、音量和语速

* `Live Translation` 标签页
  - 支持实时语音识别和翻译
  - 选择音频输入源，如麦克风、扬声器等
  - 提供保存捕获的音频、识别的字幕和翻译的字幕的功能

* `Batch` 标签页
  - 批量处理大量文件
  - 字幕、翻译、文本转语音

## 特点
* 您可以下载 YouTube 视频（mp4、webm）并将其保存为音频文件（mp3、wav、flac）。
* 通过去除噪音和分离人声，可以提高语音识别的准确性。使用 **MDX-Net** 和 Meta 的 **Demucs**。
* 通过 AI 语音识别提供自动字幕创建、机器翻译和文本转语音功能。
* 您可以轻松制作多语言视频。
* **一键安装**。安装后，无需额外费用即可**永久**使用。（※ 免费版有 **30 分钟**使用时间限制）
* 提供**网页界面**。推荐使用 Google Chrome 浏览器。

## 运行环境
* 操作系统：Windows 10/11（64位）**※ 不支持 Linux 和 Mac OS。**
* CPU：Intel 处理器 2GHz 或更高（或同等兼容处理器）
* 内存：4GB 或更多
* 硬盘：安装时至少需要 20GB 的可用空间
* 显卡：推荐支持 CUDA 12.1 的 **NVIDIA** 显卡。显存 4GB 或更多，建议 8GB 或更多。
* 需要互联网连接（用于安装和翻译工作）

## 安装和运行

### 步骤 1. 准备包
* A. 付费版
    + 将 USB 中包含的压缩文件（**voice-pro-x.zip**）解压到计算机上的适当位置。
    + 或者，将已解压的文件夹（**voice-pro-x**）复制到计算机上的适当位置。

* B. 免费版
  + 从 [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) 下载并解压最新版本（**Source code (zip)**）
  + 或者，使用 git clone 下载源代码
    
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 步骤 2. 安装和运行程序
1. 运行 `configure.bat`
   - 在 Windows 上安装 ffmpeg 和 CUDA（如果使用 NVIDIA GPU）。
   - 您只需要在第一次运行时执行此操作。
2. 运行 `start.bat`
   - 启动 Voice-Pro。网页界面将自动运行。
   - 首次运行时，会先安装 Voice-Pro。
   - Voice-Pro 安装需要互联网连接，根据系统情况，安装可能需要一个多小时。
   - 安装过程中切勿关闭 Windows 命令窗口。
   - 如果安装过程中出现问题，请删除 installer_files 文件夹并重新运行 start.bat。

### 运行界面

[此处应该有一张图片，但在文本格式中无法显示]

### 步骤 3. 卸载程序
* 运行 `uninstall.bat`：
  - 删除 installer_files 文件夹。
  - 删除在 Windows 上安装的 ffmpeg 和 CUDA 包（如果选择）

* Voice-Pro 默认为**便携式**安装。要卸载程序，删除安装文件夹即可。

## 技巧与窍门

#### 如果浏览器没有自动运行
- 关闭 Windows 命令窗口并重新运行 start.bat。
- 直接运行浏览器，并在地址栏中输入 Windows 命令窗口中显示的地址（例如 **http://127.0.0.1:7892**）。

#### 如果出现 CUDA 内存不足错误
- 在 Windows 任务管理器 - 性能标签中检查 GPU 内存状态。
- 将降噪级别设置为 0 或 1。降噪级别 2 需要至少 8GB 的 GPU 内存。
- 将计算类型设置为 int 类型。float 类型质量更好，但需要更多 GPU 内存。

#### 如何提高字幕质量？
- 字幕质量往往随着更大的 Whisper 模型而提高，但并非总是如此。large > medium > small > base > tiny 
- 在计算类型中，float 类型性能较好。int 类型是通过模型量化来减少 GPU 使用并提高速度的模型。然而，性能会降低。
- 如果增加降噪级别，会去除更多背景声音，只使用剩余的语音进行语音识别。这并不总是保证好的结果。

## 注意事项
当 Windows Defender 错误地将批处理文件识别为特洛伊木马时，这通常被称为"误报"。要解决这个问题，您可以通过以下步骤：

1. 文件例外处理：在 Windows Defender 中，您可以设置某些文件或进程跳过安全扫描。操作如下：
   * 点击"开始"按钮，进入"设置"。
   * 点击"更新和安全"。
   * 选择"Windows 安全中心"，进入"病毒和威胁防护"。
   * 点击"管理病毒和威胁防护设置"。
   * 在"病毒和威胁防护设置"中选择"添加或删除排除项"。
   * 选择"文件或文件夹"，找到相关的批处理文件并将其添加为例外。
2. 临时禁用 Windows Defender：这可能是一个临时解决方案。但是，使用这种方法时必须小心，因为它可能会使您的计算机面临其他威胁。
3. 向反病毒软件报告问题：如果您确定该文件不是特洛伊木马，可以将其报告给 Microsoft 作为误报。Microsoft 将对此进行审查并采取必要的行动。

## 联系我们
* 电子邮件：<abus.aikorea@gmail.com>
* 主页（韩语）：<https://abuskorea.imweb.me>
* Naver 智能商店（软件）：<https://smartstore.naver.com/abus/products/10385660040>
* Naver 智能商店（解决方案）：<https://smartstore.naver.com/abus/products/10298346364>
* Coupang（韩国）：<https://www.coupang.com/vp/products/7875503674>
* Amazon（美国）：<https://www.amazon.com/dp/B0D5H8Z4FL>
* Amazon（日本）：<https://www.amazon.co.jp/dp/B0CTHT2JH3>

## YouTube
* 产品信息：<https://youtu.be/heEN4UIQLjc>
* 自动字幕∙翻译：<https://youtu.be/uQ14hoEiI4c?si=Io9K_vIDYyeu9Z8_>
* 家庭卡拉 OK：<https://youtube.com/playlist?list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6&si=TZBh5AFjcr7_dyiI>

## 鸣谢
* FacebookResearch Demucs：<https://github.com/facebookresearch/demucs>
* yt-dlp：<https://github.com/yt-dlp/yt-dlp>
* gradio：<https://github.com/gradio-app/gradio>

## 版权
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)