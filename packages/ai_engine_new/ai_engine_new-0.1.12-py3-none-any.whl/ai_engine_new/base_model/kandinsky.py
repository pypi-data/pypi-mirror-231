from abc import ABC, abstractmethod
from typing import Union, Dict

import base64

from httpx._client import Client, AsyncClient

class BaseKandinskyAI(ABC):
    client: Union[Client, AsyncClient]

    def __init__(self, width="512", height="512"):
        self.width = width
        self.height = height

    def load(self, image_data: str) -> bytes:
        img_bytes = base64.b64decode(image_data)
        return img_bytes

    @abstractmethod
    def ask(self):
        pass
