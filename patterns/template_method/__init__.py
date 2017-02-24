from ..base_client import BaseClient
from .concept import Client


class ClientTemplateMethod(BaseClient):

    clients = {
        'concept': Client
    }
