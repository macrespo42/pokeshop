from pydantic import BaseModel
from typing import Optional
import datetime


class Edition(BaseModel):
    code: str
    name: str
    year: int


class CardCreateRequest(BaseModel):
    name: str
    rarity: str
    edition: Edition
    physical_state: str
    type: str
    status: str
    illustration: Optional[str]
    is_holo: bool = False


class CardGetRequest(BaseModel):
    id: str


class SearchCardRequest(BaseModel):
    name: Optional[str]
    rarity: Optional[str]
    edition: Optional[Edition]
    physical_state: Optional[str]
    type: Optional[str]
    status: Optional[str]
    illustration: Optional[str]


class CardResponse(BaseModel):
    id: str
    name: str
    rarity: str
    edition: Edition
    physical_state: str
    type: str
    status: str
    illustration: Optional[str]
    is_holo: bool
    created_at: datetime.datetime
