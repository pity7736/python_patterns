from ..commands import ExitCommand
from .menu import Menu
from .product_menu_command import ProductMenuCommand


class MainMenu(Menu):

    def _get_options(self):
        self.exit_command = ExitCommand('Salir')
        commands = (
            ProductMenuCommand('Productos'),
            self.exit_command
        )
        return commands

    def run(self):
        while self.exit_command.is_closed() is False:
            super(MainMenu, self).run()
