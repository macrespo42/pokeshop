import dataclasses
import datetime
import uuid
from dataclasses import dataclass, field
from typing import ClassVar, Optional


@dataclass(frozen=True)
class Rarity:
    _valid: ClassVar[set] = {
        "common",
        "uncommon",
        "rare",
        "rare_holo",
        "ultra_rare",
        "secret",
    }

    value: str

    def __post_init__(self):
        if self.value not in self._valid:
            raise ValueError("Invalid Rarity")


@dataclass(frozen=True)
class PhysicalState:
    _valid: ClassVar[set] = {"mint", "near mint", "excellent", "played", "damaged"}

    value: str

    def __post_init__(self):
        if self.value not in self._valid:
            raise ValueError("Invalid Physical State")


@dataclass(frozen=True)
class Status:
    _valid: ClassVar[set] = {"available", "reserved", "sold", "retired"}
    value: str

    def __post_init__(self):
        if self.value not in self._valid:
            raise ValueError("Invalid Status")


@dataclass(frozen=True)
class Edition:
    code: str
    name: str
    years: int

    def __post_init__(self):
        if self.years < 2000:
            raise ValueError("Invalid Edition Years")
        if len(self.name) == 0 or len(self.name) > 32 or not self.name.isalpha():
            raise ValueError("Invalid Edition Name")
        if len(self.code) == 0 or len(self.code) > 32:
            raise ValueError("Invalid Edition Code")


@dataclass(frozen=True)
class PokemonType:
    _valid: ClassVar[set] = {
        "normal",
        "fire",
        "water",
        "electric",
        "grass",
        "ice",
        "fighting",
        "poison",
        "ground",
        "flying",
        "psychic",
        "bug",
        "rock",
        "ghost",
        "dragon",
        "dark",
        "steel",
        "fairy",
    }
    value: str

    def __post_init__(self):
        if self.value not in self._valid:
            raise ValueError("Invalid Pokemon Type")


@dataclass(frozen=True)
class Name:
    value: str

    def __post_init__(self):
        if len(self.value) == 0 or len(self.value) > 32 or not self.value.isalpha():
            raise ValueError("Invalid Name")


@dataclass(frozen=True)
class Card:
    name: Name
    rarity: Rarity
    edition: Edition
    physical_state: PhysicalState
    type: PokemonType
    status: Status
    illustration: Optional[str]
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_holo: bool = False
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    def __post_init__(self):
        if self.status.value != "available":
            raise ValueError("Card must be available when added to the catalog")

        if not self.physical_state:
            raise ValueError("Card must have a physical state")

    def make_available(self):
        if self.status.value == "sold":
            raise ValueError("Can't make a sold carte Available")
        return dataclasses.replace(self, status=Status("available"))

    def sell(self):
        if self.status.value == "sold":
            raise ValueError("Card already sold")
        if self.status.value == "retired":
            raise ValueError("Can't sell a retired card")
        return dataclasses.replace(self, status=Status("sold"))
