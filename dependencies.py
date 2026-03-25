from application.use_cases.get_card import GetCard
from application.use_cases.reference_card import ReferenceCard
from application.use_cases.search_card import SearchCard
from application.use_cases.withdrawl_card import WithdrawCard
from infra.events.event_publisher import InMemoryEventPublisher
from infra.repositories.card_repository import CardRepository

_repository = CardRepository()
_event_publisher = InMemoryEventPublisher()


def get_card_use_case() -> GetCard:
    return GetCard(_repository)


def get_reference_card_use_case() -> ReferenceCard:
    return ReferenceCard(card_repository=_repository, event_publisher=_event_publisher)


def get_search_card_use_case() -> SearchCard:
    return SearchCard(card_repository=_repository)


def get_withdraw_card_use_case() -> WithdrawCard:
    return WithdrawCard(card_repository=_repository, event_publisher=_event_publisher)
