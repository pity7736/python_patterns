from command.concept.invoker import Invoker
from .receiver import Receiver
from .concrete_command1 import ConcreteCommand1
from .concrete_command2 import ConcreteCommand2


class ClientCommand:
    
    def run(self):
        invoker = Invoker()
        receiver = Receiver()
        invoker.execute(ConcreteCommand1(receiver))
        invoker.execute(ConcreteCommand2(receiver))
