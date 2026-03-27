from application.use_cases.get_card import GetCard
from tests.factories import make_card
from tests.fakes import FakeCardRepository


def test_get_card_returns_card_by_id_with_existing_card():
    card = make_card()
    repo = FakeCardRepository(cards=[card])
    use_case = GetCard(repo)

    result = use_case.execute(card.id)

    assert result == card


def test_get_card_returns_none_when_card_not_found():
    repo = FakeCardRepository()
    use_case = GetCard(repo)

    result = use_case.execute("non-existent-id")

    assert result is None
