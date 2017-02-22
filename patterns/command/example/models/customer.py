
class Customer:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)
