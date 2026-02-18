from pydantic import BaseModel
from enum import StrEnum
from typing import Optional
import datetime

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

class Card(BaseModel):
    name: str
    rarity: Rarity
    edition: str
    physical_state: PhysicalState
    type: str
    holo: bool
    illustration: Optional[str]
    created_at: datetime.datetime
    status: Status