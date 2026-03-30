import pytest

from application.use_cases.withdrawl_card import WithdrawCard
from domain.entities.card import Status
from domain.exceptions.exceptions import (
    RemoveAlreadySoldCardError,
    RemoveReservedCardError,
)
from tests.factories import make_card
from tests.fakes import FakeCardRepository, FakeEventPublisher


def test_withdraw_existing_and_available_card_should_publish_an_event():
    card = make_card()
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(card_repository=repo, event_publisher=event_publisher)

    use_case.execute(card.id)

    assert len(event_publisher.events) == 1


def test_withdraw_when_already_removed_card_should_not_publish_event():
    card = make_card(status=Status(value="retired"))
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(card_repository=repo, event_publisher=event_publisher)

    use_case.execute(card.id)

    assert len(event_publisher.events) == 0


def test_withdraw_unexisting_card_should_not_publish_event():
    repo = FakeCardRepository()
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(card_repository=repo, event_publisher=event_publisher)

    use_case.execute("non-existent-id")

    assert len(event_publisher.events) == 0


def test_withdraw_card_should_fail_when_card_already_sold():
    card = make_card(status=Status("sold"))
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(card_repository=repo, event_publisher=event_publisher)

    with pytest.raises(expected_exception=RemoveAlreadySoldCardError):
        use_case.execute(card.id)

    assert len(event_publisher.events) == 0


def test_withdraw_card_should_fail_when_card_is_reserved():
    card = make_card(status=Status("reserved"))
    repo = FakeCardRepository(cards=[card])
    event_publisher = FakeEventPublisher()
    use_case = WithdrawCard(card_repository=repo, event_publisher=event_publisher)

    with pytest.raises(expected_exception=RemoveReservedCardError):
        use_case.execute(card.id)

    assert len(event_publisher.events) == 0
