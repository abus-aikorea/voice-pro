<!--
    title: Voice-Pro: Ultimatives KI-Sprachkonvertierungs- und mehrsprachiges Übersetzungstool
    description: Leistungsstarke KI-gestützte Webanwendung für YouTube-Videoverarbeitung, Spracherkennung, Übersetzung und mehrsprachige Text-to-Speech-Funktion
    keywords: KI-Sprachkonvertierung, YouTube-Übersetzung, Untertitelgenerierung, Sprache-zu-Text, Text-zu-Speech, Sprachklonierung, mehrsprachige Übersetzung, ElevenLabs-Alternative
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: KI-Multimedia-Verarbeitungssoftware
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, WhisperX, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">Die beste KI-Spracherkennung, Übersetzung und mehrsprachige Synchronlösung 🚀</i>
</p>

<h4 align="center">
  <a href="https://www.youtube.com/channel/UCbCBWXuVbk-OBp9T4H5JjAA">
    <img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube" style="height: 20px;">
  </a>
  <a href="https://www.amazon.de/dp/B0F1LQZ42T">
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
    <img src="images/main_page_crop.deu.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />


## 🎙️ Eine KI-gestützte Webanwendung für Spracherkennung, Übersetzung und Synchronisation


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

Voice-Pro ist eine hochmoderne Web-App, die die Erstellung von Multimedia-Inhalten revolutioniert. Sie kombiniert YouTube-Video-Downloads, Stimmseparation, Spracherkennung, Übersetzung und Text-to-Speech (TTS) in einem einzigen, leistungsstarken Tool und bietet so eine ideale Lösung für Kreative, Forscher und mehrsprachige Profis.

- 🔊 Erstklassige Spracherkennung: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- 🎤 Zero-Shot-Stimmenklonierung: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 Mehrsprachige Text-to-Speech: **Edge-TTS**, **kokoro** (Die kostenpflichtige Version enthält **Azure TTS**)
- 🎥 YouTube-Verarbeitung & Audioextraktion: **yt-dlp**
- 🌍 Sofortübersetzung für über 100 Sprachen: **Deep-Translator** (Die kostenpflichtige Version enthält **Azure Translator**)
  

Als starke Alternative zu **ElevenLabs** bietet Voice-Pro Podcastern, Entwicklern und Kreativen fortschrittliche Sprachlösungen.

## ⚠️ Bitte beachten
- **Upgrade von v2.x auf v3.x**: Nicht möglich. Wir empfehlen, den Ordner `installer_files` zu löschen und die neueste Version von `start.bat` auszuführen.
- **Upgrade von v3.x auf v3.x**: Möglich. Nach dem Herunterladen des neuesten Codes führen Sie `update.bat` aus.
- **Erstbenutzer**: Bitte lesen Sie die Installationsanweisungen unten.
- **Fehlerbehebung**: In den meisten Fällen können Probleme durch das Löschen des `installer_files`-Ordners und das anschließende Ausführen von `configure.bat` gefolgt von `start.bat` behoben werden.
- 🎁 **Anfrage für einen kostenlosen Aktivierungsschlüssel**: Bitte füllen Sie dieses [Google Formulare](https://forms.gle/anMSmsR5dH9wxE6N6) aus, um Ihren Aktivierungsschlüssel zu erhalten. Aktivierungsschlüssel sind auf einen pro E-Mail-Adresse beschränkt.
- 🏆 **Anfrage für zusätzliche Aktivierungsschlüssel**: Erstellen Sie großartige Inhalte mit Voice-Pro. Bitte teilen Sie den Link zu Ihrem Beitrag in der [![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions). Wir belohnen Ihre Beiträge gerne。


## 📰 Neuigkeiten & Verlauf

<details open>
<summary>Version 3.0</summary>

- 🔥 Die **AI Cover**-Funktion wurde entfernt.  
- 🚀 Unterstützung für **m-bain/whisperX** wurde hinzugefügt.  

</details>

<details>
<summary>Version 2.0</summary>

- 🐍 Mit Python 3.10.15, Torch 2.5.1+cu124 und Gradio 5.14.0 erstellt.  
- 🆓 Die kostenlose Testversion unterstützt Medien bis zu **60 Sekunden** Länge.  
- 🔥 Die **AI Cover**-Funktion wurde hinzugefügt.  
- 🎤 Unterstützung für **CosyVoice** und **kokoro** wurde eingeführt.  
- ⏳ Beim ersten Start wird **CozyVoice2-0.5B (9GB)** heruntergeladen, was je nach Netzwerkgeschwindigkeit über eine Stunde dauern kann.  
- 🎧 Sprachproben für das Sprachklonen werden kontinuierlich aktualisiert.  
- 📝 **spaCy** wurde für natürliche satzweise Übersetzung und TTS hinzugefügt.  
- ☁️ Die Abonnement-Version umfasst den **Microsoft Azure**-Übersetzer und TTS.  
- 🏪 Die Abonnement-Version bietet **unbegrenzte Nutzung** (keine 60-Sekunden-Beschränkung) während der Abonnementlaufzeit und kann über [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com) erworben werden.  

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
</table>



## ⭐ Hauptfunktionen

### 1. Synchronstudio
- YouTube-Video-Downloads & Audioextraktion
- Stimmtrennung mit **Demucs**
- Unterstützt über 100 Sprachen für Spracherkennung & Übersetzung

### 2. Sprachtechnologien
- **Sprache-zu-Text:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**, **WhisperX**
- **Text-zu-Sprache:** 
  - **Edge-TTS**: Über 100 Sprachen, 400+ Stimmen
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: Zero-Shot-Klonen
  - **kokoro**: Platz 2 in der HuggingFace TTS-Arena

### 3. Echtzeit-Übersetzung
- Sofortige Spracherkennung
- Mehrsprachige Übersetzung in Echtzeit
- Anpassbare Audioeingaben


## 🤖 WebUI

### `Dubbing-Studio`-Tab
- All-in-One-Hub: YouTube-Downloads, Rauschunterdrückung, Untertitel, Übersetzung, TTS
- Unterstützt alle ffmpeg-kompatiblen Formate
- Ausgabeoptionen: WAV, FLAC, MP3
- Untertitel & Erkennung für über 100 Sprachen
- TTS mit einstellbarer Geschwindigkeit, Lautstärke und Tonlage
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.deu.jpg?raw=true" alt="Mehrsprachige Sprachkonvertierung und Untertitelgenerierung WebUI-Schnittstelle"/></p>

### `Whisper-Untertitel`-Tab
- Untertitel-spezifisch: Über 90 Sprachen
- Integrierte Untertitelanzeige mit Video
- Wortweise Hervorhebung & Optionen zur Rauschunterdrückung

### `Übersetzung`-Tab
- Übersetzung in über 100 Sprachen
- Unterstützt Untertiteldateien (ASS, SSA, SRT usw.)
- Echtzeit-Spracherkennung und Übersetzung
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.jpg?raw=true" alt="WebUI für Echtzeit-Spracherkennung und Übersetzung"/></p>

### `Sprachgenerierung`-Tab
- Optionen: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- Podcasts mit Promi-Stimmen & mehrsprachige Unterstützung
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.jpg?raw=true" alt="WebUI für Podcast-Erstellung mit Stimmklonierungstechnologie"/></p>


## 🎤✨ Referenzstimme

- Bitte fordern Sie die Stimme, die Sie hinzufügen möchten, auf der Issues-Seite an. [Issues](https://github.com/abus-aikorea/voice-pro/issues/50)


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



## 💻 Systemanforderungen
- **OS:** Windows 10/11 (64-Bit) ※ Linux/Mac nicht unterstützt
- **GPU:** NVIDIA mit CUDA 12.4 (empfohlen)
- **VRAM:** 4 GB+ (8 GB+ bevorzugt)
- **RAM:** 4 GB+
- **Speicher:** Mindestens 20 GB freier Speicherplatz
- **Internet:** Erforderlich

## 📀 Installation

Mit **configure.bat** und **start.bat** lässt sich Voice-Pro einfach installieren.

### 1. Paketvorbereitung
- Laden Sie die neueste Version von [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) herunter (**Source code (zip)**)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. Installation und Ausführung
1. 🚀 **configure.bat**
   - Installiert git, ffmpeg und CUDA (bei NVIDIA-GPU)
   - Einmalige Ausführung; Internet erforderlich, kann über 1 Stunde dauern
   - Schließen Sie das Befehlsfenster nicht
2. 🚀 **start.bat**
   - Startet die Voice-Pro-WebUI
   - Bei erstmaliger Ausführung werden Abhängigkeiten installiert (kann über 1 Stunde dauern)
   - Bei Problemen **installer_files** löschen und erneut ausführen

### 3. Update
- 🚀 **update.bat**: Aktualisiert die Python-Umgebung (schneller als Neuinstallation)

### 4. Deinstallation
- Führen Sie **uninstall.bat** aus oder löschen Sie den Ordner (portable Installation)

## ❓ Nutzungstipps

#### Wenn der Browser nicht automatisch startet
- Schließen Sie das Windows-Befehlsfenster und führen Sie **start.bat** erneut aus
- Öffnen Sie den Browser manuell und geben Sie die im Befehlsfenster angezeigte Adresse ein (z. B. **http://127.0.0.1:7870**)

#### Bei einem CUDA-Out-of-Memory-Fehler
- Überprüfen Sie den GPU-Speicherstatus im Windows Task-Manager – Reiter „Leistung“
- Stellen Sie den Rauschunterdrückungslevel auf 0 oder 1 ein (Level 2 erfordert mindestens 8 GB GPU-Speicher)
- Stellen Sie den Berechnungstyp auf „int“ ein („float“ bietet bessere Qualität, benötigt aber mehr GPU-Speicher)

#### Wie kann die Untertitelqualität verbessert werden?
- Größere Whisper-Modelle tendieren zu besserer Untertitelqualität (large > medium > small > base > tiny), dies ist jedoch nicht garantiert
- Unter den Berechnungstypen bietet „float“ gute Leistung; „int“ reduziert GPU-Nutzung und erhöht die Geschwindigkeit durch Modellquantisierung, allerdings mit Leistungseinbußen
- Ein höherer Rauschunterdrückungslevel entfernt mehr Hintergrundgeräusche und nutzt nur die verbleibende Stimme für die Erkennung, garantiert aber nicht immer bessere Ergebnisse



## 🚨 Hinweis
- Dieses Repository bietet eine **kostenlose Testversion** von Voice-Pro.
- Die kostenlose Testversion von Voice-Pro ermöglicht die Verarbeitung von Medien bis zu **60 Sekunden**.
- Die Abonnementversion unterstützt Microsoft Azure TTS und Translator. Kaufen Sie es auf [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com).


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

## ☕ Beiträge

Hallo, ich bin David vom Voice-Pro-Team.
Unser Team entdeckt die besten KI-Technologien der Branche und stellt sie jedem zur einfachen und bequemen Nutzung zur Verfügung.
Wir sind ein kleines Startup in Korea, das erst seit einem Jahr existiert. Wir arbeiten hart daran, Ihnen und anderen Kreativen zu helfen, großartige Inhalte zu erstellen.

Ihre ⭐⭐⭐⭐⭐ Bewertung wäre sehr willkommen, da sie unserem Unternehmen hilft, mit Ihnen zu wachsen. Bitte helfen Sie mit, unser kleines Team zu unterstützen.

Vielen Dank,
ABUS Kundenservice

- Wenn Sie an diesem Projekt teilnehmen und uns helfen möchten, können Sie gerne ein [Issues](https://github.com/abus-aikorea/voice-pro/issues) erstellen.
- Wenn etwas schief geht, senden Sie bitte einen [Pull Requests](https://github.com/abus-aikorea/voice-pro/pulls), um dieses Projekt zu verbessern.
- Jede Art von Beitrag ist willkommen.
- Für Anfragen zu Käufen, Geschäftspartnerschaften, technischer Anpassung, Investitionen und anderen Angelegenheiten kontaktieren Sie uns bitte per E-Mail (<abus.aikorea@gmail.com>).
- Wenn Ihnen dieses Projekt gefällt, geben Sie diesem Repository bitte einen Stern. Wir würden uns sehr freuen. ⭐⭐⭐
- Sie können Voice-Pro hier mit einer Spende unterstützen:   
</a>
  <a href="https://www.buymeacoffee.com/abus">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
</a>



## 📬 Kontakt
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- Kauf der kostenpflichtigen Version: [Shopify (Global)](https://r17wvy-t2.myshopify.com/de), [Naver (Korean)](https://smartstore.naver.com/abus)



## 🙏 Danksagung
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

## ©️ Urheberrecht
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)