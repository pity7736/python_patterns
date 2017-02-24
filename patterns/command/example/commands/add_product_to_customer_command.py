from .command import Command
from ..models import Customer, Product


class AddProductToCustomerCommand(Command):

    def execute(self):
        print()
        self._show_customers()
        print()
        self._show_products()
        customer_id = int(input('id cliente: '))
        customer = Customer.get_customer_from_index(customer_index=customer_id)
        products_ids = input('ids productos a insertar (separados por coma): ')
        for product_id in products_ids.split(','):
            product = Product.get_product_from_index(
                product_index=int(product_id))
            customer.add_product(product=product)

        print('productos agregados correctamente.')

    def _show_customers(self):
        print('Clientes disponibles:')
        customers = Customer.get_customers()
        if customers:
            for i, customer in enumerate(customers):
                print('{}) {}'.format(i, customer.full_name()))
        else:
            print('No hay clientes agregados.')

    def _show_products(self):
        print('Productos disponibles:')
        products = Product.get_products()
        if products:
            for i, product in enumerate(products):
                print('{}) {}'.format(i, product))
        else:
            print('No hay products agregados')
