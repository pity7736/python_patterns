
class Product:

    _products = []

    def __init__(self, code, name, amount):
        self.code = code
        self.name = name
        self.amount = amount
        self._products.append(self)

    def __str__(self):
        return 'Producto: {}. Código: {}. Cantidad: {}'.format(
            self.name,
            self.code,
            self.amount
        )

    @classmethod
    def get_products(cls):
        return cls._products