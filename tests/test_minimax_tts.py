"""Unit tests for MiniMax TTS provider."""

import os
import sys
import json
import unittest
from unittest.mock import patch, MagicMock

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Mock heavy dependencies that may not be installed in test env
for mod_name in ['pysubs2', 'pydub', 'pydub.AudioSegment', 'pydub.silence',
                 'gradio', 'structlog', 'dotenv',
                 'app.abus_genuine', 'app.abus_path',
                 'app.abus_ffmpeg', 'app.abus_text', 'app.abus_nlp_spacy',
                 'app.abus_audio', 'app.abus_files', 'app.abus_voice_ms',
                 'src.config', 'src.ui', 'src.i18n', 'src.i18n.i18n']:
    if mod_name not in sys.modules:
        sys.modules[mod_name] = MagicMock()

# Mock specific objects needed by imports
sys.modules['gradio'].Progress = MagicMock(return_value=MagicMock())
sys.modules['src.config'].UserConfig = MagicMock


class TestMiniMaxConfig(unittest.TestCase):
    """Test MiniMax configuration helpers."""

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def test_get_minimax_api_key(self):
        from app.abus_config import get_minimax_api_key
        self.assertEqual(get_minimax_api_key(), "test-key-123")

    @patch.dict(os.environ, {}, clear=True)
    def test_get_minimax_api_key_missing(self):
        # Reload module to clear cached env
        import importlib
        from app import abus_config
        importlib.reload(abus_config)
        with self.assertRaises(ValueError):
            abus_config.get_minimax_api_key()

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def test_minimax_tts_available_true(self):
        from app.abus_config import minimax_tts_available
        self.assertTrue(minimax_tts_available())

    @patch.dict(os.environ, {}, clear=True)
    def test_minimax_tts_available_false(self):
        import importlib
        from app import abus_config
        importlib.reload(abus_config)
        self.assertFalse(abus_config.minimax_tts_available())


class TestMiniMaxVoicesAndModels(unittest.TestCase):
    """Test voice and model constants."""

    def test_voices_not_empty(self):
        from app.abus_tts_minimax import MINIMAX_VOICES
        self.assertGreater(len(MINIMAX_VOICES), 0)

    def test_voices_contain_english(self):
        from app.abus_tts_minimax import MINIMAX_VOICES
        english_voices = [k for k in MINIMAX_VOICES if k.startswith("English")]
        self.assertGreaterEqual(len(english_voices), 4)

    def test_models_contain_hd(self):
        from app.abus_tts_minimax import MINIMAX_MODELS
        self.assertIn("speech-2.8-hd", MINIMAX_MODELS)

    def test_models_contain_turbo(self):
        from app.abus_tts_minimax import MINIMAX_MODELS
        self.assertIn("speech-2.8-turbo", MINIMAX_MODELS)

    def test_voice_ids_are_strings(self):
        from app.abus_tts_minimax import MINIMAX_VOICES
        for name, vid in MINIMAX_VOICES.items():
            self.assertIsInstance(vid, str)
            self.assertTrue(len(vid) > 0, f"Voice ID for {name} is empty")

    def test_all_12_voices(self):
        from app.abus_tts_minimax import MINIMAX_VOICES
        self.assertEqual(len(MINIMAX_VOICES), 12)


class TestMiniMaxTTSInit(unittest.TestCase):
    """Test MiniMaxTTS class initialization."""

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def test_default_model(self):
        from app.abus_tts_minimax import MiniMaxTTS
        tts = MiniMaxTTS()
        self.assertEqual(tts.model, "speech-2.8-hd")

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def test_custom_model(self):
        from app.abus_tts_minimax import MiniMaxTTS
        tts = MiniMaxTTS(model="speech-2.8-turbo")
        self.assertEqual(tts.model, "speech-2.8-turbo")

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def test_api_url(self):
        from app.abus_tts_minimax import MiniMaxTTS
        tts = MiniMaxTTS()
        self.assertEqual(tts.api_url, "https://api.minimax.io/v1/t2a_v2")

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def test_api_key_stored(self):
        from app.abus_tts_minimax import MiniMaxTTS
        tts = MiniMaxTTS()
        self.assertEqual(tts.api_key, "test-key-123")


class TestMiniMaxTTSGenerateAudio(unittest.TestCase):
    """Test generate_audio method."""

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def setUp(self):
        from app.abus_tts_minimax import MiniMaxTTS
        self.tts = MiniMaxTTS()

    @patch('app.abus_tts_minimax.requests.post')
    def test_generate_audio_success(self, mock_post):
        # Create a small valid MP3 (ID3 header)
        audio_hex = "fffbe400".ljust(200, '0')
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0, "status_msg": "success"},
            "data": {"audio": audio_hex},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_file = f.name

        try:
            result = self.tts.generate_audio("Hello world", "English_Graceful_Lady", output_file)
            self.assertTrue(result)
            self.assertTrue(os.path.exists(output_file))
            self.assertGreater(os.path.getsize(output_file), 0)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

    @patch('app.abus_tts_minimax.requests.post')
    def test_generate_audio_api_error(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base_resp": {"status_code": 1001, "status_msg": "invalid api key"},
            "data": {},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_file = f.name

        try:
            result = self.tts.generate_audio("Hello world", "English_Graceful_Lady", output_file)
            self.assertFalse(result)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

    @patch('app.abus_tts_minimax.requests.post')
    def test_generate_audio_empty_audio(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0, "status_msg": "success"},
            "data": {"audio": ""},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_file = f.name

        try:
            result = self.tts.generate_audio("Hello world", "English_Graceful_Lady", output_file)
            self.assertFalse(result)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

    @patch('app.abus_tts_minimax.requests.post')
    def test_generate_audio_request_exception(self, mock_post):
        import requests as req
        mock_post.side_effect = req.exceptions.ConnectionError("Connection failed")

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_file = f.name

        try:
            result = self.tts.generate_audio("Hello world", "English_Graceful_Lady", output_file)
            self.assertFalse(result)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

    @patch('app.abus_tts_minimax.requests.post')
    def test_speed_clamping(self, mock_post):
        """Speed rate is clamped to [0.5, 2.0] range."""
        audio_hex = "fffbe400".ljust(200, '0')
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0, "status_msg": "success"},
            "data": {"audio": audio_hex},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_file = f.name

        try:
            # rate=200 -> speed = 1.0 + 2.0 = 3.0 -> clamped to 2.0
            self.tts.generate_audio("Hello", "English_Graceful_Lady", output_file, rate=200)
            call_args = mock_post.call_args
            payload = call_args[1]['json'] if 'json' in call_args[1] else json.loads(call_args[1].get('data', '{}'))
            speed = payload['voice_setting']['speed']
            self.assertLessEqual(speed, 2.0)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)


class TestMiniMaxTTSValidateFile(unittest.TestCase):
    """Test file validation."""

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def setUp(self):
        from app.abus_tts_minimax import MiniMaxTTS
        self.tts = MiniMaxTTS()

    def test_validate_existing_file(self):
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            f.write(b"test audio data")
            output_file = f.name

        try:
            success, msg = self.tts._validate_file(output_file)
            self.assertTrue(success)
        finally:
            os.remove(output_file)

    def test_validate_nonexistent_file(self):
        success, msg = self.tts._validate_file("/nonexistent/path/audio.mp3")
        self.assertFalse(success)
        self.assertIn("not exist", msg)

    def test_validate_empty_file(self):
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_file = f.name

        try:
            success, msg = self.tts._validate_file(output_file)
            self.assertFalse(success)
            self.assertIn("size", msg)
        finally:
            os.remove(output_file)


class TestMiniMaxTTSRequestPayload(unittest.TestCase):
    """Test that the API request payload is correctly constructed."""

    @patch.dict(os.environ, {"MINIMAX_API_KEY": "test-key-123"})
    def setUp(self):
        from app.abus_tts_minimax import MiniMaxTTS
        self.tts = MiniMaxTTS()

    @patch('app.abus_tts_minimax.requests.post')
    def test_payload_structure(self, mock_post):
        audio_hex = "fffbe400".ljust(200, '0')
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0, "status_msg": "success"},
            "data": {"audio": audio_hex},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_file = f.name

        try:
            self.tts.generate_audio("Test text", "cute_boy", output_file)

            call_args = mock_post.call_args
            payload = call_args[1]['json']

            self.assertEqual(payload['model'], 'speech-2.8-hd')
            self.assertEqual(payload['text'], 'Test text')
            self.assertEqual(payload['voice_setting']['voice_id'], 'cute_boy')
            self.assertIn('speed', payload['voice_setting'])
            self.assertIn('vol', payload['voice_setting'])
            self.assertIn('pitch', payload['voice_setting'])
            self.assertEqual(payload['audio_setting']['format'], 'mp3')
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)

    @patch('app.abus_tts_minimax.requests.post')
    def test_authorization_header(self, mock_post):
        audio_hex = "fffbe400".ljust(200, '0')
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "base_resp": {"status_code": 0, "status_msg": "success"},
            "data": {"audio": audio_hex},
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            output_file = f.name

        try:
            self.tts.generate_audio("Test text", "cute_boy", output_file)

            call_args = mock_post.call_args
            headers = call_args[1]['headers']
            self.assertEqual(headers['Authorization'], 'Bearer test-key-123')
            self.assertEqual(headers['Content-Type'], 'application/json')
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
