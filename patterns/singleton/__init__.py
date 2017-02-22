from ..base_client import BaseClient
from .client import Client


class ClientSingleton(BaseClient):

    clients = {
        'concept': Client
    }
