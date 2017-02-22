from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):

    def template_method(self):
        print('abstract class')
        self.operation1()
        print('after operation 1')
        self.operation2()
        print('after operation 2')

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass
