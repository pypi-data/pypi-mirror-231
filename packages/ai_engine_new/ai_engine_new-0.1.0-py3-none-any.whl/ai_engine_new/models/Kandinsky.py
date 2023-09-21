from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class KandinskyAskModel(BaseModel):
    status: str
    uuid: str
    

class KandinskyResponseModel(BaseModel):
    uuid: str
    status: str
    errorDescription: Any
    images: List[str]
    censored: bool


class KandinskyStyleModel(BaseModel):
    name: str
    title: str
    title_en: str
    query: str
