from ..core import CoreBotAuth
from .stickers import Stickers
# from .messages import Messages

class Methods(Stickers):
    def __init__(self, client: CoreBotAuth):
        self._client = client
