# 🔐 Voice-Pro Watermark System - Hướng Dẫn Chi Tiết

## 📋 Tổng Quan

Hệ thống watermark cho Voice-Pro giúp bảo vệ bản quyền cho nội dung video/audio với các tính năng:

- ✅ **Text Watermark** - Chữ hiển thị trên video
- ✅ **Logo Watermark** - Logo/hình ảnh overlay
- ✅ **Audio Watermark** - Invisible watermark cho audio (steganography)
- ✅ **Batch Processing** - Xử lý hàng loạt
- ✅ **Auto Integration** - Tự động apply sau processing
- ✅ **Customizable** - Tùy chỉnh vị trí, opacity, size, etc.

---

## 🎯 Use Cases

| Scenario | Giải pháp | Benefit |
|----------|-----------|---------|
| 🎬 Content Creator | Text + Logo watermark | Branding & Copyright |
| 🎙️ Podcast Producer | Audio watermark | Track unauthorized distribution |
| 📺 YouTube Channel | YouTube preset | Professional look, avoid UI overlap |
| 🏢 Corporate Video | Professional preset | Company branding |
| 🎓 Educational Content | Subtle preset | Non-intrusive but protected |

---

## 🚀 Quick Start

### **1. Cài Đặt Dependencies**

```bash
# Voice-Pro đã có sẵn hầu hết dependencies
# Chỉ cần đảm bảo có ffmpeg và numpy, soundfile

pip install numpy soundfile json5
```

### **2. Basic Usage - CLI**

#### **Text Watermark:**
```bash
python watermark_manager.py \
    --input video.mp4 \
    --text "© 2025 My Company"
```

#### **Logo Watermark:**
```bash
python watermark_manager.py \
    --input video.mp4 \
    --logo ./assets/logo.png
```

#### **Combined (Text + Logo):**
```bash
python watermark_manager.py \
    --input video.mp4 \
    --text "© 2025 My Company" \
    --logo ./assets/logo.png \
    --text-position bottom_right \
    --logo-position top_right
```

#### **Batch Processing:**
```bash
python watermark_manager.py \
    --batch videos/*.mp4 \
    --text "© 2025 My Company" \
    --logo ./assets/logo.png
```

### **3. Python API Usage**

```python
from watermark_manager import (
    WatermarkManager,
    TextWatermarkConfig,
    ImageWatermarkConfig,
    WatermarkPosition
)

# Tạo manager
manager = WatermarkManager(output_dir="./watermarked")

# Text watermark
text_config = TextWatermarkConfig(
    text="© 2025 My Company",
    font_size=32,
    position=WatermarkPosition.BOTTOM_RIGHT,
    opacity=0.7
)

output = manager.add_text_watermark("video.mp4", text_config)
print(f"Output: {output}")

# Logo watermark
logo_config = ImageWatermarkConfig(
    image_path="./assets/logo.png",
    position=WatermarkPosition.TOP_RIGHT,
    opacity=0.8,
    scale=0.15
)

output = manager.add_image_watermark("video.mp4", logo_config)

# Combined
output = manager.add_combined_watermark(
    "video.mp4",
    text_config=text_config,
    image_config=logo_config
)
```

---

## ⚙️ Configuration

### **Config File: `watermark_config.json5`**

```json5
{
    // Text watermark
    text_watermark: {
        enabled: true,
        text: "© 2025 Voice-Pro",
        position: "bottom_right",  // top_left, top_right, center, etc.
        font_size: 24,
        font_color: "white",
        opacity: 0.5,
        margin_x: 10,
        margin_y: 10,
        shadow: true,
        background_color: null,  // "black" for background box
        background_opacity: 0.3
    },

    // Logo watermark
    logo_watermark: {
        enabled: true,
        image_path: "./assets/logo.png",
        position: "top_right",
        opacity: 0.7,
        scale: 0.15,  // 0.1 = 10% size, 1.0 = 100% size
        margin_x: 10,
        margin_y: 10
    },

    // Audio watermark (invisible)
    audio_watermark: {
        enabled: false,
        watermark_text: "VoicePro_Audio_2025",
        method: "lsb",  // Least Significant Bit
        strength: 0.1
    },

    // Batch settings
    batch: {
        enabled: true,
        skip_existing: true,
        output_dir: "./watermarked"
    }
}
```

### **Sử dụng Config:**

```python
from voicepro_watermark_integration import VoiceProWatermarkIntegration

# Load config và process
integration = VoiceProWatermarkIntegration("watermark_config.json5")
output = integration.process_video("video.mp4")
```

---

## 🎨 Customization Options

### **1. Text Watermark Options**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `text` | string | - | Text hiển thị |
| `position` | enum | bottom_right | Vị trí (8 positions) |
| `font_size` | int | 24 | Kích thước font (px) |
| `font_color` | string | white | Màu font |
| `opacity` | float | 0.5 | Độ trong suốt (0.0-1.0) |
| `margin_x` | int | 10 | Khoảng cách từ cạnh ngang |
| `margin_y` | int | 10 | Khoảng cách từ cạnh dọc |
| `shadow` | bool | true | Bóng đổ |
| `background_color` | string | null | Màu nền (optional) |

**Positions available:**
- `top_left`, `top_center`, `top_right`
- `center`
- `bottom_left`, `bottom_center`, `bottom_right`

### **2. Logo Watermark Options**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `image_path` | string | - | Đường dẫn logo PNG/JPG |
| `position` | enum | top_right | Vị trí |
| `opacity` | float | 0.7 | Độ trong suốt (0.0-1.0) |
| `scale` | float | 0.15 | Scale logo (0.1-2.0) |
| `margin_x` | int | 10 | Khoảng cách cạnh ngang |
| `margin_y` | int | 10 | Khoảng cách cạnh dọc |

**Logo requirements:**
- Format: PNG (with transparency), JPG, BMP
- Recommended: PNG với transparent background
- Size: Bất kỳ (sẽ scale tự động)

### **3. Audio Watermark Options**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `watermark_text` | string | - | Text embed vào audio |
| `method` | string | lsb | Method: lsb, phase |
| `strength` | float | 0.1 | Cường độ (0.0-1.0) |

**Notes:**
- Audio watermark là **invisible** - không nghe thấy
- Dùng để tracking unauthorized distribution
- Trade-off: Strength cao = robust hơn nhưng có thể audible

---

## 📐 Position Examples

```
┌─────────────────────────────────────┐
│ top_left    top_center    top_right │
│                                     │
│                                     │
│              center                 │
│                                     │
│                                     │
│ bottom_left  bottom_center  bottom_right │
└─────────────────────────────────────┘
```

---

## 🎯 Presets

Hệ thống có sẵn 4 presets:

### **1. Subtle** - Tinh tế, không làm phiền người xem
```json5
subtle: {
    text: {opacity: 0.3, font_size: 18},
    logo: {opacity: 0.5, scale: 0.1}
}
```
**Use case:** Educational videos, professional content

### **2. Strong** - Nổi bật, bảo vệ mạnh
```json5
strong: {
    text: {opacity: 0.8, font_size: 32},
    logo: {opacity: 0.9, scale: 0.2}
}
```
**Use case:** Preventing piracy, watermark samples

### **3. Professional** - Professional branding
```json5
professional: {
    text: {
        text: "© {year} Your Company",
        position: "bottom_right",
        opacity: 0.6,
        background_color: "black"
    },
    logo: {position: "top_left", opacity: 0.7}
}
```
**Use case:** Corporate videos, marketing content

### **4. YouTube** - Tối ưu cho YouTube
```json5
youtube: {
    text: {
        position: "bottom_center",
        margin_y: 80  // Tránh YouTube controls
    }
}
```
**Use case:** YouTube uploads

**Sử dụng preset:**
```bash
# CLI
python voicepro_watermark_integration.py \
    --input video.mp4 \
    --preset professional

# Python
integration.process_video("video.mp4", preset="professional")
```

---

## 🔗 Tích Hợp Vào Voice-Pro Pipeline

### **Method 1: Manual Integration**

Chỉnh sửa Voice-Pro processing pipeline:

```python
# Trong file xử lý chính (vd: abus_app_voice.py)
from voicepro_watermark_integration import watermark_dubbed_video

# Sau khi dubbing xong
dubbed_video = process_dubbing(input_video)

# Apply watermark
final_video = watermark_dubbed_video(dubbed_video)

return final_video
```

### **Method 2: Auto Hook** (Recommended)

Enable trong config:

```json5
{
    integration: {
        auto_apply: true,  // Tự động apply
        apply_to: {
            dubbed_video: true,
            extracted_audio: false,
            subtitle_burn: true
        }
    }
}
```

Sử dụng hook:

```python
from voicepro_watermark_integration import auto_watermark_hook

# Sau processing step
output_video = auto_watermark_hook(processed_video, 'dubbed_video')
```

### **Method 3: Gradio UI Integration**

Thêm vào Gradio UI:

```python
import gradio as gr
from voicepro_watermark_integration import VoiceProWatermarkIntegration

def process_with_watermark(video_file, watermark_text, logo_file):
    integration = VoiceProWatermarkIntegration()

    # Update config với user input
    integration.config['text_watermark']['text'] = watermark_text
    if logo_file:
        integration.config['logo_watermark']['image_path'] = logo_file
        integration.config['logo_watermark']['enabled'] = True

    output = integration.process_video(video_file)
    return output

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Watermark Settings")

    video_input = gr.Video()
    watermark_text = gr.Textbox(label="Watermark Text", value="© 2025")
    logo_upload = gr.File(label="Upload Logo (optional)")

    output_video = gr.Video()

    btn = gr.Button("Apply Watermark")
    btn.click(
        process_with_watermark,
        inputs=[video_input, watermark_text, logo_upload],
        outputs=output_video
    )
```

---

## 💡 Advanced Features

### **1. Dynamic Text**

Text tự động thay đổi theo video:

```json5
{
    text_watermark: {
        dynamic_text: {
            enabled: true,
            template: "© {year} {company} | Processed: {timestamp}"
        }
    }
}
```

Variables available:
- `{year}` - Năm hiện tại
- `{date}` - Ngày hiện tại (YYYY-MM-DD)
- `{timestamp}` - Timestamp (YYYYMMdd_HHMMSS)
- `{company}` - Company name từ config

### **2. Multiple Watermarks**

Apply nhiều text watermarks ở các vị trí khác nhau:

```python
# Watermark 1: Copyright ở bottom right
text_config1 = TextWatermarkConfig(
    text="© 2025 Company",
    position=WatermarkPosition.BOTTOM_RIGHT
)

# Watermark 2: Website ở top left
text_config2 = TextWatermarkConfig(
    text="www.company.com",
    position=WatermarkPosition.TOP_LEFT,
    font_size=18,
    opacity=0.4
)

# Apply tuần tự
temp = manager.add_text_watermark(video, text_config1)
final = manager.add_text_watermark(temp, text_config2)
```

### **3. Animated Watermark** (Advanced)

Fade in/out effect:

```bash
# Watermark fade in trong 2 giây đầu
ffmpeg -i input.mp4 \
    -vf "drawtext=text='Watermark':enable='between(t,0,2)':alpha='t/2'" \
    output.mp4
```

Note: Hiện tại cần custom ffmpeg command, có thể extend trong future versions.

### **4. Conditional Watermark**

Apply watermark dựa trên điều kiện:

```python
def conditional_watermark(video_path, video_duration, video_quality):
    """Apply different watermark based on video properties"""

    integration = VoiceProWatermarkIntegration()

    # Short videos: subtle
    if video_duration < 60:
        preset = "subtle"
    # Long videos: professional
    elif video_duration > 300:
        preset = "professional"
    # HD videos: strong
    elif video_quality == "HD":
        preset = "strong"
    else:
        preset = None

    return integration.process_video(video_path, preset=preset)
```

---

## 📊 Performance & Quality

### **Processing Time**

| Resolution | Duration | Text Only | Text + Logo | Estimated Time |
|------------|----------|-----------|-------------|----------------|
| 720p | 1 min | ✅ Fast | ✅ Fast | 10-15 sec |
| 1080p | 1 min | ✅ Fast | ⚠️ Medium | 15-25 sec |
| 1080p | 5 min | ⚠️ Medium | ⚠️ Medium | 60-90 sec |
| 4K | 1 min | ⚠️ Slow | 🔴 Slow | 45-60 sec |

**Optimization tips:**
- Text watermark nhanh hơn logo watermark
- Batch processing: Use max_workers=3-5
- Pre-optimize logo (resize trước, dùng PNG optimized)

### **Quality Settings**

```python
# High quality (default)
# - Video codec: libx264
# - CRF: 18 (lossless visual)

# Medium quality (faster)
# - CRF: 23

# Low quality (fastest, smaller file)
# - CRF: 28
```

Customize trong ffmpeg command nếu cần.

---

## 🛠️ Troubleshooting

### **Problem 1: FFmpeg not found**

**Error:** `ffmpeg: command not found`

**Solution:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### **Problem 2: Logo không hiển thị**

**Error:** Logo không xuất hiện trên video

**Checklist:**
- ✅ Check logo file tồn tại: `ls -la logo.png`
- ✅ Check logo format: Dùng PNG với alpha channel
- ✅ Check logo size: Không quá nhỏ (min 100x100px)
- ✅ Check opacity: Không quá trong suốt (<0.3)
- ✅ Check position: Có thể bị crop nếu video nhỏ

**Debug:**
```python
# Test logo riêng
logo_config = ImageWatermarkConfig(
    image_path="logo.png",
    position=WatermarkPosition.CENTER,  # Test ở center
    opacity=1.0,  # Full opacity
    scale=0.5  # Large scale
)
```

### **Problem 3: Text bị crop**

**Error:** Text watermark bị cắt ở edge

**Solution:**
```python
# Tăng margin
text_config = TextWatermarkConfig(
    text="Long watermark text",
    margin_x=30,  # Increase from 10
    margin_y=30,
    font_size=20  # Giảm font size nếu cần
)
```

### **Problem 4: Video quality giảm**

**Error:** Video sau watermark bị mờ/pixelated

**Solution:**
```bash
# Thêm quality settings vào ffmpeg command
# Edit watermark_manager.py, thêm:
'-crf', '18',  # Lower = better quality (default: 23)
'-preset', 'slow',  # Better compression
```

### **Problem 5: Processing quá chậm**

**Solutions:**
1. **Use hardware acceleration:**
   ```bash
   # NVIDIA GPU
   -c:v h264_nvenc

   # Intel Quick Sync
   -c:v h264_qsv

   # AMD
   -c:v h264_amf
   ```

2. **Batch processing optimization:**
   ```python
   # Giảm workers nếu RAM/CPU cao
   manager = WatermarkManager()
   outputs = manager.batch_watermark(videos, max_workers=2)
   ```

3. **Pre-process logo:**
   ```bash
   # Resize logo trước
   ffmpeg -i logo.png -vf scale=200:-1 logo_small.png
   ```

---

## 📚 Examples

### **Example 1: YouTube Content Creator**

```python
from voicepro_watermark_integration import VoiceProWatermarkIntegration

# Setup
integration = VoiceProWatermarkIntegration()

# Update config
integration.config['text_watermark'].update({
    'text': '© 2025 MyChannel | Subscribe!',
    'position': 'bottom_center',
    'margin_y': 80,  # Avoid YouTube controls
    'font_size': 22,
    'opacity': 0.6
})

integration.config['logo_watermark'].update({
    'enabled': True,
    'image_path': './channel_logo.png',
    'position': 'top_left',
    'scale': 0.12,
    'opacity': 0.8
})

# Process all videos in folder
import glob
videos = glob.glob('./videos/*.mp4')

for video in videos:
    output = integration.process_video(video)
    print(f"Processed: {output}")
```

### **Example 2: Corporate Training Videos**

```python
# Professional preset with company branding
integration = VoiceProWatermarkIntegration()

# Custom text with background
integration.config['text_watermark'].update({
    'text': '© 2025 ACME Corp - Internal Training',
    'position': 'bottom_right',
    'background_color': 'black',
    'background_opacity': 0.5,
    'font_color': 'white',
    'opacity': 0.9
})

# Company logo
integration.config['logo_watermark'].update({
    'enabled': True,
    'image_path': './acme_logo.png',
    'position': 'top_right',
    'scale': 0.18
})

output = integration.process_video('training_video.mp4', preset='professional')
```

### **Example 3: Podcast Audio Protection**

```python
# Invisible audio watermark
integration = VoiceProWatermarkIntegration()

integration.config['audio_watermark'].update({
    'enabled': True,
    'watermark_text': 'MyPodcast_Episode123_2025',
    'strength': 0.15
})

# Process audio
output = integration.process_audio('podcast_ep123.mp3')

# Watermark không nghe thấy nhưng có thể detect bằng tools
# Dùng để track unauthorized distribution
```

### **Example 4: Batch Processing với Custom Settings**

```python
from watermark_manager import WatermarkManager, TextWatermarkConfig
from pathlib import Path

manager = WatermarkManager(output_dir='./watermarked_batch')

# Different watermark for each video
videos = Path('./videos').glob('*.mp4')

for i, video in enumerate(videos):
    # Custom text with video number
    text_config = TextWatermarkConfig(
        text=f'© 2025 | Video #{i+1}',
        position=WatermarkPosition.BOTTOM_RIGHT,
        opacity=0.6
    )

    output = manager.add_text_watermark(str(video), text_config)
    print(f'[{i+1}] {output}')
```

---

## 🔐 Security Best Practices

### **1. Watermark cho Copyright Protection**

```python
# Strong, visible watermark
text_config = TextWatermarkConfig(
    text='© 2025 Company - DO NOT REDISTRIBUTE',
    font_size=36,
    opacity=0.8,
    position=WatermarkPosition.CENTER,
    background_color='black',
    background_opacity=0.6
)
```

### **2. Watermark cho Tracking**

```python
# Unique ID cho mỗi video/user
import uuid

unique_id = str(uuid.uuid4())[:8]
text_config = TextWatermarkConfig(
    text=f'ID:{unique_id}',
    font_size=16,
    opacity=0.3,  # Subtle
    position=WatermarkPosition.TOP_LEFT
)

# Log ID for tracking
with open('watermark_log.txt', 'a') as f:
    f.write(f'{datetime.now()},{video_path},{unique_id}\n')
```

### **3. Multi-layer Protection**

```python
# Layer 1: Visible text watermark
# Layer 2: Subtle logo watermark
# Layer 3: Invisible audio watermark

# Visible
text_config = TextWatermarkConfig(text='© 2025 Company', opacity=0.6)

# Subtle logo
logo_config = ImageWatermarkConfig(
    image_path='./watermark.png',
    opacity=0.3,  # Very subtle
    scale=0.1
)

# Video watermark
video_output = manager.add_combined_watermark(video, text_config, logo_config)

# Audio watermark
audio_config = AudioWatermarkConfig(
    watermark_text=f'Copyright_{unique_id}',
    strength=0.1
)
final_output = manager.add_audio_watermark(video_output, audio_config)
```

---

## 📈 Roadmap

### **Planned Features:**

- [ ] **Animation effects** - Fade in/out, slide, pulse
- [ ] **Rotating watermark** - Thay đổi vị trí theo thời gian
- [ ] **QR code watermark** - Embed QR code
- [ ] **Blockchain integration** - NFT watermarking
- [ ] **AI-based watermark** - Robust to video editing
- [ ] **GUI application** - Standalone watermark tool
- [ ] **Batch templates** - Save and reuse configurations
- [ ] **Cloud processing** - API for remote watermarking

---

## 🤝 Contributing

Muốn đóng góp? Tạo PR hoặc issue tại:
- GitHub: https://github.com/abus-aikorea/voice-pro

---

## 📞 Support

- Email: abus.aikorea@gmail.com
- Issues: https://github.com/abus-aikorea/voice-pro/issues

---

## 📄 License

LGPL - Same as Voice-Pro

---

**Prepared by**: Claude (Anthropic AI)
**Date**: 2025-11-13
**Version**: 1.0
