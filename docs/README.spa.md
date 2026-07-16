<!--
    title: Voice-Pro: Herramienta definitiva de conversión de voz con IA y traducción multilingüe
    description: Potente aplicación web impulsada por IA para procesamiento de videos de YouTube, reconocimiento de voz, traducción y texto a voz con soporte multilingüe
    keywords: Conversión de voz con IA, traducción de YouTube, generación de subtítulos, voz a texto, texto a voz, clonación de voz, traducción multilingüe, Alternativa de ElevenLabs
    author: ABUS
    version: 4.0.0
    last-updated: 2026-07-13
    product-type: Software de procesamiento multimedia con IA
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, CosyVoice, kokoro, uv
    license: LGPL
-->

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">La mejor solución de reconocimiento de voz, traducción y doblaje multilingüe con IA 🚀</i>
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
    <img src="images/main_page_crop.spa.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />


## 🎙️ Una aplicación web impulsada por IA para reconocimiento de voz, traducción y doblaje


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

Voice-Pro es una aplicación web de vanguardia que transforma la creación de contenido multimedia. Integra la descarga de videos de YouTube, separación de voz, reconocimiento de voz, traducción y conversión de texto a voz (TTS) en una sola herramienta poderosa, ofreciendo una solución ideal para creadores, investigadores y profesionales multilingües.

- 🔊 Reconocimiento de voz de primer nivel: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 Clonación de voz sin entrenamiento: **F5-TTS**, **E2-TTS**, **CosyVoice** (incluye **Fun-CosyVoice3**: coreano y 8 idiomas más)
- 📢 Texto a voz multilingüe: **Edge-TTS**, **kokoro** (opcionalmente **Azure TTS** con tus propias claves; consulta la sección "Servicios de Azure" más abajo)
- 🎥 Procesamiento de YouTube y extracción de audio: **yt-dlp**
- 🌍 Traducción instantánea para más de 100 idiomas: **Deep-Translator** (opcionalmente **Azure Translator** con tus propias claves)


Como una alternativa sólida a **ElevenLabs**, Voice-Pro empodera a podcasters, desarrolladores y creadores con soluciones de voz avanzadas.

## ⚠️ Por favor, tenga en cuenta
- Debido al trabajo de desarrollo de [WeConnect](https://www.wctokyoseoul.com), el desarrollo y las actualizaciones de Voice-Pro no son posibles por el momento.
- Hemos hecho público todo el código de Voice-Pro y es completamente gratuito. Voice-Pro ahora puede ser distribuido y modificado libremente por cualquiera.
- Funciona bien en Windows con GPU NVIDIA. El funcionamiento en Mac y Linux no ha sido verificado.
- Por favor, deje sus solicitudes en las páginas de [![GitHub Issues](https://img.shields.io/github/issues/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/issues)  o [![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions) .
- **Solución de problemas**: En la mayoría de los casos, los problemas se pueden resolver eliminando la carpeta `installer_files` y ejecutando de nuevo `start.bat` (una reinstalación limpia solo toma unos minutos; los modelos de IA descargados en `model/` se conservan). Los errores se muestran en la WebUI como avisos rojos (toasts) que permanecen en pantalla hasta que se cierran.



## 📰 Noticias e Historia

<details open>
<summary>version 4.0</summary>

- ⚡ **Se migró el instalador de Miniconda/pip a [uv](https://docs.astral.sh/uv/)**: instalaciones drásticamente más rápidas y totalmente reproducibles a partir de un `uv.lock` versionado. Todo permanece dentro de `installer_files/` (uv, Python, paquetes).
- 🐍 Runtime actualizado: **Python 3.12, Torch 2.8.0+cu128 (compatible con las RTX serie 50), Gradio 6.20**.
- 🎙️ Pila ASR más reciente: **faster-whisper 1.2.1** (large-v3-turbo, distil-large-v3.5), openai-whisper 20250625, whisper-timestamped 1.15.9. Se eliminó whisperX (sus dependencias fijadas bloqueaban la actualización a Gradio 6; las configuraciones existentes recurren automáticamente a faster-whisper).
- 🗣️ Pila TTS más reciente: **F5-TTS 1.1.21**, kokoro 0.9.4, edge-tts 7.x y **CosyVoice** re-integrado (main de upstream).
- 🇰🇷 Nuevo modelo TTS opcional: **Fun-CosyVoice3-0.5B**: 9 idiomas incluido el coreano, seleccionable en la pestaña CosyVoice (se descarga del repositorio oficial de HF en el primer uso).
- 🧹 CUDA Toolkit y Visual Studio Build Tools **ya no son necesarios**: todas las dependencias se distribuyen como wheels precompilados y PyTorch incluye el runtime de CUDA.
- 🛡️ Compatible con **PC restringidos / corporativos**: no se necesitan derechos de administrador — `start.bat` descarga automáticamente un **ffmpeg** portátil si no está instalado, las descargas de modelos Whisper se reparan solas tras transferencias interrumpidas o corruptas, y la traducción reintenta automáticamente con espera progresiva cuando la red limita el endpoint gratuito de Google (las líneas fallidas se informan y se conserva el texto original).
- 🚨 **Los errores ahora son visibles en la WebUI**: cada fallo muestra un aviso rojo que permanece en pantalla hasta que lo cierres (antes era una advertencia de 10 segundos fácil de pasar por alto), con mensajes accionables para las causas comunes (ffmpeg ausente, ningún medio registrado, etc.).
- 🖥️ UI: migrada a **Gradio 6** (diseño de ancho completo en todas las pestañas, pistas de subtítulos mostradas directamente en los reproductores de video).
- 🧽 `uninstall.bat` ya no requiere derechos de administrador ni fuerza un reinicio; `uninstall.bat silent` se ejecuta de forma desatendida.

</details>

<details>
<summary>version 3.2</summary>

- Nos hemos centrado en el desarrollo de [WeConnect](https://www.wctokyoseoul.com) durante los últimos meses y no hemos podido gestionar Voice-Pro en absoluto. 
- Hemos decidido abrir el código de Voice-Pro.
- Voice-Pro es completamente gratuito y es compatible con Windows, Mac, Linux.
- [WeConnect](https://www.wctokyoseoul.com) es una aplicación para el intercambio cultural global.
- Conecta con personas de todo el mundo para intercambios culturales significativos, aprendizaje de idiomas y amistades internacionales.

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

- 🪄 Soporte para modelos ajustados de **F5-TTS**
- 🌍 Idiomas compatibles
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
<summary>Versión 3.0</summary>

- 🔥 Se eliminó la función **AI Cover**.  
- 🚀 Se añadió soporte para **m-bain/whisperX**.  

</details>

<details>
<summary>Versión 2.0</summary>

- 🐍 Construido con Python 3.10.15, Torch 2.5.1+cu124 y Gradio 5.14.0.  
- 🆓 La prueba gratuita soporta medios de hasta **60 segundos** de duración.  
- 🔥 Se añadió la función **AI Cover**.  
- 🎤 Se introdujo soporte para **CosyVoice** y **kokoro**.  
- ⏳ La primera ejecución descarga **CozyVoice2-0.5B (9GB)**, lo que puede tomar más de una hora dependiendo de la velocidad de la red.  
- 🎧 Las muestras de voz para clonación se actualizarán continuamente.  
- 📝 Se añadió **spaCy** para traducción y TTS natural por frases.  
- ☁️ La versión de suscripción incluye el traductor y TTS de **Microsoft Azure**.  
- 🏪 La versión de suscripción ofrece **uso ilimitado** (sin límite de 60 segundos) durante el período de suscripción y se puede comprar en [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com).  

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

## ⭐ Características principales

### 1. Estudio de doblaje
- Descarga de videos de YouTube y extracción de audio
- Separación de voces con **Demucs**
- Soporta más de 100 idiomas para reconocimiento y traducción de voz

### 2. Tecnologías de voz
- **Voz a texto:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- **Texto a voz:** 
  - **Edge-TTS**: Más de 100 idiomas, 400+ voces
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: Clonación sin entrenamiento previo
  - **kokoro**: Clasificado #2 en la Arena TTS de HuggingFace

### 3. Traducción en tiempo real
- Reconocimiento instantáneo de voz
- Traducción multilingüe en tiempo real
- Entradas de audio personalizables


## 🤖 Interfaz Web

### Pestaña `Estudio de Doblaje`
- Centro integrado: Descargas de YouTube, eliminación de ruido, subtítulos, traducción y TTS
- Soporta todos los formatos compatibles con ffmpeg
- Opciones de salida: WAV, FLAC, MP3
- Subtítulos y reconocimiento para más de 100 idiomas
- TTS con ajustes de velocidad, volumen y tono
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.spa.jpg?raw=true" alt="Interfaz Web de Conversión de Voz Multilingüe y Generación de Subtítulos"/></p>

### Pestaña `Subtítulos Whisper`
- Enfocada en subtítulos: Más de 90 idiomas
- Visualización de subtítulos integrada con video
- Resaltado por palabra y opciones de eliminación de ruido

### Pestaña `Traducción`
- Traducción a más de 100 idiomas
- Soporte para archivos de subtítulos (ASS, SSA, SRT, etc.)
- Reconocimiento y traducción de voz en tiempo real
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.jpg?raw=true" alt="Interfaz Web para Reconocimiento de Voz y Traducción en Tiempo Real"/></p>

### Pestaña `Generación de Voz`
- Opciones: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- Podcasts con voces de celebridades y soporte multilingüe
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.jpg?raw=true" alt="Interfaz Web para Producción de Podcasts usando Tecnología de Clonación de Voz"/></p>




## 🎤✨ Voz de referencia

- Por favor, solicite la voz que desea agregar en la página de Issues. [Issues](https://github.com/abus-aikorea/voice-pro/issues/50)

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



## 💻 Requisitos del Sistema
- **SO:** Windows 10/11 (64 bits), Linux, Mac (Apple Silicon)
- **GPU:** GPU NVIDIA con un controlador reciente (>= 570 recomendado; compatible con las RTX serie 50). NO es necesario instalar CUDA Toolkit.
- **VRAM:** 4 GB o más (8 GB+ preferible)
- **RAM:** 4 GB o más
- **Almacenamiento:** Al menos 20 GB de espacio libre
- **Internet:** Requerido

## 📀 Instalación

Instala Voice-Pro fácilmente con **configure.bat** y **start.bat** (usa configure.sh y start.sh en Mac/Linux).

### 1. Preparación del Paquete
- Descarga la versión más reciente en [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) (**Source code (zip)**)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```


### 2. Instalación y Ejecución
1. 🚀 **configure.bat** (opcional)
   - Configura git y ffmpeg a nivel de sistema (CUDA Toolkit / Visual Studio ya no son necesarios)
   - Requiere derechos de administrador; ejecútalo solo una vez
   - ¿Sin derechos de administrador? Omítelo: **start.bat** descarga automáticamente un ffmpeg portátil
2. 🚀 **start.bat**
   - Inicia la interfaz web de Voice-Pro
   - La primera ejecución descarga uv + Python 3.12 e instala todas las dependencias desde el lockfile (minutos, no horas); después descarga los modelos de IA (~10GB — esta es la parte lenta)
   - La GPU/CPU se detecta automáticamente; puedes forzar la selección con la variable de entorno `GPU_CHOICE` (`G`=NVIDIA, `C`=CPU) o eliminando `installer_files\gpu_choice.txt`
   - En caso de problemas, elimina **installer_files** y vuelve a intentarlo

### 3. Actualización
- 🚀 **update.bat**: Re-sincroniza el entorno Python exactamente con el lockfile versionado (rápido)

### 4. Desinstalación
- Ejecuta **uninstall.bat** o elimina la carpeta (instalación portátil)
- No requiere derechos de administrador; añade `silent` para una eliminación desatendida (`uninstall.bat silent`)
- Solo se elimina la carpeta `installer_files`: tus carpetas `model/` y `workspace/` se conservan


## 🔑 Servicios de Azure (opcional, .env)

Por defecto, Voice-Pro utiliza servicios **gratuitos**: Deep-Translator (el endpoint web gratuito de Google) para la traducción y Edge-TTS para la síntesis de voz. Si tienes tu propia suscripción a **Microsoft Azure**, puedes cambiar ambos a las API de Azure:

1. Copia `.env.example` a `.env` en la raíz del proyecto:
   ```bash
   copy .env.example .env     # Windows
   cp .env.example .env       # Mac/Linux
   ```
2. Introduce tus credenciales de Azure:
   ```ini
   # Azure Speech Service (TTS)
   AZURE_SPEECH_KEY=your_azure_speech_key_here
   AZURE_SPEECH_REGION=eastus

   # Azure Translator Service
   AZURE_TRANSLATOR_KEY=your_azure_translator_key_here
   AZURE_TRANSLATOR_ENDPOINT=https://your-translator-resource.cognitiveservices.azure.com/
   AZURE_TRANSLATOR_REGION=eastus
   ```
3. Reinicia Voice-Pro. Las claves válidas se detectan automáticamente al iniciar: la traducción cambia a **Azure Translator** y la primera pestaña de Generación de Voz pasa a ser **Azure-TTS**.

**¿Cuándo vale la pena configurarlo?**
- 🏢 **Redes corporativas / restringidas**: los dispositivos de seguridad a menudo limitan o bloquean el endpoint gratuito `translate.google.com`, lo que ralentiza o hace fallar las traducciones largas de subtítulos. Voice-Pro reintenta con espera progresiva y conserva el texto original de las líneas fallidas (verás una advertencia con el número de fallos), pero Azure Translator evita el problema por completo.
- 🗣️ Voces TTS de mayor calidad y consistencia, y límites de uso más altos.
- **NO** subas `.env` al control de versiones: contiene tus claves privadas.


## ❓ Consejos de Uso

#### Si el navegador no se abre automáticamente
- Cierra la ventana de comandos de Windows y ejecuta **start.bat** nuevamente
- Abre el navegador manualmente e introduce la dirección mostrada en la ventana de comandos (ej.: **http://127.0.0.1:7870**)

#### Si ocurre un error CUDA Out-of-Memory
- Verifica el estado de la memoria GPU en el Administrador de Tareas de Windows - pestaña "Rendimiento"
- Configura el nivel de eliminación de ruido en 0 o 1 (el nivel 2 requiere al menos 8 GB de memoria GPU)
- Establece el tipo de cálculo en "int" (el tipo "float" ofrece mejor calidad, pero requiere más memoria GPU)

#### ¿Cómo mejorar la calidad de los subtítulos?
- Los modelos Whisper más grandes tienden a mejorar la calidad de los subtítulos (large > medium > small > base > tiny), pero no siempre es así
- Entre los tipos de cálculo, "float" ofrece buen rendimiento; "int" reduce el uso de GPU y aumenta la velocidad mediante cuantización del modelo, pero con pérdida de rendimiento
- Aumentar el nivel de eliminación de ruido elimina más sonidos de fondo y usa solo la voz restante para el reconocimiento, pero no siempre garantiza mejores resultados


## 🚨 Aviso
- Debido al trabajo de desarrollo de [WeConnect](https://www.wctokyoseoul.com), no habrá actualizaciones de Voice-Pro por el momento.
- Todo el código de Voice-Pro ha sido publicado como código abierto. Ahora es completamente gratuito de usar.
- [WeConnect](https://www.wctokyoseoul.com) es una plataforma de comunicación para el intercambio cultural global.




<br />

## ⏳ Plataformas SaaS para Subtitulado, Traducción y TTS

La siguiente tabla enumera las plataformas SaaS que admiten funciones de subtitulado, traducción y conversión de texto a voz (TTS/doblaje). Los costos se calcularon para procesar un video en coreano de 60 minutos, incluyendo la generación de subtítulos, traducción al inglés y doblaje en inglés, basados en los datos de precios más recientes al 15 de abril de 2025.

| Plataforma | Subtitulado | Traducción | TTS/Doblaje | Costo para Video de 60 min (USD, aprox.) | Características Principales |
| --- | --- | --- | --- | --- | --- |
| **[Maestra](https://maestra.ai)** | ✅ | ✅ | ✅ | $23.70 | Más de 125 idiomas, subtítulos en tiempo real, extracción de palabras clave SEO, prueba gratuita de 15 min. |
| **[Kapwing](https://www.kapwing.com)** | ✅ | ✅ | ✅ | $30\~$40 (Plan Pro, por minuto) | Subtítulos por IA, traducción a más de 100 idiomas, doblaje con sincronización labial automática, nivel gratuito. |
| **[VEED.IO](https://www.veed.io)** | ✅ | ✅ | ❌ | $24\~$36 (Plan Pro, procesamiento parcial) | Subtítulos con 99.9% de precisión, subtítulos optimizados para Instagram, editor intuitivo. |
| **[HappyScribe](https://happyscribe.com)** | ✅ | ✅ | ✅ | $36\~$48 (Pago por uso) | Más de 120 idiomas, opción de corrección profesional, seguro, transcripción de reuniones. |
| **[Sonix](https://sonix.ai)** | ✅ | ✅ | ✅ | $30\~$40 (Plan Estándar) | Más de 54 idiomas, 30 min de transcripción gratuita, integración con YouTube/Zoom. |
| **[Descript](https://descript.com)** | ✅ | ✅ | ✅ | $36\~$48 (Plan Creador) | Edición basada en texto, Overdub TTS, eliminación de palabras de relleno, 1 hora de transcripción gratuita. |
| **[AppTek](https://apptek.ai)** | ✅ | ✅ | ✅ | Precios personalizados (Contactar) | Enfocado en medios, modelos personalizados, generación de metadatos, Workbench basado en la nube. |
| **[Transkriptor](https://transkriptor.com)** | ✅ | ✅ | ❌ | $12\~$18 (Pago por uso) | Más de 100 idiomas, transcripción desde enlaces de YouTube, 99% de precisión, editor simple. |
| **[Perso.ai](https://perso.ai)** | ✅ | ✅ | ✅ | $73~$99 (Plan Pro) | 33+ idiomas, clonación de voz con IA, sincronización labial automática, corrección profesional, API REST. |

### Detalles del Cálculo de Costos

- **[Maestra](https://maestra.ai)**: Plan Premium ($158/mes, 1200 créditos). Video de 60 min: 60 créditos (subtítulos) + 60 créditos (traducción) + 60 créditos (doblaje) = 180 créditos. Costo = (180/1200) \* $158 = $23.70.
- **[Kapwing](https://www.kapwing.com)**: Plan Pro (\~$24/mes, minutos limitados). Estimado $0.50\~$0.67/min para subtítulos+traducción+doblaje (basado en tendencias de precios por minuto). Costo de 60 min: $30\~$40. Se requiere confirmación de precios exactos.
- **[VEED.IO](https://www.veed.io)**: Plan Pro (\~$24/mes). Subtítulos+traducción estimados en $0.40\~$0.60/min. Sin TTS, procesamiento parcial. Costo de 60 min: $24\~$36. Confirme en veed.io.
- **[HappyScribe](https://happyscribe.com)**: Pago por uso (\~$0.20/min transcripción, $0.20 traducción, $0.20 doblaje). Costo de 60 min: $36\~$48 (suponiendo servicios combinados). Confirme en happyscribe.com.
- **[Sonix](https://sonix.ai)**: Plan Estándar (\~$10/hora transcripción, adicional para traducción/doblaje). Estimado $0.50\~$0.67/min total. Costo de 60 min: $30\~$40. Confirme en sonix.ai.
- **[Descript](https://descript.com)**: Plan Creador (\~$24/mes, horas limitadas). Estimado $0.60\~$0.80/min para subtítulos+traducción+doblaje. Costo de 60 min: $36\~$48. Confirme en descript.com.
- **[AppTek](https://apptek.ai)**: Precios personalizados para empresas. Sin tarifas públicas por minuto. Contacte a apptek.ai para cotizaciones.
- **[Transkriptor](https://transkriptor.com)**: Pago por uso ($0.05\~$0.10/min transcripción, similar para traducción). Sin TTS, procesamiento parcial. Costo de 60 min: $12\~$18. Confirme en transkriptor.com.
- **[Perso.ai](https://perso.ai)**: Plan Pro ($73~$99/mes, 6,000 créditos). Video de 60 min: 720 créditos (STT, 0,2/s) + 3,600 créditos (doblaje, 1/s) = 4,320 créditos. Pro limita videos individuales a 30 min, por lo que el contenido de 60 min requiere dos segmentos. Confirmar en [perso.ai/pricing](https://perso.ai/pricing).

### Notas

- **Costo para Video de 60 min**: Los costos son aproximados y asumen el procesamiento de un video en coreano de 60 minutos para subtítulos, traducción al inglés y doblaje en inglés (donde esté disponible). Las plataformas sin TTS (p. ej., VEED.IO, Transkriptor) reflejan costos de procesamiento parcial.
- **Soporte de Idiomas**: La mayoría de las plataformas admiten coreano e inglés. Verifique la disponibilidad de idiomas específicos en sus sitios web.
- **Casos de Uso**:
  - Medios/Entretenimiento: AppTek, Maestra
  - Redes Sociales: Kapwing, VEED.IO
  - Podcasts/Entrevistas: Sonix, Descript
  - E-learning/Contenido Global: Transkriptor, HappyScribe
- **Actualizaciones de Precios**: Los precios pueden variar debido a cambios en los planes o promociones. Consulte los sitios web oficiales para obtener detalles actualizados.
- Para contribuciones o recomendaciones de casos de uso específicos, abra un issue o envíe un pull request en este repositorio.

<br />



## ☕ Contribuciones

Hola, soy David del equipo de Voice-Pro.
Nuestro equipo descubre las mejores tecnologías de IA de la industria y las proporciona para que cualquiera pueda usarlas de manera fácil y conveniente.
Somos una pequeña startup en Corea que solo lleva un año en funcionamiento. Estamos trabajando arduamente para ayudarlos a usted y a otros creadores a producir contenido excelente.

Su reseña de ⭐⭐⭐⭐⭐ sería muy apreciada, ya que ayuda a que nuestro negocio crezca con usted. Por favor, ayude a apoyar a nuestro pequeño equipo.

Gracias,
Servicio al Cliente de ABUS

- Si desea participar y ayudarnos con este proyecto, no dude en crear un [Issues](https://github.com/abus-aikorea/voice-pro/issues).
- Si algo sale mal, envíe un [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) para mejorar este proyecto.
- Cualquier tipo de contribución es bienvenida.
- Para consultas relacionadas con compras, asociaciones comerciales, ajustes técnicos, inversiones y otros asuntos, contáctenos por correo electrónico (<abus.aikorea@gmail.com>).
- Si le gusta este proyecto, por favor, marque este repositorio con una estrella. Lo agradeceríamos mucho. ⭐⭐⭐
- Puede apoyar a Voice-Pro con una donación aquí:    
</a>
  <a href="https://www.buymeacoffee.com/abus">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
</a>



## 📬 Contacto
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://www.wctokyoseoul.com>



## 🙏 Créditos
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

## ©️ Derechos de Autor
  <img src="images/ABUS-logo.jpg" width="100" height="100"> por [ABUS](https://www.wctokyoseoul.com)
