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


def make_card(**kwargs) -> Card:
    defaults = dict(
        name=Name("Pikachu"),
        rarity=Rarity("common"),
        edition=Edition(code="WBE3", name="REDFIRE", years=2008),
        physical_state=PhysicalState("mint"),
        type=PokemonType("electric"),
        status=Status("available"),
        illustration="/s3/pikachu.png",
        is_holo=True,
    )
    return Card(**{**defaults, **kwargs})


def make_reference_card_input(**kwargs) -> ReferenceCardInput:
    default = dict(
        name="Pikachu",
        rarity="common",
        edition_code="WBE3",
        edition_name="REDFIRE",
        edition_years=2008,
        physical_state="mint",
        type="electric",
        status="available",
        illustration="/s3/pikachu.png",
        is_holo=True,
    )

    return ReferenceCardInput(**{**default, **kwargs})
