from ..commands import AddCustomerCommand, QueryAllCustomerCommand, \
    AddProductToCustomerCommand, QueryAllCustomerProductsCommand
from .menu import Menu


class CustomerMenu(Menu):

    name = 'Menú clientes'

    def _get_options(self):
        commands = (
            AddCustomerCommand('Insertar'),
            QueryAllCustomerCommand('Consultar todos'),
            AddProductToCustomerCommand('Agregar producto(s)'),
            QueryAllCustomerProductsCommand('Consultar producto(s)')
        )
        return commands
