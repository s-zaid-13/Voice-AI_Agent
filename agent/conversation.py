from agent.prompts import SYSTEM_PROMPT


class Conversation:
    def __init__(self) -> None:
        self._messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

    def add_user_message(self, message: str) -> None:
        self._messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(self, message: str) -> None:
        self._messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def get_messages(self) -> list[dict[str, str]]:
        return self._messages.copy()

    def clear(self) -> None:
        self._messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]
