import abc


class Command(metaclass=abc.ABCMeta):

    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title

    @abc.abstractmethod
    def execute(self):
        pass
