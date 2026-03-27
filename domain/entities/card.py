import dataclasses
import datetime
import uuid
from dataclasses import dataclass, field
from typing import ClassVar, Optional

from domain.exceptions.exceptions import (
    CardAlreadySoldError,
    InvalidEditionError,
    InvalidNameError,
    InvalidPhysicalStateError,
    InvalidPokemonTypeError,
    InvalidRarityError,
    InvalidStatusError,
    RemoveAlreadySoldCardError,
    RemoveReservedCardError,
    SellAlreadySoldCardError,
)


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
            raise InvalidRarityError()


@dataclass(frozen=True)
class PhysicalState:
    _valid: ClassVar[set] = {"mint", "near mint", "excellent", "played", "damaged"}

    value: str

    def __post_init__(self):
        if self.value not in self._valid:
            raise InvalidPhysicalStateError()


@dataclass(frozen=True)
class Status:
    _valid: ClassVar[set] = {"available", "reserved", "sold", "retired"}
    value: str

    def __post_init__(self):
        if self.value not in self._valid:
            raise InvalidStatusError()


@dataclass(frozen=True)
class Edition:
    code: str
    name: str
    years: int

    def __post_init__(self):
        if self.years < 2000:
            raise InvalidEditionError("Invalid Edition Years")
        if len(self.name) == 0 or len(self.name) > 32 or not self.name.isalpha():
            raise InvalidEditionError("Invalid Edition Name")
        if len(self.code) == 0 or len(self.code) > 32:
            raise InvalidEditionError("Invalid Edition Code")


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
            raise InvalidPokemonTypeError()


@dataclass(frozen=True)
class Name:
    value: str

    def __post_init__(self):
        if len(self.value) == 0 or len(self.value) > 32 or not self.value.isalpha():
            raise InvalidNameError()


@dataclass(frozen=True)
class Card:
    name: Name
    rarity: Rarity
    edition: Edition
    physical_state: PhysicalState
    type: PokemonType
    status: Status
    illustration: Optional[str]
    id: str = field(default_factory=lambda: str(uuid.uuid7()))
    is_holo: bool = False
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    def make_available(self):
        if self.status.value == "sold":
            raise CardAlreadySoldError("Can't make a sold carte Available")

        return dataclasses.replace(self, status=Status("available"))

    def sell(self):
        if self.status.value == "sold":
            raise CardAlreadySoldError("Card already sold")
        if self.status.value == "retired":
            raise SellAlreadySoldCardError()

    def remove_card_from_catalog(self):
        if self.status.value == "sold":
            raise RemoveAlreadySoldCardError()
        if self.status.value == "reserved":
            raise RemoveReservedCardError()
        if self.status.value == "retired":
            return self
        return dataclasses.replace(self, status=Status("retired"))
