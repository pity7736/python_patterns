from .command import Command
from ..models.product import Product


class QueryProductCommand(Command):

    def execute(self):
        products = Product.get_products()
        print()
        for product in products:
            print(product)
