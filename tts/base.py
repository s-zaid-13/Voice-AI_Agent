from abc import ABC, abstractmethod
from pathlib import Path


class BaseTTS(ABC):

    @abstractmethod
    def synthesize(self, text: str) -> Path:
        pass
