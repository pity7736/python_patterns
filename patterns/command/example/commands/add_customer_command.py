from .command import Command
from ..models.customer import Customer


class AddCustomerCommand(Command):

    def execute(self):
        first_name = input('primer nombre: ')
        last_name = input('segundo nombre: ')
        Customer(first_name=first_name, last_name=last_name)
