from ._default import Default, App

class DefaultMethod:
    def __init__(self, client):
        self.default = Default(client)

class App(OnApp):
    pass
