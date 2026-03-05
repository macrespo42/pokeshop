from domain.entities.card import Card
from domain.repositories.card_repository import ICardRepository, SearchFilter


class CardRepository(ICardRepository):
    def __init__(self):
        self._cards: dict[str, Card] = {}

    def save(self, card: Card) -> None:
        card.make_available()
        self._cards[card.id] = card

    def get_by_id(self, card_id: str) -> Card | None:
        return self._cards.get(card_id)

    def get_all_available(self) -> list[Card]:
        return [v for v in self._cards.values() if v.status.value == "available"]

    def remove(self, card_id: str) -> Card:
        return self._cards.pop(card_id)

    def search(self, search_filter: SearchFilter) -> list[Card]:
        filters = [
            (search_filter.name, lambda c: c.name.value),
            (search_filter.rarity, lambda c: c.rarity.value),
            (search_filter.edition_code, lambda c: c.edition.code),
            (search_filter.edition_name, lambda c: c.edition.name),
            (search_filter.edition_years, lambda c: c.edition.years),
            (search_filter.physical_state, lambda c: c.physical_state.value),
            (search_filter.type, lambda c: c.type.value),
            (search_filter.status, lambda c: c.status.value),
        ]

        active = [(value, getter) for value, getter in filters if value is not None]

        return [
            c
            for c in self._cards.values()
            if all(getter(c) == value for value, getter in active)
        ]
