import datetime
from enum import StrEnum
from typing import Optional

from pydantic import BaseModel


class Rarity(StrEnum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    RARE_HOLO = "Rare Holo"
    ULTRA_RARE = "Ultra Rare"
    SECRET = "Secret"


class PhysicalState(StrEnum):
    MINT = "Mint"
    NEAR_MINT = "Near Mint"
    EXCELLENT = "Excellent"
    PLAYED = "Played"
    DAMAGED = "Damaged"


class Status(StrEnum):
    AVAILABLE = "Available"
    RESERVED = "Reserved"
    SOLD = "Sold"
    RETIRED = "Retired"


class Edition(BaseModel):
    code: str
    name: str
    years: int


class Card(BaseModel):
    name: str
    rarity: Rarity
    edition: Edition
    physical_state: PhysicalState
    type: str
    holo: bool = False
    illustration: Optional[str]
    created_at: datetime.datetime = datetime.datetime.now()
    status: Status = Status.AVAILABLE

    def make_available(self):
        if self.status == Status.SOLD:
            raise ValueError("Can't make a solded carte Available")
        self.status = Status.AVAILABLE

    def sell(self):
        if self.status == Status.SOLD:
            raise ValueError("Card already solded")
