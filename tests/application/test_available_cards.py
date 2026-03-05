from application.use_cases.list_available_cards import ListAvailableCards
from domain.entities.card import Name
from tests.conftest import FakeCardRepository
from tests.factories import make_card


def test_list_available_card():
    card = make_card()
    card2 = make_card(name=Name("Raichu"))
    repo = FakeCardRepository(cards=[card, card2])
    use_case = ListAvailableCards(repo)

    result = use_case.execute()

    assert len(result) == 2


def test_list_available_card_with_no_cards():
    repo = FakeCardRepository()
    use_case = ListAvailableCards(repo)

    result = use_case.execute()

    assert len(result) == 0
