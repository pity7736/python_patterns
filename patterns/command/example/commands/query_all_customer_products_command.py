from .command import Command
from ..models import Customer


class QueryAllCustomerProductsCommand(Command):

    def execute(self):
        self._show_customers()
        customer_id = int(input('id cliente: '))
        customer = Customer._customers[customer_id]
        for product in customer.get_products():
            print(product)

    def _show_customers(self):
        print('Clientes disponibles:')
        customers = Customer.get_customers()
        if customers:
            for i, customer in enumerate(customers):
                print('{}) {}'.format(i, customer.full_name()))
        else:
            print('No hay clientes agregados.')
