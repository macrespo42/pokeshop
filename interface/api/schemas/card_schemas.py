from domain.entities.card import Edition
from pydantic import BaseModel
import datetime
from typing import Optional


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
