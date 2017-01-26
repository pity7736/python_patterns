import abc


class Command(metaclass=abc.ABCMeta):
    
    def __init__(self, receiver):
        self.receiver = receiver
    
    @abc.abstractmethod
    def execute(self):
        pass