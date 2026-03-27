import pytest

from application.use_cases.reference_card import ReferenceCard
from domain.entities.card import Card, Name
from domain.exceptions.exceptions import (
    InvalidEditionError,
    InvalidNameError,
    InvalidPhysicalStateError,
    InvalidRarityError,
)
from tests.factories import make_card, make_reference_card_input
from tests.fakes import FakeCardRepository, FakeEventPublisher


@pytest.fixture
def repo():
    return FakeCardRepository()


@pytest.fixture
def event_publisher():
    return FakeEventPublisher()


@pytest.fixture
def use_case(repo, event_publisher):
    return ReferenceCard(card_repository=repo, event_publisher=event_publisher)


def test_card_creation_when_card_is_valid(use_case, event_publisher):
    card_input = make_reference_card_input(name="Ditto")
    card = make_card(name=Name(value="Ditto"))

    result = use_case.execute(card_input)

    assert isinstance(result, Card)
    assert result.name == card.name
    assert result.status.value == "available"
    assert len(event_publisher.events) == 1


def test_create_card_with_invalid_name(use_case):
    card_input = make_reference_card_input(name="")

    with pytest.raises(expected_exception=InvalidNameError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Name"


def test_create_card_with_invalid_rarity(use_case):
    card_input = make_reference_card_input(rarity="")

    with pytest.raises(expected_exception=InvalidRarityError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Rarity"


def test_create_card_with_invalid_edition_name(use_case):
    card_input = make_reference_card_input(edition_name="")

    with pytest.raises(expected_exception=InvalidEditionError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Name"


def test_create_card_with_invalid_edition_code(use_case):
    card_input = make_reference_card_input(edition_code="")

    with pytest.raises(expected_exception=InvalidEditionError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Code"


def test_create_card_with_invalid_edition_year(use_case):
    card_input = make_reference_card_input(edition_years=1999)

    with pytest.raises(expected_exception=InvalidEditionError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Years"


def test_create_card_with_invalid_physical_state(use_case):
    card_input = make_reference_card_input(physical_state="")

    with pytest.raises(expected_exception=InvalidPhysicalStateError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Physical State"
