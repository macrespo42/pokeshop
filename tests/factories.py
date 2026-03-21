from typing import TypedDict, Unpack

from application.use_cases.reference_card import ReferenceCardInput
from domain.entities.card import (
    Card,
    Edition,
    Name,
    PhysicalState,
    PokemonType,
    Rarity,
    Status,
)


class _CardKwargs(TypedDict, total=False):
    name: Name
    rarity: Rarity
    edition: Edition
    physical_state: PhysicalState
    type: PokemonType
    status: Status
    illustration: str | None
    is_holo: bool
    id: str


def make_card(**kwargs: Unpack[_CardKwargs]) -> Card:
    defaults: _CardKwargs = {
        "name": Name("Pikachu"),
        "rarity": Rarity("common"),
        "edition": Edition(code="WBE3", name="REDFIRE", years=2008),
        "physical_state": PhysicalState("mint"),
        "type": PokemonType("electric"),
        "status": Status("available"),
        "illustration": "/s3/pikachu.png",
        "is_holo": True,
    }
    return Card(**{**defaults, **kwargs})


class _ReferenceCardInputKwargs(TypedDict, total=False):
    name: str
    rarity: str
    edition_code: str
    edition_name: str
    edition_years: int
    physical_state: str
    type: str
    illustration: str | None
    is_holo: bool


def make_reference_card_input(
    **kwargs: Unpack[_ReferenceCardInputKwargs],
) -> ReferenceCardInput:
    defaults: _ReferenceCardInputKwargs = {
        "name": "Pikachu",
        "rarity": "common",
        "edition_code": "WBE3",
        "edition_name": "REDFIRE",
        "edition_years": 2008,
        "physical_state": "mint",
        "type": "electric",
        "illustration": "/s3/pikachu.png",
        "is_holo": True,
    }
    return ReferenceCardInput(**{**defaults, **kwargs})
