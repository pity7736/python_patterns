import sys


class BaseClient:

    clients = {}

    def __init__(self, _type):
        client_pattern = self.clients.get(_type)
        if client_pattern is None:
            print('invalid type')
            sys.exit(1)
        self.client = client_pattern()

    def run(self):
        self.client.run()
