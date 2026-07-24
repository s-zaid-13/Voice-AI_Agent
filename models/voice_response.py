from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class VoiceResponse:
    transcript: str
    response: str
    response_audio: Path
