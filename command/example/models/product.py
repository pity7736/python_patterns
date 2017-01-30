
class Product:

    _products = {}

    def __init__(self, code, name, amount):
        self.code = code
        self.name = name
        self.amount = amount
        self._products[self] = amount
