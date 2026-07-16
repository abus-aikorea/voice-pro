#!/usr/bin/env python3
"""
Voice-Pro Main Application (With Auto-Updater)
Khởi tạo ứng dụng với auto-update yt-dlp, parallel downloads, validation

Tự động update yt-dlp mới nhất mỗi lần chạy!
"""
import argparse
import os
import sys
import logging
from pathlib import Path
from typing import List, Dict, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass

# Setup đường dẫn
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import yt-dlp updater
from yt_dlp_updater import (
    YtDlpUpdater,
    FFmpegChecker,
    check_dependencies
)

# Import Voice-Pro modules
from src.config import UserConfig
from app.abus_hf import AbusHuggingFace
from app.abus_genuine import genuine_init
from app.abus_app_voice import create_ui
from app.abus_path import path_workspace_folder, path_gradio_folder


# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('voice-pro-app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


@dataclass
class ModelConfig:
    """Cấu hình cho mỗi model cần download"""
    file_type: str
    level: int
    required: bool = True
    description: str = ""


class VoiceProApp:
    """Class chính quản lý Voice-Pro application"""

    # Danh sách models cần download
    MODELS = [
        ModelConfig('demucs', 0, True, "Demucs - Voice separation"),
        ModelConfig('edge-tts', 0, True, "Edge TTS - Text to Speech"),
        ModelConfig('kokoro', 0, True, "Kokoro - High quality TTS"),
        ModelConfig('cosyvoice', 0, True, "CosyVoice - Voice cloning"),
    ]

    def __init__(self,
                 max_workers: int = 4,
                 skip_model_check: bool = False,
                 auto_update_ytdlp: bool = True,
                 ytdlp_install_dir: str = None):
        """
        Args:
            max_workers: Số lượng worker cho parallel downloads
            skip_model_check: Bỏ qua kiểm tra model sau download
            auto_update_ytdlp: Tự động update yt-dlp mới nhất
            ytdlp_install_dir: Thư mục cài yt-dlp (default: current dir)
        """
        self.max_workers = max_workers
        self.skip_model_check = skip_model_check
        self.auto_update_ytdlp = auto_update_ytdlp
        self.ytdlp_install_dir = ytdlp_install_dir or str(PROJECT_ROOT)
        self.download_results: Dict[str, bool] = {}

    def check_and_update_dependencies(self) -> bool:
        """
        Kiểm tra và update dependencies (yt-dlp, ffmpeg)

        Returns:
            True nếu tất cả dependencies OK
        """
        try:
            logger.info("=== Checking Dependencies ===")

            # Check và update yt-dlp
            if self.auto_update_ytdlp:
                logger.info("Auto-update yt-dlp: ENABLED")
                ytdlp_ok, ffmpeg_ok = check_dependencies(
                    install_dir=self.ytdlp_install_dir,
                    auto_update_ytdlp=True
                )
            else:
                logger.info("Auto-update yt-dlp: DISABLED")
                # Chỉ check không update
                updater = YtDlpUpdater(self.ytdlp_install_dir)
                ytdlp_ok = updater.executable_path.exists()
                ffmpeg_ok = FFmpegChecker.is_available()

                if ytdlp_ok:
                    version = updater.get_current_version()
                    logger.info(f"✓ yt-dlp: {version}")
                else:
                    logger.warning("⚠ yt-dlp not found")

                if ffmpeg_ok:
                    version = FFmpegChecker.get_version()
                    logger.info(f"✓ FFmpeg: {version}")
                else:
                    logger.warning("⚠ FFmpeg not found")

            # FFmpeg là required, yt-dlp có thể optional tùy use case
            if not ffmpeg_ok:
                logger.error("✗ FFmpeg is required!")
                logger.error(FFmpegChecker.get_install_instructions())
                return False

            if not ytdlp_ok:
                logger.warning("⚠ yt-dlp not available - YouTube features may not work")
                # Không return False vì có thể không dùng YouTube features

            logger.info("=== Dependencies Check Complete ===")
            return True

        except Exception as e:
            logger.error(f"✗ Error checking dependencies: {e}")
            return False

    def initialize(self) -> bool:
        """Khởi tạo môi trường và kiểm tra hệ thống"""
        try:
            logger.info("=== Voice-Pro Initialization ===")

            # Bước 1: Check và update dependencies
            if not self.check_and_update_dependencies():
                logger.warning("⚠ Some dependencies missing, continuing anyway...")
                # Không return False vì có thể vẫn chạy được một số features

            # Bước 2: Khởi tạo genuine/license check
            logger.info("Đang kiểm tra license...")
            genuine_init()
            logger.info("✓ License OK")

            # Bước 3: Khởi tạo Hugging Face
            logger.info("Đang khởi tạo Hugging Face...")
            AbusHuggingFace.initialize(app_name="voice")
            logger.info("✓ Hugging Face initialized")

            return True

        except Exception as e:
            logger.error(f"✗ Lỗi khởi tạo: {e}")
            return False

    def download_model(self, model: ModelConfig) -> Tuple[str, bool, str]:
        """
        Download một model từ Hugging Face

        Returns:
            Tuple[file_type, success, error_message]
        """
        try:
            logger.info(f"Downloading {model.file_type}: {model.description}")
            AbusHuggingFace.hf_download_models(
                file_type=model.file_type,
                level=model.level
            )
            logger.info(f"✓ Downloaded {model.file_type}")
            return (model.file_type, True, "")

        except Exception as e:
            error_msg = f"Lỗi download {model.file_type}: {str(e)}"
            logger.error(f"✗ {error_msg}")
            return (model.file_type, False, error_msg)

    def download_models_parallel(self) -> bool:
        """Download tất cả models song song"""
        logger.info("=== Downloading AI Models ===")
        logger.info(f"Sử dụng {self.max_workers} workers")

        # Lọc models cần download
        models_to_download = [m for m in self.MODELS if m.required]

        logger.info(f"Cần download {len(models_to_download)} models")

        # Download song song với ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit tất cả tasks
            future_to_model = {
                executor.submit(self.download_model, model): model
                for model in models_to_download
            }

            # Theo dõi tiến trình
            completed = 0
            failed = []

            for future in as_completed(future_to_model):
                model = future_to_model[future]
                file_type, success, error_msg = future.result()

                completed += 1
                self.download_results[file_type] = success

                if not success:
                    failed.append((file_type, error_msg))

                logger.info(f"Tiến trình: {completed}/{len(models_to_download)}")

        # Kiểm tra kết quả
        if failed:
            logger.error(f"✗ {len(failed)} models download thất bại:")
            for file_type, error in failed:
                logger.error(f"  - {file_type}: {error}")
            return False

        logger.info("✓ Tất cả models download thành công")
        return True

    def setup_workspace(self) -> bool:
        """Thiết lập workspace folders"""
        try:
            logger.info("Đang thiết lập workspace...")
            path_workspace_folder()
            path_gradio_folder()
            logger.info("✓ Workspace setup hoàn tất")
            return True
        except Exception as e:
            logger.error(f"✗ Lỗi setup workspace: {e}")
            return False

    def load_config(self) -> UserConfig:
        """Load user configuration"""
        try:
            logger.info("Đang load configuration...")
            config_path = PROJECT_ROOT / "app" / "config-user.json5"

            if not config_path.exists():
                logger.warning(f"⚠ Config file không tồn tại: {config_path}")
                logger.info("Sẽ sử dụng config mặc định")

            user_config = UserConfig(str(config_path))
            logger.info("✓ Configuration loaded")
            return user_config

        except Exception as e:
            logger.error(f"✗ Lỗi load config: {e}")
            raise

    def create_ui(self, user_config: UserConfig) -> bool:
        """Tạo và khởi động Gradio UI"""
        try:
            logger.info("=== Starting Web UI ===")
            create_ui(user_config=user_config)
            return True
        except Exception as e:
            logger.error(f"✗ Lỗi tạo UI: {e}")
            return False

    def run(self) -> int:
        """Chạy toàn bộ ứng dụng"""
        try:
            # Bước 1: Khởi tạo (bao gồm check dependencies)
            if not self.initialize():
                return 1

            # Bước 2: Download models
            if not self.download_models_parallel():
                logger.warning("⚠ Một số models download thất bại")
                logger.info("Ứng dụng có thể không hoạt động đầy đủ")

            # Bước 3: Setup workspace
            if not self.setup_workspace():
                return 1

            # Bước 4: Load config
            user_config = self.load_config()

            # Bước 5: Tạo UI và chạy
            if not self.create_ui(user_config):
                return 1

            logger.info("✓ Voice-Pro đang chạy!")
            return 0

        except KeyboardInterrupt:
            logger.info("\n⚠ Đã dừng bởi người dùng")
            return 130
        except Exception as e:
            logger.exception(f"✗ Lỗi không mong đợi: {e}")
            return 1


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Voice-Pro Main Application (With Auto-Updater)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Auto-update yt-dlp mới nhất mỗi lần chạy!

Examples:
  # Chạy với auto-update yt-dlp (default)
  python start-voice-with-updater.py

  # Chạy không update yt-dlp
  python start-voice-with-updater.py --no-ytdlp-update

  # Custom yt-dlp install directory
  python start-voice-with-updater.py --ytdlp-dir ./tools

  # Parallel downloads với 8 workers
  python start-voice-with-updater.py --workers 8
        """
    )

    parser.add_argument(
        '--workers',
        type=int,
        default=4,
        help='Số lượng workers cho parallel downloads (default: 4)'
    )

    parser.add_argument(
        '--skip-model-check',
        action='store_true',
        help='Bỏ qua kiểm tra model sau download'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Hiển thị log chi tiết'
    )

    parser.add_argument(
        '--sequential',
        action='store_true',
        help='Download models tuần tự thay vì song song'
    )

    parser.add_argument(
        '--no-ytdlp-update',
        action='store_true',
        help='Không tự động update yt-dlp'
    )

    parser.add_argument(
        '--ytdlp-dir',
        type=str,
        help='Thư mục cài đặt yt-dlp (default: current dir)'
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_arguments()

    # Điều chỉnh log level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Tạo app
    app = VoiceProApp(
        max_workers=1 if args.sequential else args.workers,
        skip_model_check=args.skip_model_check,
        auto_update_ytdlp=not args.no_ytdlp_update,
        ytdlp_install_dir=args.ytdlp_dir
    )

    # Chạy app
    exit_code = app.run()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
