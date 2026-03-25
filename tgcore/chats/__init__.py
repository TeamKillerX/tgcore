# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=undefined-variable
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

from ._cohere import CohereAI
from ._gemini import GeminiAI
from ._groq import GroqAI


class Chats(
    GroqAI,
    CohereAI,
    GeminiAI
):
    pass
