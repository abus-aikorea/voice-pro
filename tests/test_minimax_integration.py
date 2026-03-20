"""Integration tests for MiniMax TTS provider.

These tests require a valid MINIMAX_API_KEY environment variable.
They are skipped when the key is not available.
"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

MINIMAX_API_KEY = os.environ.get('MINIMAX_API_KEY')
SKIP_REASON = "MINIMAX_API_KEY not set"


@unittest.skipUnless(MINIMAX_API_KEY, SKIP_REASON)
class TestMiniMaxTTSIntegration(unittest.TestCase):
    """Integration tests that hit the real MiniMax TTS API."""

    def setUp(self):
        from app.abus_tts_minimax import MiniMaxTTS
        self.tts = MiniMaxTTS(model="speech-2.8-hd")
        self.output_files = []

    def tearDown(self):
        for f in self.output_files:
            if os.path.exists(f):
                os.remove(f)

    def _temp_file(self, suffix=".mp3"):
        f = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
        self.output_files.append(f.name)
        f.close()
        return f.name

    def test_generate_audio_english(self):
        output_file = self._temp_file()
        result = self.tts.generate_audio(
            "Hello, this is a test of the MiniMax text to speech API.",
            "English_Graceful_Lady",
            output_file,
        )
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 1000)

    def test_generate_audio_turbo_model(self):
        from app.abus_tts_minimax import MiniMaxTTS
        tts = MiniMaxTTS(model="speech-2.8-turbo")
        output_file = self._temp_file()
        result = tts.generate_audio(
            "Testing turbo model synthesis.",
            "Deep_Voice_Man",
            output_file,
        )
        self.assertTrue(result)
        self.assertGreater(os.path.getsize(output_file), 500)

    def test_generate_audio_with_speed(self):
        output_file = self._temp_file()
        result = self.tts.generate_audio(
            "Speed test synthesis.",
            "Friendly_Person",
            output_file,
            rate=50,
        )
        self.assertTrue(result)
        self.assertGreater(os.path.getsize(output_file), 500)


@unittest.skipUnless(MINIMAX_API_KEY, SKIP_REASON)
class TestMiniMaxTTSVoices(unittest.TestCase):
    """Test that all declared voices work with the API."""

    def setUp(self):
        from app.abus_tts_minimax import MiniMaxTTS
        self.tts = MiniMaxTTS(model="speech-2.8-turbo")
        self.output_files = []

    def tearDown(self):
        for f in self.output_files:
            if os.path.exists(f):
                os.remove(f)

    def test_english_graceful_lady(self):
        f = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        self.output_files.append(f.name)
        f.close()
        result = self.tts.generate_audio("Test voice.", "English_Graceful_Lady", f.name)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
