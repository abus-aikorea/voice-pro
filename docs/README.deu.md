<!--
    title: Voice-Pro: Ultimate AI Voice Conversion and Multilingual Translation Tool
    description: Powerful AI-powered web application for YouTube video processing, speech recognition, translation, and text-to-speech with multilingual support
    keywords: AI voice conversion, YouTube translation, subtitle generation, speech-to-text, text-to-speech, voice cloning, multilingual translation, ElevenLabs Alternative 
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: AI Multimedia Processing Software
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

# Voice-Pro: Das ultimative Tool für KI-gestützte Sprachkonvertierung und mehrsprachige Übersetzung 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md) ∙ [Deutsch](README.deu.md) ∙ [Español](README.spa.md) ∙ [Português](README.por.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

## 🎙️ Fortschrittliches KI-basiertes Multimedia-Verarbeitungstool | Whisper-Sprach erkennungs-WebUI

Voice-Pro ist eine hochmoderne Web-App, die die Erstellung von Multimedia-Inhalten revolutioniert. Sie kombiniert YouTube-Video-Downloads, Stimmseparation, Spracherkennung, Übersetzung und Text-to-Speech (TTS) in einem einzigen, leistungsstarken Tool und bietet so eine ideale Lösung für Kreative, Forscher und mehrsprachige Profis.

- 🔊 Erstklassige Spracherkennung: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 Zero-Shot-Stimmklonierung: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 Mehrsprachige Text-to-Speech: **Edge-TTS**, **kokoro**
- 🎥 YouTube-Verarbeitung & Audioextraktion: **yt-dlp**
- 🌍 Sofortige Übersetzung in über 100 Sprachen: **Deep-Translator**
- 🔇 Professionelle Gesangsisolierung: **UVR5**
- 🔥 AI-Cover-Erstellung: **RVC**

Als starke Alternative zu **ElevenLabs** bietet Voice-Pro Podcastern, Entwicklern und Kreativen fortschrittliche Sprachlösungen.

## ⚠️ Hinweise
- Voice-Pro wurde auf **v2.x** aktualisiert (Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0)
- 🆓 Die kostenlose Testversion unterstützt bis zu **60 Sekunden** Medienverarbeitung
- 🔥 Neue **AI-Cover**-Funktion hinzugefügt
- 🎤 Unterstützung für **CosyVoice** und **kokoro** hinzugefügt
- ⏳ Beim ersten Start wird **CozyVoice2-0.5B (9 GB)** heruntergeladen. Je nach Netzwerkgeschwindigkeit kann dies über eine Stunde dauern
- 🎧 Stimmproben für die Klonierung werden kontinuierlich aktualisiert
- **Anleitung:**
  - **Bestehende Nutzer:** Führen Sie **update.bat** aus, um auf v2.0.x zu aktualisieren
  - **Neue Nutzer:** Siehe Installationsabschnitt unten — führen Sie **configure.bat** aus, dann **start.bat**

## 🚄 Demos

### `Dubbing-Studio`-Tab: Transkription, Übersetzung & TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c" width="100%" style="max-width: 720px;" controls muted aria-describedby="studio-demo-description"></video>
  <p id="studio-demo-description">Demo des umfassenden Medienverarbeitungs-Workflows im Studio-Tab: Zeigt einen durchgehenden Prozess von YouTube-Video-Download über KI-basierte Stimmseparation, automatische Whisper-Untertitel, mehrsprachige Übersetzung bis hin zu professioneller Synchronisation mit F5-TTS.</p>
</div>

### `F5-TTS-Multi`-Tab: Podcast-Erstellung
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls muted aria-describedby="tts-demo-description"></video>
  <p id="tts-demo-description">Demo der innovativen KI-Stimmklonierung von F5-TTS: Präsentiert fortschrittliche Sprachkonvertierungstechnologie, die die tatsächlichen Stimmen von Mark Zuckerberg und Elon Musk präzise nachahmt, um völlig neue Inhalte zu erstellen.</p>
</div>

### `AI-Cover`-Tab
<div aria-labelledby="ai-cover-description">
  <video src="https://github.com/user-attachments/assets/88a47ab1-a18b-4779-97c8-7c1da84f5fc3" width="100%" style="max-width: 720px;" controls muted aria-describedby="ai-cover-description"></video>
  <p id="ai-cover-description">Erstellt eine Trump-Version von IUs „Cupid“, Kim Kwang-seoks „Ich vermisse dich“ und „Brief eines Gefreiten“.</p>
</div>

### `Live-Übersetzung`-Tab: Echtzeit-Erkennung und Übersetzung
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls muted aria-describedby="translate-demo-description"></video>
  <p id="translate-demo-description">Demo der Echtzeit-Mehrsprachigkeitsfunktion: Zeigt einen innovativen Prozess der mehrsprachigen Medienverarbeitung, der BBC-Nachrichteninhalte sofort erfasst, Untertitel in Echtzeit generiert und diese direkt in andere Sprachen übersetzt.</p>
</div>

## ⭐ Hauptfunktionen

### 1. Dubbing-Studio
- YouTube-Video-Downloads & Audioextraktion
- Stimmseparation mit **MDX-Net** und **Demucs**
- Unterstützung für Spracherkennung und Übersetzung in über 100 Sprachen

### 2. Sprachtechnologien
- **Sprache-zu-Text:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- **Text-zu-Sprache:**
  - **Edge-TTS**: Über 100 Sprachen, mehr als 400 Stimmen
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: Zero-Shot-Klonierung
  - **kokoro**: Platz 2 im HuggingFace TTS Arena
- 🔥 **AI-Cover (Sprache-zu-Sprache):** Gesangsentfernung mit **UVR5**, Modulation mit **RVC**

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
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt="Mehrsprachige Sprachkonvertierung und Untertitelgenerierung WebUI-Schnittstelle"/></p>

### `Whisper-Untertitel`-Tab
- Untertitel-spezifisch: Über 90 Sprachen
- Integrierte Untertitelanzeige mit Video
- Wortweise Hervorhebung & Optionen zur Rauschunterdrückung

### `Übersetzung`-Tab
- Übersetzung in über 100 Sprachen
- Unterstützt Untertiteldateien (ASS, SSA, SRT usw.)
- Echtzeit-Spracherkennung und Übersetzung
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="WebUI für Echtzeit-Spracherkennung und Übersetzung"/></p>

### `Sprachgenerierung`-Tab
- Optionen: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- Podcasts mit Promi-Stimmen & mehrsprachige Unterstützung
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="WebUI für Podcast-Erstellung mit Stimmklonierungstechnologie"/></p>

### 🔥 `AI-Cover`-Tab
- Gesangsentfernung: **MDX-Net**, **Demucs**
- Stimmmodulation: **RVC**
- AI-Stimmen können von [Discord AI Hub](https://discord.com/channels/1159260121998827560/@home) heruntergeladen oder über <abus.aikorea@gmail.com> angefordert werden
<p align="center"><img style="width: 90%; height: 90%" src="images/ai_cover.png?raw=true" alt="WebUI für Podcast-Erstellung mit Stimmklonierungstechnologie"/></p>

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
- Öffnen Sie den Browser manuell und geben Sie die im Befehlsfenster angezeigte Adresse ein (z. B. **http://127.0.0.1:7892**)

#### Bei einem CUDA-Out-of-Memory-Fehler
- Überprüfen Sie den GPU-Speicherstatus im Windows Task-Manager – Reiter „Leistung“
- Stellen Sie den Rauschunterdrückungslevel auf 0 oder 1 ein (Level 2 erfordert mindestens 8 GB GPU-Speicher)
- Stellen Sie den Berechnungstyp auf „int“ ein („float“ bietet bessere Qualität, benötigt aber mehr GPU-Speicher)

#### Wie kann die Untertitelqualität verbessert werden?
- Größere Whisper-Modelle tendieren zu besserer Untertitelqualität (large > medium > small > base > tiny), dies ist jedoch nicht garantiert
- Unter den Berechnungstypen bietet „float“ gute Leistung; „int“ reduziert GPU-Nutzung und erhöht die Geschwindigkeit durch Modellquantisierung, allerdings mit Leistungseinbußen
- Ein höherer Rauschunterdrückungslevel entfernt mehr Hintergrundgeräusche und nutzt nur die verbleibende Stimme für die Erkennung, garantiert aber nicht immer bessere Ergebnisse

## 📢 Vorsichtshinweise

Windows Defender könnte eine Warnung über eine nicht vertrauenswürdige Anwendung anzeigen und die weitere Ausführung von Voice-Pro verhindern.
- **SmartScreen „Warnung“-Einstellung:** Klicken Sie auf „Weitere Infos“ und dann auf „Trotzdem ausführen“
- **SmartScreen „Blockieren“-Einstellung:** Öffnen Sie die Eigenschaften von **start.bat**, aktivieren Sie „Entsperren“, übernehmen Sie die Änderungen und führen Sie **start.bat** erneut aus
<p align="center"><img style="width: 40%; height: 40%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/></p>

Falls Windows Defender eine Batch-Datei fälschlicherweise als Trojaner erkennt, spricht man oft von einem „False Positive“. Zur Lösung dieses Problems können Sie folgende Schritte unternehmen:
1. **Datei-Ausnahmebehandlung:** In Windows Defender können Sie bestimmte Dateien oder Prozesse von der Sicherheitsprüfung ausnehmen. Gehen Sie wie folgt vor:
   - Klicken Sie auf die Schaltfläche „Start“ und gehen Sie zu „Einstellungen“
   - Klicken Sie auf „Update und Sicherheit“
   - Wählen Sie „Windows-Sicherheit“ und gehen Sie zu „Viren- und Bedrohungsschutz“
   - Klicken Sie auf „Einstellungen für Viren- und Bedrohungsschutz verwalten“
   - Wählen Sie unter „Einstellungen für Viren- und Bedrohungsschutz“ die Option „Ausnahme hinzufügen“
   - Wählen Sie „Datei oder Ordner“, suchen Sie die betroffene Batch-Datei und fügen Sie sie als Ausnahme hinzu
2. **Windows Defender vorübergehend deaktivieren:** Dies kann eine temporäre Lösung sein. Seien Sie jedoch vorsichtig, da Ihr Computer anderen Bedrohungen ausgesetzt sein könnte
3. **Problem an Antivirensoftware melden:** Wenn Sie sicher sind, dass die Datei kein Trojaner ist, können Sie sie Microsoft als „False Positive“ melden. Microsoft wird dies prüfen und entsprechende Maßnahmen ergreifen

## ☕ Hinweis
- Dieses Repository bietet eine **kostenlose Testversion** von Voice-Pro
- Die kostenlose Testversion unterstützt die Verarbeitung von bis zu **60 Sekunden** Medien
- Die Vollversion von Voice-Pro kann über die offizielle ABUS-Website (<https://abuskorea.imweb.me>) erworben werden
- Wenn Sie uns über [Buy Me a Coffee](https://github.com/abus-aikorea/voice-pro/discussions/10#discussioncomment-11527327) mit einem ☕ unterstützen, erhalten Sie als Dankeschön einen Nutzungsgutschein für bis zu einem Monat
- Bei Fragen zu Käufen, Partnerschaften, Tuning, Investitionen etc. kontaktieren Sie uns bitte per E-Mail unter <abus.aikorea@gmail.com>

## 📬 Kontakt
- E-Mail: <abus.aikorea@gmail.com>
- Homepage (Koreanisch): <https://abuskorea.imweb.me>
- Amazon: [US](https://www.amazon.com/dp/B0DBR69JPL) | [Japan](https://www.amazon.co.jp/dp/B0DBVRJ542) | [Singapore](https://www.amazon.sg/dp/B0DCGKL8R4) | [UAE](https://www.amazon.ae/dp/B0DCGKM7FF)
- Naver: [Software](https://smartstore.naver.com/abus/products/10385660040) | [Solution](https://smartstore.naver.com/abus/products/10298346364)

## 👍 YouTube
- [Produktinformationen](https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [Karaoke: Pop](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)

## 🙏 Danksagung
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

## ©️ Urheberrecht
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)