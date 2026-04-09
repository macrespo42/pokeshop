from application.use_cases.search_card import SearchCard, SearchCardInput, SearchFilter
from tests.factories import make_card
from tests.fakes import FakeCardRepository


def test_search_card_should_call_repository_with_given_search_card_input():
    repo = FakeCardRepository()
    use_case = SearchCard(repo)

    use_case.execute(SearchCardInput(name="Raichu", rarity="rare"))

    assert repo.search_called_with == SearchFilter(name="Raichu", rarity="rare")


def test_search_card_returns_should_return_the_repository_result():
    repo = FakeCardRepository()
    repo.search_return_value = [make_card()]
    use_case = SearchCard(repo)

    result = use_case.execute(SearchCardInput(name="Pikachu"))

    assert result == repo.search_return_value
