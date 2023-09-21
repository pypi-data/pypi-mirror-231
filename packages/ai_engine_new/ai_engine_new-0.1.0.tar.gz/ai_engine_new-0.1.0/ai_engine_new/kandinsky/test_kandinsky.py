import asyncio

from typing import List

from ai_engine import Kandinsky, AsyncKandinsky
from ai_engine.models import (KandinskyAskModel, 
                                KandinskyStyleModel, 
                                KandinskyResponseModel)

def test_sync_kandinsky():
    model = Kandinsky()
    assert isinstance(
        model.generate("anime waifu in bikini"), 
        KandinskyResponseModel
    )

def test_async_kandinsky():
    async_model = AsyncKandinsky()
    assert isinstance(asyncio.run(
        async_model.generate("anime waifu in bikini")),
                      KandinskyResponseModel)

def test_many_async_kandinsky():
    async def test():
        async_model = AsyncKandinsky()
        tasks = [asyncio.create_task(async_model.generate("anime waifu in bikini")) for _ in range(10)]
        return await asyncio.gather(*tasks)
    assert isinstance(asyncio.run(test()),
                      list)

def test_async_styles():
    async_model = AsyncKandinsky()
    assert isinstance(asyncio.run(async_model.get_styles()), list)

def test_sync_styles():
    model = Kandinsky()
    assert isinstance(model.get_styles(), list)