#!/usr/bin/env python3
"""
Watermark Manager for Voice-Pro
Hệ thống quản lý watermark cho video và audio - Bảo vệ bản quyền

Features:
- ✅ Text watermark cho video
- ✅ Logo/Image watermark cho video
- ✅ Audio watermark (steganography)
- ✅ Batch processing
- ✅ Configurable positions, opacity, size
- ✅ Animation effects (optional)
"""

import os
import sys
import logging
import subprocess
from pathlib import Path
from typing import Optional, Tuple, Dict, List
from dataclasses import dataclass
from enum import Enum
import json
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class WatermarkPosition(Enum):
    """Vị trí watermark trên video"""
    TOP_LEFT = "top_left"
    TOP_RIGHT = "top_right"
    TOP_CENTER = "top_center"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_RIGHT = "bottom_right"
    BOTTOM_CENTER = "bottom_center"
    CENTER = "center"
    CUSTOM = "custom"


@dataclass
class TextWatermarkConfig:
    """Cấu hình cho text watermark"""
    text: str
    font_size: int = 24
    font_color: str = "white"
    font_file: Optional[str] = None
    position: WatermarkPosition = WatermarkPosition.BOTTOM_RIGHT
    opacity: float = 0.5
    margin_x: int = 10
    margin_y: int = 10
    shadow: bool = True
    background_color: Optional[str] = None
    background_opacity: float = 0.3


@dataclass
class ImageWatermarkConfig:
    """Cấu hình cho image/logo watermark"""
    image_path: str
    position: WatermarkPosition = WatermarkPosition.TOP_RIGHT
    opacity: float = 0.7
    scale: float = 1.0  # 0.1 to 2.0
    margin_x: int = 10
    margin_y: int = 10


@dataclass
class AudioWatermarkConfig:
    """Cấu hình cho audio watermark"""
    watermark_text: str
    method: str = "lsb"  # lsb, phase, spread_spectrum
    strength: float = 0.1


class WatermarkManager:
    """
    Quản lý watermarking cho video và audio
    """

    def __init__(self, output_dir: str = "./watermarked"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.ffmpeg_path = self._find_ffmpeg()

    def _find_ffmpeg(self) -> str:
        """Tìm ffmpeg executable"""
        try:
            result = subprocess.run(['which', 'ffmpeg'],
                                  capture_output=True,
                                  text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return 'ffmpeg'
        except:
            return 'ffmpeg'

    def _get_video_info(self, video_path: str) -> Dict:
        """Lấy thông tin video (resolution, duration, etc.)"""
        try:
            cmd = [
                'ffprobe',
                '-v', 'quiet',
                '-print_format', 'json',
                '-show_format',
                '-show_streams',
                video_path
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                return json.loads(result.stdout)
            return {}
        except Exception as e:
            logger.error(f"Lỗi lấy video info: {e}")
            return {}

    def _calculate_position(self,
                          position: WatermarkPosition,
                          video_width: int,
                          video_height: int,
                          watermark_width: int,
                          watermark_height: int,
                          margin_x: int,
                          margin_y: int) -> Tuple[str, str]:
        """
        Tính toán vị trí watermark trên video

        Returns:
            Tuple[x_position, y_position] for ffmpeg
        """
        positions = {
            WatermarkPosition.TOP_LEFT: (
                str(margin_x),
                str(margin_y)
            ),
            WatermarkPosition.TOP_RIGHT: (
                f"(W-w-{margin_x})",
                str(margin_y)
            ),
            WatermarkPosition.TOP_CENTER: (
                "(W-w)/2",
                str(margin_y)
            ),
            WatermarkPosition.BOTTOM_LEFT: (
                str(margin_x),
                f"(H-h-{margin_y})"
            ),
            WatermarkPosition.BOTTOM_RIGHT: (
                f"(W-w-{margin_x})",
                f"(H-h-{margin_y})"
            ),
            WatermarkPosition.BOTTOM_CENTER: (
                "(W-w)/2",
                f"(H-h-{margin_y})"
            ),
            WatermarkPosition.CENTER: (
                "(W-w)/2",
                "(H-h)/2"
            )
        }

        return positions.get(position, positions[WatermarkPosition.BOTTOM_RIGHT])

    def add_text_watermark(self,
                          input_video: str,
                          config: TextWatermarkConfig,
                          output_path: Optional[str] = None) -> str:
        """
        Thêm text watermark vào video

        Args:
            input_video: Đường dẫn video input
            config: TextWatermarkConfig
            output_path: Đường dẫn output (optional)

        Returns:
            Đường dẫn file output
        """
        try:
            logger.info(f"Thêm text watermark: {config.text}")

            # Generate output path
            if not output_path:
                input_path = Path(input_video)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = self.output_dir / f"{input_path.stem}_watermarked_{timestamp}{input_path.suffix}"

            # Get video info
            video_info = self._get_video_info(input_video)
            video_stream = next((s for s in video_info.get('streams', [])
                               if s['codec_type'] == 'video'), {})
            video_width = int(video_stream.get('width', 1920))
            video_height = int(video_stream.get('height', 1080))

            # Calculate position
            x_pos, y_pos = self._calculate_position(
                config.position,
                video_width,
                video_height,
                0, 0,  # Text size tính sau
                config.margin_x,
                config.margin_y
            )

            # Build drawtext filter
            drawtext_params = [
                f"text='{config.text}'",
                f"fontsize={config.font_size}",
                f"fontcolor={config.font_color}@{config.opacity}",
                f"x={x_pos}",
                f"y={y_pos}",
            ]

            if config.font_file:
                drawtext_params.append(f"fontfile={config.font_file}")

            if config.shadow:
                drawtext_params.append(f"shadowcolor=black@0.5")
                drawtext_params.append(f"shadowx=2")
                drawtext_params.append(f"shadowy=2")

            if config.background_color:
                drawtext_params.append(f"box=1")
                drawtext_params.append(f"boxcolor={config.background_color}@{config.background_opacity}")
                drawtext_params.append(f"boxborderw=5")

            drawtext_filter = "drawtext=" + ":".join(drawtext_params)

            # FFmpeg command
            cmd = [
                self.ffmpeg_path,
                '-i', input_video,
                '-vf', drawtext_filter,
                '-codec:a', 'copy',  # Copy audio without re-encoding
                '-y',
                str(output_path)
            ]

            logger.debug(f"FFmpeg command: {' '.join(cmd)}")

            # Run ffmpeg
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                logger.info(f"✓ Text watermark hoàn thành: {output_path}")
                return str(output_path)
            else:
                logger.error(f"✗ FFmpeg error: {result.stderr}")
                raise Exception(f"FFmpeg failed: {result.stderr}")

        except Exception as e:
            logger.error(f"✗ Lỗi thêm text watermark: {e}")
            raise

    def add_image_watermark(self,
                           input_video: str,
                           config: ImageWatermarkConfig,
                           output_path: Optional[str] = None) -> str:
        """
        Thêm image/logo watermark vào video

        Args:
            input_video: Đường dẫn video input
            config: ImageWatermarkConfig
            output_path: Đường dẫn output (optional)

        Returns:
            Đường dẫn file output
        """
        try:
            logger.info(f"Thêm logo watermark: {config.image_path}")

            # Check image exists
            if not os.path.exists(config.image_path):
                raise FileNotFoundError(f"Logo không tồn tại: {config.image_path}")

            # Generate output path
            if not output_path:
                input_path = Path(input_video)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = self.output_dir / f"{input_path.stem}_logo_{timestamp}{input_path.suffix}"

            # Get video info
            video_info = self._get_video_info(input_video)
            video_stream = next((s for s in video_info.get('streams', [])
                               if s['codec_type'] == 'video'), {})
            video_width = int(video_stream.get('width', 1920))
            video_height = int(video_stream.get('height', 1080))

            # Calculate position
            x_pos, y_pos = self._calculate_position(
                config.position,
                video_width,
                video_height,
                0, 0,  # Logo size tính từ scale
                config.margin_x,
                config.margin_y
            )

            # Build overlay filter
            # Scale logo
            scale_filter = f"scale=iw*{config.scale}:ih*{config.scale}"

            # Set opacity
            format_filter = f"format=rgba,colorchannelmixer=aa={config.opacity}"

            # Combine filters
            overlay_filter = f"[1:v]{scale_filter},{format_filter}[wm];[0:v][wm]overlay={x_pos}:{y_pos}"

            # FFmpeg command
            cmd = [
                self.ffmpeg_path,
                '-i', input_video,
                '-i', config.image_path,
                '-filter_complex', overlay_filter,
                '-codec:a', 'copy',
                '-y',
                str(output_path)
            ]

            logger.debug(f"FFmpeg command: {' '.join(cmd)}")

            # Run ffmpeg
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                logger.info(f"✓ Logo watermark hoàn thành: {output_path}")
                return str(output_path)
            else:
                logger.error(f"✗ FFmpeg error: {result.stderr}")
                raise Exception(f"FFmpeg failed: {result.stderr}")

        except Exception as e:
            logger.error(f"✗ Lỗi thêm logo watermark: {e}")
            raise

    def add_combined_watermark(self,
                              input_video: str,
                              text_config: Optional[TextWatermarkConfig] = None,
                              image_config: Optional[ImageWatermarkConfig] = None,
                              output_path: Optional[str] = None) -> str:
        """
        Thêm cả text và logo watermark cùng lúc

        Args:
            input_video: Đường dẫn video input
            text_config: TextWatermarkConfig (optional)
            image_config: ImageWatermarkConfig (optional)
            output_path: Đường dẫn output (optional)

        Returns:
            Đường dẫn file output
        """
        try:
            logger.info("Thêm combined watermark (text + logo)")

            if not text_config and not image_config:
                raise ValueError("Cần ít nhất 1 config (text hoặc image)")

            # Generate output path
            if not output_path:
                input_path = Path(input_video)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = self.output_dir / f"{input_path.stem}_combined_{timestamp}{input_path.suffix}"

            # Build complex filter
            filters = []

            # Image watermark first (if exists)
            if image_config:
                if not os.path.exists(image_config.image_path):
                    raise FileNotFoundError(f"Logo không tồn tại: {image_config.image_path}")

                video_info = self._get_video_info(input_video)
                video_stream = next((s for s in video_info.get('streams', [])
                                   if s['codec_type'] == 'video'), {})
                video_width = int(video_stream.get('width', 1920))
                video_height = int(video_stream.get('height', 1080))

                x_pos, y_pos = self._calculate_position(
                    image_config.position,
                    video_width, video_height,
                    0, 0,
                    image_config.margin_x,
                    image_config.margin_y
                )

                scale_filter = f"scale=iw*{image_config.scale}:ih*{image_config.scale}"
                format_filter = f"format=rgba,colorchannelmixer=aa={image_config.opacity}"
                overlay_filter = f"[1:v]{scale_filter},{format_filter}[wm];[0:v][wm]overlay={x_pos}:{y_pos}[v1]"
                filters.append(overlay_filter)

            # Text watermark
            if text_config:
                video_info = self._get_video_info(input_video)
                video_stream = next((s for s in video_info.get('streams', [])
                                   if s['codec_type'] == 'video'), {})
                video_width = int(video_stream.get('width', 1920))
                video_height = int(video_stream.get('height', 1080))

                x_pos, y_pos = self._calculate_position(
                    text_config.position,
                    video_width, video_height,
                    0, 0,
                    text_config.margin_x,
                    text_config.margin_y
                )

                drawtext_params = [
                    f"text='{text_config.text}'",
                    f"fontsize={text_config.font_size}",
                    f"fontcolor={text_config.font_color}@{text_config.opacity}",
                    f"x={x_pos}",
                    f"y={y_pos}",
                ]

                if text_config.font_file:
                    drawtext_params.append(f"fontfile={text_config.font_file}")

                if text_config.shadow:
                    drawtext_params.append(f"shadowcolor=black@0.5")
                    drawtext_params.append(f"shadowx=2")
                    drawtext_params.append(f"shadowy=2")

                if text_config.background_color:
                    drawtext_params.append(f"box=1")
                    drawtext_params.append(f"boxcolor={text_config.background_color}@{text_config.background_opacity}")
                    drawtext_params.append(f"boxborderw=5")

                input_label = "[v1]" if image_config else "[0:v]"
                drawtext_filter = f"{input_label}drawtext=" + ":".join(drawtext_params)
                filters.append(drawtext_filter)

            filter_complex = ";".join(filters)

            # Build FFmpeg command
            cmd = [self.ffmpeg_path, '-i', input_video]

            if image_config:
                cmd.extend(['-i', image_config.image_path])

            cmd.extend([
                '-filter_complex', filter_complex,
                '-codec:a', 'copy',
                '-y',
                str(output_path)
            ])

            logger.debug(f"FFmpeg command: {' '.join(cmd)}")

            # Run ffmpeg
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                logger.info(f"✓ Combined watermark hoàn thành: {output_path}")
                return str(output_path)
            else:
                logger.error(f"✗ FFmpeg error: {result.stderr}")
                raise Exception(f"FFmpeg failed: {result.stderr}")

        except Exception as e:
            logger.error(f"✗ Lỗi thêm combined watermark: {e}")
            raise

    def add_audio_watermark(self,
                           input_audio: str,
                           config: AudioWatermarkConfig,
                           output_path: Optional[str] = None) -> str:
        """
        Thêm invisible watermark vào audio

        Sử dụng LSB (Least Significant Bit) steganography
        để embed watermark không nghe thấy

        Args:
            input_audio: Đường dẫn audio input
            config: AudioWatermarkConfig
            output_path: Đường dẫn output (optional)

        Returns:
            Đường dẫn file output
        """
        try:
            logger.info(f"Thêm audio watermark: {config.watermark_text}")

            # Generate output path
            if not output_path:
                input_path = Path(input_audio)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = self.output_dir / f"{input_path.stem}_watermarked_{timestamp}{input_path.suffix}"

            # Import audio processing libraries
            try:
                import numpy as np
                import soundfile as sf
            except ImportError:
                logger.error("Cần cài đặt: pip install numpy soundfile")
                raise

            # Load audio
            audio_data, sample_rate = sf.read(input_audio)

            # Convert watermark text to binary
            watermark_binary = ''.join(format(ord(c), '08b') for c in config.watermark_text)

            # Embed watermark using LSB
            watermarked_audio = self._embed_watermark_lsb(
                audio_data,
                watermark_binary,
                config.strength
            )

            # Save watermarked audio
            sf.write(str(output_path), watermarked_audio, sample_rate)

            logger.info(f"✓ Audio watermark hoàn thành: {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"✗ Lỗi thêm audio watermark: {e}")
            raise

    def _embed_watermark_lsb(self,
                             audio_data: 'np.ndarray',
                             watermark_binary: str,
                             strength: float) -> 'np.ndarray':
        """
        Embed watermark vào audio sử dụng LSB method

        Args:
            audio_data: Audio array
            watermark_binary: Binary string của watermark
            strength: Cường độ watermark (0.0 - 1.0)

        Returns:
            Watermarked audio array
        """
        import numpy as np

        # Make copy
        watermarked = audio_data.copy()

        # Handle stereo
        if len(watermarked.shape) > 1:
            watermarked = watermarked[:, 0]  # Use only first channel

        # Convert to int for bit manipulation
        watermarked_int = (watermarked * 32767).astype(np.int16)

        # Embed watermark
        for i, bit in enumerate(watermark_binary):
            if i >= len(watermarked_int):
                break

            # Clear LSB
            watermarked_int[i] = watermarked_int[i] & ~1

            # Set LSB to watermark bit
            if bit == '1':
                watermarked_int[i] = watermarked_int[i] | 1

        # Convert back to float
        watermarked_float = watermarked_int.astype(np.float32) / 32767.0

        # Apply strength
        watermarked_float = audio_data * (1 - strength) + watermarked_float * strength

        return watermarked_float

    def batch_watermark(self,
                       input_files: List[str],
                       text_config: Optional[TextWatermarkConfig] = None,
                       image_config: Optional[ImageWatermarkConfig] = None) -> List[str]:
        """
        Batch watermarking cho nhiều files

        Args:
            input_files: List các file paths
            text_config: Text watermark config (optional)
            image_config: Image watermark config (optional)

        Returns:
            List các output file paths
        """
        outputs = []

        for i, input_file in enumerate(input_files):
            try:
                logger.info(f"Processing [{i+1}/{len(input_files)}]: {input_file}")

                output = self.add_combined_watermark(
                    input_file,
                    text_config,
                    image_config
                )
                outputs.append(output)

            except Exception as e:
                logger.error(f"Lỗi xử lý {input_file}: {e}")
                outputs.append(None)

        success_count = sum(1 for o in outputs if o is not None)
        logger.info(f"✓ Hoàn thành: {success_count}/{len(input_files)} files")

        return outputs


# ============================================================================
# CLI Interface
# ============================================================================

def main():
    """CLI interface cho watermark manager"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Voice-Pro Watermark Manager',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:

1. Text watermark:
   python watermark_manager.py --input video.mp4 --text "© 2025 My Company"

2. Logo watermark:
   python watermark_manager.py --input video.mp4 --logo logo.png

3. Combined (text + logo):
   python watermark_manager.py --input video.mp4 --text "© 2025" --logo logo.png

4. Custom position and style:
   python watermark_manager.py --input video.mp4 \\
       --text "Watermark" \\
       --text-position bottom_right \\
       --text-size 32 \\
       --text-opacity 0.7

5. Batch processing:
   python watermark_manager.py --batch videos/*.mp4 --text "© 2025"
        """
    )

    # Input
    parser.add_argument('--input', '-i', help='Input video file')
    parser.add_argument('--batch', '-b', nargs='+', help='Batch input files')
    parser.add_argument('--output', '-o', help='Output file path')

    # Text watermark
    parser.add_argument('--text', '-t', help='Text watermark')
    parser.add_argument('--text-position', default='bottom_right',
                       choices=[p.value for p in WatermarkPosition])
    parser.add_argument('--text-size', type=int, default=24)
    parser.add_argument('--text-color', default='white')
    parser.add_argument('--text-opacity', type=float, default=0.5)
    parser.add_argument('--text-shadow', action='store_true', default=True)

    # Logo watermark
    parser.add_argument('--logo', '-l', help='Logo image file')
    parser.add_argument('--logo-position', default='top_right',
                       choices=[p.value for p in WatermarkPosition])
    parser.add_argument('--logo-scale', type=float, default=0.15)
    parser.add_argument('--logo-opacity', type=float, default=0.7)

    # Audio watermark
    parser.add_argument('--audio-watermark', help='Audio watermark text')

    # Output
    parser.add_argument('--output-dir', default='./watermarked')

    args = parser.parse_args()

    # Validate
    if not args.input and not args.batch:
        parser.error("Cần --input hoặc --batch")

    if not args.text and not args.logo and not args.audio_watermark:
        parser.error("Cần ít nhất 1 loại watermark: --text, --logo, hoặc --audio-watermark")

    # Create manager
    manager = WatermarkManager(output_dir=args.output_dir)

    # Prepare configs
    text_config = None
    if args.text:
        text_config = TextWatermarkConfig(
            text=args.text,
            font_size=args.text_size,
            font_color=args.text_color,
            opacity=args.text_opacity,
            position=WatermarkPosition(args.text_position),
            shadow=args.text_shadow
        )

    image_config = None
    if args.logo:
        image_config = ImageWatermarkConfig(
            image_path=args.logo,
            position=WatermarkPosition(args.logo_position),
            scale=args.logo_scale,
            opacity=args.logo_opacity
        )

    # Process
    try:
        if args.batch:
            # Batch processing
            outputs = manager.batch_watermark(args.batch, text_config, image_config)
            print(f"\n✓ Processed {len(outputs)} files")
            for out in outputs:
                if out:
                    print(f"  - {out}")
        else:
            # Single file
            output = manager.add_combined_watermark(
                args.input,
                text_config,
                image_config,
                args.output
            )
            print(f"\n✓ Output: {output}")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
