<!--
    title: Voice-Pro: Herramienta definitiva de conversión de voz con IA y traducción multilingüe
    description: Potente aplicación web impulsada por IA para procesamiento de videos de YouTube, reconocimiento de voz, traducción y texto a voz con soporte multilingüe
    keywords: Conversión de voz con IA, traducción de YouTube, generación de subtítulos, voz a texto, texto a voz, clonación de voz, traducción multilingüe, Alternativa de ElevenLabs
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: Software de procesamiento multimedia con IA
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">La mejor solución de reconocimiento de voz, traducción y doblaje multilingüe con IA 🚀</i>
</p>

<h4 align="center">
  <a href="https://www.youtube.com/channel/UCbCBWXuVbk-OBp9T4H5JjAA">
    <img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube" style="height: 20px;">
  </a>
  <a href="https://www.amazon.com/dp/B0F1LQZ42T">
    <img src="https://img.shields.io/badge/Amazon-f90.svg?style=flat-square&logo=amazon&logoColor=white" alt="Amazon" style="height: 20px;">
  </a>
  <a href="https://r17wvy-t2.myshopify.com">
    <img src="https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white" alt="Shopify" style="height: 20px;">
  </a>
    <a href="https://www.buymeacoffee.com/abus">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 20px;">
  </a>
  <a href="https://github.com/abus-aikorea/voice-pro/releases">
    <img src="https://img.shields.io/github/v/release/abus-aikorea/voice-pro" alt="release" style="height: 20px;">
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
- 🎤 Clonación de voz Zero-Shot: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 Conversión de texto a voz multilingüe: **Edge-TTS**, **kokoro**
- 🎥 Procesamiento de videos de YouTube y extracción de audio: **yt-dlp**
- 🌍 Traducción instantánea a más de 100 idiomas: **Deep-Translator**
- 🔇 Separación vocal de nivel profesional: **UVR5**
- 🔥 Creación de covers por IA: **RVC**

Como una alternativa sólida a **ElevenLabs**, Voice-Pro empodera a podcasters, desarrolladores y creadores con soluciones de voz avanzadas.

## ⚠️ Tenga en cuenta
  - Actualización de v1.x a v2.x: **No es posible**. Por lo tanto, se recomienda eliminar la carpeta installer_files y ejecutar la última versión de **start.bat**.
  - Actualización de v2.x a v2.x: **Posible**. Después de descargar el código más reciente, ejecute **update.bat**.
  - Usuarios por primera vez: Consulte las instrucciones de instalación a continuación.
  - Solución de problemas: En la mayoría de los casos, los problemas se pueden resolver eliminando la carpeta **installer_files** y luego ejecutando **configure.bat** y **start.bat** en secuencia.

## 📰 Noticias e historial
- Voice-Pro se ha actualizado a **v2.x** (Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0)
- 🆓 La versión de prueba gratuita admite medios de hasta **60 segundos** de duración.
- 🔥 Se ha añadido la función de **Covers de IA**.
- 🎤 Se ha añadido soporte para **CosyVoice** y **kokoro**.
- ⏳ La primera ejecución descarga **CozyVoice2-0.5B (9GB)**. Puede tardar más de una hora dependiendo de la velocidad de la red.
- 🎧 Las muestras de voz para clonación de voz se actualizarán continuamente.
- Se ha introducido **spaCy** para traducción y TTS natural oración por oración.
- ☁️ La versión de suscripción admite **Translator** y **TTS** de **Microsoft Azure**.
- 🏪 La versión de suscripción ofrece **uso ilimitado** dentro del período de suscripción (sin límite de 60 segundos) y se puede comprar a través de [**Shopify**](https://r17wvy-t2.myshopify.com/es).


## ▶️ Demostraciones

### Pestaña `Estudio de Doblaje`: Transcripción, Traducción y TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/1cf084a4-3286-4055-86d2-238ed179560e"
   width="100%" 
   style="max-width: 720px;" 
   controls="controls" 
   muted="muted"
   aria-describedby="studio-demo-description2">
  </video> 
  <p id="studio-demo-description">Demostración del flujo de trabajo completo de procesamiento de medios en la pestaña Estudio: Muestra un proceso integral de transformación de medios, desde la descarga de videos de YouTube hasta la separación de voz por IA, subtítulos automáticos con Whisper, traducción multilingüe y doblaje profesional usando F5-TTS.</p>
</div>

### Pestaña `F5-TTS-Multi`: Creación de Podcasts
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls muted aria-describedby="tts-demo-description"></video>
  <p id="tts-demo-description">Demostración de la innovadora tecnología de clonación de voz por IA de F5-TTS: Presenta una tecnología avanzada de conversión de voz que imita con precisión las voces reales de Mark Zuckerberg y Elon Musk para crear contenidos completamente nuevos.</p>
</div>

### Pestaña `AI Cover`
<div aria-labelledby="ai-cover-description">
  <video src="https://github.com/user-attachments/assets/88a47ab1-a18b-4779-97c8-7c1da84f5fc3" width="100%" style="max-width: 720px;" controls muted aria-describedby="ai-cover-description"></video>
  <p id="ai-cover-description">Crea una versión de Trump de "Cupid" de IU, "Te Echo de Menos" de Kim Kwang-seok y "Carta de un Soldado".</p>
</div>

### Pestaña `Traducción en Vivo`: Reconocimiento y Traducción en Tiempo Real
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls muted aria-describedby="translate-demo-description"></video>
  <p id="translate-demo-description">Demostración de la función de traducción multilingüe en tiempo real: Muestra un proceso innovador de procesamiento de medios multilingües que captura instantáneamente contenidos de noticias de la BBC, genera subtítulos en tiempo real y los traduce de inmediato a otros idiomas.</p>
</div>

## ⭐ Características Principales

### 1. Estudio de Doblaje
- Descarga de videos de YouTube y extracción de audio
- Separación de voz con **MDX-Net** y **Demucs**
- Soporte para reconocimiento de voz y traducción en más de 100 idiomas

### 2. Tecnologías de Voz
- **Voz a Texto:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- **Texto a Voz:**
  - **Edge-TTS**: Más de 100 idiomas, más de 400 voces
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: Clonación Zero-Shot
  - **kokoro**: 2º lugar en el HuggingFace TTS Arena
- 🔥 **AI Cover (Voz a Voz):** Eliminación vocal con **UVR5**, modulación con **RVC**

### 3. Traducción en Tiempo Real
- Reconocimiento de voz instantáneo
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

### 🔥 Pestaña `AI Cover`
- Eliminación vocal: **MDX-Net**, **Demucs**
- Modulación de voz: **RVC**
- Descarga voces IA en [Discord AI Hub](https://discord.com/channels/1159260121998827560/@home) o solicita a través de <abus.aikorea@gmail.com>
<p align="center"><img style="width: 90%; height: 90%" src="images/ai_cover.jpg?raw=true" alt="Interfaz Web para Producción de Podcasts usando Tecnología de Clonación de Voz"/></p>



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
- **SO:** Windows 10/11 (64 bits) ※ Linux/Mac no soportados
- **GPU:** NVIDIA con soporte CUDA 12.4 (recomendado)
- **VRAM:** 4 GB o más (8 GB+ preferible)
- **RAM:** 4 GB o más
- **Almacenamiento:** Al menos 20 GB de espacio libre
- **Internet:** Requerido

## 📀 Instalación

Instala Voice-Pro fácilmente con **configure.bat** y **start.bat**.

### 1. Preparación del Paquete
- Descarga la versión más reciente en [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) (**Source code (zip)**)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```


### 2. Instalación y Ejecución
1. 🚀 **configure.bat**
   - Instala git, ffmpeg y CUDA (si usas GPU NVIDIA)
   - Ejecútalo solo una vez; requiere internet, puede tomar más de 1 hora
   - No cierres la ventana de comandos
2. 🚀 **start.bat**
   - Inicia la interfaz web de Voice-Pro
   - En la primera ejecución, instala dependencias (puede tomar más de 1 hora)
   - En caso de problemas, elimina **installer_files** y ejecuta de nuevo

### 3. Actualización
- 🚀 **update.bat**: Actualiza el entorno Python (más rápido que reinstalar)

### 4. Desinstalación
- Ejecuta **uninstall.bat** o elimina la carpeta (instalación portátil)

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
- Este repositorio ofrece una **prueba gratuita** de Voice-Pro.
- La versión de prueba gratuita de Voice-Pro le permite procesar hasta **60 segundos** de medios.
- La versión de suscripción es compatible con Microsoft Azure TTS y Translator. Cómprelo en [Shopify](https://r17wvy-t2.myshopify.com/es).


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

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)



## 📬 Contacto
- Email: <abus.aikorea@gmail.com>
- Homepage (Korean): <https://abuskorea.imweb.me>
- Naver (Korean): [30-day subscription](https://smartstore.naver.com/abus/products/11308510267)
- Shopify (Global): [30-day subscription](https://r17wvy-t2.myshopify.com/es)

## 👍 YouTube
- [PlayList](https://www.youtube.com/watch?v=Tu2okoHY174&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [Karaoke: Pop](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)

## 🙏 Créditos
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

## ©️ Derechos de Autor
<img src="images/ABUS-logo.jpg" width="100" height="100"> por [ABUS](https://abuskorea.imweb.me)