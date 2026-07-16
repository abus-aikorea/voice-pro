#!/usr/bin/env python3
"""
Voice-Pro Watermark Integration
Tích hợp watermark vào Voice-Pro pipeline

Tự động apply watermark sau khi xử lý video/audio
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import Optional, Dict, Any
from watermark_manager import (
    WatermarkManager,
    TextWatermarkConfig,
    ImageWatermarkConfig,
    AudioWatermarkConfig,
    WatermarkPosition
)

logger = logging.getLogger(__name__)


class VoiceProWatermarkIntegration:
    """
    Tích hợp watermark vào Voice-Pro workflow
    """

    def __init__(self, config_path: str = "watermark_config.json5"):
        """
        Args:
            config_path: Đường dẫn đến config file
        """
        self.config = self._load_config(config_path)
        self.manager = WatermarkManager(
            output_dir=self.config.get('batch', {}).get('output_dir', './watermarked')
        )

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load watermark configuration"""
        try:
            if not os.path.exists(config_path):
                logger.warning(f"Config không tồn tại: {config_path}, dùng default")
                return self._get_default_config()

            # Load JSON5
            try:
                import json5
                with open(config_path, 'r', encoding='utf-8') as f:
                    return json5.load(f)
            except ImportError:
                # Fallback to JSON
                with open(config_path, 'r', encoding='utf-8') as f:
                    # Remove comments for standard JSON
                    content = '\n'.join(
                        line for line in f
                        if not line.strip().startswith('//')
                    )
                    return json.loads(content)

        except Exception as e:
            logger.error(f"Lỗi load config: {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """Default configuration"""
        return {
            'text_watermark': {
                'enabled': True,
                'text': '© 2025 Voice-Pro',
                'position': 'bottom_right',
                'opacity': 0.5,
                'font_size': 24
            },
            'logo_watermark': {
                'enabled': False
            },
            'audio_watermark': {
                'enabled': False
            },
            'batch': {
                'output_dir': './watermarked'
            }
        }

    def _create_text_config(self) -> Optional[TextWatermarkConfig]:
        """Tạo TextWatermarkConfig từ config"""
        text_cfg = self.config.get('text_watermark', {})

        if not text_cfg.get('enabled', False):
            return None

        # Handle dynamic text
        text = text_cfg.get('text', '')
        if text_cfg.get('dynamic_text', {}).get('enabled'):
            text = self._render_dynamic_text(
                text_cfg['dynamic_text'].get('template', text)
            )

        return TextWatermarkConfig(
            text=text,
            font_size=text_cfg.get('font_size', 24),
            font_color=text_cfg.get('font_color', 'white'),
            font_file=text_cfg.get('font_file'),
            position=WatermarkPosition(text_cfg.get('position', 'bottom_right')),
            opacity=text_cfg.get('opacity', 0.5),
            margin_x=text_cfg.get('margin_x', 10),
            margin_y=text_cfg.get('margin_y', 10),
            shadow=text_cfg.get('shadow', True),
            background_color=text_cfg.get('background_color'),
            background_opacity=text_cfg.get('background_opacity', 0.3)
        )

    def _create_image_config(self) -> Optional[ImageWatermarkConfig]:
        """Tạo ImageWatermarkConfig từ config"""
        logo_cfg = self.config.get('logo_watermark', {})

        if not logo_cfg.get('enabled', False):
            return None

        image_path = logo_cfg.get('image_path')
        if not image_path or not os.path.exists(image_path):
            logger.warning(f"Logo không tồn tại: {image_path}")
            return None

        return ImageWatermarkConfig(
            image_path=image_path,
            position=WatermarkPosition(logo_cfg.get('position', 'top_right')),
            opacity=logo_cfg.get('opacity', 0.7),
            scale=logo_cfg.get('scale', 0.15),
            margin_x=logo_cfg.get('margin_x', 10),
            margin_y=logo_cfg.get('margin_y', 10)
        )

    def _render_dynamic_text(self, template: str) -> str:
        """Render dynamic text template"""
        from datetime import datetime

        replacements = {
            'year': str(datetime.now().year),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'timestamp': datetime.now().strftime('%Y%m%d_%H%M%S'),
            'company': 'Voice-Pro'
        }

        text = template
        for key, value in replacements.items():
            text = text.replace(f'{{{key}}}', value)

        return text

    def process_video(self,
                     input_video: str,
                     output_path: Optional[str] = None,
                     preset: Optional[str] = None) -> str:
        """
        Xử lý video với watermark

        Args:
            input_video: Đường dẫn video input
            output_path: Đường dẫn output (optional)
            preset: Preset name (subtle, strong, professional, youtube)

        Returns:
            Đường dẫn video output
        """
        try:
            logger.info(f"Processing video: {input_video}")

            # Apply preset if specified
            if preset:
                self._apply_preset(preset)

            # Create configs
            text_config = self._create_text_config()
            image_config = self._create_image_config()

            if not text_config and not image_config:
                logger.warning("Không có watermark config nào enabled")
                return input_video

            # Process
            output = self.manager.add_combined_watermark(
                input_video,
                text_config,
                image_config,
                output_path
            )

            return output

        except Exception as e:
            logger.error(f"Lỗi xử lý video: {e}")
            raise

    def process_audio(self,
                     input_audio: str,
                     output_path: Optional[str] = None) -> str:
        """
        Xử lý audio với invisible watermark

        Args:
            input_audio: Đường dẫn audio input
            output_path: Đường dẫn output (optional)

        Returns:
            Đường dẫn audio output
        """
        try:
            audio_cfg = self.config.get('audio_watermark', {})

            if not audio_cfg.get('enabled', False):
                logger.info("Audio watermark không enabled")
                return input_audio

            audio_config = AudioWatermarkConfig(
                watermark_text=audio_cfg.get('watermark_text', 'VoicePro_Audio'),
                method=audio_cfg.get('method', 'lsb'),
                strength=audio_cfg.get('strength', 0.1)
            )

            output = self.manager.add_audio_watermark(
                input_audio,
                audio_config,
                output_path
            )

            return output

        except Exception as e:
            logger.error(f"Lỗi xử lý audio: {e}")
            raise

    def _apply_preset(self, preset_name: str):
        """Apply a preset configuration"""
        presets = self.config.get('presets', {})
        preset = presets.get(preset_name)

        if not preset:
            logger.warning(f"Preset không tồn tại: {preset_name}")
            return

        # Update text config
        if 'text' in preset:
            self.config['text_watermark'].update(preset['text'])

        # Update logo config
        if 'logo' in preset:
            self.config['logo_watermark'].update(preset['logo'])

    def hook_voicepro_pipeline(self, video_path: str, pipeline_type: str) -> str:
        """
        Hook vào Voice-Pro pipeline để tự động apply watermark

        Args:
            video_path: Đường dẫn video sau khi xử lý
            pipeline_type: dubbed_video, subtitle_burn, extracted_audio

        Returns:
            Đường dẫn video đã watermark
        """
        integration_cfg = self.config.get('integration', {})

        # Check if auto apply enabled
        if not integration_cfg.get('auto_apply', False):
            return video_path

        # Check if apply to this pipeline type
        apply_to = integration_cfg.get('apply_to', {})
        if not apply_to.get(pipeline_type, False):
            return video_path

        # Determine file type
        file_ext = Path(video_path).suffix.lower()
        is_video = file_ext in ['.mp4', '.mkv', '.avi', '.mov', '.webm']
        is_audio = file_ext in ['.mp3', '.wav', '.flac', '.aac', '.ogg']

        # Process accordingly
        if is_video:
            return self.process_video(video_path)
        elif is_audio:
            return self.process_audio(video_path)
        else:
            logger.warning(f"Unsupported file type: {file_ext}")
            return video_path


# ============================================================================
# Helper Functions for Voice-Pro Integration
# ============================================================================

def watermark_dubbed_video(video_path: str, config_path: str = "watermark_config.json5") -> str:
    """
    Helper function: Watermark video sau khi dubbing

    Usage trong Voice-Pro:
        output_video = watermark_dubbed_video(dubbed_video_path)
    """
    integration = VoiceProWatermarkIntegration(config_path)
    return integration.process_video(video_path)


def watermark_batch_videos(video_paths: list, config_path: str = "watermark_config.json5") -> list:
    """
    Helper function: Watermark batch videos

    Usage trong Voice-Pro:
        watermarked_videos = watermark_batch_videos([video1, video2, video3])
    """
    integration = VoiceProWatermarkIntegration(config_path)
    outputs = []

    for video in video_paths:
        try:
            output = integration.process_video(video)
            outputs.append(output)
        except Exception as e:
            logger.error(f"Lỗi watermark {video}: {e}")
            outputs.append(None)

    return outputs


def auto_watermark_hook(file_path: str, pipeline_type: str) -> str:
    """
    Auto watermark hook - Gọi sau mỗi pipeline step

    Usage trong Voice-Pro pipeline:
        # Sau khi dubbing xong
        output_video = auto_watermark_hook(dubbed_video, 'dubbed_video')

        # Sau khi burn subtitle
        output_video = auto_watermark_hook(subtitle_video, 'subtitle_burn')

    Args:
        file_path: File path sau processing
        pipeline_type: dubbed_video, subtitle_burn, extracted_audio

    Returns:
        Watermarked file path (hoặc original nếu không apply)
    """
    try:
        integration = VoiceProWatermarkIntegration()
        return integration.hook_voicepro_pipeline(file_path, pipeline_type)
    except Exception as e:
        logger.error(f"Auto watermark hook failed: {e}")
        return file_path  # Return original on error


# ============================================================================
# CLI
# ============================================================================

def main():
    """CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(description='Voice-Pro Watermark Integration')

    parser.add_argument('input', help='Input video/audio file')
    parser.add_argument('--config', default='watermark_config.json5',
                       help='Config file path')
    parser.add_argument('--preset', choices=['subtle', 'strong', 'professional', 'youtube'],
                       help='Use preset configuration')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--type', choices=['video', 'audio'], default='video',
                       help='File type')

    args = parser.parse_args()

    # Create integration
    integration = VoiceProWatermarkIntegration(args.config)

    # Process
    try:
        if args.type == 'video':
            output = integration.process_video(args.input, args.output, args.preset)
        else:
            output = integration.process_audio(args.input, args.output)

        print(f"\n✓ Output: {output}")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
