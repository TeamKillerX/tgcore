from ._groq import GroqAI
from ._cohere import CohereAI

class Chats(
    GroqAI,
    CohereAI
):
    pass
