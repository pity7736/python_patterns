from .command import Command
from ..models.product import Product


class AddProductCommand(Command):

    def execute(self):
        code = input('Código: ')
        name = input('Nombre: ')
        amount = int(input('Cantidad: '))
        Product(code=code, name=name, amount=amount)
