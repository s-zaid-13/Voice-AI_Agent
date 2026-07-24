from google import genai

from config.settings import settings
from llm.base import BaseLLM
from utils.exceptions import LLMError
from utils.logger import logger


class GeminiLLM(BaseLLM):
    def __init__(self) -> None:
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.GEMINI_MODEL

    def generate(self, messages: list[dict[str, str]]) -> str:
        try:
            logger.info("Generating response...")

            prompt = ""

            for message in messages:
                role = message["role"].capitalize()
                prompt += f"{role}: {message['content']}\n"

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            logger.info("Response generated.")

            return response.text.strip()

        except Exception as exc:
            raise LLMError("Failed to generate response.") from exc
