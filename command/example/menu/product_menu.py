from .add_product_command import AddProductCommand
from .menu import Menu
from .query_product_command import QueryProductCommand


class ProductMenu(Menu):

    def _set_options(self):
        commands = (
            AddProductCommand('Insertar'),
            QueryProductCommand('Consultar')
        )
        self.commands.extend(commands)
