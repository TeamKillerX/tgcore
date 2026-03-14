from ._blackforest import Blackforest
from ._capcut import Capcut
from ._facebook import Facebook
from ._pinterest import Pinterest
from ._threads import Threads
from ._tiktok import TikTok
from ._tools import AllTools
from ._twitter import Twitter
from ._all_in_one import Aio

class Platform:
    def __init__(self, client):
        self.facebook = Facebook(client)
        self.tiktok = TikTok(client)
        self.tools = AllTools(client)
        self.pinterest = Pinterest(client)
        self.blackforest = Blackforest(client)
        self.capcut = Capcut(client)
        self.threads = Threads(client)
        self.twitter = Twitter(client)
        self.aio = Aio(client)
