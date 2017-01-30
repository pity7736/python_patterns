from ..commands import AddProductCommand, QueryProductCommand
from .menu import Menu


class ProductMenu(Menu):

    def _set_options(self):
        commands = (
            AddProductCommand('Insertar'),
            QueryProductCommand('Consultar')
        )
        self.commands.extend(commands)
