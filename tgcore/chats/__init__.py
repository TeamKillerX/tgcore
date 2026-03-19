from ._cohere import CohereAI
from ._gemini import GeminiAI
from ._groq import GroqAI


class Chats(
    GroqAI,
    CohereAI,
    GeminiAI
):
    pass
