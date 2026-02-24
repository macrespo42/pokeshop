from domain.entities.card import Card
from domain.repositories.card_repository import CardRepository


class ListAvailableCards:

    def __init__(self, card_repository: CardRepository) -> None:
        self.repository = card_repository

    def execute(self) -> list[Card]:
        return self.repository.get_all_available()
