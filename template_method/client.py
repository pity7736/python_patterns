from .concrete_class1 import ConcreteClass1
from .concrete_class2 import ConcreteClass2


class Client:

    def run(self):
        concrete_class1 = ConcreteClass1()
        concrete_class1.template_method()

        concrete_class2 = ConcreteClass2()
        concrete_class2.template_method()
