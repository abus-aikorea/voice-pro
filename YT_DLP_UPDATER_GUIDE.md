# 🚀 YT-DLP Auto-Updater for Voice-Pro

## 📋 Tổng Quan

Hệ thống tự động tải và cập nhật yt-dlp mới nhất mỗi khi chạy Voice-Pro.

### ✨ Features

- ✅ **Auto-detect** version mới nhất từ GitHub
- ✅ **Cross-platform** (Windows, Linux, macOS)
- ✅ **Smart update** - Chỉ update khi cần
- ✅ **Backup** - Tự động backup version cũ
- ✅ **Fallback** - Khôi phục nếu update fail
- ✅ **FFmpeg check** - Kiểm tra FFmpeg availability
- ✅ **Logging** - Log đầy đủ mọi hoạt động

---

## 🎯 Why Auto-Update?

### **Vấn đề:**
- YouTube thường xuyên thay đổi API
- yt-dlp cũ → download fail
- Phải manual update → mất thời gian

### **Giải pháp:**
- ✅ Tự động check version mới nhất
- ✅ Tự động download nếu cần
- ✅ Luôn sử dụng yt-dlp mới nhất
- ✅ Không lo YouTube API changes

---

## 🚀 Quick Start

### **1. Standalone Usage**

```bash
# Update yt-dlp
python yt_dlp_updater.py --update

# Check version
python yt_dlp_updater.py --check

# Force update
python yt_dlp_updater.py --update --force

# Check all dependencies
python yt_dlp_updater.py --check-all
```

### **2. Integrated với Voice-Pro**

```bash
# Chạy Voice-Pro với auto-update (recommended)
python start-voice-with-updater.py

# Chạy không auto-update
python start-voice-with-updater.py --no-ytdlp-update
```

### **3. Batch Processing với Auto-Update**

```bash
# Batch process với auto-update
python batch_url_processor_auto.py --file urls.txt

# Skip auto-update
python batch_url_processor_auto.py --file urls.txt --no-ytdlp-update
```

---

## ⚙️ How It Works

### **Update Flow:**

```
┌─────────────────────────────────────────┐
│ 1. Check current version                │
│    yt-dlp --version                     │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│ 2. Fetch latest version from GitHub    │
│    API: github.com/yt-dlp/releases      │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│ 3. Compare versions                     │
│    Current == Latest?                   │
└──────────────┬──────────────────────────┘
               ▼
       ┌───────┴───────┐
       │               │
    [Same]          [Different]
       │               │
       ▼               ▼
  ✓ Skip       ┌───────────────┐
               │ 4. Backup old │
               │ 5. Download   │
               │ 6. Verify     │
               └───────────────┘
```

### **Version Checking:**

```python
from yt_dlp_updater import YtDlpUpdater

updater = YtDlpUpdater()

# Check versions
current = updater.get_current_version()
# → "2024.11.10"

latest = updater.get_latest_version()
# → "2024.11.13"

# Is update needed?
need_update, current, latest = updater.is_update_needed()
# → (True, "2024.11.10", "2024.11.13")
```

---

## 📖 API Documentation

### **Class: YtDlpUpdater**

#### **Constructor**

```python
updater = YtDlpUpdater(install_dir=None)
```

**Parameters:**
- `install_dir` (str, optional): Thư mục cài đặt yt-dlp (default: current dir)

#### **Methods**

**`get_current_version() -> Optional[str]`**
```python
version = updater.get_current_version()
# Returns: "2024.11.13" or None
```

**`get_latest_version() -> Optional[str]`**
```python
version = updater.get_latest_version()
# Returns: "2024.11.13" or None
```

**`is_update_needed() -> Tuple[bool, Optional[str], Optional[str]]`**
```python
need_update, current, latest = updater.is_update_needed()
# Returns: (True, "2024.11.10", "2024.11.13")
```

**`download_ytdlp(force=False) -> bool`**
```python
success = updater.download_ytdlp(force=True)
# Returns: True if successful
```

**`ensure_ytdlp(auto_update=True) -> bool`**
```python
# Đảm bảo yt-dlp sẵn sàng (download nếu chưa có, update nếu cần)
success = updater.ensure_ytdlp(auto_update=True)
# Returns: True if yt-dlp ready
```

**`get_ytdlp_path() -> str`**
```python
path = updater.get_ytdlp_path()
# Returns: "/path/to/yt-dlp" or "/path/to/yt-dlp.exe"
```

### **Class: FFmpegChecker**

#### **Static Methods**

**`is_available() -> bool`**
```python
if FFmpegChecker.is_available():
    print("FFmpeg OK")
```

**`get_version() -> Optional[str]`**
```python
version = FFmpegChecker.get_version()
# Returns: "4.4.2" or None
```

**`get_install_instructions() -> str`**
```python
if not FFmpegChecker.is_available():
    print(FFmpegChecker.get_install_instructions())
```

**`ensure_ffmpeg() -> bool`**
```python
if FFmpegChecker.ensure_ffmpeg():
    print("FFmpeg ready")
```

### **Helper Functions**

**`auto_update_ytdlp(install_dir=None, force=False) -> bool`**
```python
from yt_dlp_updater import auto_update_ytdlp

# Quick auto-update
success = auto_update_ytdlp()
```

**`check_dependencies(install_dir=None, auto_update_ytdlp=True) -> Tuple[bool, bool]`**
```python
from yt_dlp_updater import check_dependencies

# Check both yt-dlp and ffmpeg
ytdlp_ok, ffmpeg_ok = check_dependencies(auto_update_ytdlp=True)
```

---

## 💡 Usage Examples

### **Example 1: Simple Update**

```python
from yt_dlp_updater import YtDlpUpdater

# Create updater
updater = YtDlpUpdater()

# Update yt-dlp
if updater.download_ytdlp():
    print("✓ Updated successfully")
else:
    print("✗ Update failed")
```

### **Example 2: Check Before Update**

```python
from yt_dlp_updater import YtDlpUpdater

updater = YtDlpUpdater()

# Check if update needed
need_update, current, latest = updater.is_update_needed()

if need_update:
    print(f"Update available: {current} → {latest}")
    updater.download_ytdlp()
else:
    print(f"Already latest: {current}")
```

### **Example 3: Ensure yt-dlp Ready**

```python
from yt_dlp_updater import YtDlpUpdater

updater = YtDlpUpdater()

# Ensure yt-dlp sẵn sàng (download + update nếu cần)
if updater.ensure_ytdlp(auto_update=True):
    # Use yt-dlp
    ytdlp_path = updater.get_ytdlp_path()
    print(f"yt-dlp ready at: {ytdlp_path}")
```

### **Example 4: Check All Dependencies**

```python
from yt_dlp_updater import check_dependencies

# Check yt-dlp + ffmpeg
ytdlp_ok, ffmpeg_ok = check_dependencies(auto_update_ytdlp=True)

if ytdlp_ok and ffmpeg_ok:
    print("✓ All dependencies ready")
    # Proceed with processing
else:
    print("✗ Missing dependencies")
    if not ytdlp_ok:
        print("  - yt-dlp missing")
    if not ffmpeg_ok:
        print("  - FFmpeg missing")
```

### **Example 5: Custom Install Directory**

```python
from yt_dlp_updater import YtDlpUpdater

# Install yt-dlp vào custom directory
updater = YtDlpUpdater(install_dir="./tools")

updater.ensure_ytdlp(auto_update=True)

# Get path
ytdlp_path = updater.get_ytdlp_path()
# → "./tools/yt-dlp" or "./tools/yt-dlp.exe"
```

### **Example 6: Integration vào Script**

```python
#!/usr/bin/env python3
"""My YouTube downloader with auto-update"""

from yt_dlp_updater import auto_update_ytdlp, get_ytdlp_path
import subprocess

def main():
    # Auto-update yt-dlp trước khi dùng
    print("Checking yt-dlp...")
    if not auto_update_ytdlp():
        print("Failed to ensure yt-dlp")
        return 1

    # Get yt-dlp path
    ytdlp = get_ytdlp_path()

    # Use yt-dlp
    video_url = "https://youtube.com/watch?v=..."
    subprocess.run([ytdlp, video_url])

if __name__ == '__main__':
    main()
```

---

## 🔧 Configuration

### **Environment Variables** (Optional)

```bash
# Custom GitHub API token (nếu bị rate limit)
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"

# Proxy settings
export HTTP_PROXY="http://proxy:8080"
export HTTPS_PROXY="http://proxy:8080"
```

### **Logging Configuration**

```python
import logging

# Điều chỉnh log level
logging.basicConfig(level=logging.DEBUG)  # Chi tiết hơn

# Hoặc disable logging
logging.basicConfig(level=logging.ERROR)  # Chỉ errors
```

---

## 🐛 Troubleshooting

### **Problem 1: GitHub API rate limit**

**Error:** `API rate limit exceeded`

**Solution:**
```bash
# Đợi 1 giờ hoặc dùng GitHub token
export GITHUB_TOKEN="your_github_token"
python yt_dlp_updater.py --update
```

### **Problem 2: Download fails**

**Error:** `Failed to download yt-dlp`

**Checklist:**
- ✅ Check internet connection
- ✅ Check proxy settings
- ✅ Try manual download: https://github.com/yt-dlp/yt-dlp/releases
- ✅ Check disk space

**Manual fix:**
```bash
# Download manually
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o yt-dlp
chmod +x yt-dlp  # Linux/Mac

# Hoặc Windows
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe -o yt-dlp.exe
```

### **Problem 3: Permission denied**

**Error:** `Permission denied when downloading`

**Solution:**
```bash
# Chạy với sudo (Linux/Mac)
sudo python yt_dlp_updater.py --update

# Hoặc change ownership
sudo chown $USER:$USER yt-dlp
```

### **Problem 4: Old backup cluttering**

**Solution:**
```bash
# Cleanup backup files
python yt_dlp_updater.py --cleanup
```

---

## 📊 Performance

### **Download Time:**

| Connection | File Size | Time |
|------------|-----------|------|
| Fast (>50 Mbps) | ~10 MB | 2-5 sec |
| Medium (10-50 Mbps) | ~10 MB | 5-15 sec |
| Slow (<10 Mbps) | ~10 MB | 15-30 sec |

### **Version Check:**

- GitHub API call: < 1 second
- Local version check: < 0.1 second

---

## 🔐 Security

### **Download Verification:**

1. ✅ Download từ official GitHub releases only
2. ✅ HTTPS connection
3. ✅ Backup trước khi update
4. ✅ Rollback nếu fail

### **Best Practices:**

```python
# 1. Always verify after download
updater = YtDlpUpdater()
if updater.download_ytdlp():
    version = updater.get_current_version()
    if version:
        print(f"✓ Verified: {version}")
    else:
        print("⚠ Download success but verification failed")

# 2. Keep backups
# Backups tự động tạo với .bak extension

# 3. Check hash (future feature)
# TODO: Implement checksum verification
```

---

## 🚦 Integration Patterns

### **Pattern 1: Pre-flight Check**

```python
def main():
    # Check dependencies trước khi chạy app
    from yt_dlp_updater import check_dependencies

    ytdlp_ok, ffmpeg_ok = check_dependencies()

    if not ytdlp_ok or not ffmpeg_ok:
        print("Dependencies missing!")
        sys.exit(1)

    # Proceed with app
    run_app()
```

### **Pattern 2: Lazy Update**

```python
def download_video(url):
    # Update chỉ khi cần dùng
    from yt_dlp_updater import YtDlpUpdater

    updater = YtDlpUpdater()

    # Check nếu đã quá 7 ngày → update
    # (TODO: implement age checking)

    ytdlp = updater.get_ytdlp_path()
    subprocess.run([ytdlp, url])
```

### **Pattern 3: Background Update**

```python
import threading

def update_ytdlp_background():
    """Update yt-dlp trong background thread"""
    from yt_dlp_updater import auto_update_ytdlp
    auto_update_ytdlp()

def main():
    # Start background update
    thread = threading.Thread(target=update_ytdlp_background, daemon=True)
    thread.start()

    # Continue with app
    # Update sẽ hoàn tất trong background
```

---

## 📈 Roadmap

### **Planned Features:**

- [ ] **Checksum verification** - Verify download integrity
- [ ] **Delta updates** - Download only changes
- [ ] **Version pinning** - Pin to specific version
- [ ] **Auto-rollback** - Rollback if new version has issues
- [ ] **Update notifications** - Notify khi có version mới
- [ ] **Offline mode** - Cache versions for offline use
- [ ] **Update scheduler** - Schedule updates (daily, weekly)

---

## 💻 Platform-Specific Notes

### **Windows:**
- Executable: `yt-dlp.exe`
- Location: Current directory or in PATH
- No permission issues

### **Linux/macOS:**
- Executable: `yt-dlp`
- Auto `chmod +x` after download
- May need sudo for system-wide install

### **Cross-platform Path:**

```python
from yt_dlp_updater import YtDlpUpdater

updater = YtDlpUpdater()

# Works on all platforms
ytdlp_path = updater.get_ytdlp_path()

# Use in subprocess
subprocess.run([ytdlp_path, url])
```

---

## 📞 Support

### **Issues:**
- GitHub: https://github.com/abus-aikorea/voice-pro/issues

### **Logs:**
```bash
# Check logs
cat voice-pro-app.log
cat batch-url-processor.log

# Enable debug logging
python yt_dlp_updater.py --update --verbose
```

---

## 📄 License

LGPL - Same as Voice-Pro

---

**Version:** 1.0.0
**Date:** 2025-11-13
**Author:** Claude (Anthropic AI) for Voice-Pro
