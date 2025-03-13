<!--
    title: Voice-Pro: Ultimatives KI-Sprachkonvertierungs- und mehrsprachiges Übersetzungstool
    description: Leistungsstarke KI-gestützte Webanwendung für YouTube-Videoverarbeitung, Spracherkennung, Übersetzung und mehrsprachige Text-to-Speech-Funktion
    keywords: KI-Sprachkonvertierung, YouTube-Übersetzung, Untertitelgenerierung, Sprache-zu-Text, Text-zu-Speech, Sprachklonierung, mehrsprachige Übersetzung, ElevenLabs-Alternative
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: KI-Multimedia-Verarbeitungssoftware
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

# Voice-Pro: Das ultimative Tool für KI-gestützte Sprachkonvertierung und mehrsprachige Übersetzung 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md) ∙ [Deutsch](README.deu.md) ∙ [Español](README.spa.md) ∙ [Português](README.por.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

## 🎙️ Leistungsstarke KI-gestützte Webanwendung für YouTube-Videoverarbeitung, Spracherkennung, Übersetzung und mehrsprachige Text-to-Speech-Funktion

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
  - Upgrade von v1.x auf v2.x: **Unmöglich**. Daher wird empfohlen, den installer_files Ordner zu löschen und die neueste Version von start.bat auszuführen.
  - Upgrade von v2.x auf v2.x: **Möglich**. Laden Sie den neuesten Code herunter und führen Sie update.bat aus.
  - Erstanwender: Bitte beachten Sie die Installationsanleitung unten.
  - Fehlerbehebung: In den meisten Fällen wird das Problem durch Löschen des **installer_files** Ordners und anschließendes Ausführen von configure.bat und start.bat nacheinander behoben.


## 🚄 Demos

### `Dubbing-Studio`-Tab: Transkription, Übersetzung & TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/1cf084a4-3286-4055-86d2-238ed179560e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description2">
   </video>
  
  <p id="studio-demo-description">
  
  Demo des umfassenden Medienverarbeitungs-Workflows im Studio-Tab: Zeigt einen durchgehenden Prozess von YouTube-Video-Download über KI-basierte Stimmseparation, automatische Whisper-Untertitel, mehrsprachige Übersetzung bis hin zu professioneller Synchronisation mit F5-TTS.</p>
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
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.deu.png?raw=true" alt="Mehrsprachige Sprachkonvertierung und Untertitelgenerierung WebUI-Schnittstelle"/></p>

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


## 🎤✨ Referenzstimme

- Bitte fordern Sie die Stimme, die Sie hinzufügen möchten, auf der Issues-Seite an. [Issues](https://github.com/abus-aikorea/voice-pro/issues/50)

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


## 🚨 Hinweis
- Dieses Repository bietet eine **kostenlose Testversion** von Voice-Pro.
- Die kostenlose Testversion von Voice-Pro ermöglicht die Verarbeitung von Medien bis zu **60 Sekunden**.
- Die Abonnementversion unterstützt Microsoft Azure TTS und Translator. Kaufen Sie es auf [Shopify](https://r17wvy-t2.myshopify.com/de).


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

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)



## 📬 Kontakt
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- Naver (Korean): [30-day subscription](https://smartstore.naver.com/abus/products/11308510267)
- Shopify (Global): [30-day subscription](https://r17wvy-t2.myshopify.com/de)

## 👍 YouTube
- [PlayList](https://www.youtube.com/watch?v=Tu2okoHY174&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [Karaoke: Pop](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)

## 🙏 Danksagung
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
* CosyVoice: <https://github.com/FunAudioLLM/CosyVoice>
* kokoro: <https://github.com/hexgrad/kokoro>
* Deep-Translator: <https://github.com/nidhaloff/deep-translator>
* spaCy: <https://github.com/explosion/spaCy>

## ©️ Urheberrecht
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)