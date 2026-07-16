#!/usr/bin/env python3
"""
Batch URL Processor for Voice-Pro
Xử lý nhiều YouTube URLs cùng lúc với parallel processing
"""
import argparse
import logging
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import json
import time

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('batch-url-processor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


@dataclass
class VideoJob:
    """Data class cho mỗi video job"""
    url: str
    index: int
    status: str = "pending"
    output_file: str = ""
    error: str = ""
    start_time: float = 0
    end_time: float = 0


class BatchURLProcessor:
    """Xử lý batch URLs với parallel processing"""

    def __init__(self,
                 max_workers: int = 3,
                 output_dir: str = "./batch_output",
                 retry_count: int = 2):
        """
        Args:
            max_workers: Số lượng videos download đồng thời
            output_dir: Thư mục output
            retry_count: Số lần retry khi fail
        """
        self.max_workers = max_workers
        self.output_dir = Path(output_dir)
        self.retry_count = retry_count
        self.jobs: List[VideoJob] = []
        self.results: Dict[str, VideoJob] = {}

        # Tạo output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def load_urls_from_file(self, file_path: str) -> List[str]:
        """
        Load URLs từ file text

        Format hỗ trợ:
        - Mỗi dòng 1 URL
        - # để comment
        - Dòng trống bỏ qua
        """
        urls = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Bỏ qua comment và dòng trống
                    if line and not line.startswith('#'):
                        urls.append(line)

            logger.info(f"✓ Loaded {len(urls)} URLs from {file_path}")
            return urls

        except Exception as e:
            logger.error(f"✗ Lỗi đọc file {file_path}: {e}")
            return []

    def validate_url(self, url: str) -> bool:
        """Validate URL có phải YouTube không"""
        youtube_domains = [
            'youtube.com',
            'youtu.be',
            'm.youtube.com',
            'www.youtube.com'
        ]
        return any(domain in url.lower() for domain in youtube_domains)

    def process_single_url(self, job: VideoJob) -> VideoJob:
        """
        Xử lý 1 URL (download + process)

        Note: Function này gọi Voice-Pro downloader
        """
        job.start_time = time.time()
        job.status = "processing"

        try:
            logger.info(f"[{job.index}] Đang xử lý: {job.url}")

            # Validate URL
            if not self.validate_url(job.url):
                raise ValueError(f"URL không hợp lệ: {job.url}")

            # Import Voice-Pro modules
            try:
                from app.abus_downloader import download_youtube
                from app.abus_path import path_youtube_folder
            except ImportError:
                logger.warning("⚠ Không thể import Voice-Pro modules")
                logger.info("Sử dụng yt-dlp fallback...")
                return self._fallback_download(job)

            # Setup output path
            output_base = path_youtube_folder()

            # Download video
            result = download_youtube(
                url=job.url,
                output_path=str(output_base),
                format='best',
                audio_only=False
            )

            if result and result.get('success'):
                job.status = "completed"
                job.output_file = result.get('filepath', '')
                logger.info(f"✓ [{job.index}] Hoàn thành: {job.output_file}")
            else:
                raise Exception("Download thất bại")

        except Exception as e:
            job.status = "failed"
            job.error = str(e)
            logger.error(f"✗ [{job.index}] Lỗi: {e}")

        finally:
            job.end_time = time.time()

        return job

    def _fallback_download(self, job: VideoJob) -> VideoJob:
        """
        Fallback download sử dụng yt-dlp trực tiếp
        """
        try:
            import yt_dlp

            output_template = str(self.output_dir / f"video_{job.index}_%(title)s.%(ext)s")

            ydl_opts = {
                'format': 'best',
                'outtmpl': output_template,
                'quiet': False,
                'no_warnings': False,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(job.url, download=True)
                job.output_file = ydl.prepare_filename(info)
                job.status = "completed"
                logger.info(f"✓ [{job.index}] Downloaded: {job.output_file}")

        except Exception as e:
            job.status = "failed"
            job.error = str(e)
            logger.error(f"✗ [{job.index}] Fallback failed: {e}")

        return job

    def process_batch(self, urls: List[str]) -> Dict[str, VideoJob]:
        """
        Xử lý batch URLs với parallel processing

        Returns:
            Dict mapping URL -> VideoJob
        """
        # Tạo jobs
        self.jobs = [
            VideoJob(url=url, index=i+1)
            for i, url in enumerate(urls)
        ]

        logger.info(f"=== Batch Processing: {len(self.jobs)} URLs ===")
        logger.info(f"Workers: {self.max_workers}")
        logger.info(f"Output: {self.output_dir}")

        # Process với ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit tất cả jobs
            future_to_job = {
                executor.submit(self.process_single_url, job): job
                for job in self.jobs
            }

            # Track progress
            completed = 0
            for future in as_completed(future_to_job):
                job = future.result()
                self.results[job.url] = job
                completed += 1

                # Progress
                logger.info(f"Progress: {completed}/{len(self.jobs)}")

        return self.results

    def generate_report(self) -> Dict:
        """Tạo báo cáo kết quả"""
        total = len(self.results)
        completed = sum(1 for j in self.results.values() if j.status == "completed")
        failed = sum(1 for j in self.results.values() if j.status == "failed")

        report = {
            "summary": {
                "total": total,
                "completed": completed,
                "failed": failed,
                "success_rate": f"{(completed/total*100):.1f}%" if total > 0 else "0%"
            },
            "jobs": []
        }

        for job in self.results.values():
            duration = job.end_time - job.start_time if job.end_time > 0 else 0
            report["jobs"].append({
                "index": job.index,
                "url": job.url,
                "status": job.status,
                "output_file": job.output_file,
                "error": job.error,
                "duration_seconds": round(duration, 2)
            })

        return report

    def save_report(self, filename: str = "batch_report.json"):
        """Lưu report ra file"""
        report = self.generate_report()
        report_path = self.output_dir / filename

        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        logger.info(f"✓ Report saved: {report_path}")
        return report_path

    def print_summary(self):
        """In ra summary"""
        report = self.generate_report()

        print("\n" + "="*60)
        print("📊 BATCH PROCESSING SUMMARY")
        print("="*60)
        print(f"Total URLs:      {report['summary']['total']}")
        print(f"✓ Completed:     {report['summary']['completed']}")
        print(f"✗ Failed:        {report['summary']['failed']}")
        print(f"Success Rate:    {report['summary']['success_rate']}")
        print("="*60)

        # Chi tiết failed jobs
        if report['summary']['failed'] > 0:
            print("\n⚠️  Failed Jobs:")
            for job_data in report['jobs']:
                if job_data['status'] == 'failed':
                    print(f"  [{job_data['index']}] {job_data['url']}")
                    print(f"      Error: {job_data['error']}")

        print()


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Batch URL Processor for Voice-Pro',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:

1. Xử lý URLs từ file:
   python batch_url_processor.py --file urls.txt

2. Xử lý URLs trực tiếp:
   python batch_url_processor.py --urls "URL1" "URL2" "URL3"

3. Chỉ định số workers và output:
   python batch_url_processor.py --file urls.txt --workers 5 --output ./videos

4. Format file urls.txt:
   # Video list
   https://youtube.com/watch?v=ABC
   https://youtube.com/watch?v=DEF
   # Comment bắt đầu bằng #
   https://youtube.com/watch?v=GHI
        """
    )

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

    return parser.parse_args()


def main():
    """Main entry point"""
    try:
        args = parse_arguments()

        # Load URLs
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

        # Tạo processor
        processor = BatchURLProcessor(
            max_workers=args.workers,
            output_dir=args.output,
            retry_count=args.retry
        )

        # Process batch
        logger.info(f"Bắt đầu xử lý {len(urls)} URLs...")
        results = processor.process_batch(urls)

        # Save report
        processor.save_report(args.report)

        # Print summary
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
