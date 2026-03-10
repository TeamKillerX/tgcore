from ._facebook import Facebook
from ._tiktok import TikTok
from ._pinterest import Pinterest

class Platform:
    def __init__(self, client):
        self.facebook = Facebook(client)
        self.tiktok = TikTok(client)
        self.pinterest = Pinterest(client)
