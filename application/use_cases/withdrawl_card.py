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

    def execute(self, card_id: str) -> Card | None:
        card = self.repository.get_by_id(card_id)
        if card:
            retired_card = card.remove_card_from_catalog()
            self.repository.save(retired_card)
            if retired_card is not card:
                self.event_publisher.publish_event(CardRemoved(card_id=card_id))
        return card
