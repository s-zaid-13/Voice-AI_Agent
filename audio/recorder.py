from pathlib import Path

from audio.audio_utils import generate_recording_path
from utils.exceptions import RecorderError
from utils.logger import logger


class AudioRecorder:
    def save(self, audio_bytes: bytes, input_format: str = "webm") -> Path:

        try:

            output_path = generate_recording_path().with_suffix(f".{input_format}")

            output_path.write_bytes(audio_bytes)

            logger.info("Recording saved: %s", output_path)

            return output_path

        except Exception as exc:

            raise RecorderError("Failed to save recording.") from exc
