from ..commands import Command
from .customer_menu import CustomerMenu


class CustomerMenuCommand(Command):

    def execute(self):
        customer_menu = CustomerMenu()
        customer_menu.run()
