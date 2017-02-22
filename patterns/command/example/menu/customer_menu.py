from ..commands import AddCustomerCommand, QueryAllCustomer, \
    AddProductToCustomer, QueryAllCustomerProductsCommand
from .menu import Menu


class CustomerMenu(Menu):

    def _get_options(self):
        commands = (
            AddCustomerCommand('Insertar'),
            QueryAllCustomer('Consultar todos'),
            AddProductToCustomer('Agregar producto(s)'),
            QueryAllCustomerProductsCommand('Consultar producto(s)')
        )
        return commands
