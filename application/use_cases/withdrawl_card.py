from domain.entities.card import Card
from domain.repositories.card_repository import ICardRepository


class WithdrawCard:
    def __init__(self, card_repository: ICardRepository) -> None:
        self.repository = card_repository

    def execute(self, card_id: str) -> Card:
        return self.repository.remove(card_id)
