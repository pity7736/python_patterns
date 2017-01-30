from .command import Command


class ExitCommand(Command):

    def __init__(self, title):
        super(ExitCommand, self).__init__(title=title)
        self.reset()

    def execute(self):
        self._closed = True

    def reset(self):
        self._closed = False

    def is_closed(self):
        return self._closed
