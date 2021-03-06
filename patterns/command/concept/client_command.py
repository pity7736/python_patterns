from .concrete_command1 import ConcreteCommand1
from .concrete_command2 import ConcreteCommand2
from .invoker import Invoker
from .receiver import Receiver


class Client:

    def run(self):
        invoker = Invoker()
        receiver = Receiver()
        invoker.execute(ConcreteCommand1(receiver))
        invoker.execute(ConcreteCommand2(receiver))
