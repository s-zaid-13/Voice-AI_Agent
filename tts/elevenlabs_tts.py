from pathlib import Path

from elevenlabs.client import ElevenLabs

from audio.audio_utils import generate_response_path
from config.settings import settings
from tts.base import BaseTTS
from utils.exceptions import TTSError
from utils.logger import logger


class ElevenLabsTTS(BaseTTS):
    def __init__(self) -> None:
        self.client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)

    def synthesize(self, text: str) -> Path:
        output_path = generate_response_path()

        try:
            logger.info("Generating speech...")

            audio = self.client.text_to_speech.convert(
                voice_id=settings.VOICE_ID,
                model_id=settings.TTS_MODEL,
                text=text,
            )

            with output_path.open("wb") as file:
                for chunk in audio:
                    file.write(chunk)

            logger.info("Speech generated.")

            return output_path

        except Exception as exc:
            raise TTSError("Failed to generate speech.") from exc
