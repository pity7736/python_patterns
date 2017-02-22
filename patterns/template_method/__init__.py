from ..base_client import BaseClient
from .client import Client


class ClientTemplateMethod(BaseClient):

    clients = {
        'concept': Client
    }
