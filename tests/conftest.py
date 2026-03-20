import pytest

from domain.entities.card import Card
from domain.event.event_publisher import Event, IEventPublisher
from domain.repositories.card_repository import ICardRepository, SearchFilter


class FakeCardRepository(ICardRepository):
    def __init__(self, cards: list[Card] = None):
        self._cards = {c.id: c for c in (cards or [])}

    def save(self, card: Card) -> None:
        self._cards[card.id] = card

    def get_by_id(self, card_id: str) -> Card:
        return self._cards.get(card_id)

    def get_all_available(self) -> list[Card]:
        return [c for c in self._cards.values() if c.status.value == "available"]

    def remove(self, card_id: str) -> Card:
        return self._cards.pop(card_id, None)

    def search(self, search_filter: SearchFilter) -> list[Card]:
        results = list(self._cards.values())
        if search_filter.name is not None:
            results = [c for c in results if c.name.value == search_filter.name]
        if search_filter.rarity is not None:
            results = [c for c in results if c.rarity.value == search_filter.rarity]
        if search_filter.edition_code is not None:
            results = [
                c for c in results if c.edition.code == search_filter.edition_code
            ]
        if search_filter.edition_name is not None:
            results = [
                c for c in results if c.edition.name == search_filter.edition_name
            ]
        if search_filter.edition_years is not None:
            results = [
                c for c in results if c.edition.years == search_filter.edition_years
            ]
        if search_filter.physical_state is not None:
            results = [
                c
                for c in results
                if c.physical_state.value == search_filter.physical_state
            ]
        if search_filter.type is not None:
            results = [c for c in results if c.type.value == search_filter.type]
        if search_filter.status is not None:
            results = [c for c in results if c.status.value == search_filter.status]
        return results


class FakeEventPublisher(IEventPublisher):
    def publish_event(self, event: Event) -> None:
        print(f"Pushing event: {event}")


@pytest.fixture
def fake_repo():
    return FakeCardRepository()


@pytest.fixture
def fake_event_published():
    return FakeEventPublisher()
