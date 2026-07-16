#!/usr/bin/env python3
"""
YT-DLP Auto Updater for Voice-Pro
Tự động tải và cập nhật yt-dlp mới nhất

Features:
- ✅ Cross-platform (Windows, Linux, macOS)
- ✅ Auto-detect latest version
- ✅ Download từ GitHub releases
- ✅ Version checking (skip nếu đã latest)
- ✅ Fallback nếu download fail
- ✅ Logging đầy đủ
"""

import os
import sys
import platform
import subprocess
import logging
import urllib.request
import json
from pathlib import Path
from typing import Optional, Tuple
import tempfile
import shutil

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class YtDlpUpdater:
    """
    Auto updater cho yt-dlp
    """

    # GitHub API endpoints
    GITHUB_API_LATEST = "https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest"
    GITHUB_RELEASE_BASE = "https://github.com/yt-dlp/yt-dlp/releases/latest/download"

    def __init__(self, install_dir: Optional[str] = None):
        """
        Args:
            install_dir: Thư mục cài đặt yt-dlp (default: current dir)
        """
        self.install_dir = Path(install_dir) if install_dir else Path.cwd()
        self.platform = platform.system().lower()
        self.executable_name = self._get_executable_name()
        self.executable_path = self.install_dir / self.executable_name

    def _get_executable_name(self) -> str:
        """Lấy tên executable tùy platform"""
        if self.platform == "windows":
            return "yt-dlp.exe"
        else:
            return "yt-dlp"

    def _get_download_url(self) -> str:
        """Lấy download URL tùy platform"""
        base_url = self.GITHUB_RELEASE_BASE

        if self.platform == "windows":
            return f"{base_url}/yt-dlp.exe"
        elif self.platform == "darwin":  # macOS
            return f"{base_url}/yt-dlp_macos"
        else:  # Linux
            return f"{base_url}/yt-dlp"

    def get_latest_version(self) -> Optional[str]:
        """
        Lấy version mới nhất từ GitHub API

        Returns:
            Version string (vd: "2024.11.13") hoặc None nếu fail
        """
        try:
            logger.info("Đang kiểm tra version mới nhất...")

            # Call GitHub API
            req = urllib.request.Request(self.GITHUB_API_LATEST)
            req.add_header('User-Agent', 'Voice-Pro-YtDlp-Updater')

            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                version = data.get('tag_name', '').strip()
                logger.info(f"✓ Version mới nhất: {version}")
                return version

        except Exception as e:
            logger.error(f"✗ Lỗi lấy latest version: {e}")
            return None

    def get_current_version(self) -> Optional[str]:
        """
        Lấy version hiện tại của yt-dlp

        Returns:
            Version string hoặc None nếu chưa cài
        """
        if not self.executable_path.exists():
            logger.info("yt-dlp chưa được cài đặt")
            return None

        try:
            result = subprocess.run(
                [str(self.executable_path), '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                version = result.stdout.strip()
                logger.info(f"Version hiện tại: {version}")
                return version

            return None

        except Exception as e:
            logger.error(f"✗ Lỗi kiểm tra version hiện tại: {e}")
            return None

    def is_update_needed(self) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Kiểm tra có cần update không

        Returns:
            Tuple[need_update, current_version, latest_version]
        """
        current_version = self.get_current_version()
        latest_version = self.get_latest_version()

        if latest_version is None:
            logger.warning("⚠ Không thể kiểm tra latest version")
            return False, current_version, None

        if current_version is None:
            logger.info("ℹ yt-dlp chưa cài đặt, cần download")
            return True, None, latest_version

        # Compare versions
        if current_version != latest_version:
            logger.info(f"ℹ Update available: {current_version} → {latest_version}")
            return True, current_version, latest_version
        else:
            logger.info("✓ yt-dlp đã là version mới nhất")
            return False, current_version, latest_version

    def download_ytdlp(self, force: bool = False) -> bool:
        """
        Download yt-dlp mới nhất

        Args:
            force: Bắt buộc download dù đã có version mới

        Returns:
            True nếu thành công
        """
        try:
            # Check nếu cần update
            if not force:
                need_update, current, latest = self.is_update_needed()
                if not need_update:
                    logger.info("✓ Không cần update")
                    return True

            logger.info("="*60)
            logger.info("[CẬP NHẬT] Đang tải yt-dlp mới nhất...")
            logger.info("="*60)

            # Backup old version (if exists)
            if self.executable_path.exists():
                backup_path = self.executable_path.with_suffix('.bak')
                logger.info(f"Backup version cũ: {backup_path}")
                shutil.copy2(self.executable_path, backup_path)

                # Delete old
                self.executable_path.unlink()
                logger.info("Đã xóa version cũ")

            # Download URL
            download_url = self._get_download_url()
            logger.info(f"Download từ: {download_url}")

            # Download với progress
            temp_path = self.install_dir / f"{self.executable_name}.tmp"

            def report_progress(block_num, block_size, total_size):
                """Report download progress"""
                if total_size > 0:
                    percent = min(100, block_num * block_size * 100 / total_size)
                    mb_downloaded = block_num * block_size / 1024 / 1024
                    mb_total = total_size / 1024 / 1024
                    sys.stdout.write(
                        f"\r  Đang tải: {percent:.1f}% ({mb_downloaded:.1f}/{mb_total:.1f} MB)"
                    )
                    sys.stdout.flush()

            # Download
            urllib.request.urlretrieve(
                download_url,
                temp_path,
                reporthook=report_progress
            )
            print()  # New line after progress

            # Move temp to final location
            shutil.move(str(temp_path), str(self.executable_path))

            # Make executable (Unix-like systems)
            if self.platform != "windows":
                os.chmod(self.executable_path, 0o755)
                logger.info("✓ Đã set executable permission")

            logger.info("="*60)
            logger.info("[CẬP NHẬT] Đã cập nhật thành công yt-dlp mới nhất!")
            logger.info("="*60)

            # Verify download
            new_version = self.get_current_version()
            if new_version:
                logger.info(f"✓ Version mới: {new_version}")
                return True
            else:
                logger.error("✗ Download thành công nhưng không verify được version")
                return False

        except Exception as e:
            logger.error(f"✗ Lỗi download yt-dlp: {e}")

            # Restore backup if exists
            backup_path = self.executable_path.with_suffix('.bak')
            if backup_path.exists():
                logger.info("Khôi phục version cũ từ backup...")
                shutil.copy2(backup_path, self.executable_path)

            return False

    def ensure_ytdlp(self, auto_update: bool = True) -> bool:
        """
        Đảm bảo yt-dlp có sẵn và updated

        Args:
            auto_update: Tự động update nếu có version mới

        Returns:
            True nếu yt-dlp sẵn sàng
        """
        try:
            # Check exists
            if not self.executable_path.exists():
                logger.info("yt-dlp chưa cài đặt, đang download...")
                return self.download_ytdlp(force=True)

            # Check update
            if auto_update:
                need_update, current, latest = self.is_update_needed()
                if need_update:
                    logger.info(f"Update available: {current} → {latest}")
                    return self.download_ytdlp(force=True)

            logger.info("✓ yt-dlp sẵn sàng")
            return True

        except Exception as e:
            logger.error(f"✗ Lỗi ensure yt-dlp: {e}")
            return False

    def get_ytdlp_path(self) -> str:
        """
        Lấy đường dẫn đến yt-dlp executable

        Returns:
            Absolute path string
        """
        return str(self.executable_path.absolute())

    def cleanup_backups(self):
        """Xóa các backup files"""
        try:
            backup_path = self.executable_path.with_suffix('.bak')
            if backup_path.exists():
                backup_path.unlink()
                logger.info("✓ Đã xóa backup file")
        except Exception as e:
            logger.error(f"✗ Lỗi xóa backup: {e}")


class FFmpegChecker:
    """
    Kiểm tra FFmpeg availability
    (Không auto-download vì phức tạp, chỉ check)
    """

    @staticmethod
    def is_available() -> bool:
        """Kiểm tra FFmpeg có sẵn không"""
        try:
            result = subprocess.run(
                ['ffmpeg', '-version'],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except:
            return False

    @staticmethod
    def get_version() -> Optional[str]:
        """Lấy version của FFmpeg"""
        try:
            result = subprocess.run(
                ['ffmpeg', '-version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                # Extract version from first line
                first_line = result.stdout.split('\n')[0]
                # Example: "ffmpeg version 4.4.2-0ubuntu0.22.04.1"
                if 'version' in first_line:
                    version = first_line.split('version')[1].split()[0]
                    return version
        except:
            pass
        return None

    @staticmethod
    def get_install_instructions() -> str:
        """Hướng dẫn cài đặt FFmpeg"""
        system = platform.system().lower()

        if system == "windows":
            return """
FFmpeg chưa được cài đặt!

Cài đặt FFmpeg trên Windows:
1. Download từ: https://www.gyan.dev/ffmpeg/builds/
2. Giải nén và copy ffmpeg.exe vào folder này
3. Hoặc thêm vào PATH environment variable

Hoặc dùng chocolatey:
  choco install ffmpeg
"""
        elif system == "darwin":
            return """
FFmpeg chưa được cài đặt!

Cài đặt FFmpeg trên macOS:
  brew install ffmpeg
"""
        else:  # Linux
            return """
FFmpeg chưa được cài đặt!

Cài đặt FFmpeg:
  # Ubuntu/Debian
  sudo apt update && sudo apt install ffmpeg

  # Fedora
  sudo dnf install ffmpeg

  # Arch
  sudo pacman -S ffmpeg
"""

    @classmethod
    def ensure_ffmpeg(cls) -> bool:
        """
        Đảm bảo FFmpeg có sẵn

        Returns:
            True nếu FFmpeg sẵn sàng
        """
        if cls.is_available():
            version = cls.get_version()
            logger.info(f"✓ FFmpeg sẵn sàng (version: {version})")
            return True
        else:
            logger.error("✗ FFmpeg không tìm thấy!")
            logger.error(cls.get_install_instructions())
            return False


# ============================================================================
# Helper Functions
# ============================================================================

def auto_update_ytdlp(install_dir: Optional[str] = None,
                      force: bool = False) -> bool:
    """
    Helper: Tự động update yt-dlp

    Args:
        install_dir: Thư mục cài đặt (default: current dir)
        force: Force update dù đã latest

    Returns:
        True nếu thành công
    """
    updater = YtDlpUpdater(install_dir)
    return updater.ensure_ytdlp(auto_update=True)


def get_ytdlp_path(install_dir: Optional[str] = None) -> Optional[str]:
    """
    Helper: Lấy path đến yt-dlp executable

    Args:
        install_dir: Thư mục cài đặt

    Returns:
        Path string hoặc None nếu không tìm thấy
    """
    updater = YtDlpUpdater(install_dir)
    if updater.executable_path.exists():
        return updater.get_ytdlp_path()
    return None


def check_dependencies(install_dir: Optional[str] = None,
                      auto_update_ytdlp: bool = True) -> Tuple[bool, bool]:
    """
    Helper: Kiểm tra tất cả dependencies

    Args:
        install_dir: Thư mục cài yt-dlp
        auto_update_ytdlp: Tự động update yt-dlp

    Returns:
        Tuple[ytdlp_ok, ffmpeg_ok]
    """
    logger.info("="*60)
    logger.info("Đang kiểm tra dependencies...")
    logger.info("="*60)

    # Check yt-dlp
    updater = YtDlpUpdater(install_dir)
    ytdlp_ok = updater.ensure_ytdlp(auto_update=auto_update_ytdlp)

    # Check ffmpeg
    ffmpeg_ok = FFmpegChecker.ensure_ffmpeg()

    logger.info("="*60)
    logger.info(f"yt-dlp: {'✓ OK' if ytdlp_ok else '✗ FAIL'}")
    logger.info(f"FFmpeg: {'✓ OK' if ffmpeg_ok else '✗ FAIL'}")
    logger.info("="*60)

    return ytdlp_ok, ffmpeg_ok


# ============================================================================
# CLI
# ============================================================================

def main():
    """CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(
        description='YT-DLP Auto Updater for Voice-Pro',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:

1. Check and update yt-dlp:
   python yt_dlp_updater.py --update

2. Force update (re-download):
   python yt_dlp_updater.py --update --force

3. Check version only:
   python yt_dlp_updater.py --check

4. Check all dependencies:
   python yt_dlp_updater.py --check-all

5. Custom install directory:
   python yt_dlp_updater.py --update --dir ./tools
        """
    )

    parser.add_argument('--update', action='store_true',
                       help='Update yt-dlp to latest version')
    parser.add_argument('--check', action='store_true',
                       help='Check current version')
    parser.add_argument('--check-all', action='store_true',
                       help='Check all dependencies (yt-dlp + ffmpeg)')
    parser.add_argument('--force', action='store_true',
                       help='Force update even if already latest')
    parser.add_argument('--dir', type=str,
                       help='Install directory (default: current dir)')
    parser.add_argument('--cleanup', action='store_true',
                       help='Cleanup backup files')

    args = parser.parse_args()

    # Default to check if no action specified
    if not any([args.update, args.check, args.check_all, args.cleanup]):
        args.check = True

    # Create updater
    updater = YtDlpUpdater(args.dir)

    try:
        # Cleanup
        if args.cleanup:
            updater.cleanup_backups()
            return

        # Check all dependencies
        if args.check_all:
            ytdlp_ok, ffmpeg_ok = check_dependencies(args.dir, auto_update_ytdlp=False)
            sys.exit(0 if (ytdlp_ok and ffmpeg_ok) else 1)

        # Update
        if args.update:
            success = updater.download_ytdlp(force=args.force)
            sys.exit(0 if success else 1)

        # Check version
        if args.check:
            current = updater.get_current_version()
            latest = updater.get_latest_version()

            print("\n" + "="*60)
            print("YT-DLP Version Info")
            print("="*60)
            print(f"Current: {current or 'Not installed'}")
            print(f"Latest:  {latest or 'Unknown'}")

            if current and latest and current != latest:
                print("\n⚠ Update available!")
                print(f"Run: python yt_dlp_updater.py --update")
            elif current and latest and current == latest:
                print("\n✓ Already latest version")

            print("="*60)

    except KeyboardInterrupt:
        print("\n⚠ Cancelled by user")
        sys.exit(130)
    except Exception as e:
        logger.exception(f"✗ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
