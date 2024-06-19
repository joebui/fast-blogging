from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class ArticleResponse(BaseModel):
    id: int
    title: str
    owner_id: int
    description: Optional[str]
    content: Optional[str]
    created_at: datetime
