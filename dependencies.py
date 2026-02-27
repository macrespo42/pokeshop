from infra.repositories.card_repository import CardRepository
from use_cases.get_card import GetCard
from use_cases.list_available_cards import ListAvailableCards
from use_cases.reference_card import ReferenceCard
from use_cases.search_card import SearchCard
from use_cases.withdrawl_card import WithdrawCard

_repository = CardRepository()


def get_card_use_case() -> GetCard:
    return GetCard(_repository)


def get_list_available_card_use_case() -> ListAvailableCards:
    return ListAvailableCards(_repository)


def get_reference_card_use_case() -> ReferenceCard:
    return ReferenceCard(_repository)


def get_search_card_use_case() -> SearchCard:
    return SearchCard(_repository)


def get_withdrawl_card_use_case() -> WithdrawCard:
    return WithdrawCard(_repository)
