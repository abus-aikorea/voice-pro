#!/usr/bin/env python3
"""
Watermark Examples for Voice-Pro
Các ví dụ sử dụng watermark system

Run:
    python watermark_examples.py
"""

import sys
from pathlib import Path

# Import watermark modules
from watermark_manager import (
    WatermarkManager,
    TextWatermarkConfig,
    ImageWatermarkConfig,
    AudioWatermarkConfig,
    WatermarkPosition
)
from voicepro_watermark_integration import VoiceProWatermarkIntegration


def example_1_simple_text():
    """
    Example 1: Simple text watermark
    Watermark text đơn giản nhất
    """
    print("\n" + "="*60)
    print("Example 1: Simple Text Watermark")
    print("="*60)

    manager = WatermarkManager(output_dir="./examples/example1")

    text_config = TextWatermarkConfig(
        text="© 2025 Voice-Pro",
        position=WatermarkPosition.BOTTOM_RIGHT
    )

    # Replace with your video
    input_video = "sample_video.mp4"

    if not Path(input_video).exists():
        print(f"❌ Sample video not found: {input_video}")
        print("Please create a sample video or update the path")
        return

    output = manager.add_text_watermark(input_video, text_config)
    print(f"✅ Output: {output}")


def example_2_custom_style():
    """
    Example 2: Custom style text watermark
    Text với custom font, color, shadow
    """
    print("\n" + "="*60)
    print("Example 2: Custom Style Text")
    print("="*60)

    manager = WatermarkManager(output_dir="./examples/example2")

    text_config = TextWatermarkConfig(
        text="© 2025 My Company",
        font_size=32,
        font_color="yellow",
        position=WatermarkPosition.TOP_CENTER,
        opacity=0.8,
        shadow=True,
        background_color="black",
        background_opacity=0.5
    )

    input_video = "sample_video.mp4"

    if Path(input_video).exists():
        output = manager.add_text_watermark(input_video, text_config)
        print(f"✅ Output: {output}")
    else:
        print(f"❌ Sample video not found: {input_video}")


def example_3_logo_watermark():
    """
    Example 3: Logo watermark
    Thêm logo vào video
    """
    print("\n" + "="*60)
    print("Example 3: Logo Watermark")
    print("="*60)

    manager = WatermarkManager(output_dir="./examples/example3")

    logo_config = ImageWatermarkConfig(
        image_path="./assets/logo.png",  # Your logo here
        position=WatermarkPosition.TOP_RIGHT,
        opacity=0.7,
        scale=0.15,
        margin_x=20,
        margin_y=20
    )

    input_video = "sample_video.mp4"
    logo_path = "./assets/logo.png"

    if not Path(logo_path).exists():
        print(f"❌ Logo not found: {logo_path}")
        print("Please add a logo.png file to ./assets/ folder")
        return

    if Path(input_video).exists():
        output = manager.add_image_watermark(input_video, logo_config)
        print(f"✅ Output: {output}")
    else:
        print(f"❌ Sample video not found: {input_video}")


def example_4_combined():
    """
    Example 4: Combined text + logo watermark
    Kết hợp text và logo
    """
    print("\n" + "="*60)
    print("Example 4: Combined Text + Logo")
    print("="*60)

    manager = WatermarkManager(output_dir="./examples/example4")

    text_config = TextWatermarkConfig(
        text="© 2025 Voice-Pro | AI Powered",
        font_size=24,
        position=WatermarkPosition.BOTTOM_RIGHT,
        opacity=0.6,
        shadow=True
    )

    logo_config = ImageWatermarkConfig(
        image_path="./assets/logo.png",
        position=WatermarkPosition.TOP_LEFT,
        opacity=0.8,
        scale=0.12
    )

    input_video = "sample_video.mp4"

    if Path(input_video).exists() and Path("./assets/logo.png").exists():
        output = manager.add_combined_watermark(
            input_video,
            text_config,
            logo_config
        )
        print(f"✅ Output: {output}")
    else:
        print("❌ Missing files. Need:")
        print("  - sample_video.mp4")
        print("  - ./assets/logo.png")


def example_5_batch_processing():
    """
    Example 5: Batch processing
    Xử lý nhiều videos cùng lúc
    """
    print("\n" + "="*60)
    print("Example 5: Batch Processing")
    print("="*60)

    manager = WatermarkManager(output_dir="./examples/example5")

    text_config = TextWatermarkConfig(
        text="© 2025 Batch Processed",
        position=WatermarkPosition.BOTTOM_CENTER
    )

    # List of videos
    videos = list(Path("./videos").glob("*.mp4"))

    if not videos:
        print("❌ No videos found in ./videos/ folder")
        print("Please add some .mp4 files to ./videos/")
        return

    print(f"Found {len(videos)} videos")

    outputs = manager.batch_watermark(
        [str(v) for v in videos],
        text_config=text_config
    )

    print(f"✅ Processed {len(outputs)} videos")
    for i, out in enumerate(outputs):
        if out:
            print(f"  [{i+1}] {out}")


def example_6_using_config():
    """
    Example 6: Using configuration file
    Sử dụng file config
    """
    print("\n" + "="*60)
    print("Example 6: Using Configuration File")
    print("="*60)

    integration = VoiceProWatermarkIntegration("watermark_config.json5")

    input_video = "sample_video.mp4"

    if Path(input_video).exists():
        output = integration.process_video(input_video)
        print(f"✅ Output: {output}")
    else:
        print(f"❌ Sample video not found: {input_video}")


def example_7_presets():
    """
    Example 7: Using presets
    Sử dụng presets có sẵn
    """
    print("\n" + "="*60)
    print("Example 7: Using Presets")
    print("="*60)

    integration = VoiceProWatermarkIntegration("watermark_config.json5")

    input_video = "sample_video.mp4"

    if not Path(input_video).exists():
        print(f"❌ Sample video not found: {input_video}")
        return

    presets = ["subtle", "strong", "professional", "youtube"]

    for preset in presets:
        print(f"\n  Processing with preset: {preset}")
        output = integration.process_video(
            input_video,
            preset=preset,
            output_path=f"./examples/example7/video_{preset}.mp4"
        )
        print(f"  ✅ {output}")


def example_8_audio_watermark():
    """
    Example 8: Audio watermark (invisible)
    Watermark audio không nghe thấy
    """
    print("\n" + "="*60)
    print("Example 8: Audio Watermark (Invisible)")
    print("="*60)

    manager = WatermarkManager(output_dir="./examples/example8")

    audio_config = AudioWatermarkConfig(
        watermark_text="VoicePro_Copyright_2025",
        method="lsb",
        strength=0.1
    )

    input_audio = "sample_audio.mp3"

    if Path(input_audio).exists():
        output = manager.add_audio_watermark(input_audio, audio_config)
        print(f"✅ Output: {output}")
        print("Note: Watermark is invisible, cannot be heard")
    else:
        print(f"❌ Sample audio not found: {input_audio}")


def example_9_dynamic_text():
    """
    Example 9: Dynamic text watermark
    Text tự động thay đổi (timestamp, etc.)
    """
    print("\n" + "="*60)
    print("Example 9: Dynamic Text Watermark")
    print("="*60)

    from datetime import datetime

    manager = WatermarkManager(output_dir="./examples/example9")

    # Dynamic text với timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    text_config = TextWatermarkConfig(
        text=f"© 2025 Voice-Pro | Processed: {current_time}",
        font_size=20,
        position=WatermarkPosition.BOTTOM_RIGHT,
        opacity=0.5
    )

    input_video = "sample_video.mp4"

    if Path(input_video).exists():
        output = manager.add_text_watermark(input_video, text_config)
        print(f"✅ Output: {output}")
    else:
        print(f"❌ Sample video not found: {input_video}")


def example_10_unique_tracking():
    """
    Example 10: Unique tracking watermark
    Watermark với unique ID cho mỗi video (tracking)
    """
    print("\n" + "="*60)
    print("Example 10: Unique Tracking Watermark")
    print("="*60)

    import uuid

    manager = WatermarkManager(output_dir="./examples/example10")

    # Generate unique ID
    unique_id = str(uuid.uuid4())[:8]

    text_config = TextWatermarkConfig(
        text=f"ID: {unique_id}",
        font_size=18,
        position=WatermarkPosition.TOP_LEFT,
        opacity=0.4,
        font_color="white",
        background_color="black",
        background_opacity=0.3
    )

    input_video = "sample_video.mp4"

    if Path(input_video).exists():
        output = manager.add_text_watermark(input_video, text_config)
        print(f"✅ Output: {output}")
        print(f"✅ Unique ID: {unique_id}")

        # Log for tracking
        log_file = "./examples/example10/tracking_log.txt"
        with open(log_file, "a") as f:
            from datetime import datetime
            f.write(f"{datetime.now()},{input_video},{unique_id},{output}\n")

        print(f"✅ Logged to: {log_file}")
    else:
        print(f"❌ Sample video not found: {input_video}")


def create_sample_logo():
    """
    Create a simple sample logo using PIL
    Tạo logo mẫu đơn giản
    """
    try:
        from PIL import Image, ImageDraw, ImageFont

        # Create 200x200 logo with transparent background
        size = (200, 200)
        img = Image.new('RGBA', size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Draw circle
        circle_color = (41, 128, 185, 200)  # Blue with alpha
        draw.ellipse([20, 20, 180, 180], fill=circle_color)

        # Draw text
        text = "VP"
        text_color = (255, 255, 255, 255)

        # Try to use a font
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        except:
            font = ImageFont.load_default()

        # Calculate text position
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = (size[0] - text_width) / 2
        text_y = (size[1] - text_height) / 2

        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Save
        Path("./assets").mkdir(exist_ok=True)
        img.save("./assets/logo.png")

        print("✅ Created sample logo: ./assets/logo.png")
        return True

    except ImportError:
        print("⚠️  PIL not installed. Install with: pip install Pillow")
        return False
    except Exception as e:
        print(f"❌ Error creating logo: {e}")
        return False


def print_menu():
    """Print example menu"""
    print("\n" + "="*60)
    print("Voice-Pro Watermark Examples")
    print("="*60)
    print("\n1.  Simple Text Watermark")
    print("2.  Custom Style Text")
    print("3.  Logo Watermark")
    print("4.  Combined Text + Logo")
    print("5.  Batch Processing")
    print("6.  Using Configuration File")
    print("7.  Using Presets")
    print("8.  Audio Watermark (Invisible)")
    print("9.  Dynamic Text Watermark")
    print("10. Unique Tracking Watermark")
    print("\n0.  Create Sample Logo")
    print("q.  Quit")
    print("="*60)


def main():
    """Main menu"""
    examples = {
        "1": example_1_simple_text,
        "2": example_2_custom_style,
        "3": example_3_logo_watermark,
        "4": example_4_combined,
        "5": example_5_batch_processing,
        "6": example_6_using_config,
        "7": example_7_presets,
        "8": example_8_audio_watermark,
        "9": example_9_dynamic_text,
        "10": example_10_unique_tracking,
        "0": create_sample_logo
    }

    while True:
        print_menu()
        choice = input("\nSelect example (1-10, 0 for logo, q to quit): ").strip()

        if choice.lower() == 'q':
            print("\nGoodbye!")
            break

        if choice in examples:
            try:
                examples[choice]()
            except Exception as e:
                print(f"\n❌ Error: {e}")
                import traceback
                traceback.print_exc()

            input("\nPress Enter to continue...")
        else:
            print("\n❌ Invalid choice")


if __name__ == '__main__':
    # Check if running with argument
    if len(sys.argv) > 1:
        example_num = sys.argv[1]
        if example_num in [str(i) for i in range(11)]:
            examples = {
                "0": create_sample_logo,
                "1": example_1_simple_text,
                "2": example_2_custom_style,
                "3": example_3_logo_watermark,
                "4": example_4_combined,
                "5": example_5_batch_processing,
                "6": example_6_using_config,
                "7": example_7_presets,
                "8": example_8_audio_watermark,
                "9": example_9_dynamic_text,
                "10": example_10_unique_tracking,
            }
            examples[example_num]()
        else:
            print(f"Invalid example number: {example_num}")
            print("Use: python watermark_examples.py [0-10]")
    else:
        # Interactive menu
        main()
