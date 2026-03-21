from unittest.mock import patch

import pytest

from application.use_cases.reference_card import ReferenceCard
from domain.entities.card import Card, Name
from domain.event.card import CardReference
from domain.exceptions.exceptions import (
    InvalidEditionError,
    InvalidNameError,
    InvalidPhysicalStateError,
    InvalidRarityError,
)
from tests.conftest import FakeCardRepository, FakeEventPublisher
from tests.factories import make_card, make_reference_card_input


def test_card_creation_when_card_is_valid():
    card_input = make_reference_card_input(name="Ditto")
    card = make_card(name=Name("Ditto"))
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = ReferenceCard(repo, event_publisher=event_publisher)

    result = use_case.execute(card_input)

    assert isinstance(result, Card)
    assert result.name == card.name
    assert result.status.value == "available"
    mock_publish.assert_called_with(CardReference(card_id=result.id))


def test_create_card_with_invalid_name():
    card_input = make_reference_card_input(name="")
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = ReferenceCard(repo, event_publisher=event_publisher)

    with pytest.raises(InvalidNameError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Name"


def test_create_card_with_invalid_rarity():
    card_input = make_reference_card_input(rarity="")
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = ReferenceCard(repo, event_publisher=event_publisher)

    with pytest.raises(InvalidRarityError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Rarity"


def test_create_card_with_invalid_edition_name():
    card_input = make_reference_card_input(edition_name="")
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = ReferenceCard(repo, event_publisher=event_publisher)

    with pytest.raises(InvalidEditionError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Name"


def test_create_card_with_invalid_edition_code():
    card_input = make_reference_card_input(edition_code="")
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = ReferenceCard(repo, event_publisher=event_publisher)

    with pytest.raises(InvalidEditionError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Code"


def test_create_card_with_invalid_edition_year():
    card_input = make_reference_card_input(edition_years=1999)
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = ReferenceCard(repo, event_publisher=event_publisher)

    with pytest.raises(InvalidEditionError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Years"


def test_create_card_with_invalid_physical_state():
    card_input = make_reference_card_input(physical_state="")
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = ReferenceCard(repo, event_publisher=event_publisher)

    with pytest.raises(InvalidPhysicalStateError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Physical State"
