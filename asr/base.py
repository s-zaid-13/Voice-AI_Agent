from abc import ABC, abstractmethod
from pathlib import Path


class BaseASR(ABC):
    @abstractmethod
    def transcribe(self, audio_path: Path) -> str:
        pass
