from abc import ABC, abstractmethod

from domain.entities.card import Card


class CardRepository(ABC):
    @abstractmethod
    def save(self, card: Card) -> None:
        pass

    @abstractmethod
    def get_by_id(self, card_id: str) -> Card:
        pass

    @abstractmethod
    def get_all_available(self) -> list[Card]:
        pass

    @abstractmethod
    def remove(self, name: str) -> Card:
        pass
