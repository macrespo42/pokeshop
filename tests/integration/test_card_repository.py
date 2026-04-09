import pytest

from domain.entities.card import Name, Rarity, Status
from domain.repositories.card_repository import SearchFilter
from infra.repositories.card_repository import CardRepository
from tests.factories import make_card


@pytest.fixture
def repo() -> CardRepository:
    return CardRepository()


def test_save_then_get_by_id_returns_card(repo):
    card = make_card()
    repo.save(card)

    result = repo.get_by_id(card.id)

    assert result == card


def test_save_overwrites_existing_card(repo):
    card = make_card()
    updated_card = make_card(id=card.id, status=Status("sold"))
    repo.save(card)
    repo.save(updated_card)

    result = repo.get_by_id(card.id)

    assert result.status.value == "sold"


def test_get_by_id_when_card_does_not_exist_returns_none(repo):
    result = repo.get_by_id("non-existent-id")

    assert result is None


def test_search_with_no_filter_returns_all_cards(repo):
    repo.save(make_card(name=Name("Pikachu")))
    repo.save(make_card(name=Name("Bulbizarre")))

    results = repo.search(SearchFilter())

    assert len(results) == 2


def test_search_by_name_returns_only_matching_card(repo):
    repo.save(make_card(name=Name("Pikachu")))
    repo.save(make_card(name=Name("Bulbizarre")))

    results = repo.search(SearchFilter(name="Bulbizarre"))

    assert len(results) == 1
    assert results[0].name.value == "Bulbizarre"


def test_search_by_rarity_returns_only_matching_cards(repo):
    repo.save(make_card(rarity=Rarity("common")))
    repo.save(make_card(rarity=Rarity("rare")))
    repo.save(make_card(rarity=Rarity("common")))

    results = repo.search(SearchFilter(rarity="common"))

    assert len(results) == 2
    assert all(c.rarity.value == "common" for c in results)


def test_search_by_status_returns_only_matching_cards(repo):
    repo.save(make_card(status=Status("available")))
    repo.save(make_card(status=Status("sold")))

    results = repo.search(SearchFilter(status="available"))

    assert len(results) == 1
    assert results[0].status.value == "available"


def test_search_with_no_match_returns_empty_list(repo):
    repo.save(make_card(rarity=Rarity("common")))

    results = repo.search(SearchFilter(rarity="secret"))

    assert results == []


def test_search_with_multiple_filters_returns_only_exact_matches(repo):
    repo.save(make_card(rarity=Rarity("secret")))
    repo.save(make_card(rarity=Rarity("secret"), name=Name("Psyduck")))
    repo.save(make_card(rarity=Rarity("ultra_rare"), name=Name("Psyduck")))

    results = repo.search(SearchFilter(name="Psyduck", rarity="secret"))

    assert len(results) == 1
    assert results[0].rarity.value == "secret"
    assert results[0].name.value == "Psyduck"
