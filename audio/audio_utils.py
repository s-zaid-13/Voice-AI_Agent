from datetime import datetime
from pathlib import Path

from utils.file_handler import ensure_directory

RECORDINGS_DIR = Path("data/recordings")
RESPONSES_DIR = Path("data/responses")

SAMPLE_RATE = 16000
CHANNELS = 1


def generate_recording_path() -> Path:
    ensure_directory(RECORDINGS_DIR)
    filename = f"recording_{datetime.now():%Y%m%d_%H%M%S}.wav"
    return RECORDINGS_DIR / filename


def generate_response_path() -> Path:
    ensure_directory(RESPONSES_DIR)
    filename = f"response_{datetime.now():%Y%m%d_%H%M%S}.mp3"
    return RESPONSES_DIR / filename
