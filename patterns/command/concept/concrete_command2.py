from .command import Command


class ConcreteCommand2(Command):

    def execute(self):
        self.receiver.action2()
