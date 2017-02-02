import sys

from .client import Client


class ClientSingleton:

    def __init__(self, _type):
        if _type != 'concept':
            print('invalid type')
            sys.exit()

        self.client = Client()

    def run(self):
        self.client.run()
