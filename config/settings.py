from pathlib import Path

from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
    VOICE_ID = os.getenv("VOICE_ID", "")

    GROQ_ASR_MODEL = "whisper-large-v3-turbo"
    GEMINI_MODEL = "gemini-3.5-flash-lite"
    TTS_MODEL = "eleven_multilingual_v2"


settings = Settings()
