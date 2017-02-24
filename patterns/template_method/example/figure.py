from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):

    name = ''

    def get_area(self):
        area = self._get_area()
        print('El area del {} es {}'.format(self.name, area))

    @abstractmethod
    def _get_area(self):
        pass
