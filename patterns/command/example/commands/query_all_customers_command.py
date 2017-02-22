from .command import Command
from ..models.customer import Customer


class QueryAllCustomer(Command):

    def execute(self):
        customers = Customer.get_customers()
        print()
        for i, customer in enumerate(customers):
            print('{}) {}'.format(i, customer.full_name()))
