from typing import List, Union, Dict
from time import sleep
import re

import pydantic
import httpx

from ai_engine_new.models import DreamCheckTask, DreamCreateTask, DreamArtStyle
from ai_engine_new.base_model import BaseDreamAI
from ai_engine_new.wombo.urls import urls, auth_key_headers, headers_gen

class Dream(BaseDreamAI):
    def __init__(self, 
                 proxies: Union[str, Dict] = None,
                 max_requests_per_token: int = 30, 
                 out_msg = "") -> None:
        self.client = httpx.Client(proxies=proxies)
        self.max_requests_per_token = max_requests_per_token
        self.out_msg = out_msg

    def _get_js_filename(self) -> str:
        response = self.client.get(urls["js_filename"])
        js_filename = re.findall(r"_app-(\w+)", response.text)
        return js_filename[0]

    def _get_google_key(self) -> str:
        js_filename = self._get_js_filename()
        url = f"https://dream.ai/_next/static/chunks/pages/_app-{js_filename}.js"
        response = self.client.get(url)
        if key := re.findall(r'"(AI\w+)"', response.text):
          return key[0]
        raise KeyError("Error with get_google_key")
      
    def _get_auth_key(self) -> str:
        if self._counter_calls_auth < self.max_requests_per_token and self._auth_token:
            self._counter_calls_auth += 1
            return self._auth_token
        params = {"key": self._get_google_key()}
        json_data = {"returnSecureToken": True}

        response = self.client.post(
            urls["auth_key"],
            headers=auth_key_headers,
            params=params,
            json=json_data,
            timeout=20,
        )
        result = response.json()
        if _auth_token := result.get("idToken"):
            self._auth_token = _auth_token
            self._counter_calls_auth = 0
            return self._auth_token
        raise ValueError("Error on the server side, the token was not returned")

    def get_styles(self) -> List[DreamArtStyle]:
        res = self.client.get(urls["styles"])
        if list(map(int, pydantic.VERSION.split(".")))[0] != 1:
            return pydantic.TypeAdapter(
                List[DreamArtStyle]).validate_python(res.json())
        else:
            return pydantic.parse_obj_as(List[DreamArtStyle], res.json())

    def check_task(self, task_id: str, only_bool: bool = False) -> Union[DreamCheckTask, bool]:
        
        response = self.client.get(urls["draw_url"] + f"/{task_id}", 
                                   headers=headers_gen(auth_key=self._get_auth_key()), 
                                   timeout=10)
        if result_row := response.json():
            if list(map(int,pydantic.VERSION.split(".")))[0] != 1:
                result = DreamCheckTask.model_validate(result_row)
            else:
                result = DreamCheckTask.parse_obj(result_row)
        return bool(result.photo_url_list) if only_bool else result

    def create_task(self, text: str, style: int = 84) -> DreamCreateTask:
        if auth_key := self._get_auth_key():
            data = (
                    '{"is_premium":false,"input_spec":{"prompt":"%s","style":%d,"display_freq":10}}'
                    % (text[:200], style)
            )
            response = self.client.post(
                url=urls["draw_url"], 
                headers=headers_gen(auth_key), 
                data=data, 
                timeout=20
            )
            if result_row := response.json():
                if list(map(int,pydantic.VERSION.split(".")))[0] != 1:
                    result = DreamCheckTask.model_validate(result_row)
                else:
                    result = DreamCheckTask.parse_obj(result_row)
                return result
            raise httpx.HTTPError(f"Incorrect response data {result_row}")

    def generate(self, 
                text: str,
                style: int = 84,
                timeout: int = 60,
                check_for: int = 3) -> DreamCheckTask:
        task = self.create_task(text=text, style=style)
        for _ in range(timeout, 0, -check_for):
            check_task = self.check_task(task.id)
            if check_task.photo_url_list and check_task.state != "generating":
                return check_task
            sleep(check_for)
        else:
            raise TimeoutError(self.out_msg)
