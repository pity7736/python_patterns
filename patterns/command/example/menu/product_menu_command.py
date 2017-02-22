from ..commands import Command
from .product_menu import ProductMenu


class ProductMenuCommand(Command):

    def execute(self):
        product_menu = ProductMenu()
        product_menu.run()
