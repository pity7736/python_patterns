from .circle import Circle
from .square import Square
from .triangle import Triangle


class Areas:

    figures = [
        Circle,
        Square,
        Triangle
    ]

    def run(self):
        self._show_figures()
        figure = self._get_figure()
        print('Escogiste {}'.format(figure.name))

        figure.get_area()

    def _get_figure(self):
        while True:
            try:
                index = int(input('Ingrese número de figura: '))
            except ValueError:
                print('Ingrese un número')
            else:
                if 0 < index < len(self.figures):
                    figure = self.figures[index]
                    return figure()
                print('opción inválida')

    def _show_figures(self):
        print('Figuras disponibles')
        for i, figure in enumerate(self.figures):
            print('{}) {}'.format(i, figure.name))
