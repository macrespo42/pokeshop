from application.use_cases.withdrawl_card import WithdrawCard
from tests.conftest import FakeCardRepository, FakeEventPublisher
from tests.factories import make_card


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
