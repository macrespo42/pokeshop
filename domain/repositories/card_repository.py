from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from domain.entities.card import Card


@dataclass(frozen=True)
class SearchFilter:
    name: Optional[str] = None
    rarity: Optional[str] = None
    edition_code: Optional[str] = None
    edition_name: Optional[str] = None
    edition_years: Optional[int] = None
    physical_state: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None


class ICardRepository(ABC):
    @abstractmethod
    def save(self, card: Card) -> None:
        pass

    @abstractmethod
    def get_by_id(self, card_id: str) -> Card | None:
        pass

    @abstractmethod
    def get_all_available(self) -> list[Card]:
        pass

    @abstractmethod
    def remove(self, card_id: str) -> Card:
        pass

    @abstractmethod
    def search(self, search_filter: SearchFilter) -> list[Card]:
        pass
