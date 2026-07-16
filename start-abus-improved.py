#!/usr/bin/env python3
"""
Voice-Pro Application Launcher (Improved Version)
Khởi động ứng dụng với error handling và logging đầy đủ
"""
import argparse
import os
import sys
import shutil
import logging
from pathlib import Path
from typing import Optional
from one_click import *


# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('voice-pro.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class VoiceProLauncher:
    """Class quản lý việc khởi động Voice-Pro application"""

    VALID_APP_NAMES = ['voice']  # Danh sách app hợp lệ

    def __init__(self, app_name: str, is_update: bool = False):
        self.app_name = self._validate_app_name(app_name)
        self.is_update = is_update
        self.python_filename = f'start-{self.app_name}.py'

    def _validate_app_name(self, app_name: str) -> str:
        """Validate và sanitize app name"""
        # Loại bỏ ký tự nguy hiểm
        sanitized = ''.join(c for c in app_name if c.isalnum() or c in '-_')

        if sanitized != app_name:
            logger.warning(f"App name đã được sanitized: '{app_name}' -> '{sanitized}'")

        if sanitized not in self.VALID_APP_NAMES:
            logger.error(f"App name không hợp lệ: {sanitized}")
            logger.info(f"Các app hợp lệ: {', '.join(self.VALID_APP_NAMES)}")
            sys.exit(1)

        return sanitized

    def check_environment(self) -> bool:
        """Kiểm tra môi trường hệ thống"""
        try:
            logger.info("Đang kiểm tra môi trường hệ thống...")
            OneClick.oc_check_env()
            logger.info("✓ Môi trường hệ thống OK")
            return True
        except Exception as e:
            logger.error(f"✗ Lỗi kiểm tra môi trường: {e}")
            return False

    def check_app_script(self) -> bool:
        """Kiểm tra file script của app có tồn tại không"""
        if not os.path.exists(self.python_filename):
            logger.error(f"✗ Không tìm thấy file: {self.python_filename}")
            return False

        logger.info(f"✓ Đã tìm thấy script: {self.python_filename}")
        return True

    def setup_dependencies(self) -> bool:
        """Cài đặt hoặc cập nhật dependencies"""
        try:
            is_installed = OneClick.oc_is_installed()

            if not is_installed:
                logger.info("Đang cài đặt dependencies lần đầu...")
                OneClick.oc_install_webui(self.app_name, False)
                logger.info("✓ Cài đặt thành công")
                return True

            elif self.is_update:
                logger.info("Đang cập nhật dependencies...")
                OneClick.oc_install_webui(self.app_name, True)
                logger.info("✓ Cập nhật thành công")
                return True
            else:
                logger.info("✓ Dependencies đã được cài đặt")
                return True

        except Exception as e:
            logger.error(f"✗ Lỗi setup dependencies: {e}")
            return False

    def launch_app(self) -> bool:
        """Khởi động ứng dụng"""
        if self.is_update:
            logger.info("Chế độ update - không khởi động app")
            return True

        try:
            logger.info(f"Đang khởi động {self.app_name}...")
            # Sử dụng list để tránh shell injection
            OneClick.oc_run_cmd(f"python {self.python_filename}", environment=True)
            return True
        except Exception as e:
            logger.error(f"✗ Lỗi khởi động app: {e}")
            return False

    def run(self) -> int:
        """Chạy toàn bộ quy trình khởi động"""
        logger.info(f"=== Voice-Pro Launcher ===")
        logger.info(f"App: {self.app_name}")
        logger.info(f"Update mode: {self.is_update}")

        # Bước 1: Kiểm tra môi trường
        if not self.check_environment():
            return 1

        # Bước 2: Kiểm tra script
        if not self.check_app_script():
            return 1

        # Bước 3: Setup dependencies
        if not self.setup_dependencies():
            return 1

        # Bước 4: Khởi động app
        if not self.launch_app():
            return 1

        logger.info("✓ Hoàn tất!")
        return 0


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Voice-Pro Application Launcher',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python start-abus.py voice                  # Khởi động app voice
  python start-abus.py voice --update         # Cập nhật dependencies
  python start-abus.py voice --verbose        # Chạy với logging chi tiết
        """
    )

    parser.add_argument(
        'app_name',
        type=str,
        help='Tên ứng dụng cần khởi động (vd: voice)'
    )

    parser.add_argument(
        '--update',
        action='store_true',
        help='Chế độ cập nhật dependencies'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Hiển thị log chi tiết'
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    try:
        args = parse_arguments()

        # Điều chỉnh log level
        if args.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

        # Tạo launcher và chạy
        launcher = VoiceProLauncher(
            app_name=args.app_name,
            is_update=args.update
        )

        exit_code = launcher.run()
        sys.exit(exit_code)

    except KeyboardInterrupt:
        logger.info("\n⚠ Đã hủy bởi người dùng")
        sys.exit(130)
    except Exception as e:
        logger.exception(f"✗ Lỗi không mong đợi: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
