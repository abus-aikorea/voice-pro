"""WebVTT format regressions; runnable without audio or model dependencies."""

from pathlib import Path
import tempfile
import unittest

from app.abus_subtitle import get_serialized_vtt, get_vtt, parse_vtt


class WebVTTHeaderTests(unittest.TestCase):
    def parse_text(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "captions.vtt"
            path.write_bytes(text.encode("utf-8"))
            return parse_vtt(path)

    def test_writers_use_standard_magic(self):
        segments = [{"start": 0.0, "end": 1.0, "text": "Hello"}]
        cues = [{"index": "1", "timestamp": "00:00:00.000 --> 00:00:01.000", "sentence": "Hello"}]
        for output in (get_vtt(segments), get_serialized_vtt(cues)):
            with self.subTest(output=output):
                self.assertTrue(output.startswith("WEBVTT\n\n"))
                self.assertEqual(self.parse_text(output), cues)

    def test_standard_header_with_bom_comments_and_line_endings(self):
        for bom in ("", "\ufeff"):
            for newline in ("\n", "\r\n"):
                for header in ("WEBVTT", "WEBVTT captions", "WEBVTT\tcaptions"):
                    with self.subTest(bom=bool(bom), newline=newline, header=header):
                        content = bom + newline.join([
                            header, "", "1", "00:00:00.000 --> 00:00:01.000",
                            "Hello", "world", "",
                        ])
                        self.assertEqual(self.parse_text(content), [{
                            "index": "1",
                            "timestamp": "00:00:00.000 --> 00:00:01.000",
                            "sentence": "Hello world",
                        }])

    def test_legacy_mixed_case_exports_remain_readable(self):
        content = "WebVTT\n\n1\n00:00:00.000 --> 00:00:01.000\nHello\n"
        self.assertEqual(self.parse_text(content)[0]["sentence"], "Hello")

    def test_cue_identifier_is_not_treated_as_another_header(self):
        content = "WEBVTT\n\nWEBVTT-cue\n00:00:00.000 --> 00:00:01.000\nHello\n"
        self.assertEqual(self.parse_text(content)[0]["index"], "WEBVTT-cue")

    def test_header_only_file(self):
        self.assertEqual(self.parse_text("WEBVTT\n\n"), [])


if __name__ == "__main__":
    unittest.main()
