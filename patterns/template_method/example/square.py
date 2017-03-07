from .figure import Figure


class Square(Figure):

    name = 'Cuadrado'

    def _get_area(self):
        side = float(input('Ingrese longitud del lado: '))
        return side ** 2
