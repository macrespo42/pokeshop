from application.use_cases.withdrawl_card import WithdrawCard
from tests.conftest import FakeCardRepository
from tests.factories import make_card


def test_remove_card():
    card = make_card()
    repo = FakeCardRepository(cards=[card])
    use_case = WithdrawCard(repo)

    result = use_case.execute(card.id)

    assert result == card


def test_remove_card_returns_none_when_no_exist():
    repo = FakeCardRepository()
    use_case = WithdrawCard(repo)

    result = use_case.execute("non-existent-id")

    assert result is None
