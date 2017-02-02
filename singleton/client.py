from .singleton import Singleton


class Client:

    def run(self):
        singleton1 = Singleton()
        singleton2 = Singleton()

        print('id objeto 1: {}'.format(id(singleton1)))
        print('id objeto 2: {}'.format(id(singleton2)))
        assert singleton1 is singleton2
