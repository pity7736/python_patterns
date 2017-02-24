from ..base_client import BaseClient
from .concept import Client
from .example import Areas


class ClientTemplateMethod(BaseClient):

    clients = {
        'concept': Client,
        'example': Areas
    }
