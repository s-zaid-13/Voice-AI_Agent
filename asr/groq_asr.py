from pathlib import Path

from groq import Groq

from asr.base import BaseASR
from config.settings import settings
from utils.exceptions import ASRError
from utils.logger import logger


class GroqASR(BaseASR):
    def __init__(self) -> None:
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.GROQ_ASR_MODEL

    def transcribe(self, audio_path: Path) -> str:
        try:
            logger.info("Transcribing audio...")

            with audio_path.open("rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    file=(audio_path.name, audio_file.read()),
                    model=self.model,
                    response_format="text",
                )

            logger.info("Transcription completed.")

            return transcription.strip()

        except Exception as exc:
            raise ASRError("Failed to transcribe audio.") from exc
