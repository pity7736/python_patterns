from .add_product_command import AddProductCommand
from .menu import Menu


class ProductMenu(Menu):

    def _set_options(self):
        commands = (
            AddProductCommand('Insertar'),
        )
        self.commands.extend(commands)
