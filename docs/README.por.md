<!--
    title: Voice-Pro: Ferramenta definitiva de conversão de voz AI e tradução multilíngue
    description: Poderoso aplicativo da web com tecnologia AI para processamento de vídeo do YouTube, reconhecimento de fala, tradução e texto para fala com suporte multilíngue
    keywords: Conversão de voz AI, tradução do YouTube, geração de legendas, fala para texto, texto para fala, clonagem de voz, tradução multilíngue, Alternativa ElevenLabs
    author: ABUS
    version: 4.0.0
    last-updated: 2026-07-13
    product-type: Software de processamento multimídia AI
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, CosyVoice, kokoro, uv
    license: LGPL
-->

<h1 align="center">
Voice-Pro
</h1>

<p align="center">
  <i align="center">A melhor solução de reconhecimento de voz, tradução e dublagem multilíngue com IA 🚀</i>
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
    <img src="images/main_page_crop.por.jpg?raw=true" alt="Dubbing Studio"/>
</p>
<br />


## 🎙️ Um aplicativo web baseado em IA para reconhecimento de voz, tradução e dublagem


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

Voice-Pro é um aplicativo web de ponta que transforma a criação de conteúdo multimídia. Ele integra download de vídeos do YouTube, separação de voz, reconhecimento de fala, tradução e conversão de texto em fala (TTS) em uma única ferramenta poderosa, oferecendo uma solução ideal para criadores, pesquisadores e profissionais multilíngues.

- 🔊 Reconhecimento de fala de alto nível: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 Clonagem de voz sem treinamento (zero-shot): **F5-TTS**, **E2-TTS**, **CosyVoice** (incl. **Fun-CosyVoice3** — coreano e mais 8 idiomas)
- 📢 Texto para fala multilíngue: **Edge-TTS**, **kokoro** (opcionalmente **Azure TTS** com suas próprias chaves — consulte a seção "Serviços Azure" abaixo)
- 🎥 Processamento de YouTube e extração de áudio: **yt-dlp**
- 🌍 Tradução instantânea para mais de 100 idiomas: **Deep-Translator** (opcionalmente **Azure Translator** com suas próprias chaves)


Como uma alternativa robusta ao **ElevenLabs**, o Voice-Pro capacita podcasters, desenvolvedores e criadores com soluções de voz avançadas.

## ⚠️ Por favor, note
- Devido ao trabalho de desenvolvimento do [WeConnect](https://www.wctokyoseoul.com), o desenvolvimento e as atualizações do Voice-Pro não são possíveis por enquanto.
- Tornamos todo o código do Voice-Pro de código aberto e completamente gratuito. O Voice-Pro agora pode ser distribuído e modificado livremente por qualquer pessoa.
- Funciona bem no Windows com GPU NVIDIA. O funcionamento no Mac e Linux não foi verificado.
- Por favor, deixe suas solicitações nas páginas de [![GitHub Issues](https://img.shields.io/github/issues/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/issues)  ou [![GitHub Discussions](https://img.shields.io/github/discussions/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/discussions) .
- **Resolução de problemas**: Na maioria dos casos, os problemas podem ser resolvidos excluindo a pasta `installer_files` e, em seguida, executando `start.bat` novamente (uma reinstalação limpa leva apenas alguns minutos; os modelos de IA baixados em `model/` são mantidos). Os erros são exibidos na WebUI como notificações vermelhas (toasts) que permanecem na tela até serem fechadas.



## 📰 Notícias e Histórico

<details open>
<summary>version 4.0</summary>

- ⚡ **Instalador migrado de Miniconda/pip para [uv](https://docs.astral.sh/uv/)** — instalações drasticamente mais rápidas e totalmente reproduzíveis a partir de um `uv.lock` versionado. Tudo permanece dentro de `installer_files/` (uv, Python, pacotes).
- 🐍 Runtime atualizado: **Python 3.12, Torch 2.8.0+cu128 (suporte à série RTX 50), Gradio 6.20**.
- 🎙️ Stack de ASR mais recente: **faster-whisper 1.2.1** (large-v3-turbo, distil-large-v3.5), openai-whisper 20250625, whisper-timestamped 1.15.9. O whisperX foi removido (suas dependências fixadas bloqueavam a atualização para o Gradio 6; configurações existentes voltam automaticamente para o faster-whisper).
- 🗣️ Stack de TTS mais recente: **F5-TTS 1.1.21**, kokoro 0.9.4, edge-tts 7.x e **CosyVoice** re-incorporado (upstream main).
- 🇰🇷 Novo modelo TTS opcional: **Fun-CosyVoice3-0.5B** — 9 idiomas, incluindo coreano, selecionável na aba CosyVoice (baixado do repositório oficial do HF no primeiro uso).
- 🧹 CUDA Toolkit e Visual Studio Build Tools **não são mais necessários** — todas as dependências vêm com wheels pré-compilados e o PyTorch inclui o runtime CUDA.
- 🛡️ Amigável para **PCs restritos / corporativos**: não são necessários direitos de administrador — o `start.bat` baixa automaticamente um **ffmpeg** portátil se ele não estiver instalado, os downloads dos modelos Whisper se recuperam sozinhos após transferências interrompidas/corrompidas, e a tradução tenta novamente automaticamente com backoff quando a rede limita a taxa do endpoint gratuito do Google (as linhas com falha são relatadas e os textos originais são mantidos).
- 🚨 **Os erros agora são visíveis na WebUI**: cada falha exibe uma notificação de erro vermelha que permanece na tela até você fechá-la (antes era um aviso de 10 segundos, fácil de passar despercebido), com mensagens acionáveis para causas comuns (ffmpeg ausente, nenhuma mídia registrada, etc.).
- 🖥️ Interface: migrada para o **Gradio 6** (layout de largura total em todas as abas, faixas de legenda exibidas diretamente nos players de vídeo).
- 🧽 O `uninstall.bat` não requer mais direitos de administrador e não força mais a reinicialização; `uninstall.bat silent` executa sem supervisão.

</details>

<details>
<summary>version 3.2</summary>

- Estivemos focados no desenvolvimento do [WeConnect](https://www.wctokyoseoul.com) nos últimos meses e não conseguimos gerenciar o Voice-Pro. 
- Decidimos abrir o código do Voice-Pro.
- O Voice-Pro é completamente gratuito e suporta Windows, Mac, Linux.
- [WeConnect](https://www.wctokyoseoul.com) é um aplicativo para intercâmbio cultural global.
- Conecte-se com pessoas de todo o mundo para intercâmbios culturais significativos, aprendizado de idiomas e amizades internacionais.

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

- 🪄 Suporte para modelos ajustados do **F5-TTS**
- 🌍 Idiomas suportados
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
<summary>Versão 3.0</summary>

- 🔥 A função **AI Cover** foi removida.  
- 🚀 Suporte para **m-bain/whisperX** foi adicionado.  

</details>

<details>
<summary>Versão 2.0</summary>

- 🐍 Construído com Python 3.10.15, Torch 2.5.1+cu124 e Gradio 5.14.0.  
- 🆓 A versão de teste gratuita suporta mídias de até **60 segundos** de duração.  
- 🔥 A função **AI Cover** foi adicionada.  
- 🎤 Suporte para **CosyVoice** e **kokoro** foi introduzido.  
- ⏳ A primeira execução baixa **CozyVoice2-0.5B (9GB)**, o que pode levar mais de uma hora dependendo da velocidade da rede.  
- 🎧 Amostras de voz para clonagem serão atualizadas continuamente.  
- 📝 **spaCy** foi adicionado para tradução e TTS naturais por sentença.  
- ☁️ A versão por assinatura inclui o tradutor e TTS do **Microsoft Azure**.  
- 🏪 A versão por assinatura oferece **uso ilimitado** (sem limite de 60 segundos) durante o período de assinatura e pode ser adquirida no [![Shopify](https://img.shields.io/badge/Shopify-7ab55c.svg?style=flat-square&logo=shopify&logoColor=white)](https://r17wvy-t2.myshopify.com).  

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


## ⭐ Recursos principais

### 1. Estúdio de dublagem
- Downloads de vídeos do YouTube e extração de áudio
- Separação de vozes com **Demucs**
- Suporta mais de 100 idiomas para reconhecimento e tradução de fala

### 2. Tecnologias de fala
- **Fala para texto:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- **Texto para fala:** 
  - **Edge-TTS**: Mais de 100 idiomas, 400+ vozes
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: Clonagem sem treinamento prévio
  - **kokoro**: Classificado como #2 na Arena TTS do HuggingFace

### 3. Tradução em tempo real
- Reconhecimento instantâneo de fala
- Tradução multilíngue em tempo real
- Entradas de áudio personalizáveis


## 🤖 Interface Web

### Aba `Estúdio de Dublagem`
- Centro integrado: Downloads do YouTube, remoção de ruído, legendas, tradução e TTS
- Suporta todos os formatos compatíveis com ffmpeg
- Opções de saída: WAV, FLAC, MP3
- Legendas e reconhecimento para mais de 100 idiomas
- TTS com ajustes de velocidade, volume e tom
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.por.jpg?raw=true" alt="Interface Web de Conversão de Voz Multilíngue e Geração de Legendas"/></p>

### Aba `Legendas Whisper`
- Foco em legendas: Mais de 90 idiomas
- Exibição de legendas integrada ao vídeo
- Destaque por palavra e opções de remoção de ruído

### Aba `Tradução`
- Tradução para mais de 100 idiomas
- Suporte a arquivos de legendas (ASS, SSA, SRT, etc.)
- Reconhecimento e tradução de voz em tempo real
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.jpg?raw=true" alt="Interface Web para Reconhecimento de Fala e Tradução em Tempo Real"/></p>

### Aba `Geração de Voz`
- Opções: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- Podcasts com vozes de celebridades e suporte multilíngue
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.jpg?raw=true" alt="Interface Web para Produção de Podcasts usando Tecnologia de Clonagem de Voz"/></p>


## 🎤✨ Voz de referência

- Por favor, solicite a voz que você deseja adicionar na página de Issues. [Issues](https://github.com/abus-aikorea/voice-pro/issues/50)

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


## 💻 Requisitos do Sistema
- **SO:** Windows 10/11 (64 bits), Linux, Mac (Apple Silicon)
- **GPU:** GPU NVIDIA com driver recente (>= 570 recomendado; suporte à série RTX 50). A instalação do CUDA Toolkit NÃO é necessária.
- **VRAM:** 4 GB ou mais (8 GB+ preferível)
- **RAM:** 4 GB ou mais
- **Armazenamento:** Pelo menos 20 GB de espaço livre
- **Internet:** Obrigatória

## 📀 Instalação

Instale o Voice-Pro facilmente com **configure.bat** e **start.bat** (use configure.sh e start.sh no Mac/Linux).

### 1. Preparação do Pacote
- Baixe a versão mais recente em [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) (**Source code (zip)**)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. Instalação e Execução
1. 🚀 **configure.bat** (opcional)
   - Configura git e ffmpeg em todo o sistema (CUDA Toolkit / Visual Studio não são mais necessários)
   - Requer direitos de administrador; execute apenas uma vez
   - Sem direitos de administrador? Pule esta etapa — o **start.bat** baixa automaticamente um ffmpeg portátil
2. 🚀 **start.bat**
   - Inicia a interface web (WebUI) do Voice-Pro
   - A primeira execução baixa o uv + Python 3.12 e instala todas as dependências a partir do lockfile (questão de minutos, não de horas); em seguida, baixa os modelos de IA (~10GB — esta é a parte demorada)
   - GPU/CPU é detectado automaticamente; para alterar, use a variável de ambiente `GPU_CHOICE` (`G`=NVIDIA, `C`=CPU) ou exclua `installer_files\gpu_choice.txt`
   - Em caso de problemas, delete **installer_files** e tente novamente

### 3. Atualização
- 🚀 **update.bat**: Ressincroniza o ambiente Python exatamente com o lockfile versionado (rápido)

### 4. Desinstalação
- Execute **uninstall.bat** ou delete a pasta (instalação portátil)
- Não requer direitos de administrador; adicione `silent` para remoção sem supervisão (`uninstall.bat silent`)
- Apenas a pasta `installer_files` é removida — suas pastas `model/` e `workspace/` são mantidas


## 🔑 Serviços Azure (opcional, .env)

Por padrão, o Voice-Pro usa serviços **gratuitos**: Deep-Translator (endpoint web gratuito do Google) para tradução e Edge-TTS para síntese de fala. Se você tiver sua própria assinatura do **Microsoft Azure**, pode mudar ambos para as APIs do Azure:

1. Copie `.env.example` para `.env` na raiz do projeto:
   ```bash
   copy .env.example .env     # Windows
   cp .env.example .env       # Mac/Linux
   ```
2. Preencha suas credenciais do Azure:
   ```ini
   # Azure Speech Service (TTS)
   AZURE_SPEECH_KEY=your_azure_speech_key_here
   AZURE_SPEECH_REGION=eastus

   # Azure Translator Service
   AZURE_TRANSLATOR_KEY=your_azure_translator_key_here
   AZURE_TRANSLATOR_ENDPOINT=https://your-translator-resource.cognitiveservices.azure.com/
   AZURE_TRANSLATOR_REGION=eastus
   ```
3. Reinicie o Voice-Pro. Chaves válidas são detectadas automaticamente na inicialização — a tradução passa a usar o **Azure Translator** e a primeira aba de Geração de Voz se torna **Azure-TTS**.

**Quando vale a pena configurar isso?**
- 🏢 **Redes corporativas / restritas**: dispositivos de segurança frequentemente limitam a taxa ou bloqueiam o endpoint gratuito `translate.google.com`, o que torna lentas — ou faz falhar — traduções longas de legendas. O Voice-Pro tenta novamente com backoff e mantém o texto original das linhas com falha (você verá um aviso com a contagem de falhas), mas o Azure Translator evita o problema completamente.
- 🗣️ Vozes TTS de maior qualidade e consistência, além de limites de taxa mais altos.
- **NÃO** faça commit do `.env` no controle de versão — ele contém suas chaves privadas.

## ❓ Dicas de Uso

#### Se o navegador não abrir automaticamente
- Feche a janela de comando do Windows e execute **start.bat** novamente
- Abra o navegador manualmente e insira o endereço exibido na janela de comando (ex.: **http://127.0.0.1:7870**)

#### Se ocorrer um erro CUDA Out-of-Memory
- Verifique o status da memória da GPU no Gerenciador de Tarefas do Windows - guia "Desempenho"
- Defina o nível de remoção de ruído para 0 ou 1 (o nível 2 requer pelo menos 8 GB de memória GPU)
- Configure o tipo de cálculo como "int" (o tipo "float" tem melhor qualidade, mas exige mais memória GPU)

#### Como melhorar a qualidade das legendas?
- Modelos Whisper maiores tendem a melhorar a qualidade das legendas (large > medium > small > base > tiny), mas isso não é garantido
- Entre os tipos de cálculo, "float" oferece bom desempenho; "int" reduz o uso da GPU e aumenta a velocidade por meio de quantização do modelo, mas com perda de desempenho
- Aumentar o nível de remoção de ruído elimina mais sons de fundo e usa apenas a voz restante para reconhecimento, mas não garante sempre bons resultados



## 🚨 Aviso
- Devido ao trabalho de desenvolvimento do [WeConnect](https://www.wctokyoseoul.com), não haverá atualizações do Voice-Pro por enquanto.
- Todo o código do Voice-Pro foi publicado como código aberto. Agora é completamente gratuito de usar.
- [WeConnect](https://www.wctokyoseoul.com) é uma plataforma de comunicação para intercâmbio cultural global.





<br />

## ⏳ Plataformas SaaS para Legendagem, Tradução e TTS

A tabela a seguir lista plataformas SaaS que suportam funcionalidades de legendagem, tradução e conversão de texto em fala (TTS/dublagem). Os custos foram calculados para o processamento de um vídeo em coreano de 60 minutos, incluindo geração de legendas, tradução para o inglês e dublagem em inglês, com base nos dados de preços mais recentes de 15 de abril de 2025.

| Plataforma | Legendagem | Tradução | TTS/Dublagem | Custo para Vídeo de 60 min (USD, aprox.) | Principais Características |
| --- | --- | --- | --- | --- | --- |
| **[Maestra](https://maestra.ai)** | ✅ | ✅ | ✅ | $23.70 | Mais de 125 idiomas, legendas em tempo real, extração de palavras-chave SEO, teste gratuito de 15 min. |
| **[Kapwing](https://www.kapwing.com)** | ✅ | ✅ | ✅ | $30\~$40 (Plano Pro, por minuto) | Legendas por IA, tradução para mais de 100 idiomas, dublagem com sincronização labial automática, nível gratuito. |
| **[VEED.IO](https://www.veed.io)** | ✅ | ✅ | ❌ | $24\~$36 (Plano Pro, processamento parcial) | Legendas com 99,9% de precisão, legendas otimizadas para Instagram, editor intuitivo. |
| **[HappyScribe](https://happyscribe.com)** | ✅ | ✅ | ✅ | $36\~$48 (Pagamento por uso) | Mais de 120 idiomas, opção de revisão profissional, seguro, transcrição de reuniões. |
| **[Sonix](https://sonix.ai)** | ✅ | ✅ | ✅ | $30\~$40 (Plano Standard) | Mais de 54 idiomas, 30 min de transcrição gratuita, integração com YouTube/Zoom. |
| **[Descript](https://descript.com)** | ✅ | ✅ | ✅ | $36\~$48 (Plano Criador) | Edição baseada em texto, Overdub TTS, remoção de palavras de preenchimento, 1 hora de transcrição gratuita. |
| **[AppTek](https://apptek.ai)** | ✅ | ✅ | ✅ | Preços personalizados (Contato) | Focado em mídia, modelos personalizados, geração de metadados, Workbench baseado na nuvem. |
| **[Transkriptor](https://transkriptor.com)** | ✅ | ✅ | ❌ | $12\~$18 (Pagamento por uso) | Mais de 100 idiomas, transcrição de links do YouTube, 99% de precisão, editor simples. |
| **[Perso.ai](https://perso.ai)** | ✅ | ✅ | ✅ | $73~$99 (Plano Pro) | 33+ idiomas, clonagem de voz com IA, sincronização labial automática, revisão profissional, API REST. |

### Detalhes do Cálculo de Custos

- **[Maestra](https://maestra.ai)**: Plano Premium ($158/mês, 1200 créditos). Vídeo de 60 min: 60 créditos (legendas) + 60 créditos (tradução) + 60 créditos (dublagem) = 180 créditos. Custo = (180/1200) \* $158 = $23.70.
- **[Kapwing](https://www.kapwing.com)**: Plano Pro (\~$24/mês, minutos limitados). Estimado $0.50\~$0.67/min para legendas+tradução+dublagem (com base em tendências de preços por minuto). Custo de 60 min: $30\~$40. Confirmação de preços exatos necessária.
- **[VEED.IO](https://www.veed.io)**: Plano Pro (\~$24/mês). Legendas+tradução estimadas em $0.40\~$0.60/min. Sem TTS, processamento parcial. Custo de 60 min: $24\~$36. Confirme em veed.io.
- **[HappyScribe](https://happyscribe.com)**: Pagamento por uso (\~$0.20/min transcrição, $0.20 tradução, $0.20 dublagem). Custo de 60 min: $36\~$48 (assumindo serviços combinados). Confirme em happyscribe.com.
- **[Sonix](https://sonix.ai)**: Plano Standard (\~$10/hora transcrição, adicional para tradução/dublagem). Estimado $0.50\~$0.67/min total. Custo de 60 min: $30\~$40. Confirme em sonix.ai.
- **[Descript](https://descript.com)**: Plano Criador (\~$24/mês, horas limitadas). Estimado $0.60\~$0.80/min para legendas+tradução+dublagem. Custo de 60 min: $36\~$48. Confirme em descript.com.
- **[AppTek](https://apptek.ai)**: Preços personalizados para empresas. Sem taxas públicas por minuto. Contate apptek.ai para cotações.
- **[Transkriptor](https://transkriptor.com)**: Pagamento por uso ($0.05\~$0.10/min transcrição, similar para tradução). Sem TTS, processamento parcial. Custo de 60 min: $12\~$18. Confirme em transkriptor.com.
- **[Perso.ai](https://perso.ai)**: Plano Pro ($73~$99/mês, 6.000 créditos). Vídeo de 60 min: 720 créditos (STT, 0,2/s) + 3.600 créditos (dublagem, 1/s) = 4.320 créditos. Pro limita vídeos individuais a 30 min, portanto conteúdo de 60 min requer dois segmentos. Confirmar em [perso.ai/pricing](https://perso.ai/pricing).

### Notas

- **Custo para Vídeo de 60 min**: Os custos são aproximados e assumem o processamento de um vídeo em coreano de 60 minutos para legendas, tradução para o inglês e dublagem em inglês (quando disponível). Plataformas sem TTS (ex.: VEED.IO, Transkriptor) refletem custos de processamento parcial.
- **Suporte a Idiomas**: A maioria das plataformas suporta coreano e inglês. Verifique a disponibilidade de idiomas específicos nos respectivos sites.
- **Casos de Uso**:
  - Mídia/Entretenimento: AppTek, Maestra
  - Redes Sociais: Kapwing, VEED.IO
  - Podcasts/Entrevistas: Sonix, Descript
  - E-learning/Conteúdo Global: Transkriptor, HappyScribe
- **Atualizações de Preços**: Os preços podem variar devido a mudanças nos planos ou promoções. Consulte os sites oficiais para detalhes atualizados.
- Para contribuições ou recomendações de casos de uso específicos, abra um issue ou envie um pull request neste repositório.

<br />



## ☕ Contribuições

Olá, sou David da equipe Voice-Pro.
Nossa equipe descobre as melhores tecnologias de IA do setor e as fornece para que qualquer pessoa possa usá-las de forma fácil e conveniente.
Somos uma pequena startup na Coreia que existe há apenas um ano. Estamos trabalhando arduamente para ajudar você e outros criadores a produzir conteúdo excelente.

Sua avaliação de ⭐⭐⭐⭐⭐ seria muito apreciada, pois ajuda nossa empresa a crescer com você. Por favor, ajude a apoiar nossa pequena equipe.

Obrigado,
Serviço de Atendimento ao Cliente ABUS


- Se você deseja participar e nos ajudar com este projeto, sinta-se à vontade para criar um [Issues](https://github.com/abus-aikorea/voice-pro/issues).
- Se algo der errado, envie um [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) para melhorar este projeto.
- Qualquer tipo de contribuição é bem-vindo.
- Para dúvidas relacionadas a compras, parcerias comerciais, ajustes técnicos, investimentos e outros assuntos, entre em contato conosco por e-mail (<abus.aikorea@gmail.com>).
- Se você gosta deste projeto, por favor, dê uma estrela a este repositório. Nós agradeceríamos muito. ⭐⭐⭐
- Você pode apoiar o Voice-Pro com uma doação aqui:    
</a>
  <a href="https://www.buymeacoffee.com/abus">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me a Coffee" style="height: 20px;">
</a>



## 📬 Contato
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

## ©️ Direitos Autorais
  <img src="images/ABUS-logo.jpg" width="100" height="100"> por [ABUS](https://www.wctokyoseoul.com)
