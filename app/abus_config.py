"""
Configuration module for loading environment variables.
Supports .env file loading via python-dotenv.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


def get_env(key: str, default: str = None) -> str:
    """
    Get environment variable value.
    
    Args:
        key: Environment variable name
        default: Default value if not found (None will return None)
    
    Returns:
        Environment variable value or default
    """
    return os.getenv(key, default)


def get_azure_speech_key() -> str:
    """Get Azure Speech TTS API key from environment."""
    key = get_env('AZURE_SPEECH_KEY')
    if not key:
        raise ValueError(
            "AZURE_SPEECH_KEY environment variable is required. "
            "Please set it in your .env file or environment."
        )
    return key


def get_azure_speech_region() -> str:
    """Get Azure Speech TTS region from environment."""
    region = get_env('AZURE_SPEECH_REGION')
    if not region:
        raise ValueError(
            "AZURE_SPEECH_REGION environment variable is required. "
            "Please set it in your .env file or environment."
        )
    return region


def get_azure_translator_key() -> str:
    """Get Azure Translator API key from environment."""
    key = get_env('AZURE_TRANSLATOR_KEY')
    if not key:
        raise ValueError(
            "AZURE_TRANSLATOR_KEY environment variable is required. "
            "Please set it in your .env file or environment."
        )
    return key


def get_azure_translator_endpoint() -> str:
    """Get Azure Translator endpoint from environment."""
    endpoint = get_env('AZURE_TRANSLATOR_ENDPOINT')
    if not endpoint:
        raise ValueError(
            "AZURE_TRANSLATOR_ENDPOINT environment variable is required. "
            "Please set it in your .env file or environment."
        )
    return endpoint


def get_azure_translator_region() -> str:
    """Get Azure Translator region from environment."""
    region = get_env('AZURE_TRANSLATOR_REGION')
    if not region:
        raise ValueError(
            "AZURE_TRANSLATOR_REGION environment variable is required. "
            "Please set it in your .env file or environment."
        )
    return region


def azure_translator_available() -> bool:
    """Check if Azure Translator is available via environment variables."""
    return (
        get_env('AZURE_TRANSLATOR_KEY') is not None and
        get_env('AZURE_TRANSLATOR_ENDPOINT') is not None
    )


def get_minimax_api_key() -> str:
    """Get MiniMax TTS API key from environment."""
    key = get_env('MINIMAX_API_KEY')
    if not key:
        raise ValueError(
            "MINIMAX_API_KEY environment variable is required. "
            "Please set it in your .env file or environment."
        )
    return key


def minimax_tts_available() -> bool:
    """Check if MiniMax TTS is available via environment variables."""
    return get_env('MINIMAX_API_KEY') is not None


