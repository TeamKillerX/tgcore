from ._groq import GroqAI
from ._cohere import CohereAI
from ._gemini import GeminiAI

class Chats(
    GroqAI,
    CohereAI,
    GeminiAI
):
    pass
