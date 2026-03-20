from unittest.mock import patch

from application.use_cases.withdrawl_card import WithdrawCard
from domain.event.card import CardRemoved
from tests.conftest import FakeCardRepository, FakeEventPublisher
from tests.factories import make_card


def test_remove_card():
    card = make_card()
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(repo, event_publisher=event_publisher)

    with patch.object(event_publisher, "publish_event") as mock_publish:
        result = use_case.execute(card.id)

    assert result == card
    mock_publish.assert_called_once_with(CardRemoved(card_id=card.id))


def test_remove_card_returns_none_when_no_exist():
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(repo, event_publisher=event_publisher)

    with patch.object(event_publisher, "publish_event") as mock_publish:
        result = use_case.execute("non-existent-id")

    assert result is None
    mock_publish.assert_not_called()
