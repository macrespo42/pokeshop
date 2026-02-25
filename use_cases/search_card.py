from dataclasses import dataclass
from typing import Optional

from domain.entities.card import Card
from domain.repositories.card_repository import CardRepository, SearchFilter


@dataclass(frozen=True)
class SearchCardInput:
    name: Optional[str] = None
    rarity: Optional[str] = None
    edition_code: Optional[str] = None
    edition_name: Optional[str] = None
    edition_years: Optional[int] = None
    physical_state: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None


class SearchCard:
    def __init__(self, card_repository: CardRepository) -> None:
        self.repository = card_repository

    def execute(self, search_card_input: SearchCardInput) -> list[Card]:
        search_filter = SearchFilter(
            name=search_card_input.name,
            rarity=search_card_input.rarity,
            edition_code=search_card_input.edition_code,
            edition_name=search_card_input.edition_name,
            edition_years=search_card_input.edition_years,
            physical_state=search_card_input.physical_state,
            type=search_card_input.type,
            status=search_card_input.status,
        )
        return self.repository.search(search_filter)
