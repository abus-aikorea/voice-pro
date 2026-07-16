# 🔐 Voice-Pro Watermark System

## Quick Start

### 1️⃣ Simple Text Watermark
```bash
python watermark_manager.py --input video.mp4 --text "© 2025 My Company"
```

### 2️⃣ Logo Watermark
```bash
python watermark_manager.py --input video.mp4 --logo ./assets/logo.png
```

### 3️⃣ Combined (Text + Logo)
```bash
python watermark_manager.py \
    --input video.mp4 \
    --text "© 2025 My Company" \
    --logo ./assets/logo.png
```

---

## 📁 Files

| File | Purpose |
|------|---------|
| `watermark_manager.py` | Core watermark engine |
| `voicepro_watermark_integration.py` | Integration với Voice-Pro |
| `watermark_config.json5` | Configuration file |
| `watermark_examples.py` | 10 examples |
| `WATERMARK_GUIDE.md` | Documentation đầy đủ (40+ trang) |

---

## 🎯 Features

- ✅ **Text Watermark** - Customizable font, color, position, opacity
- ✅ **Logo Watermark** - PNG/JPG overlay với alpha channel
- ✅ **Audio Watermark** - Invisible steganography
- ✅ **Batch Processing** - Process nhiều files
- ✅ **4 Presets** - Subtle, Strong, Professional, YouTube
- ✅ **Auto Integration** - Tích hợp tự động vào Voice-Pro pipeline

---

## 📖 Documentation

**Chi tiết:** [WATERMARK_GUIDE.md](WATERMARK_GUIDE.md)

**Quick links:**
- [Configuration Options](WATERMARK_GUIDE.md#-configuration)
- [Customization](WATERMARK_GUIDE.md#-customization-options)
- [Presets](WATERMARK_GUIDE.md#-presets)
- [Integration](WATERMARK_GUIDE.md#-tích-hợp-vào-voice-pro-pipeline)
- [Examples](WATERMARK_GUIDE.md#-examples)
- [Troubleshooting](WATERMARK_GUIDE.md#-troubleshooting)

---

## 🚀 Examples

Run interactive examples:
```bash
python watermark_examples.py
```

Or run specific example:
```bash
python watermark_examples.py 1   # Simple text
python watermark_examples.py 4   # Combined
python watermark_examples.py 7   # Presets
```

---

## ⚙️ Configuration

Edit `watermark_config.json5`:

```json5
{
    text_watermark: {
        enabled: true,
        text: "© 2025 Your Company",
        position: "bottom_right",
        opacity: 0.6
    },
    logo_watermark: {
        enabled: true,
        image_path: "./assets/logo.png",
        position: "top_right",
        scale: 0.15
    }
}
```

---

## 🔗 Integration với Voice-Pro

### Method 1: Manual
```python
from voicepro_watermark_integration import watermark_dubbed_video

# Sau khi dubbing
output = watermark_dubbed_video(dubbed_video)
```

### Method 2: Auto Hook
```python
from voicepro_watermark_integration import auto_watermark_hook

# Auto apply
output = auto_watermark_hook(video, 'dubbed_video')
```

---

## 📊 Performance

| Resolution | Duration | Processing Time |
|------------|----------|-----------------|
| 720p | 1 min | ~15 sec |
| 1080p | 1 min | ~25 sec |
| 1080p | 5 min | ~90 sec |

---

## 🎨 Presets

| Preset | Use Case |
|--------|----------|
| **subtle** | Educational, professional content |
| **strong** | Anti-piracy, watermark samples |
| **professional** | Corporate videos, marketing |
| **youtube** | YouTube uploads (avoid UI overlap) |

Usage:
```bash
python voicepro_watermark_integration.py --input video.mp4 --preset professional
```

---

## 🛠️ Requirements

- ✅ FFmpeg (auto-detect)
- ✅ Python 3.7+
- ✅ numpy, soundfile (cho audio watermark)
- ✅ json5 (optional, for config)

Install:
```bash
pip install numpy soundfile json5
```

---

## 💡 Tips

1. **Logo format:** Use PNG with transparent background
2. **Position:** Avoid corners on mobile videos
3. **Opacity:** 0.5-0.7 for subtle, 0.8+ for strong
4. **YouTube:** Use bottom_center position with margin_y=80
5. **Batch:** Use workers=3-5 for optimal speed

---

## 🐛 Troubleshooting

**FFmpeg not found?**
```bash
sudo apt install ffmpeg  # Ubuntu
brew install ffmpeg      # macOS
```

**Logo không hiển thị?**
- Check file exists
- Use PNG format
- Increase opacity to 1.0
- Test at CENTER position

**Video quality giảm?**
- Tăng CRF trong code (lower = better)
- Use preset='slow' for better compression

**More:** [Troubleshooting Guide](WATERMARK_GUIDE.md#-troubleshooting)

---

## 📞 Support

- **Email:** abus.aikorea@gmail.com
- **Issues:** https://github.com/abus-aikorea/voice-pro/issues
- **Docs:** [WATERMARK_GUIDE.md](WATERMARK_GUIDE.md)

---

## 📄 License

LGPL - Same as Voice-Pro

---

**Version:** 1.0.0
**Date:** 2025-11-13
**Author:** Claude (Anthropic AI) for Voice-Pro
