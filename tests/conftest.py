from typing import Callable

from domain.entities.card import Card, Name
from domain.event.event_publisher import Event, IEventPublisher
from domain.repositories.card_repository import ICardRepository, SearchFilter


class FakeCardRepository(ICardRepository):
    def __init__(self, cards: list[Card] | None = None):
        self._cards = {c.id: c for c in (cards or [])}
        self.search_called_with: SearchFilter | None = None
        self.search_return_value: list[Card] = []

    def save(self, card: Card) -> None:
        self._cards[card.id] = card

    def get_by_id(self, card_id: str) -> Card | None:
        return self._cards.get(card_id)

    def get_all_available(self) -> list[Card]:
        return [c for c in self._cards.values() if c.status.value == "available"]

    def remove(self, card_id: str) -> Card:
        return self._cards.pop(card_id, None)

    def search(self, search_filter: SearchFilter) -> list[Card]:
        self.search_called_with = search_filter
        return self.search_return_value


class FakeEventPublisher(IEventPublisher):
    def __init__(self):
        self.events = []

    def publish_event(self, event: Event) -> None:
        self.events.append(event)
