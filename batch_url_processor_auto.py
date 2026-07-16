#!/usr/bin/env python3
"""
Batch URL Processor (With Auto-Updater)
Xử lý nhiều YouTube URLs cùng lúc với auto-update yt-dlp

Tự động update yt-dlp mới nhất trước khi download!
"""
import sys
import logging
from pathlib import Path

# Import yt-dlp updater
from yt_dlp_updater import YtDlpUpdater, FFmpegChecker

# Import original batch processor
from batch_url_processor import (
    BatchURLProcessor,
    parse_arguments as original_parse_arguments,
    main as original_main
)

logger = logging.getLogger(__name__)


def check_and_update_ytdlp(ytdlp_dir: str = None, skip_update: bool = False) -> bool:
    """
    Check và update yt-dlp trước khi batch processing

    Args:
        ytdlp_dir: Thư mục cài yt-dlp
        skip_update: Skip auto-update

    Returns:
        True nếu yt-dlp sẵn sàng
    """
    try:
        logger.info("="*60)
        logger.info("Checking yt-dlp...")
        logger.info("="*60)

        updater = YtDlpUpdater(ytdlp_dir)

        if skip_update:
            logger.info("Auto-update: DISABLED")
            # Chỉ check
            if not updater.executable_path.exists():
                logger.error("✗ yt-dlp not found!")
                logger.error("Run with auto-update or install yt-dlp manually")
                return False

            version = updater.get_current_version()
            logger.info(f"✓ yt-dlp: {version}")
            return True

        else:
            logger.info("Auto-update: ENABLED")
            # Check và update
            success = updater.ensure_ytdlp(auto_update=True)

            if success:
                version = updater.get_current_version()
                logger.info(f"✓ yt-dlp ready: {version}")
                return True
            else:
                logger.error("✗ Failed to ensure yt-dlp")
                return False

    except Exception as e:
        logger.error(f"✗ Error checking yt-dlp: {e}")
        return False


def parse_arguments():
    """Parse arguments with additional yt-dlp options"""
    import argparse

    # Use original parser as base
    parser = argparse.ArgumentParser(
        description='Batch URL Processor (With Auto-Updater)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Auto-update yt-dlp trước khi download!

Examples:

1. Batch processing với auto-update (default):
   python batch_url_processor_auto.py --file urls.txt

2. Skip auto-update:
   python batch_url_processor_auto.py --file urls.txt --no-ytdlp-update

3. Custom yt-dlp directory:
   python batch_url_processor_auto.py --file urls.txt --ytdlp-dir ./tools

4. Process với nhiều workers:
   python batch_url_processor_auto.py --file urls.txt --workers 5
        """
    )

    # Input
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        '--file', '-f',
        type=str,
        help='File chứa danh sách URLs (mỗi dòng 1 URL)'
    )
    input_group.add_argument(
        '--urls', '-u',
        nargs='+',
        help='List URLs trực tiếp'
    )

    # Processing
    parser.add_argument(
        '--workers', '-w',
        type=int,
        default=3,
        help='Số lượng workers download song song (default: 3)'
    )

    parser.add_argument(
        '--output', '-o',
        type=str,
        default='./batch_output',
        help='Thư mục output (default: ./batch_output)'
    )

    parser.add_argument(
        '--retry',
        type=int,
        default=2,
        help='Số lần retry khi fail (default: 2)'
    )

    parser.add_argument(
        '--report',
        type=str,
        default='batch_report.json',
        help='Tên file report (default: batch_report.json)'
    )

    # YT-DLP options
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
    """Main entry point với auto-update yt-dlp"""
    try:
        args = parse_arguments()

        # Bước 1: Check và update yt-dlp
        ytdlp_ok = check_and_update_ytdlp(
            ytdlp_dir=args.ytdlp_dir,
            skip_update=args.no_ytdlp_update
        )

        if not ytdlp_ok:
            logger.error("✗ yt-dlp not ready!")
            logger.error("Cannot proceed with batch processing")
            sys.exit(1)

        # Bước 2: Check FFmpeg (optional warning)
        if not FFmpegChecker.is_available():
            logger.warning("⚠ FFmpeg not found - may affect some features")
            logger.warning(FFmpegChecker.get_install_instructions())

        # Bước 3: Load URLs
        if args.file:
            processor = BatchURLProcessor(
                max_workers=args.workers,
                output_dir=args.output,
                retry_count=args.retry
            )
            urls = processor.load_urls_from_file(args.file)
        else:
            urls = args.urls

        if not urls:
            logger.error("✗ Không có URL nào để xử lý")
            sys.exit(1)

        # Bước 4: Tạo processor
        processor = BatchURLProcessor(
            max_workers=args.workers,
            output_dir=args.output,
            retry_count=args.retry
        )

        # Bước 5: Process batch
        logger.info(f"Bắt đầu xử lý {len(urls)} URLs...")
        results = processor.process_batch(urls)

        # Bước 6: Save report
        processor.save_report(args.report)

        # Bước 7: Print summary
        processor.print_summary()

        # Exit code
        failed = sum(1 for j in results.values() if j.status == "failed")
        sys.exit(1 if failed > 0 else 0)

    except KeyboardInterrupt:
        logger.info("\n⚠ Đã hủy bởi người dùng")
        sys.exit(130)
    except Exception as e:
        logger.exception(f"✗ Lỗi không mong đợi: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
