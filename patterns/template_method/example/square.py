from .figure import Figure


class Square(Figure):

    name = 'Cuadrado'

    def _get_area(self):
        lado = float(input('Ingrese longitud del lado: '))
        return lado ** 2
