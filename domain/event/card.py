from dataclasses import dataclass

from domain.event.event_publisher import Event


@dataclass(frozen=True)
class CardReference(Event):
    card_id: str


@dataclass(frozen=True)
class CardRemoved(Event):
    card_id: str
