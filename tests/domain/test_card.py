import pytest
from domain.entities.card import (
    Card,
    Name,
    Rarity,
    Edition,
    PhysicalState,
    PokemonType,
    Status,
)


@pytest.fixture(name="card")
def card_fixture():
    return Card(
        name=Name("Pikachu"),
        rarity=Rarity(value="rare"),
        edition=Edition(code="EG4W", name="RED", years=2002),
        physical_state=PhysicalState(value="mint"),
        type=PokemonType(value="electric"),
        status=Status(value="available"),
        illustration="foo",
        is_holo=False,
    )


def test_given_card_when_sold_cannot_be_available(card):
    with pytest.raises(ValueError):
        card.sell()
        card.make_available()


def test_given_card_when_sold_cannot_be_sold_again(card):
    with pytest.raises(ValueError):
        card.sell()
        card.make_available()
