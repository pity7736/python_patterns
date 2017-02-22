from ..base_client import BaseClient
from .concept import Client
from .example import MainMenu


class ClientCommand(BaseClient):

    clients = {
        'concept': Client,
        'example': MainMenu
    }
