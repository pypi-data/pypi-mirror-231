import asyncio

from typing import List

from ai_engine import Dream, AsyncDream
from ai_engine.models import DreamCheckTask, DreamArtStyle

def test_sync_dream():
    model = Dream()
    assert isinstance(model.generate("anime waifu in bikini"), DreamCheckTask)

def test_async_dream():
    async_model = AsyncDream()
    assert isinstance(asyncio.run(
        async_model.generate("anime waifu in bikini")),
                      DreamCheckTask)

def test_many_async_dream():
    async def test():
        async_model = AsyncDream()
        tasks = [asyncio.create_task(async_model.generate("anime waifu in bikini")) for _ in range(10)]
        return await asyncio.gather(*tasks)
    assert isinstance(asyncio.run(test()),
                      list)

def test_async_styles():
    async_model = AsyncDream()
    assert isinstance(asyncio.run(async_model.get_styles()), list)

def test_sync_styles():
    model = Dream()
    assert isinstance(model.get_styles(), list)