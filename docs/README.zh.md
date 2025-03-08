<!--
    title: Voice-Pro：终极AI语音转换和多语言翻译工具
    description: 强大的AI驱动Web应用程序，用于YouTube视频处理、语音识别、翻译和多语言支持的文本到语音转换
    keywords: AI语音转换, YouTube翻译, 字幕生成, 语音转文本, 文本转语音, 语音克隆, 多语言翻译, ElevenLabs替代品
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AI多媒体处理软件
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

# Voice-Pro: 终极AI语音转换和多语言翻译工具 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md) ∙ [Deutsch](README.deu.md) ∙ [Español](README.spa.md) ∙ [Português](README.por.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

## 🎙️ 强大的AI驱动Web应用程序，用于YouTube视频处理、语音识别、翻译和多语言支持的文本到语音转换

Voice-Pro是一款革新多媒体内容制作的先进网页应用。它将YouTube视频下载、音频分离、语音识别、翻译和文本转语音(TTS)集成到一个强大的工具中，为创作者、研究人员和多语言专家提供理想的解决方案。

- 🔊 顶级语音识别：**Whisper**、**Faster-Whisper**、**Whisper-Timestamped**
- 🎤 零样本声音克隆：**F5-TTS**、**E2-TTS**、**CosyVoice**
- 📢 多语言文本转语音：**Edge-TTS**、**kokoro**
- 🎥 YouTube处理和音频提取：**yt-dlp**
- 🌍 100多种语言即时翻译：**Deep-Translator**
- 🔇 专业级人声分离：**UVR5**
- 🔥 AI翻唱制作：**RVC**

作为**ElevenLabs**的强大替代方案，Voice-Pro为播客主持人、开发者和创作者提供高级语音解决方案。

## ⚠️ 注意事项
- Voice-Pro已更新至**v2.x**版本（Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0）
- 🆓 免费试用版支持最长**60秒**的媒体处理
- 🔥 新增**AI翻唱**功能
- 🎤 新增**CosyVoice**和**kokoro**支持
- ⏳ 首次运行时需下载**CozyVoice2-0.5B (9GB)**，根据网络速度可能需要1小时以上
- 🎧 声音克隆用的语音样本将持续更新
- **提示：**
  - 从 v1.x 升级到 v2.x：**不可能**。因此，建议删除 installer_files 文件夹并运行最新版本的 start.bat。
  - 从 v2.x 升级到 v2.x：**可能**。下载最新代码后，运行 update.bat。
  - 首次用户：请参考以下安装方法。
  - 问题解决：在大多数情况下，删除 **installer_files** 文件夹并依次运行 configure.bat 和 start.bat 即可解决问题。


## 🚄 演示

### `配音工作室`标签页：转录、翻译和TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c" width="100%" style="max-width: 720px;" controls muted aria-describedby="studio-demo-description"></video>
  <video src="https://github.com/user-attachments/assets/1cf084a4-3286-4055-86d2-238ed179560e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description2">
  </video>   
  <p id="studio-demo-description">工作室标签页的综合媒体处理工作流程演示：从YouTube视频下载到AI语音分离、Whisper自动字幕、多语言翻译，再到使用F5-TTS进行专业配音的一站式媒体转换过程。</p>
</div>

### `F5-TTS-Multi`标签页：播客制作
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls muted aria-describedby="tts-demo-description"></video>
  <p id="tts-demo-description">F5-TTS的创新AI声音克隆技术演示：精确模仿马克·扎克伯格和埃隆·马斯克的真实声音，创建全新内容的高级语音转换技术展示。</p>
</div>

### `AI翻唱`标签页
<div aria-labelledby="ai-cover-description">
  <video src="https://github.com/user-attachments/assets/88a47ab1-a18b-4779-97c8-7c1da84f5fc3" width="100%" style="max-width: 720px;" controls muted aria-describedby="ai-cover-description"></video>
  <p id="ai-cover-description">制作特朗普版本的IU《Cupid》、金光石《想念的人》、《士兵的信》。</p>
</div>

### `实时翻译`标签页：实时识别和翻译
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls muted aria-describedby="translate-demo-description"></video>
  <p id="translate-demo-description">实时多语言翻译功能演示：即时捕获BBC新闻内容，生成实时字幕，并立即翻译成其他语言的创新多语言媒体处理过程。</p>
</div>

## ⭐ 主要功能

### 1. 配音工作室
- YouTube视频下载和音频提取
- 使用**MDX-Net**和**Demucs**进行语音分离
- 支持100多种语言的语音识别和翻译

### 2. 语音技术
- **语音转文本：** **Whisper**、**Faster-Whisper**、**Whisper-Timestamped**
- **文本转语音：**
  - **Edge-TTS**：支持100多种语言，400多种声音
  - **E2-TTS**、**F5-TTS**、**CosyVoice**：零样本克隆
  - **kokoro**：在HuggingFace TTS Arena中排名第二
- 🔥 **AI翻唱（语音转语音）：** 使用**UVR5**移除人声，使用**RVC**进行变声

### 3. 实时翻译
- 即时语音识别
- 实时多语言翻译
- 可自定义音频输入

## 🤖 网页界面

### `配音工作室`标签页
- 集成中心：YouTube下载、降噪、字幕、翻译、TTS
- 支持所有ffmpeg兼容格式
- 输出选项：WAV、FLAC、MP3
- 支持100多种语言的字幕和识别
- 可调节TTS的速度、音量、音调
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.zh.png?raw=true" alt="多语言语音转换和字幕生成网页界面"/></p>

### `Whisper字幕`标签页
- 专用字幕：90多种语言
- 视频集成字幕显示
- 单词级高亮和降噪选项

### `翻译`标签页
- 100多种语言翻译
- 支持字幕文件（ASS、SSA、SRT等）
- 实时语音识别和翻译
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="实时语音识别和翻译网页界面"/></p>

### `语音生成`标签页
- 选项：**Edge-TTS**、**F5-TTS**、**CosyVoice**、**kokoro**
- 使用名人声音制作播客和多语言支持
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="使用语音克隆技术制作播客的网页界面"/></p>

### 🔥 `AI翻唱`标签页
- 人声移除：**MDX-Net**、**Demucs**
- 语音变调：**RVC**
- AI声音可从[Discord AI Hub](https://discord.com/channels/1159260121998827560/@home)下载或发邮件至<abus.aikorea@gmail.com>请求
<p align="center"><img style="width: 90%; height: 90%" src="images/ai_cover.png?raw=true" alt="使用语音克隆技术制作播客的网页界面"/></p>



## 🎤✨ 参考声音

- 请在Issues页面上请求想添加的声音。[Issues](https://github.com/abus-aikorea/voice-pro/issues/50)

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
- 直接启动浏览器，在地址栏输入Windows命令窗口显示的地址（例如**http://127.0.0.1:7892**）

#### 出现CUDA内存不足错误时
- 在Windows任务管理器-性能标签中检查GPU内存状态
- 将降噪级别设置为0或1。降噪级别2需要8GB以上的GPU内存
- 将计算类型设置为int类型。float类型质量更好但需要更多GPU内存

#### 如何提高字幕质量？
- 字幕质量通常随着使用更大的Whisper模型而提高，但并不总是如此。large > medium > small > base > tiny
- 在计算类型中，float类型性能更好。int类型通过模型量化降低GPU使用量并提高速度，但性能较差
- 提高降噪级别可以更多地去除背景音，只将剩余的语音用于语音识别。但不总是能保证更好的结果

## 📢 注意事项

Windows Defender可能会显示不受信任应用程序的警告，并阻止Voice-Pro继续运行。
如果SmartScreen安全级别设置为"警告"，请点击"更多信息"后点击"仍要运行"。
如果SmartScreen设置为"阻止"级别，则没有可以运行安装的按钮。在这种情况下，打开start.bat文件的属性，勾选"解除阻止"，应用更改后重新运行start.bat文件。

<p align="center">
  <img style="width: 40%; height: 40%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  

如果Windows Defender错误地将批处理文件识别为特洛伊木马，这通常被称为"误报"。要解决这个问题，可以采取以下步骤：

1. 文件例外处理：可以在Windows Defender中设置特定文件或进程跳过安全检查。请按照以下步骤操作：
   * 点击"开始"按钮，进入"设置"
   * 点击"更新和安全"
   * 选择"Windows安全中心"，进入"病毒和威胁防护"
   * 点击"管理病毒和威胁防护设置"
   * 在"病毒和威胁防护设置"中选择"添加或删除排除项"
   * 选择"文件或文件夹"，找到相关批处理文件并添加为例外

2. 暂时禁用Windows Defender：这可以作为临时解决方案。但使用此方法时，请注意计算机可能会暴露于其他威胁中。

3. 向防病毒软件报告问题：如果您确信该文件不是特洛伊木马，可以向Microsoft报告为误报。Microsoft会审查后采取必要的措施。


## 🚨 通知
- 此存储库提供 Voice-Pro 的**免费试用版**。
- Voice-Pro 的免费试用版允许您处理长达 **60 秒**的媒体。
- Voice-Pro 的正式版本可通过 ABUS 官方网站 (<https://abuskorea.imweb.me>) 购买。

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
- 如果您想参与并帮助我们进行此项目，请随时创建一个 [Issues](https://github.com/abus-aikorea/voice-pro/issues)。
- 如果出现问题，请提交一个 [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) 以改进此项目。
- 欢迎任何类型的贡献。
- 有关购买、商业伙伴关系、技术调整、投资和其他相关事宜的咨询，请通过电子邮件 (<abus.aikorea@gmail.com>) 与我们联系。
- 如果您喜欢这个项目，请给这个存储库加星标。我们将非常感谢。 ⭐⭐⭐
- 您可以在这里通过捐赠支持 Voice-Pro：

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)



## 📬 联系方式
- 电子邮件：<abus.aikorea@gmail.com>
- 主页（韩语）：<https://abuskorea.imweb.me>
- Amazon：[US](https://www.amazon.com/dp/B0DBR69JPL) | [Japan](https://www.amazon.co.jp/dp/B0DBVRJ542) | [Singapore](https://www.amazon.sg/dp/B0DCGKL8R4) | [UAE](https://www.amazon.ae/dp/B0DCGKM7FF)
- 韩国Naver：[软件](https://smartstore.naver.com/abus/products/10385660040) | [解决方案](https://smartstore.naver.com/abus/products/10298346364)

## 👍 YouTube
- [产品信息](https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [卡拉OK：流行音乐](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)

## 🙏 鸣谢
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

## ©️ 版权信息
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)   