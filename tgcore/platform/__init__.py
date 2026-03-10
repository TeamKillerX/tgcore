from ._facebook import Facebook
from ._pinterest import Pinterest
from ._tiktok import TikTok


class Platform:
    def __init__(self, client):
        self.facebook = Facebook(client)
        self.tiktok = TikTok(client)
        self.pinterest = Pinterest(client)
