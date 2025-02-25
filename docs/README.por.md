<!--
    title: Voice-Pro: Ferramenta definitiva de conversão de voz AI e tradução multilíngue
    description: Poderoso aplicativo da web com tecnologia AI para processamento de vídeo do YouTube, reconhecimento de fala, tradução e texto para fala com suporte multilíngue
    keywords: Conversão de voz AI, tradução do YouTube, geração de legendas, fala para texto, texto para fala, clonagem de voz, tradução multilíngue, Alternativa ElevenLabs
    author: ABUS
    version: 2.0.0
    last-updated: 2025-02-23
    product-type: Software de processamento multimídia AI
    platforms: Windows
    technology-stack: Whisper, Edge-TTS, Gradio, CUDA, Faster-Whisper, Whisper-Timestamped, E2-TTS, F5-TTS, YouTube Downloader, Demucs, MDX-Net, RVC, CosyVoice, kokoro
    license: LGPL
-->

# Voice-Pro: Ferramenta Definitiva de Conversão de Voz por IA e Tradução Multilíngue 🔊

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md) ∙ [Deutsch](README.deu.md) ∙ [Español](README.spa.md) ∙ [Português](README.por.md)

[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/releases)

## 🎙️ Poderoso aplicativo da web com tecnologia AI para processamento de vídeo do YouTube, reconhecimento de fala, tradução e texto para fala com suporte multilíngue

Voice-Pro é um aplicativo web de ponta que transforma a criação de conteúdo multimídia. Ele integra download de vídeos do YouTube, separação de voz, reconhecimento de fala, tradução e conversão de texto em fala (TTS) em uma única ferramenta poderosa, oferecendo uma solução ideal para criadores, pesquisadores e profissionais multilíngues.

- 🔊 Reconhecimento de fala de alto nível: **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- 🎤 Clonagem de voz Zero-Shot: **F5-TTS**, **E2-TTS**, **CosyVoice**
- 📢 Conversão de texto em fala multilíngue: **Edge-TTS**, **kokoro**
- 🎥 Processamento de vídeos do YouTube e extração de áudio: **yt-dlp**
- 🌍 Tradução instantânea para mais de 100 idiomas: **Deep-Translator**
- 🔇 Separação vocal de nível profissional: **UVR5**
- 🔥 Criação de capas por IA: **RVC**

Como uma alternativa robusta ao **ElevenLabs**, o Voice-Pro capacita podcasters, desenvolvedores e criadores com soluções de voz avançadas.

## ⚠️ Observações
- O Voice-Pro foi atualizado para a versão **v2.x** (Python 3.10.15, Torch 2.5.1+cu124, Gradio 5.14.0)
- 🆓 A versão de teste gratuita suporta até **60 segundos** de processamento de mídia
- 🔥 Nova função **AI Cover** adicionada
- 🎤 Suporte para **CosyVoice** e **kokoro** incluído
- ⏳ Na primeira execução, será feito o download do **CozyVoice2-0.5B (9GB)**. Dependendo da velocidade da rede, pode levar mais de uma hora
- 🎧 Amostras de voz para clonagem serão continuamente atualizadas
- **Orientações:**
  - Atualização de v1.x para v2.x: **Impossível**. Portanto, recomenda-se excluir a pasta installer_files e executar a versão mais recente de start.bat.
  - Atualização de v2.x para v2.x: **Possível**. Baixe o código mais recente e execute update.bat.
  - Novos usuários: Consulte as instruções de instalação abaixo.
  - Solução de problemas: Na maioria dos casos, excluir a pasta **installer_files** e executar configure.bat e start.bat sequencialmente resolverá o problema.

## 🚄 Demonstrações

### Aba `Estúdio de Dublagem`: Transcrição, Tradução e TTS
<div aria-labelledby="studio-demo-description">
  <video src="https://github.com/user-attachments/assets/f18e7f54-7bc0-4c26-96f9-9f6b70c7114c" width="100%" style="max-width: 720px;" controls muted aria-describedby="studio-demo-description"></video>
  <p id="studio-demo-description">Demonstração do fluxo de trabalho completo de processamento de mídia na aba Estúdio: Mostra um processo contínuo de transformação de mídia, desde o download de vídeos do YouTube até a separação de vozes por IA, legendas automáticas com Whisper, tradução multilíngue e dublagem profissional usando F5-TTS.</p>
</div>

### Aba `F5-TTS-Multi`: Criação de Podcasts
<div aria-labelledby="tts-demo-description">
  <video src="https://github.com/user-attachments/assets/2d4b7d84-ca19-4efd-a847-a66fa0db616e" width="100%" style="max-width: 720px;" controls muted aria-describedby="tts-demo-description"></video>
  <p id="tts-demo-description">Demonstração da tecnologia inovadora de clonagem de voz por IA do F5-TTS: Apresenta uma tecnologia avançada de conversão de voz que imita precisamente as vozes reais de Mark Zuckerberg e Elon Musk para criar conteúdos totalmente novos.</p>
</div>

### Aba `AI Cover`
<div aria-labelledby="ai-cover-description">
  <video src="https://github.com/user-attachments/assets/88a47ab1-a18b-4779-97c8-7c1da84f5fc3" width="100%" style="max-width: 720px;" controls muted aria-describedby="ai-cover-description"></video>
  <p id="ai-cover-description">Cria uma versão de Trump para "Cupid" de IU, "Saudades de Você" de Kim Kwang-seok e "Carta de um Soldado".</p>
</div>

### Aba `Tradução ao Vivo`: Reconhecimento e Tradução em Tempo Real
<div aria-labelledby="translate-demo-description">
  <video src="https://github.com/user-attachments/assets/eb53dd3a-df0a-4f7f-819c-cf92d477e2d1" width="100%" style="max-width: 720px;" controls muted aria-describedby="translate-demo-description"></video>
  <p id="translate-demo-description">Demonstração da função de tradução multilíngue em tempo real: Apresenta um processo inovador de processamento de mídia multilíngue que captura instantaneamente conteúdos de notícias da BBC, gera legendas em tempo real e as traduz imediatamente para outros idiomas.</p>
</div>

## ⭐ Principais Recursos

### 1. Estúdio de Dublagem
- Download de vídeos do YouTube e extração de áudio
- Separação de voz com **MDX-Net** e **Demucs**
- Suporte para reconhecimento de fala e tradução em mais de 100 idiomas

### 2. Tecnologias de Voz
- **Fala para Texto:** **Whisper**, **Faster-Whisper**, **Whisper-Timestamped**
- **Texto para Fala:**
  - **Edge-TTS**: Mais de 100 idiomas, mais de 400 vozes
  - **E2-TTS**, **F5-TTS**, **CosyVoice**: Clonagem Zero-Shot
  - **kokoro**: 2º lugar no HuggingFace TTS Arena
- 🔥 **AI Cover (Fala para Fala):** Remoção vocal com **UVR5**, modulação com **RVC**

### 3. Tradução em Tempo Real
- Reconhecimento de fala instantâneo
- Tradução multilíngue em tempo real
- Entradas de áudio personalizáveis

## 🤖 Interface Web

### Aba `Estúdio de Dublagem`
- Centro integrado: Downloads do YouTube, remoção de ruído, legendas, tradução e TTS
- Suporta todos os formatos compatíveis com ffmpeg
- Opções de saída: WAV, FLAC, MP3
- Legendas e reconhecimento para mais de 100 idiomas
- TTS com ajustes de velocidade, volume e tom
<p align="center"><img style="width: 90%; height: 90%" src="images/main_page.por.png?raw=true" alt="Interface Web de Conversão de Voz Multilíngue e Geração de Legendas"/></p>

### Aba `Legendas Whisper`
- Foco em legendas: Mais de 90 idiomas
- Exibição de legendas integrada ao vídeo
- Destaque por palavra e opções de remoção de ruído

### Aba `Tradução`
- Tradução para mais de 100 idiomas
- Suporte a arquivos de legendas (ASS, SSA, SRT, etc.)
- Reconhecimento e tradução de voz em tempo real
<p align="center"><img style="width: 90%; height: 90%" src="images/live_translation_bbc.png?raw=true" alt="Interface Web para Reconhecimento de Fala e Tradução em Tempo Real"/></p>

### Aba `Geração de Voz`
- Opções: **Edge-TTS**, **F5-TTS**, **CosyVoice**, **kokoro**
- Podcasts com vozes de celebridades e suporte multilíngue
<p align="center"><img style="width: 90%; height: 90%" src="images/tts_f5_multi.png?raw=true" alt="Interface Web para Produção de Podcasts usando Tecnologia de Clonagem de Voz"/></p>

### 🔥 Aba `AI Cover`
- Remoção vocal: **MDX-Net**, **Demucs**
- Modulação de voz: **RVC**
- Faça download de vozes IA no [Discord AI Hub](https://discord.com/channels/1159260121998827560/@home) ou solicite por <abus.aikorea@gmail.com>
<p align="center"><img style="width: 90%; height: 90%" src="images/ai_cover.png?raw=true" alt="Interface Web para Produção de Podcasts usando Tecnologia de Clonagem de Voz"/></p>

## 💻 Requisitos do Sistema
- **SO:** Windows 10/11 (64 bits) ※ Linux/Mac não suportados
- **GPU:** NVIDIA com suporte a CUDA 12.4 (recomendado)
- **VRAM:** 4 GB ou mais (8 GB+ preferível)
- **RAM:** 4 GB ou mais
- **Armazenamento:** Pelo menos 20 GB de espaço livre
- **Internet:** Obrigatória

## 📀 Instalação

Instale o Voice-Pro facilmente com **configure.bat** e **start.bat**.

### 1. Preparação do Pacote
- Baixe a versão mais recente em [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/voice-pro)](https://github.com/abus-aikorea/voice-pro/) (**Source code (zip)**)
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
```

### 2. Instalação e Execução
1. 🚀 **configure.bat**
   - Instala git, ffmpeg e CUDA (se usar GPU NVIDIA)
   - Execute apenas uma vez; requer internet, pode levar mais de 1 hora
   - Não feche a janela de comando
2. 🚀 **start.bat**
   - Inicia a interface web do Voice-Pro
   - Na primeira execução, instala dependências (pode levar mais de 1 hora)
   - Em caso de problemas, delete **installer_files** e execute novamente

### 3. Atualização
- 🚀 **update.bat**: Atualiza o ambiente Python (mais rápido que reinstalar)

### 4. Desinstalação
- Execute **uninstall.bat** ou delete a pasta (instalação portátil)

## ❓ Dicas de Uso

#### Se o navegador não abrir automaticamente
- Feche a janela de comando do Windows e execute **start.bat** novamente
- Abra o navegador manualmente e insira o endereço exibido na janela de comando (ex.: **http://127.0.0.1:7892**)

#### Se ocorrer um erro CUDA Out-of-Memory
- Verifique o status da memória da GPU no Gerenciador de Tarefas do Windows - guia "Desempenho"
- Defina o nível de remoção de ruído para 0 ou 1 (o nível 2 requer pelo menos 8 GB de memória GPU)
- Configure o tipo de cálculo como "int" (o tipo "float" tem melhor qualidade, mas exige mais memória GPU)

#### Como melhorar a qualidade das legendas?
- Modelos Whisper maiores tendem a melhorar a qualidade das legendas (large > medium > small > base > tiny), mas isso não é garantido
- Entre os tipos de cálculo, "float" oferece bom desempenho; "int" reduz o uso da GPU e aumenta a velocidade por meio de quantização do modelo, mas com perda de desempenho
- Aumentar o nível de remoção de ruído elimina mais sons de fundo e usa apenas a voz restante para reconhecimento, mas não garante sempre bons resultados

## 📢 Avisos

O Windows Defender pode exibir um aviso sobre um aplicativo não confiável e impedir a execução adicional do Voice-Pro.
- **Configuração "Aviso" do SmartScreen:** Clique em "Mais informações" e depois em "Executar mesmo assim"
- **Configuração "Bloquear" do SmartScreen:** Abra as propriedades do **start.bat**, marque "Desbloquear", aplique as alterações e execute novamente o **start.bat**
<p align="center"><img style="width: 40%; height: 40%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/></p>

Quando o Windows Defender reconhece erroneamente um arquivo em lote como um Trojan, isso é frequentemente chamado de "Falso Positivo". Para resolver esse problema, siga estas etapas:
1. **Tratamento de exceções de arquivo:** No Windows Defender, você pode configurar arquivos ou processos específicos para ignorar a verificação de segurança. Siga os passos abaixo:
   - Clique no botão "Iniciar" e vá para "Configurações"
   - Clique em "Atualização e Segurança"
   - Selecione "Segurança do Windows" e vá para "Proteção contra vírus e ameaças"
   - Clique em "Gerenciar configurações de proteção contra vírus e ameaças"
   - Selecione "Adicionar uma exclusão" em "Configurações de proteção contra vírus e ameaças"
   - Escolha "Arquivo ou Pasta", localize o arquivo em lote problemático e adicione-o como exceção
2. **Desativar temporariamente o Windows Defender:** Isso pode ser uma solução temporária. No entanto, tome cuidado ao usar esse método, pois seu computador pode ficar exposto a outras ameaças
3. **Reportar o problema ao software antivírus:** Se você tiver certeza de que o arquivo não é um Trojan, pode reportá-lo à Microsoft como "Falso Positivo". A Microsoft revisará e tomará as medidas necessárias


## 🚨 Aviso
- Este repositório oferece uma **versão de teste gratuita** do Voice-Pro.
- A versão de teste gratuita do Voice-Pro permite processar até **60 segundos** de mídia.
- A versão oficial do Voice-Pro pode ser adquirida através do site oficial da ABUS (<https://abuskorea.imweb.me>).


## ☕ Contribuições
- Se você deseja participar e nos ajudar com este projeto, sinta-se à vontade para criar um [Issues](https://github.com/abus-aikorea/voice-pro/issues).
- Se algo der errado, envie um [Pull requests](https://github.com/abus-aikorea/voice-pro/pulls) para melhorar este projeto.
- Qualquer tipo de contribuição é bem-vindo.
- Para dúvidas relacionadas a compras, parcerias comerciais, ajustes técnicos, investimentos e outros assuntos, entre em contato conosco por e-mail (<abus.aikorea@gmail.com>).
- Se você gosta deste projeto, por favor, dê uma estrela a este repositório. Nós agradeceríamos muito. ⭐⭐⭐
- Você pode apoiar o Voice-Pro com uma doação aqui:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abus)



## 📬 Contato
- E-mail: <abus.aikorea@gmail.com>
- Página inicial (Coreano): <https://abuskorea.imweb.me>
- Amazon: [US](https://www.amazon.com/dp/B0DBR69JPL) | [Japan](https://www.amazon.co.jp/dp/B0DBVRJ542) | [Singapore](https://www.amazon.sg/dp/B0DCGKL8R4) | [UAE](https://www.amazon.ae/dp/B0DCGKM7FF)
- Naver: [Software](https://smartstore.naver.com/abus/products/10385660040) | [Solução](https://smartstore.naver.com/abus/products/10298346364)

## 👍 YouTube
- [Informações do Produto](https://www.youtube.com/watch?v=z8g8LMhoh_o&list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq)
- [Karaokê: Pop](https://www.youtube.com/watch?v=MqQP3ewvJUk&list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6) | [K-Pop](https://www.youtube.com/watch?v=v6qjf_ELsLA&list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8) | [J-Pop](https://www.youtube.com/watch?v=KKLzoWHFAxw&list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq)

## 🙏 Créditos
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

## ©️ Direitos Autorais
<img src="images/ABUS-logo.jpg" width="100" height="100"> por [ABUS](https://abuskorea.imweb.me)