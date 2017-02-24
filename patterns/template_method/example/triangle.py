from .figure import Figure


class Triangle(Figure):

    name = 'Triángulo'

    def _get_area(self):
        base = float(input('Ingrese longitud de la base: '))
        height = float(input('Ingrese altura: '))
        return base * height / 2
