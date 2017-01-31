import sys

from .concept import Client
from .example import MainMenu


class ClientCommand:

    clients = {
        'concept': Client,
        'example': MainMenu
    }

    def __init__(self, _type):
        client_pattern = self.clients.get(_type)
        if client_pattern is None:
            print('invalid type')
            sys.exit()
        self.clients = client_pattern()

    def run(self):
        self.clients.run()
