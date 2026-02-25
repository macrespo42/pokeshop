from domain.entities.card import Card
from domain.repositories.card_repository import CardRepository


class GetCard:
    def __init__(self, card_repository: CardRepository) -> None:
        self.repository = card_repository

    def execute(self, card_id: str) -> Card:
        return self.repository.get_by_id(card_id)
