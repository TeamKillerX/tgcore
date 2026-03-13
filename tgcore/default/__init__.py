from ._default import Default

class DefaultMethod:
    def __init__(self, client):
        self.default = Default(client)
