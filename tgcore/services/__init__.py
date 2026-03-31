from ._carbon import Carbon
from ._screenshot import Screenshot


class Services:
    def __init__(self, client):
        self.carbon = Carbon(client)
        self.screenshot = Screenshot(client)
