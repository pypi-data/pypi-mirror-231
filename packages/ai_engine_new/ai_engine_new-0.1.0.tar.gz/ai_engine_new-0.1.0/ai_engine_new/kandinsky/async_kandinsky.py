from ai_engine.base_model import BaseKandinskyAI
from ai_engine.kandinsky.data import headers, data, urls, ratios
from ai_engine.models import (KandinskyStyleModel, 
                                KandinskyAskModel, 
                                KandinskyResponseModel)

from typing import Union, List, Dict
import asyncio

import pydantic
import httpx


class AsyncKandinsky(BaseKandinskyAI):
    def __init__(self, 
                 proxies: Union[str, Dict] = None,
                 width: str = "512", 
                 height: str = "512"):
        super().__init__(width=width, height=height)
        self.client = httpx.AsyncClient(proxies=proxies)
        
    async def ask(self,prompt='cat', 
                style='',
                width: str = None,
                height: str = None) -> KandinskyAskModel:
        if not (width := width or self.width) and not (height := height or self.height):
            raise AttributeError("You're a genius! How did you manage to lose the width and height!?!?")
        request_data = data.format(style=style, 
                                   prompt=prompt, 
                                   width=width, 
                                   height=height)
        resp = await self.client.post(urls["ask"], 
                                headers=headers, 
                                data=request_data)
        if resp_row := resp.json():
            if list(map(int,pydantic.VERSION.split(".")))[0] != 1:
                result = KandinskyAskModel.model_validate(resp_row)
            else:
                result = KandinskyAskModel.parse_obj(resp_row)
            return result
        raise httpx.HTTPError(f"Incorrect response {resp_row}")

    async def check(self, id: str) -> Union[KandinskyResponseModel, bool]:
        response = await self.client.get(
            urls["check"].format(id=id),
            headers=headers
        )
        if resp_row := response.json():
            try:
                if list(map(int,pydantic.VERSION.split(".")))[0] != 1:
                    result = KandinskyResponseModel.model_validate(resp_row)
                else:
                    result = KandinskyResponseModel.parse_obj(resp_row)
            except Exception:
                return resp_row
        return result

    async def generate(self, prompt: str, 
                 style='DEFAULT', 
                 ratio='1:1', 
                 timeout=60, 
                 check_for=1) -> KandinskyResponseModel:
        width = ratios[ratio][0] if ratio in ratios else self.width
        height = ratios[ratio][1] if ratio in ratios else self.height
        res = await self.ask(prompt,style, width, height)
        if res.status != "INITIAL": 
            return False
        response = await self.check(res.uuid)
        for _ in range(timeout, 0, -check_for):
            if isinstance(response, KandinskyResponseModel):
                break
            if response.get("status") in range(400, 600):
                raise AttributeError("Generating failed")
            await asyncio.sleep(check_for/2)
            response = await self.check(res.uuid)
        else:
            raise TimeoutError
        return response

    async def get_styles(self):
        res = await self.client.get(urls["styles"])
        if list(map(int, pydantic.VERSION.split(".")))[0] != 1:
            return pydantic.TypeAdapter(
                List[KandinskyStyleModel]).validate_python(res.json())
        else:
            return pydantic.parse_obj_as(List[KandinskyStyleModel], res.json())