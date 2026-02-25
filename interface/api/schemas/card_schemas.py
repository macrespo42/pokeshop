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
    is_holo: bool =  False

class CardGetRequest(BaseModel):
    id: str

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