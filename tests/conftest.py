import pytest

from domain.entities.card import Card
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
        return list(self._cards.values())


@pytest.fixture
def fake_repo():
    return FakeCardRepository()