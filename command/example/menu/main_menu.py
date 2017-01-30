from .menu import Menu
from .product_menu_command import ProductMenuCommand
from .exit_command import ExitCommand


class MainMenu(Menu):

    def _set_options(self):
        self.exit_command = ExitCommand('Salir')
        commands = (
            ProductMenuCommand('Productos'),
            self.exit_command
        )
        self.commands.extend(commands)

    def run(self):
        #         self.exit_command.reset()
        while self.exit_command.is_closed() is False:
            super(MainMenu, self).run()
