from abc import ABC, abstractmethod
from typing import Union

from httpx._client import Client, AsyncClient

class BaseDreamAI(ABC):
    client: Union[Client, AsyncClient]
    _counter_calls_auth: int = 0
    _auth_token: str = ""

    @abstractmethod
    def _get_js_filename(self) -> str:
      pass

    @abstractmethod
    def _get_google_key(self) -> str:
        pass

    @abstractmethod
    def _get_auth_key(self) -> str:
        pass

    @abstractmethod
    def create_task(self, text: str, style: int):
        pass

    @abstractmethod
    def check_task(self, task_id: str, only_bool: bool):
        pass

    @abstractmethod
    def generate(
            self,
            text: str,
            style: int,
            timeout: int,
            check_for: int):
        pass