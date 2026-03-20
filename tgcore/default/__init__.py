from ._default import Default, OnApp


class DefaultMethod:
    def __init__(self, client):
        self.default = Default(client)
