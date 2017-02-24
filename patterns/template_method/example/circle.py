from math import pi

from .figure import Figure


class Circle(Figure):

    name = 'Círculo'

    def _get_area(self):
        radius = float(input('Ingrese el radio: '))
        return pi * radius ** 2
