# 📦 Hướng Dẫn Batch Processing trong Voice-Pro

## 📋 Tổng Quan

Voice-Pro hỗ trợ **3 loại batch processing**:

| Loại | Hỗ Trợ | Cách Sử Dụng |
|------|--------|--------------|
| 🎥 YouTube Playlist | ✅ Built-in | Paste playlist URL vào Dubbing Studio tab |
| 📝 Batch TTS | ✅ Built-in | Chọn folder chứa text files |
| 🔤 Batch Subtitle Translation | ✅ Built-in | Chọn folder chứa .srt files |
| 🔗 Multiple URLs | ✅ **Script mới** | Sử dụng `batch_url_processor.py` |

---

## 🎯 Method 1: YouTube Playlist (Built-in)

### ✅ Ưu điểm:
- Tích hợp sẵn trong Voice-Pro
- Không cần script bên ngoài
- Tự động download tất cả videos

### 📝 Cách sử dụng:

1. **Tạo YouTube Playlist:**
   - Vào YouTube → Library → Create Playlist
   - Thêm tất cả videos muốn xử lý

2. **Copy Playlist URL:**
   ```
   https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxxx
   ```

3. **Paste vào Voice-Pro:**
   - Mở Voice-Pro WebUI
   - Tab "Dubbing Studio"
   - Paste URL vào ô "YouTube URL"
   - Chọn cài đặt (quality, format, etc.)
   - Click "Download"

4. **Kết quả:**
   - Tất cả videos trong playlist được download
   - Xử lý tuần tự hoặc batch (tùy implementation)

### ⚠️ Lưu ý:
- Playlist phải public hoặc unlisted
- Cẩn thận với playlist lớn (>50 videos)
- Check disk space trước

---

## 🚀 Method 2: Batch URL Processor (Script Mới)

### ✅ Ưu điểm:
- Xử lý **nhiều URLs riêng lẻ** (không cần tạo playlist)
- **Parallel processing** - nhanh hơn
- Progress tracking & error handling
- Generate detailed reports

### 📝 Cách sử dụng:

#### **Bước 1: Chuẩn bị file URLs**

Tạo file `my_videos.txt`:
```txt
# Danh sách videos cần download
https://www.youtube.com/watch?v=ABC123
https://www.youtube.com/watch?v=DEF456
https://www.youtube.com/watch?v=GHI789
https://youtu.be/JKL012
```

#### **Bước 2: Chạy batch processor**

**Cú pháp cơ bản:**
```bash
python batch_url_processor.py --file my_videos.txt
```

**Với options:**
```bash
# 5 workers, output vào ./videos
python batch_url_processor.py --file my_videos.txt --workers 5 --output ./videos

# Chỉ định số lần retry
python batch_url_processor.py --file my_videos.txt --retry 3

# Chỉ định tên report file
python batch_url_processor.py --file my_videos.txt --report my_report.json
```

**URLs trực tiếp (không cần file):**
```bash
python batch_url_processor.py --urls \
  "https://youtube.com/watch?v=ABC" \
  "https://youtube.com/watch?v=DEF" \
  "https://youtube.com/watch?v=GHI"
```

#### **Bước 3: Xem kết quả**

Output structure:
```
batch_output/
├── video_1_Title1.mp4
├── video_2_Title2.mp4
├── video_3_Title3.mp4
├── batch_report.json
└── batch-url-processor.log
```

**Report JSON:**
```json
{
  "summary": {
    "total": 3,
    "completed": 2,
    "failed": 1,
    "success_rate": "66.7%"
  },
  "jobs": [
    {
      "index": 1,
      "url": "https://youtube.com/watch?v=ABC",
      "status": "completed",
      "output_file": "./batch_output/video_1_Title1.mp4",
      "duration_seconds": 45.2
    },
    {
      "index": 2,
      "url": "https://youtube.com/watch?v=DEF",
      "status": "completed",
      "output_file": "./batch_output/video_2_Title2.mp4",
      "duration_seconds": 52.8
    },
    {
      "index": 3,
      "url": "https://youtube.com/watch?v=GHI",
      "status": "failed",
      "error": "Video unavailable",
      "duration_seconds": 5.1
    }
  ]
}
```

---

## 📊 So Sánh Methods

| Tiêu chí | Playlist (Built-in) | Batch Processor (Script) |
|----------|---------------------|--------------------------|
| **Setup** | ✅ Không cần setup | ⚠️ Cần chạy script |
| **Flexibility** | ⚠️ Phải tạo playlist | ✅ List URLs tự do |
| **Speed** | ⚠️ Tuần tự | ✅ Parallel (nhanh hơn) |
| **Error Handling** | ⚠️ Cơ bản | ✅ Retry + detailed logs |
| **Progress Tracking** | ⚠️ Basic | ✅ Real-time + reports |
| **Use Case** | Videos liên quan | URLs random |

---

## 💡 Best Practices

### 1. **Chọn số workers phù hợp**
```bash
# Internet nhanh (>50 Mbps): 5-8 workers
python batch_url_processor.py --file urls.txt --workers 8

# Internet trung bình (10-50 Mbps): 3-5 workers
python batch_url_processor.py --file urls.txt --workers 4

# Internet chậm (<10 Mbps): 1-2 workers
python batch_url_processor.py --file urls.txt --workers 2
```

### 2. **Batch size**
```bash
# Chia nhỏ nếu có nhiều videos
# Thay vì 100 URLs cùng lúc:
split -l 20 all_urls.txt batch_

# Chạy từng batch:
python batch_url_processor.py --file batch_aa
python batch_url_processor.py --file batch_ab
```

### 3. **Error recovery**
```bash
# Nếu batch fail, lọc ra failed URLs từ report:
cat batch_report.json | jq '.jobs[] | select(.status=="failed") | .url' > failed_urls.txt

# Retry failed URLs:
python batch_url_processor.py --file failed_urls.txt --retry 5
```

### 4. **Disk space check**
```bash
# Check space trước khi download
df -h

# Estimate: 1 video HD (1080p) ~ 100-500 MB
# 50 videos ~ 5-25 GB
```

---

## 🔧 Troubleshooting

### ❌ Problem 1: "Too many requests" error

**Nguyên nhân:** YouTube rate limiting

**Giải pháp:**
```bash
# Giảm workers
python batch_url_processor.py --file urls.txt --workers 2

# Thêm delay giữa các requests (TODO: implement in script)
# Hoặc chia nhỏ batch
```

### ❌ Problem 2: Script không tìm thấy Voice-Pro modules

**Nguyên nhân:** Import error

**Giải pháp:**
```bash
# Script sẽ tự động fallback sang yt-dlp
# Hoặc chạy từ Voice-Pro directory:
cd /path/to/voice-pro
python batch_url_processor.py --file urls.txt
```

### ❌ Problem 3: Download quá chậm

**Nguyên nhân:** Network hoặc quality settings

**Giải pháp:**
```bash
# Modify script để chọn quality thấp hơn
# Hoặc download audio-only:
# Sửa trong script: audio_only=True
```

---

## 🎓 Advanced Usage

### 1. **Integration với Voice-Pro pipeline**

```bash
# Step 1: Batch download
python batch_url_processor.py --file urls.txt --output ./videos

# Step 2: Process mỗi video qua Voice-Pro
for video in ./videos/*.mp4; do
    python voice_pro_cli.py --input "$video" --transcribe --translate --tts
done
```

### 2. **Scheduled batch processing**

**Linux/Mac crontab:**
```bash
# Download videos hàng ngày lúc 2 AM
0 2 * * * cd /path/to/voice-pro && python batch_url_processor.py --file daily_urls.txt
```

**Windows Task Scheduler:**
```powershell
# Tạo scheduled task
schtasks /create /tn "VoiceProBatch" /tr "python C:\voice-pro\batch_url_processor.py --file urls.txt" /sc daily /st 02:00
```

### 3. **Monitor progress**

```bash
# Tail logs real-time
tail -f batch-url-processor.log

# Watch report file
watch -n 5 "cat batch_report.json | jq '.summary'"
```

---

## 📚 Workflow Examples

### **Example 1: Podcast Processing**

```bash
# 1. Download podcast episodes
python batch_url_processor.py --file podcast_urls.txt --output ./podcasts

# 2. Transcribe all episodes
for ep in ./podcasts/*.mp4; do
    # Process through Voice-Pro Dubbing Studio
    echo "Processing: $ep"
done

# 3. Generate subtitles & translations
# (Use Voice-Pro WebUI or CLI)
```

### **Example 2: Educational Videos**

```bash
# URLs file: lectures.txt
https://youtube.com/watch?v=lecture1
https://youtube.com/watch?v=lecture2
https://youtube.com/watch?v=lecture3

# Download
python batch_url_processor.py --file lectures.txt --output ./lectures

# Generate subtitles for all
# Use Voice-Pro Whisper Caption tab
```

### **Example 3: Content Creation**

```bash
# Collect reference videos
cat > references.txt << EOF
https://youtube.com/watch?v=ref1
https://youtube.com/watch?v=ref2
https://youtube.com/watch?v=ref3
EOF

# Download with 8 workers (fast)
python batch_url_processor.py --file references.txt --workers 8 --output ./refs

# Extract audio for voice cloning
# Use Voice-Pro Speech Generation tab
```

---

## 🆘 Getting Help

### Script help:
```bash
python batch_url_processor.py --help
```

### Check logs:
```bash
# Application log
cat batch-url-processor.log

# Voice-Pro logs
cat voice-pro.log
cat voice-pro-app.log
```

### Report issues:
- GitHub Issues: https://github.com/abus-aikorea/voice-pro/issues
- Include logs and report JSON

---

## 📋 Summary

### **Khi nào dùng gì?**

| Scenario | Recommended Method |
|----------|-------------------|
| 📺 Videos cùng chủ đề | YouTube Playlist |
| 🔗 URLs random từ nhiều nguồn | Batch URL Processor |
| 🎵 Download nhanh nhiều videos | Batch Processor (parallel) |
| 📝 Batch TTS/Translation | Built-in Voice-Pro |
| 🔄 Automated/Scheduled jobs | Batch Processor + Cron |

### **Key Takeaways:**

1. ✅ Voice-Pro **ĐÃ HỖ TRỢ** batch processing qua Playlist
2. ✅ **Script mới** cho phép xử lý multiple URLs linh hoạt hơn
3. ⚡ Parallel processing giúp **tiết kiệm thời gian đáng kể**
4. 📊 Reports chi tiết giúp **tracking và debugging**
5. 🔧 Có thể **customize** script theo nhu cầu

---

**Prepared by**: Claude (Anthropic AI)
**Date**: 2025-11-13
**Version**: 1.0
