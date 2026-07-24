from pathlib import Path

from agent.conversation import Conversation
from audio import AudioRecorder
from asr import GroqASR
from llm import GeminiLLM
from models import VoiceResponse
from tts import ElevenLabsTTS


class VoiceAgent:
    def __init__(self) -> None:
        self.recorder = AudioRecorder()

        self.asr = GroqASR()
        self.llm = GeminiLLM()
        self.tts = ElevenLabsTTS()

        self.conversation = Conversation()

    def transcribe(self, audio_path: Path) -> str:
        return self.asr.transcribe(audio_path)

    def generate_response(self, user_message: str) -> str:
        self.conversation.add_user_message(user_message)

        assistant_response = self.llm.generate(self.conversation.get_messages())

        self.conversation.add_assistant_message(assistant_response)

        return assistant_response

    def generate_audio(self, text: str) -> Path:
        return self.tts.synthesize(text)

    def speak(self, audio_path: Path) -> None:
        self.player.play(audio_path)

    def process(self, audio_path: Path) -> VoiceResponse:

        transcript = self.transcribe(audio_path)

        response = self.generate_response(transcript)

        response_audio = self.generate_audio(response)

        return VoiceResponse(
            transcript=transcript, response=response, response_audio=response_audio
        )
