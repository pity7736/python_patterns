
class Customer:

    _customers = []

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._products = []
        self._customers.append(self)

    @classmethod
    def get_customers(cls):
        return cls._customers

    @classmethod
    def get_customer_from_index(cls, customer_index):
        return cls._customers[customer_index]

    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    def add_product(self, product):
        self._products.append(product)

    def get_products(self):
        return self._products
