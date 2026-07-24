class VoiceAgentError(Exception):
    pass


class RecorderError(VoiceAgentError):
    pass


class PlayerError(VoiceAgentError):
    pass


class ASRError(VoiceAgentError):
    pass


class LLMError(VoiceAgentError):
    pass


class TTSError(VoiceAgentError):
    pass
