
class Product:

    _products = []

    def __init__(self, code, name, amount):
        self.code = code
        self.name = name
        self.amount = amount
        self._products.append(self)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)

    @classmethod
    def get_products(cls):
        print()
        for product in cls._products:
            print('Producto: {}. Cantidad: {}'.format(product, product.amount))
