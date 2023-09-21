from __future__ import annotations

from typing import List, Any, Optional

from pydantic import BaseModel, Field
    


class InputSpec(BaseModel):
    gen_type: str
    style: int
    prompt: str
    aspect_ratio_width: int
    aspect_ratio_height: int
    aspect_ratio: str


class DreamCreateTask(BaseModel):
    id: str
    user_id: str
    state: str
    input_spec: InputSpec
    premium: bool
    created_at: str
    updated_at: str
    is_nsfw: bool
    photo_url_list: List
    generated_photo_keys: List
    result: Any


class Result(BaseModel):
    final: str


class DreamCheckTask(BaseModel):
    id: str
    user_id: str
    state: str
    input_spec: InputSpec
    premium: bool
    created_at: str
    updated_at: str
    is_nsfw: bool
    photo_url_list: List[str]
    generated_photo_keys: List[str]
    result: Optional[Result] = None


class DreamArtStyle(BaseModel):
    id: int
    name: str
    is_visible: bool
    created_at: str
    updated_at: str
    deleted_at: Any
    photo_url: str
    is_premium: bool
    type: str = Field(alias="model_type")
    is_new: bool
