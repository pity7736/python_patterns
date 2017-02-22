from .command import Command


class ConcreteCommand1(Command):

    def execute(self):
        self.receiver.action1()
