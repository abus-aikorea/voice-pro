<!--
    title: Voice-Pro: ابزار نهایی تبدیل صدا با هوش مصنوعی و ترجمهٔ چندزبانه
    description: وب‌اپلیکیشن قدرتمند مبتنی بر هوش مصنوعی برای پردازش ویدیوی YouTube، تشخیص گفتار، ترجمه، و تبدیل متن به گفتار با پشتیبانی چندزبانه
    keywords: تبدیل صدا با هوش مصنوعی, ترجمه YouTube, تولید زیرنویس, گفتار به متن, متن به گفتار, کلون صدا, ترجمه چندزبانه, جایگزین ElevenLabs
    author: ABUS
    version: 4.0.0
    last-updated: 2026-07-13
    product-type: AI Multimedia Processing Software
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, CosyVoice, kokoro, uv
    license: LGPL
-->



<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center" dir="rtl">بهترین راهکار تشخیص گفتار، ترجمه و دوبلهٔ چندزبانه با هوش مصنوعی 🚀</i>
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
    <img src="images/main_page_crop.eng.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />



## 🎙️ وب‌اپلیکیشن مبتنی بر هوش مصنوعی برای تشخیص گفتار، ترجمه و دوبله


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

Voice-Pro یک وب‌اپلیکیشن پیشرفته است که تولید محتوای چندرسانه‌ای را دگرگون می‌کند. دانلود ویدیوی YouTube، جداسازی صدا، تشخیص گفتار، ترجمه و تبدیل متن به گفتار (TTS) را در یک ابزار واحد برای سازندگان محتوا، پژوهشگران و حرفه‌ای‌های چندزبانه یکپارچه کرده است.
- 🔊 تشخیص گفتار سطح بالا: **Whisper**، **Faster-Whisper**، **Whisper-Timestamped**
- 🎤 کلون صدای Zero-shot: **F5-TTS**، **E2-TTS**، **CosyVoice** (از جمله **Fun-CosyVoice3** — کره‌ای و ۸ زبان دیگر)
- 📢 تبدیل متن به گفتار چندزبانه: **Edge-TTS**، **kokoro** (اختیاری: **Azure TTS** با کلیدهای خودتان — بخش Azure را در ادامه ببینید)
- 🎥 پردازش YouTube و استخراج صوت: **yt-dlp**
- 🌍 ترجمهٔ فوری برای بیش از ۱۰۰ زبان: **Deep-Translator** (اختیاری: **Azure Translator** با کلیدهای خودتان)


Voice-Pro به‌عنوان جایگزینی قدرتمند برای **ElevenLabs**، پادکسترها، توسعه‌دهندگان و سازندگان محتوا را با راهکارهای پیشرفتهٔ صوتی همراه می‌کند.

## ⚠️ توجه داشته باشید
- به‌دلیل کار روی [WeConnect](https://www.wctokyoseoul.com)، توسعه و به‌روزرسانی Voice-Pro فعلاً ممکن نیست.
- تمام کد Voice-Pro متن‌باز و کاملاً رایگان شده است. از این پس هر کسی می‌تواند آن را آزادانه توزیع و تغییر دهد.
- روی Windows با NVIDIA GPU به‌خوبی کار می‌کند. عملکرد روی Mac و Linux تأیید نشده است.
- درخواست‌های خود را در صفحات [![GitHub Issues](https://img.shields.io/github/issues/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/issues) یا [![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions) ثبت کنید.
- **رفع مشکل**: در بیشتر موارد، با حذف پوشهٔ `installer_files` و اجرای دوبارهٔ `start.bat` مشکل برطرف می‌شود (نصب مجدد تمیز فقط چند دقیقه طول می‌کشد؛ مدل‌های هوش مصنوعی دانلودشده در `model/` باقی می‌مانند). خطاها در WebUI به‌صورت اعلان قرمز (toast) نمایش داده می‌شوند و تا بستن آن‌ها روی صفحه می‌مانند.


## 📰 اخبار و تاریخچه

<details open>
<summary>version 4.0</summary>

- ⚡ **نصب‌کننده از Miniconda/pip به [uv](https://docs.astral.sh/uv/) منتقل شد** — نصب بسیار سریع‌تر و کاملاً تکرارپذیر از روی `uv.lock` نسخه‌شده. همه چیز داخل `installer_files/` می‌ماند (uv، Python، بسته‌ها).
- 🐍 ارتقای محیط اجرا: **Python 3.12، Torch 2.8.0+cu128 (پشتیبانی از سری RTX 50)، Gradio 6.20**.
- 🎙️ جدیدترین مجموعهٔ ASR: **faster-whisper 1.2.1** (large-v3-turbo، distil-large-v3.5)، openai-whisper 20250625، whisper-timestamped 1.15.9. whisperX حذف شد (پین وابستگی‌هایش مانع ارتقا به Gradio 6 می‌شد؛ تنظیمات موجود به‌صورت خودکار به faster-whisper برمی‌گردند).
- 🗣️ جدیدترین مجموعهٔ TTS: **F5-TTS 1.1.21**، kokoro 0.9.4، edge-tts 7.x، و **CosyVoice** به‌روزشده از upstream (شاخهٔ main).
- 🇰🇷 مدل TTS اختیاری جدید: **Fun-CosyVoice3-0.5B** — ۹ زبان از جمله کره‌ای، قابل انتخاب در برگهٔ CosyVoice (در اولین استفاده از مخزن رسمی HF دانلود می‌شود).
- 🧹 **دیگر نیازی به CUDA Toolkit و Visual Studio Build Tools نیست** — همهٔ وابستگی‌ها به‌صورت wheel ازپیش‌ساخته عرضه می‌شوند و PyTorch خود runtime کودا را همراه دارد.
- 🛡️ مناسب برای **رایانه‌های محدود / سازمانی**: نیازی به دسترسی Administrator نیست — اگر ffmpeg نصب نباشد، `start.bat` یک ffmpeg قابل‌حمل را خودکار دانلود می‌کند، دانلود مدل‌های Whisper پس از قطع یا خرابی انتقال خودش را ترمیم می‌کند، و ترجمه هنگام محدودیت نرخ (rate-limit) در endpoint رایگان Google با backoff دوباره تلاش می‌کند (خطوط ناموفق گزارش می‌شوند و متن اصلی حفظ می‌شود).
- 🚨 **خطاها اکنون در WebUI دیده می‌شوند**: هر شکست یک اعلان قرمز نشان می‌دهد که تا بستن آن روی صفحه می‌ماند (قبلاً هشدار ۱۰ ثانیه‌ای بود و به‌راحتی از دست می‌رفت)، همراه با پیام‌های کاربردی برای علت‌های رایج (نبود ffmpeg، ثبت‌نشدن رسانه، و غیره).
- 🖥️ رابط کاربری: مهاجرت به **Gradio 6** (چیدمان تمام‌عرض برای همهٔ برگه‌ها، نمایش ترک‌های زیرنویس مستقیماً در پخش‌کننده‌های ویدیو).
- 🧽 `uninstall.bat` دیگر به دسترسی Administrator نیاز ندارد و سیستم را اجباری راه‌اندازی مجدد نمی‌کند؛ `uninstall.bat silent` بدون پرسش اجرا می‌شود.

</details>

<details>
<summary>version 3.2</summary>

- در چند ماه گذشته روی توسعهٔ [WeConnect](https://www.wctokyoseoul.com) متمرکز بوده‌ایم و اصلاً نتوانسته‌ایم Voice-Pro را مدیریت کنیم.
- تصمیم گرفتیم تمام کد Voice-Pro را متن‌باز کنیم.
- Voice-Pro کاملاً رایگان است و از Windows، Mac و Linux پشتیبانی می‌کند.
- [WeConnect](https://www.wctokyoseoul.com) برنامه‌ای برای تبادل فرهنگی جهانی است.
- با افراد سراسر جهان برای تبادل فرهنگی معنادار، یادگیری زبان و دوستی‌های بین‌المللی در ارتباط باشید.

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

- 🪄 پشتیبانی از مدل‌های fine-tuned مربوط به **F5-TTS**
- 🌍 زبان‌های پشتیبانی‌شده
  - <img src="https://flagcdn.com/16x12/us.png" alt="United Kingdom Flag" style="vertical-align: middle;"> انگلیسی و <img src="https://flagcdn.com/16x12/cn.png" alt="China Flag" style="vertical-align: middle;"> چینی: <a href="https://huggingface.co/SWivid/F5-TTS/tree/main/F5TTS_v1_Base"> SWivid/F5-TTS_v1 </a> 
  - <img src="https://flagcdn.com/16x12/fi.png" alt="Finland Flag" style="vertical-align: middle;"> فنلاندی: <a href="https://huggingface.co/AsmoKoskinen/F5-TTS_Finnish_Model"> AsmoKoskinen/F5-TTS_Finnish_Model </a> 
  - <img src="https://flagcdn.com/16x12/fr.png" alt="France Flag" style="vertical-align: middle;"> فرانسوی: <a href="https://huggingface.co/RASPIAUDIO/F5-French-MixedSpeakers-reduced"> RASPIAUDIO/F5-French-MixedSpeakers-reduced </a> 
  - <img src="https://flagcdn.com/16x12/in.png" alt="India Flag" style="vertical-align: middle;"> هندی: <a href="https://huggingface.co/SPRINGLab/F5-Hindi-24KHz"> SPRINGLab/F5-Hindi-24KHz </a>  
  - <img src="https://flagcdn.com/16x12/it.png" alt="Italy Flag" style="vertical-align: middle;"> ایتالیایی: <a href="https://huggingface.co/alien79/F5-TTS-italian"> alien79/F5-TTS-italian </a>  
  - <img src="https://flagcdn.com/16x12/jp.png" alt="Japan Flag" style="vertical-align: middle;"> ژاپنی: <a href="https://huggingface.co/Jmica/F5TTS/tree/main/JA_21999120"> Jmica/F5TTS/JA_21999120 </a>  
  - <img src="https://flagcdn.com/16x12/ru.png" alt="Russia Flag" style="vertical-align: middle;"> روسی: <a href="https://huggingface.co/hotstone228/F5-TTS-Russian"> hotstone228/F5-TTS-Russian </a> 
  - <img src="https://flagcdn.com/16x12/es.png" alt="Spain Flag" style="vertical-align: middle;"> اسپانیایی: <a href="https://huggingface.co/jpgallegoar/F5-Spanish"> jpgallegoar/F5-Spanish </a> 
  
</details>

<details>
<summary>version 3.0</summary>

- 🔥 قابلیت **AI Cover** حذف شد.
- 🚀 پشتیبانی از **m-bain/whisperX** اضافه شد.
  
</details>

<details>
<summary>version 2.0</summary>

- 🐍 ساخته‌شده با Python 3.10.15، Torch 2.5.1+cu124 و Gradio 5.14.0.
- 🆓 نسخهٔ آزمایشی رایگان از رسانه تا طول **۶۰ ثانیه** پشتیبانی می‌کند.
- 🔥 قابلیت **AI Cover** اضافه شد.
- 🎤 پشتیبانی از **CosyVoice** و **kokoro** معرفی شد.
- ⏳ اجرای اول **CozyVoice2-0.5B (۹ گیگابایت)** را دانلود می‌کند که بسته به سرعت شبکه ممکن است بیش از یک ساعت طول بکشد.
- 🎧 نمونه‌های صدا برای کلون به‌طور پیوسته به‌روز می‌شوند.
- 📝 **spaCy** برای ترجمه و TTS طبیعی جمله‌به‌جمله اضافه شد.
- ☁️ نسخهٔ اشتراکی شامل Translator و TTS مربوط به **Microsoft Azure** است.
- 🏪 اشتراک در دورهٔ اشتراک، **استفادهٔ نامحدود** دارد (بدون محدودیت ۶۰ ثانیه) و از طریق [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com) در دسترس است.
  
</details>

## 🎥 نمایش در YouTube

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


## ⭐ امکانات اصلی

### 1. Dubbing Studio
- دانلود ویدیوی YouTube و استخراج صوت
- جداسازی صدا با **Demucs**
- پشتیبانی از بیش از ۱۰۰ زبان برای تشخیص گفتار و ترجمه

### 2. فناوری‌های گفتار
- **گفتار به متن (Speech-to-Text):** **Whisper**، **Faster-Whisper**، **Whisper-Timestamped**
- **متن به گفتار (Text-to-Speech):** 
  - **Edge-TTS**: بیش از ۱۰۰ زبان، بیش از ۴۰۰ صدا
  - **E2-TTS**، **F5-TTS**، **CosyVoice**: کلون Zero-shot
  - **kokoro**: رتبهٔ ۲ در HuggingFace TTS Arena

### 3. ترجمهٔ بلادرنگ
- تشخیص گفتار فوری
- ترجمهٔ چندزبانه در لحظه
- ورودی‌های صوتی قابل تنظیم


## 🤖 WebUI

### برگهٔ `Dubbing Studio`
- مرکز همه‌کاره: دانلود YouTube، حذف نویز، زیرنویس، ترجمه و TTS
- پشتیبانی از همهٔ فرمت‌های سازگار با ffmpeg
- گزینه‌های خروجی: WAV، FLAC، MP3
- زیرنویس و تشخیص برای بیش از ۱۰۰ زبان
- TTS با کنترل سرعت، بلندی صدا و زیروبمی (pitch)
  
<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.eng.jpg?raw=true" alt="رابط WebUI برای تبدیل صدای چندزبانه و تولید زیرنویس"/>
</p>  


### برگهٔ `Whisper Caption`
- متمرکز بر زیرنویس: بیش از ۹۰ زبان
- نمایش زیرنویس یکپارچه با ویدیو
- برجسته‌سازی در سطح واژه و گزینه‌های Denoise

### برگهٔ `Translate`
- ترجمه برای بیش از ۱۰۰ زبان
- پشتیبانی از فایل‌های زیرنویس (ASS، SSA، SRT و غیره)
- تشخیص صدا و ترجمهٔ بلادرنگ

<p align="center">
  <img style="width: 90%; height: 90%" src="images/live_translation_bbc.jpg?raw=true" alt="رابط WebUI برای تشخیص گفتار و ترجمهٔ بلادرنگ"/>
</p>  

### برگهٔ `Speech Generation`
- گزینه‌ها: **Edge-TTS**، **F5-TTS**، **CosyVoice**، **kokoro**
- پادکست با صدای افراد مشهور و پشتیبانی چندزبانه

<p align="center">
  <img style="width: 90%; height: 90%" src="images/tts_f5_multi.jpg?raw=true" alt="رابط WebUI تولید پادکست با فناوری کلون صدا"/>
</p>  



## 🎤✨ صدای مرجع

- صدایی را که می‌خواهید اضافه شود در صفحهٔ Issues درخواست کنید. [Issues](https://github.com/abus-aikorea/voice-pro/issues/50)  

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


## 💻 نیازمندی‌های سیستم
- **سیستم‌عامل:** Windows 10/11 (64-bit)، Linux، Mac (Apple Silicon)
- **GPU:** کارت گرافیک NVIDIA با درایور جدید (>= 570 توصیه می‌شود؛ سری RTX 50 پشتیبانی می‌شود). نصب CUDA Toolkit لازم نیست.
- **VRAM:** ۴ گیگابایت به بالا (۸ گیگابایت یا بیشتر ترجیح داده می‌شود)
- **RAM:** ۴ گیگابایت به بالا
- **فضای ذخیره‌سازی:** بیش از ۲۰ گیگابایت فضای خالی
- **اینترنت:** لازم است



## 📀 نصب

Voice-Pro را به‌سادگی با **configure.bat** و **start.bat** نصب کنید (در Mac/Linux از configure.sh و start.sh استفاده کنید).


### 1. دریافت بسته

  + مخزن را کلون کنید یا آخرین انتشار (**Source code (zip)**) را از  [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) دانلود کنید
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```
  

### 2. نصب و اجرا
1. 🚀 **configure.bat** (اختیاری)
   - git و ffmpeg را در سطح سیستم نصب می‌کند (دیگر به CUDA Toolkit / Visual Studio نیازی نیست)
   - به دسترسی Administrator نیاز دارد؛ یک‌بار اجرا کنید
   - دسترسی Administrator ندارید؟ از آن بگذرید — **start.bat** یک ffmpeg قابل‌حمل را خودکار دانلود می‌کند
2. 🚀 **start.bat**
   - WebUI مربوط به Voice-Pro را راه‌اندازی می‌کند
   - اجرای اول uv + Python 3.12 را دانلود می‌کند و همهٔ وابستگی‌ها را از lockfile نصب می‌کند (دقایق، نه ساعت‌ها)، سپس مدل‌های هوش مصنوعی را دانلود می‌کند (حدود ۱۰ گیگابایت — این بخش کند است)
   - GPU/CPU به‌صورت خودکار تشخیص داده می‌شود؛ با متغیر محیطی `GPU_CHOICE` (`G`=NVIDIA، `C`=CPU) یا با حذف `installer_files\gpu_choice.txt` می‌توانید آن را تغییر دهید
   - اگر مشکلی پیش آمد، پوشهٔ **installer_files** را حذف کنید و دوباره تلاش کنید

### 3. به‌روزرسانی
- 🚀 **update.bat**: محیط Python را دقیقاً با lockfile نسخه‌شده همگام می‌کند (سریع)

### 4. حذف نصب
- **uninstall.bat** را اجرا کنید یا پوشه را حذف کنید (نصب قابل‌حمل)
- نیازی به دسترسی Administrator نیست؛ برای حذف بدون پرسش، `silent` را اضافه کنید (`uninstall.bat silent`)
- فقط پوشهٔ `installer_files` حذف می‌شود — پوشه‌های `model/` و `workspace/` شما باقی می‌مانند


## 🔑 سرویس‌های Azure (اختیاری، .env)

به‌طور پیش‌فرض Voice-Pro از سرویس‌های **رایگان** استفاده می‌کند: Deep-Translator (endpoint وب رایگان Google) برای ترجمه و Edge-TTS برای سنتز گفتار. اگر اشتراک **Microsoft Azure** خودتان را دارید، می‌توانید هر دو را به APIهای Azure تغییر دهید:

1. فایل `.env.example` را در ریشهٔ پروژه به `.env` کپی کنید:
   ```bash
   copy .env.example .env     # Windows
   cp .env.example .env       # Mac/Linux
   ```
2. اطلاعات Azure خود را وارد کنید:
   ```ini
   # Azure Speech Service (TTS)
   AZURE_SPEECH_KEY=your_azure_speech_key_here
   AZURE_SPEECH_REGION=eastus

   # Azure Translator Service
   AZURE_TRANSLATOR_KEY=your_azure_translator_key_here
   AZURE_TRANSLATOR_ENDPOINT=https://your-translator-resource.cognitiveservices.azure.com/
   AZURE_TRANSLATOR_REGION=eastus
   ```
3. Voice-Pro را دوباره راه‌اندازی کنید. کلیدهای معتبر در شروع به‌صورت خودکار تشخیص داده می‌شوند — ترجمه به **Azure Translator** تغییر می‌کند و اولین برگهٔ Speech Generation به **Azure-TTS** تبدیل می‌شود.

**چه زمانی ارزش راه‌اندازی دارد؟**
- 🏢 **شبکه‌های سازمانی / محدود**: تجهیزات امنیتی اغلب endpoint رایگان `translate.google.com` را محدود یا مسدود می‌کنند و ترجمهٔ زیرنویس‌های طولانی کند یا ناموفق می‌شود. Voice-Pro با backoff دوباره تلاش می‌کند و متن اصلی خطوط ناموفق را نگه می‌دارد (هشداری با تعداد خطا می‌بینید)، اما Azure Translator کلاً این مشکل را کنار می‌زند.
- 🗣️ صداهای TTS با کیفیت و ثبات بالاتر، و محدودیت نرخ بیشتر.
- فایل `.env` را **هرگز** به کنترل نسخه commit نکنید — کلیدهای خصوصی شما در آن است.


## ❓ نکات و ترفندها

#### اگر مرورگر به‌صورت خودکار باز نشد
- پنجرهٔ Command در Windows را ببندید و دوباره start.bat را اجرا کنید.
- مرورگر را خودتان باز کنید و آدرس نمایش‌داده‌شده در پنجرهٔ Command را در نوار آدرس وارد کنید (مثلاً **http://127.0.0.1:7870**).

#### اگر خطای CUDA Out-Of-Memory رخ داد
- وضعیت حافظهٔ GPU را در Windows Task Manager، برگهٔ Performance، بررسی کنید.
- سطح Denoise را روی ۰ یا ۱ بگذارید. سطح Denoise برابر ۲ دست‌کم به ۸ گیگابایت حافظهٔ GPU نیاز دارد.
- Compute Type را روی نوع int بگذارید. نوع float کیفیت بهتری دارد، اما حافظهٔ GPU بیشتری می‌خواهد.

#### چطور کیفیت زیرنویس را بهتر کنیم؟
- کیفیت زیرنویس معمولاً با مدل‌های بزرگ‌تر Whisper بهتر می‌شود، اما همیشه این‌طور نیست. large > medium > small > base > tiny
- در میان انواع Compute Type، نوع float عملکرد خوبی دارد. نوع int با quantization مدل، مصرف GPU را کم و سرعت را زیاد می‌کند؛ در عوض عملکرد افت می‌کند.
- با افزایش سطح Denoise، صدای پس‌زمینه بیشتر حذف می‌شود و فقط صدای باقی‌مانده برای تشخیص گفتار استفاده می‌شود. همیشه نتیجهٔ بهتر را تضمین نمی‌کند.
  


## 🚨 اطلاعیه
- به‌دلیل کار روی توسعهٔ [WeConnect](https://www.wctokyoseoul.com)، فعلاً به‌روزرسانی برای Voice-Pro نخواهد بود.
- تمام کد Voice-Pro متن‌باز شده است. اکنون استفاده از آن کاملاً رایگان است.
- [WeConnect](https://www.wctokyoseoul.com) یک پلتفرم ارتباطی برای تبادل فرهنگی جهانی است.



<br />

## ⏳ پلتفرم‌های SaaS برای زیرنویس، ترجمه و TTS

جدول زیر پلتفرم‌های SaaS را فهرست می‌کند که زیرنویس، ترجمه و تبدیل متن به گفتار (TTS/دوبله) را پشتیبانی می‌کنند. هزینه‌ها برای پردازش یک ویدیوی ۶۰ دقیقه‌ای کره‌ای محاسبه شده‌اند؛ شامل تولید زیرنویس، ترجمه به انگلیسی و دوبلهٔ انگلیسی، بر اساس آخرین داده‌های قیمت در ۱۵ آوریل ۲۰۲۵.

| Platform        | Subtitling | Translation | TTS/Dubbing | Cost for 60-min Video (USD, Approx.) | Key Features                                                                 |
|-----------------|------------|-------------|-------------|-------------------------------------|------------------------------------------------------------------------------|
| **[Maestra](https://maestra.ai)**     | ✅         | ✅          | ✅          | $23.70                              | بیش از ۱۲۵ زبان، زیرنویس بلادرنگ، استخراج کلیدواژهٔ SEO، آزمایش رایگان ۱۵ دقیقه‌ای. |
| **[Kapwing](https://www.kapwing.com)**     | ✅         | ✅          | ✅          | $30~$40 (Pro plan, per minute)     | زیرنویس هوش مصنوعی، ترجمه به بیش از ۱۰۰ زبان، دوبله با هم‌زمانی لب، سطح رایگان.   |
| **[VEED.IO](https://www.veed.io)**     | ✅         | ✅          | ❌          | $24~$36 (Pro plan, partial)        | زیرنویس با دقت ۹۹٫۹٪، کپشن بهینه‌شده برای Instagram، ویرایشگر ساده.     |
| **[HappyScribe](https://happyscribe.com)** | ✅         | ✅          | ✅          | $36~$48 (Pay-as-you-go)            | بیش از ۱۲۰ زبان، ویراستاری حرفه‌ای، امن، پیاده‌سازی جلسات.     |
| **[Sonix](https://sonix.ai)**       | ✅         | ✅          | ✅          | $30~$40 (Standard plan)            | بیش از ۵۴ زبان، ۳۰ دقیقه پیاده‌سازی رایگان، یکپارچگی با YouTube/Zoom.           |
| **[Descript](https://descript.com)**    | ✅         | ✅          | ✅          | $36~$48 (Creator plan)             | ویرایش مبتنی بر متن، Overdub TTS، حذف کلمات پرکننده، ۱ ساعت پیاده‌سازی رایگان. |
| **[AppTek](https://apptek.ai)**      | ✅         | ✅          | ✅          | Custom pricing (Contact)            | متمرکز بر رسانه، مدل‌های سفارشی، تولید metadata، Workbench ابری.     |
| **[Transkriptor](https://transkriptor.com)**| ✅         | ✅          | ❌          | $12~$18 (Pay-as-you-go)            | بیش از ۱۰۰ زبان، پیاده‌سازی از لینک YouTube، دقت ۹۹٪، ویرایشگر ساده.      |

### جزئیات محاسبهٔ هزینه
- **[Maestra](https://maestra.ai/)**: طرح Premium (۱۵۸ دلار در ماه، ۱۲۰۰ اعتبار). ویدیوی ۶۰ دقیقه‌ای: ۶۰ اعتبار (زیرنویس) + ۶۰ اعتبار (ترجمه) + ۶۰ اعتبار (دوبله) = ۱۸۰ اعتبار. هزینه = (180/1200) * $158 = $23.70.[](https://maestra.ai/pricing)
- **[Kapwing](https://www.kapwing.com)**: طرح Pro (حدود ۲۴ دلار در ماه، دقایق محدود). برآورد ۰٫۵۰ تا ۰٫۶۷ دلار در دقیقه برای زیرنویس+ترجمه+دوبله. هزینهٔ ۶۰ دقیقه: ۳۰ تا ۴۰ دلار. قیمت دقیق نیاز به تأیید دارد.
- **[VEED.IO](https://www.veed.io)**: طرح Pro (حدود ۲۴ دلار در ماه). زیرنویس+ترجمه حدود ۰٫۴۰ تا ۰٫۶۰ دلار در دقیقه. بدون TTS، پردازش ناقص. هزینهٔ ۶۰ دقیقه: ۲۴ تا ۳۶ دلار. در [veed.io](https://veed.io) تأیید کنید.
- **[HappyScribe](https://happyscribe.com)**: پرداخت به‌ازای مصرف (حدود ۰٫۲۰ دلار در دقیقه پیاده‌سازی، ۰٫۲۰ ترجمه، ۰٫۲۰ دوبله). هزینهٔ ۶۰ دقیقه: ۳۶ تا ۴۸ دلار (با فرض خدمات ترکیبی). در [happyscribe.com](https://happyscribe.com) تأیید کنید.
- **[Sonix](https://sonix.ai)**: طرح Standard (حدود ۱۰ دلار در ساعت پیاده‌سازی، به‌اضافه ترجمه/دوبله). برآورد مجموع ۰٫۵۰ تا ۰٫۶۷ دلار در دقیقه. هزینهٔ ۶۰ دقیقه: ۳۰ تا ۴۰ دلار. در [sonix.ai](https://sonix.ai) تأیید کنید.
- **[Descript](https://descript.com)**: طرح Creator (حدود ۲۴ دلار در ماه، ساعات محدود). برآورد ۰٫۶۰ تا ۰٫۸۰ دلار در دقیقه برای زیرنویس+ترجمه+دوبله. هزینهٔ ۶۰ دقیقه: ۳۶ تا ۴۸ دلار. در [descript.com](https://descript.com) تأیید کنید.
- **[AppTek](https://apptek.ai)**: قیمت سفارشی برای سازمان. نرخ عمومی به‌ازای دقیقه اعلام نشده. برای برآورد با [apptek.ai](https://apptek.ai) تماس بگیرید.
- **[Transkriptor](https://transkriptor.com)**: پرداخت به‌ازای مصرف (۰٫۰۵ تا ۰٫۱۰ دلار در دقیقه پیاده‌سازی، مشابه برای ترجمه). بدون TTS، پردازش ناقص. هزینهٔ ۶۰ دقیقه: ۱۲ تا ۱۸ دلار. در [transkriptor.com](https://transkriptor.com) تأیید کنید.

### یادداشت‌ها
- **هزینه برای ویدیوی ۶۰ دقیقه‌ای**: هزینه‌ها تقریبی‌اند و فرض می‌کنند یک ویدیوی کره‌ای ۶۰ دقیقه‌ای برای زیرنویس، ترجمه به انگلیسی و دوبلهٔ انگلیسی (در صورت وجود) پردازش شود. پلتفرم‌های بدون TTS (مثلاً VEED.IO و Transkriptor) هزینهٔ پردازش ناقص را نشان می‌دهند.
- **پشتیبانی زبان**: بیشتر پلتفرم‌ها از کره‌ای و انگلیسی پشتیبانی می‌کنند. در دسترس بودن زبان خاص را در وب‌سایت آن‌ها بررسی کنید.
- **موارد استفاده**:
  - رسانه / سرگرمی: AppTek، Maestra
  - شبکه‌های اجتماعی: Kapwing، VEED.IO
  - پادکست / مصاحبه: Sonix، Descript
  - آموزش الکترونیکی / محتوای جهانی: Transkriptor، HappyScribe
- **به‌روزرسانی قیمت**: قیمت‌ها ممکن است به‌دلیل تغییر طرح یا تخفیف فرق کند. جزئیات به‌روز را در وب‌سایت رسمی ببینید.
- برای مشارکت یا پیشنهاد مورد استفادهٔ خاص، یک issue باز کنید یا یک pull request در همین مخزن بفرستید.

<br />

## ☕ مشارکت

سلام، من دیوید از تیم Voice-Pro هستم.
تیم ما بهترین فناوری‌های هوش مصنوعی صنعت را پیدا می‌کند و آن‌ها را به‌شکلی ساده و راحت در اختیار همه می‌گذارد.
یک استارتاپ کوچک در کره هستیم که تازه یک سال از آغاز کارمان می‌گذرد. سخت می‌کوشیم تا شما و دیگر سازندگان محتوا بتوانید محتوای عالی تولید کنید.

اگر نظر ⭐⭐⭐⭐⭐ بگذارید بسیار سپاسگزار می‌شویم؛ این کار به رشد کسب‌وکار ما در کنار شما کمک می‌کند. لطفاً از تیم کوچک ما حمایت کنید.

با تشکر،
خدمات مشتریان ABUS

- اگر می‌خواهید در این پروژه مشارکت کنید و کمک کنید، یک [Issues](https://github.com/abus-aikorea/voice-pro/issues) بسازید.
- اگر مشکلی پیش آمد، برای بهبود پروژه یک [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) بفرستید.
- هر نوع مشارکتی خوش‌آمد است.
- برای پرسش‌های مربوط به خرید، همکاری تجاری، تنظیم فنی، سرمایه‌گذاری و موارد دیگر، با ایمیل تماس بگیرید (<abus.aikorea@gmail.com>).
- اگر این پروژه را می‌پسندید، به این مخزن ستاره بدهید. بسیار ممنون می‌شویم. ⭐⭐⭐
- می‌توانید از Voice-Pro با کمک مالی در اینجا حمایت کنید:    
</a>
  <a href="https://www.buymeacoffee.com/abus">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
</a>



## 📬 تماس
- ایمیل: <abus.aikorea@gmail.com>
- صفحهٔ اصلی (کره‌ای): <https://www.wctokyoseoul.com>

## 🙏 اعتبارها
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



## ©️ حق‌نشر
  <img src="images/ABUS-logo.jpg" width="100" height="100"> از [ABUS](https://www.wctokyoseoul.com)
