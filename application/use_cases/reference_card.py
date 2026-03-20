from dataclasses import dataclass

from domain.entities.card import (
    Card,
    Edition,
    Name,
    PhysicalState,
    PokemonType,
    Rarity,
    Status,
)
from domain.event.card import CardReference
from domain.event.event_publisher import IEventPublisher
from domain.repositories.card_repository import ICardRepository


@dataclass(frozen=True)
class ReferenceCardInput:
    name: str
    rarity: str
    edition_code: str
    edition_name: str
    edition_years: int
    physical_state: str
    type: str
    illustration: str | None
    is_holo: bool = False


class ReferenceCard:
    def __init__(
        self, card_repository: ICardRepository, event_publisher: IEventPublisher
    ) -> None:
        self.repository = card_repository
        self.event_publisher = event_publisher

    def execute(self, card_input: ReferenceCardInput) -> Card:
        card = Card(
            name=Name(card_input.name),
            rarity=Rarity(card_input.rarity),
            edition=Edition(
                code=card_input.edition_code,
                name=card_input.edition_name,
                years=card_input.edition_years,
            ),
            physical_state=PhysicalState(card_input.physical_state),
            type=PokemonType(card_input.type),
            status=Status(value="available"),
            illustration=card_input.illustration,
            is_holo=card_input.is_holo,
        )

        self.repository.save(card)
        self.event_publisher.publish_event(CardReference(card_id=card.id))

        return card
