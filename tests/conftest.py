from typing import Callable

import pytest

from domain.entities.card import Card
from domain.event.event_publisher import Event, IEventPublisher
from domain.repositories.card_repository import ICardRepository, SearchFilter


class FakeCardRepository(ICardRepository):
    def __init__(self, cards: list[Card] | None = None):
        self._cards = {c.id: c for c in (cards or [])}

    def save(self, card: Card) -> None:
        self._cards[card.id] = card

    def get_by_id(self, card_id: str) -> Card | None:
        return self._cards.get(card_id)

    def get_all_available(self) -> list[Card]:
        return [c for c in self._cards.values() if c.status.value == "available"]

    def remove(self, card_id: str) -> Card:
        return self._cards.pop(card_id, None)

    def search(self, search_filter: SearchFilter) -> list[Card]:
        results = list(self._cards.values())
        filters: list[tuple[object, Callable[[Card], object]]] = [
            (search_filter.name, lambda c: c.name.value),
            (search_filter.rarity, lambda c: c.rarity.value),
            (search_filter.edition_code, lambda c: c.edition.code),
            (search_filter.edition_name, lambda c: c.edition.name),
            (search_filter.edition_years, lambda c: c.edition.years),
            (search_filter.physical_state, lambda c: c.physical_state.value),
            (search_filter.type, lambda c: c.type.value),
            (search_filter.status, lambda c: c.status.value),
        ]
        for value, getter in filters:
            if value is not None:
                results = [c for c in results if getter(c) == value]
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
