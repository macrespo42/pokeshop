import pytest

from application.use_cases.withdrawl_card import WithdrawCard
from domain.entities.card import Status
from domain.exceptions.exceptions import (
    RemoveAlreadySoldCardError,
    RemoveReservedCardError,
)
from tests.factories import make_card
from tests.fakes import FakeCardRepository, FakeEventPublisher


def test_withdraw_existing_card():
    card = make_card()
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(repo, event_publisher=event_publisher)

    result = use_case.execute(card.id)

    assert result == card
    assert len(event_publisher.events) == 1


def test_withdraw_when_retire_card_twice_should_publish_event_once():
    card = make_card()
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(repo, event_publisher=event_publisher)

    use_case.execute(card.id)
    result = use_case.execute(card.id)

    assert result is not None
    assert result.status.value == "retired"
    assert len(event_publisher.events) == 1


def test_withdraw_card_who_does_not_exist():
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(repo, event_publisher=event_publisher)

    result = use_case.execute("non-existent-id")

    assert result is None
    assert len(event_publisher.events) == 0


def test_withdraw_card_already_sold():
    card = make_card(status=Status("sold"))
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(repo, event_publisher=event_publisher)

    with pytest.raises(expected_exception=RemoveAlreadySoldCardError):
        use_case.execute(card.id)

    assert len(event_publisher.events) == 0


def test_withdraw_reserved_card():
    card = make_card(status=Status("reserved"))
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(repo, event_publisher=event_publisher)

    with pytest.raises(expected_exception=RemoveReservedCardError):
        use_case.execute(card.id)

    assert len(event_publisher.events) == 0
