from domain.entities.card import Card
from domain.event.card import CardRemoved
from domain.event.event_publisher import IEventPublisher
from domain.repositories.card_repository import ICardRepository


class WithdrawCard:
    def __init__(
        self, card_repository: ICardRepository, event_publisher: IEventPublisher
    ) -> None:
        self.repository = card_repository
        self.event_publisher = event_publisher

    def execute(self, card_id: str) -> Card:
        removed = self.repository.remove(card_id)
        if removed:
            self.event_publisher.publish_event(CardRemoved(card_id=card_id))
        return removed
