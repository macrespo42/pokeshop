from domain.entities.card import Card, Name, Rarity, Edition, PhysicalState, PokemonType, Status


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