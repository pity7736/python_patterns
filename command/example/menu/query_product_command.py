from .command import Command
from ..models.product import Product


class QueryProductCommand(Command):

    def execute(self):
        Product.get_products()
