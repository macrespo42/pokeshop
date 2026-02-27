from domain.entities.card import Card
from domain.repositories.card_repository import ICardRepository


class CardRepository(ICardRepository):
    def __init__(self):
        self._cards = dict[str, Card]

    def save(self, card: Card) -> None:
        card.make_available()
        self._cards[card.id] = card

    def get_by_id(self, card_id: str) -> Card:
        return self._cards.get(card_id)

    def get_all_available(self) -> list[Card]:
        return [v for v in self._cards.values() if v.status.value == "available"]

    def remove(self, card_id: str) -> Card:
        return self._cards.pop(card_id)

    def search(self, search_filter):
        return super().search(search_filter)
