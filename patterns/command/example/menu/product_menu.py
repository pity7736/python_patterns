from ..commands import AddProductCommand, QueryProductCommand
from .menu import Menu


class ProductMenu(Menu):

    def _get_options(self):
        commands = (
            AddProductCommand('Insertar'),
            QueryProductCommand('Consultar')
        )
        return commands
