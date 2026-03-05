import pytest

from application.use_cases.reference_card import ReferenceCard
from domain.entities.card import Card, Name
from tests.conftest import FakeCardRepository
from tests.factories import make_card, make_reference_card_input


def test_valid_card_creation():
    card_input = make_reference_card_input(name="Ditto")
    card = make_card(name=Name("Ditto"))
    repo = FakeCardRepository()
    use_case = ReferenceCard(repo)

    result = use_case.execute(card_input)

    assert isinstance(result, Card)
    assert result.name == card.name
    assert result.status.value == "available"


def test_create_unavailable_card():
    card_input = make_reference_card_input(status="retired")
    repo = FakeCardRepository()
    use_case = ReferenceCard(repo)

    with pytest.raises(ValueError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Card must be available when added to the catalog"


def test_create_card_with_bad_name():
    card_input = make_reference_card_input(name="")
    repo = FakeCardRepository()
    use_case = ReferenceCard(repo)

    with pytest.raises(ValueError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Name"


def test_create_card_with_bad_rarity():
    card_input = make_reference_card_input(rarity="")
    repo = FakeCardRepository()
    use_case = ReferenceCard(repo)

    with pytest.raises(ValueError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Rarity"


def test_create_card_with_bad_edition_name():
    card_input = make_reference_card_input(edition_name="")
    repo = FakeCardRepository()
    use_case = ReferenceCard(repo)

    with pytest.raises(ValueError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Name"


def test_create_card_with_bad_edition_code():
    card_input = make_reference_card_input(edition_code="")
    repo = FakeCardRepository()
    use_case = ReferenceCard(repo)

    with pytest.raises(ValueError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Code"


def test_create_card_with_bad_edition_year():
    card_input = make_reference_card_input(edition_years=1999)
    repo = FakeCardRepository()
    use_case = ReferenceCard(repo)

    with pytest.raises(ValueError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Edition Years"


def test_create_card_with_bad_physical_state():
    card_input = make_reference_card_input(physical_state="")
    repo = FakeCardRepository()
    use_case = ReferenceCard(repo)

    with pytest.raises(ValueError) as e:
        use_case.execute(card_input)
    assert str(e.value) == "Invalid Physical State"
