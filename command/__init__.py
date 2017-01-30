import sys

from .concept import ClientCommand
from .example import MainMenu


class RunCommand:

    runners = {
        'concept': ClientCommand,
        'example': MainMenu
    }

    def __init__(self, _type):
        runner = self.runners.get(_type)
        if runner is None:
            print('invalid type')
            sys.exit()
        self.runner = runner()

    def run(self):
        self.runner.run()
