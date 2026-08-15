<!--
    title: Voice-Pro: Ultimatives KI-Sprachkonvertierungs- und mehrsprachiges Übersetzungstool
    description: Leistungsstarke KI-gestützte Webanwendung für YouTube-Videoverarbeitung, Spracherkennung, Übersetzung und mehrsprachige Text-to-Speech-Funktion
    keywords: KI-Sprachkonvertierung, YouTube-Übersetzung, Untertitelgenerierung, Sprache-zu-Text, Text-zu-Speech, Sprachklonierung, mehrsprachige Übersetzung, ElevenLabs-Alternative
    author: ABUS
    version: 4.0.0
    last-updated: 2026-07-13
    product-type: KI-Multimedia-Verarbeitungssoftware
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, CosyVoice, kokoro, uv
    license: LGPL
-->

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">Die beste KI-Spracherkennung, Übersetzung und mehrsprachige Synchronlösung 🚀</i>
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
  </a> ∙ 
  <a href="README.fas.md">
    <img src="https://flagcdn.com/16x12/ir.png" alt="Iran Flag" style="vertical-align: middle;"> فارسی
  </a>
</p>

Voice-Pro ist eine hochmoderne Web-App, die die Erstellung von Multimedia-Inhalten revolutioniert. Sie kombiniert YouTube-Video-Downloads, Stimmseparation, Spracherkennung, Übersetzung und Text-to-Speech (TTS) in einem einzigen, leistungsstarken Tool und bietet so eine ideale Lösung für Kreative, Forscher und mehrsprachige Profis.

- 🔊 Erstklassige Spracherkennung: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 Zero-Shot-Stimmenklonierung: **F5-TTS**, **E2-TTS**, **CosyVoice** (inkl. **Fun-CosyVoice3** — Koreanisch und 8 weitere Sprachen)
- 📢 Mehrsprachige Text-to-Speech: **Edge-TTS**, **kokoro** (optional **Azure TTS** mit eigenen Schlüsseln — siehe den Abschnitt „Azure-Dienste“ weiter unten)
- 🎥 YouTube-Verarbeitung & Audioextraktion: **yt-dlp**
- 🌍 Sofortübersetzung für über 100 Sprachen: **Deep-Translator** (optional **Azure Translator** mit eigenen Schlüsseln)
  

Als starke Alternative zu **ElevenLabs** bietet Voice-Pro Podcastern, Entwicklern und Kreativen fortschrittliche Sprachlösungen.

## ⚠️ Bitte beachten
- Aufgrund der [WeConnect](https://www.wctokyoseoul.com)-Entwicklungsarbeit sind Voice-Pro-Entwicklung und Updates vorerst nicht möglich.
- Wir haben den gesamten Voice-Pro-Code als Open Source veröffentlicht und vollständig kostenlos gemacht. Voice-Pro kann jetzt von jedem frei verteilt und modifiziert werden.
- Es funktioniert gut unter Windows mit NVIDIA GPU. Der Betrieb unter Mac und Linux wurde nicht überprüft.
- Bitte hinterlassen Sie Ihre Anfragen auf den [![GitHub Issues](https://img.shields.io/github/issues/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/issues)- oder [![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions)-Seiten.
- **Fehlerbehebung**: In den meisten Fällen können Probleme durch das Löschen des `installer_files`-Ordners und das anschließende erneute Ausführen von `start.bat` behoben werden (eine saubere Neuinstallation dauert nur wenige Minuten; heruntergeladene KI-Modelle in `model/` bleiben erhalten). Fehler werden in der WebUI als rote Toast-Meldungen angezeigt, die sichtbar bleiben, bis sie geschlossen werden.



## 📰 Neuigkeiten & Verlauf

<details open>
<summary>version 4.0</summary>

- ⚡ **Installer von Miniconda/pip auf [uv](https://docs.astral.sh/uv/) migriert** — deutlich schnellere, vollständig reproduzierbare Installationen aus einer eingecheckten `uv.lock`. Alles bleibt innerhalb von `installer_files/` (uv, Python, Pakete).
- 🐍 Laufzeitumgebung aktualisiert: **Python 3.12, Torch 2.8.0+cu128 (RTX 50-Serie unterstützt), Gradio 6.20**.
- 🎙️ Neuester ASR-Stack: **faster-whisper 1.2.1** (large-v3-turbo, distil-large-v3.5), openai-whisper 20250625, whisper-timestamped 1.15.9. whisperX wurde entfernt (seine Abhängigkeits-Pins blockierten das Gradio-6-Upgrade; bestehende Konfigurationen fallen auf faster-whisper zurück).
- 🗣️ Neuester TTS-Stack: **F5-TTS 1.1.21**, kokoro 0.9.4, edge-tts 7.x sowie neu übernommenes **CosyVoice** (Upstream main).
- 🇰🇷 Neues optionales TTS-Modell: **Fun-CosyVoice3-0.5B** — 9 Sprachen einschließlich Koreanisch, auswählbar im CosyVoice-Tab (wird bei der ersten Verwendung aus dem offiziellen HF-Repository heruntergeladen).
- 🧹 CUDA Toolkit und Visual Studio Build Tools sind **nicht mehr erforderlich** — alle Abhängigkeiten werden als vorgefertigte Wheels ausgeliefert, und PyTorch bringt die CUDA-Laufzeitumgebung mit.
- 🛡️ Geeignet für **eingeschränkte PCs / Firmen-PCs**: keine Administratorrechte nötig — `start.bat` lädt automatisch ein portables **ffmpeg** herunter, falls keines installiert ist, Whisper-Modell-Downloads reparieren sich nach unterbrochenen/beschädigten Übertragungen selbst, und die Übersetzung wiederholt Anfragen automatisch mit Backoff, wenn das Netzwerk den kostenlosen Google-Endpunkt drosselt (fehlgeschlagene Zeilen werden gemeldet, die Originale bleiben erhalten).
- 🚨 **Fehler sind jetzt in der WebUI sichtbar**: Jeder Fehlschlag zeigt eine rote Fehler-Toast-Meldung, die auf dem Bildschirm bleibt, bis Sie sie schließen (zuvor eine 10-sekündige Warnung, die leicht zu übersehen war), mit hilfreichen Hinweisen zu häufigen Ursachen (fehlendes ffmpeg, keine Medien registriert usw.).
- 🖥️ UI: Migration auf **Gradio 6** (Layout in voller Breite für alle Tabs, Untertitelspuren werden direkt in den Videoplayern angezeigt).
- 🧽 `uninstall.bat` benötigt keine Administratorrechte mehr und erzwingt keinen Neustart mehr; `uninstall.bat silent` läuft unbeaufsichtigt.

</details>

<details>
<summary>version 3.2</summary>

- Wir haben uns in den letzten Monaten auf die Entwicklung von [WeConnect](https://www.wctokyoseoul.com) konzentriert und konnten Voice-Pro überhaupt nicht verwalten. 
- Wir haben beschlossen, den gesamten Voice-Pro-Code zu öffnen.
- Voice-Pro ist vollständig kostenlos und unterstützt Windows, Mac, Linux.
- [WeConnect](https://www.wctokyoseoul.com) ist eine Anwendung für den globalen Kulturaustausch.
- Verbinden Sie sich mit Menschen aus aller Welt für bedeutungsvolle Kulturaustausche, Sprachenlernen und internationale Freundschaften.

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

- 🪄 Unterstützung für feinabgestimmte Modelle von **F5-TTS**
- 🌍 Unterstützte Sprachen
  - <img src="https://flagcdn.com/16x12/us.png" alt="United Kingdom Flag" style="vertical-align: middle;"> English & <img src="https://flagcdn.com/16x12/cn.png" alt="China Flag" style="vertical-align: middle;"> Chinese: <a href="https://huggingface.co/SWivid/F5-TTS/tree/main/F5TTS_v1_Base"> SWivid/F5-TTS_v1 </a> 
  - <img src="https://flagcdn.com/16x12/fi.png" alt="Spain Flag" style="vertical-align: middle;"> Finnish: <a href="https://huggingface.co/AsmoKoskinen/F5-TTS_Finnish_Model"> AsmoKoskinen/F5-TTS_Finnish_Model </a> 
  - <img src="https://flagcdn.com/16x12/fr.png" alt="Spain Flag" style="vertical-align: middle;"> French: <a href="https://huggingface.co/RASPIAUDIO/F5-French-MixedSpeakers-reduced"> RASPIAUDIO/F5-French-MixedSpeakers-reduced </a> 
  - <img src="https://flagcdn.com/16x12/in.png" alt="Spain Flag" style="vertical-align: middle;"> Hindi: <a href="https://huggingface.co/SPRINGLab/F5-Hindi-24KHz"> SPRINGLab/F5-Hindi-24KHz </a>  
  - <img src="https://flagcdn.com/16x12/it.png" alt="Spain Flag" style="vertical-align: middle;"> Italian: <a href="https://huggingface.co/alien79/F5-TTS-italian"> alien79/F5-TTS-italian </a>  
  - <img src="https://flagcdn.com/16x12/jp.png" alt="Spain Flag" style="vertical-align: middle;"> Japanese: <a href="https://huggingface.co/Jmica/F5TTS/tree/main/JA_21999120"> Jmica/F5TTS/JA_21999120 </a>  
  - <img src="https://flagcdn.com/16x12/ru.png" alt="Spain Flag" style="vertical-align: middle;"> Russian: <a href="https://huggingface.co/hotstone228/F5-TTS-Russian"> hotstone228/F5-TTS-Russian </a> 
  - <img src="https://flagcdn.com/16x12/es.png" alt="Spain Flag" style="vertical-align: middle;"> Spanish: <a href="https://huggingface.co/jpgallegoar/F5-Spanish"> jpgallegoar/F5-Spanish </a> 
  
</details>

<details>
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



## ⭐ Hauptfunktionen

### 1. Synchronstudio
- YouTube-Video-Downloads & Audioextraktion
- Stimmtrennung mit **Demucs**
- Unterstützt über 100 Sprachen für Spracherkennung & Übersetzung

### 2. Sprachtechnologien
- **Sprache-zu-Text:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
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
- **OS:** Windows 10/11 (64-Bit), Linux, Mac (Apple Silicon)
- **GPU:** NVIDIA GPU mit aktuellem Treiber (>= 570 empfohlen; RTX 50-Serie unterstützt). Eine Installation des CUDA Toolkit ist NICHT erforderlich.
- **VRAM:** 4 GB+ (8 GB+ bevorzugt)
- **RAM:** 4 GB+
- **Speicher:** Mindestens 20 GB freier Speicherplatz
- **Internet:** Erforderlich

## 📀 Installation

Mit **configure.bat** und **start.bat** lässt sich Voice-Pro einfach installieren (auf Mac/Linux verwenden Sie configure.sh und start.sh).

### 1. Paketvorbereitung
- Laden Sie die neueste Version von [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) herunter (**Source code (zip)**)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. Installation und Ausführung
1. 🚀 **configure.bat** (optional)
   - Richtet git und ffmpeg systemweit ein (CUDA Toolkit / Visual Studio werden nicht mehr benötigt)
   - Erfordert Administratorrechte; einmalige Ausführung
   - Keine Administratorrechte? Überspringen Sie diesen Schritt — **start.bat** lädt automatisch ein portables ffmpeg herunter
2. 🚀 **start.bat**
   - Startet die Voice-Pro-WebUI
   - Beim ersten Start werden uv + Python 3.12 heruntergeladen und alle Abhängigkeiten aus dem Lockfile installiert (Minuten, nicht Stunden), anschließend werden die KI-Modelle heruntergeladen (~10GB — dies ist der langsame Teil)
   - GPU/CPU wird automatisch erkannt; übersteuern Sie dies mit der Umgebungsvariable `GPU_CHOICE` (`G`=NVIDIA, `C`=CPU) oder durch Löschen von `installer_files\gpu_choice.txt`
   - Bei Problemen **installer_files** löschen und erneut versuchen

### 3. Update
- 🚀 **update.bat**: Synchronisiert die Python-Umgebung exakt mit dem eingecheckten Lockfile (schnell)

### 4. Deinstallation
- Führen Sie **uninstall.bat** aus oder löschen Sie den Ordner (portable Installation)
- Keine Administratorrechte erforderlich; fügen Sie `silent` für eine unbeaufsichtigte Entfernung hinzu (`uninstall.bat silent`)
- Nur der Ordner `installer_files` wird entfernt — Ihre Ordner `model/` und `workspace/` bleiben erhalten

## 🔑 Azure-Dienste (optional, .env)

Standardmäßig verwendet Voice-Pro **kostenlose** Dienste: Deep-Translator (der kostenlose Web-Endpunkt von Google) für die Übersetzung und Edge-TTS für die Sprachsynthese. Wenn Sie über ein eigenes **Microsoft Azure**-Abonnement verfügen, können Sie beide auf die Azure-APIs umstellen:

1. Kopieren Sie `.env.example` nach `.env` im Projektstammverzeichnis:
   ```bash
   copy .env.example .env     # Windows
   cp .env.example .env       # Mac/Linux
   ```
2. Tragen Sie Ihre Azure-Zugangsdaten ein:
   ```ini
   # Azure Speech Service (TTS)
   AZURE_SPEECH_KEY=your_azure_speech_key_here
   AZURE_SPEECH_REGION=eastus

   # Azure Translator Service
   AZURE_TRANSLATOR_KEY=your_azure_translator_key_here
   AZURE_TRANSLATOR_ENDPOINT=https://your-translator-resource.cognitiveservices.azure.com/
   AZURE_TRANSLATOR_REGION=eastus
   ```
3. Starten Sie Voice-Pro neu. Gültige Schlüssel werden beim Start automatisch erkannt — die Übersetzung wechselt zu **Azure Translator**, und der erste Sprachgenerierung-Tab wird zu **Azure-TTS**.

**Wann lohnt sich die Einrichtung?**
- 🏢 **Firmennetzwerke / eingeschränkte Netzwerke**: Sicherheits-Appliances drosseln oder blockieren häufig den kostenlosen `translate.google.com`-Endpunkt, wodurch lange Untertitelübersetzungen verlangsamt werden oder fehlschlagen. Voice-Pro wiederholt Anfragen mit Backoff und behält bei fehlgeschlagenen Zeilen den Originaltext bei (Sie sehen eine Warnung mit der Anzahl der Fehlschläge), aber Azure Translator vermeidet das Problem vollständig.
- 🗣️ Hochwertigere/konsistentere TTS-Stimmen und höhere Ratenlimits.
- Committen Sie `.env` **NICHT** in die Versionsverwaltung — die Datei enthält Ihre privaten Schlüssel.

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
- Aufgrund der [WeConnect](https://www.wctokyoseoul.com)-Entwicklungsarbeit wird es vorerst keine Voice-Pro-Updates geben.
- Der gesamte Voice-Pro-Code wurde als Open Source veröffentlicht. Er kann jetzt vollständig kostenlos verwendet werden.
- [WeConnect](https://www.wctokyoseoul.com) ist eine Kommunikationsplattform für den globalen Kulturaustausch.


<br />

## ⏳ SaaS-Plattformen für Untertitelung, Übersetzung und TTS

Die folgende Tabelle listet SaaS-Plattformen auf, die Untertitelung, Übersetzung und Text-to-Speech (TTS/Synchronisation) unterstützen. Die Kosten wurden basierend auf den neuesten verfügbaren Preisdaten vom 15. April 2025 berechnet und beinhalten die Verarbeitung eines 60-minütigen koreanischen Videos mit Untertitelgenerierung, englischer Übersetzung und englischer Synchronisation.

| Plattform | Untertitelung | Übersetzung | TTS/Synchronisation | Kosten für 60-min Video (USD, ca.) | Hauptmerkmale |
| --- | --- | --- | --- | --- | --- |
| **[Maestra](https://maestra.ai)** | ✅ | ✅ | ✅ | $23.70 | Über 125 Sprachen, Echtzeit-Untertitel, SEO-Keyword-Extraktion, 15-min kostenlose Testversion. |
| **[Kapwing](https://www.kapwing.com)** | ✅ | ✅ | ✅ | $30\~$40 (Pro-Plan, pro Minute) | KI-Untertitel, Übersetzung in über 100 Sprachen, automatische Lip-Sync-Synchronisation, kostenloser Tarif. |
| **[VEED.IO](https://www.veed.io)** | ✅ | ✅ | ❌ | $24\~$36 (Pro-Plan, teilweise) | 99,9 % genaue Untertitel, Instagram-optimierte Untertitel, intuitiver Editor. |
| **[HappyScribe](https://happyscribe.com)** | ✅ | ✅ | ✅ | $36\~$48 (Pay-as-you-go) | Über 120 Sprachen, professionelle Korrekturoption, sicher, Transkription von Meetings. |
| **[Sonix](https://sonix.ai)** | ✅ | ✅ | ✅ | $30\~$40 (Standard-Plan) | Über 54 Sprachen, 30-min kostenlose Transkription, YouTube/Zoom-Integration. |
| **[Descript](https://descript.com)** | ✅ | ✅ | ✅ | $36\~$48 (Creator-Plan) | Textbasierte Bearbeitung, Overdub TTS, Entfernung von Füllwörtern, 1-Stunde kostenlose Transkription. |
| **[AppTek](https://apptek.ai)** | ✅ | ✅ | ✅ | Individuelle Preisgestaltung (Kontakt) | Medienfokussiert, individuelle Modelle, Metadatengenerierung, cloudbasierte Workbench. |
| **[Transkriptor](https://transkriptor.com)** | ✅ | ✅ | ❌ | $12\~$18 (Pay-as-you-go) | Über 100 Sprachen, YouTube-Link-Transkription, 99 % Genauigkeit, einfacher Editor. |

### Details zur Kostenberechnung

- **[Maestra](https://maestra.ai)**: Premium-Plan ($158/Monat, 1200 Credits). 60-min Video: 60 Credits (Untertitel) + 60 Credits (Übersetzung) + 60 Credits (Synchronisation) = 180 Credits. Kosten = (180/1200) \* $158 = $23.70.
- **[Kapwing](https://www.kapwing.com)**: Pro-Plan (\~$24/Monat, begrenzte Minuten). Geschätzt $0.50\~$0.67/Minute für Untertitel+Übersetzung+Synchronisation (basierend auf Preistrends). 60-min Kosten: $30\~$40. Exakte Preise erfordern Bestätigung.
- **[VEED.IO](https://www.veed.io)**: Pro-Plan (\~$24/Monat). Untertitel+Übersetzung geschätzt $0.40\~$0.60/Minute. Kein TTS, daher teilweise Verarbeitung. 60-min Kosten: $24\~$36. Bestätigen Sie auf veed.io.
- **[HappyScribe](https://happyscribe.com)**: Pay-as-you-go (\~$0.20/Minute Transkription, $0.20 Übersetzung, $0.20 Synchronisation). 60-min Kosten: $36\~$48 (unter Annahme kombinierter Dienste). Bestätigen Sie auf happyscribe.com.
- **[Sonix](https://sonix.ai)**: Standard-Plan (\~$10/Stunde Transkription, zusätzlich für Übersetzung/Synchronisation). Geschätzt $0.50\~$0.67/Minute gesamt. 60-min Kosten: $30\~$40. Bestätigen Sie auf sonix.ai.
- **[Descript](https://descript.com)**: Creator-Plan (\~$24/Monat, begrenzte Stunden). Geschätzt $0.60\~$0.80/Minute für Untertitel+Übersetzung+Synchronisation. 60-min Kosten: $36\~$48. Bestätigen Sie auf descript.com.
- **[AppTek](https://apptek.ai)**: Individuelle Preisgestaltung für Unternehmen. Keine öffentlichen Minutenpreise. Kontaktieren Sie apptek.ai für Angebote.
- **[Transkriptor](https://transkriptor.com)**: Pay-as-you-go ($0.05\~$0.10/Minute Transkription, ähnlich für Übersetzung). Kein TTS, daher teilweise Verarbeitung. 60-min Kosten: $12\~$18. Bestätigen Sie auf transkriptor.com.

### Hinweise

- **Kosten für 60-min Video**: Die Kosten sind Näherungswerte und basieren auf der Verarbeitung eines 60-minütigen koreanischen Videos für Untertitel, englische Übersetzung und englische Synchronisation (falls verfügbar). Plattformen ohne TTS (z. B. VEED.IO, Transkriptor) berücksichtigen teilweise Verarbeitungskosten.
- **Sprachunterstützung**: Die meisten Plattformen unterstützen Koreanisch und Englisch. Überprüfen Sie die Verfügbarkeit spezifischer Sprachen auf den jeweiligen Websites.
- **Anwendungsfälle**:
  - Medien/Unterhaltung: AppTek, Maestra
  - Soziale Medien: Kapwing, VEED.IO
  - Podcasts/Interviews: Sonix, Descript
  - E-Learning/globale Inhalte: Transkriptor, HappyScribe
- **Preisaktualisierungen**: Preise können aufgrund von Planänderungen oder Aktionen variieren. Überprüfen Sie die offiziellen Websites für aktuelle Details.
- Für Beiträge oder Empfehlungen zu spezifischen Anwendungsfällen öffnen Sie ein Issue oder reichen Sie einen Pull Request in diesem Repository ein!

<br />

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
- Homepage (Korean): <https://www.wctokyoseoul.com>



## 🙏 Danksagung
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

## ©️ Urheberrecht
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://www.wctokyoseoul.com)