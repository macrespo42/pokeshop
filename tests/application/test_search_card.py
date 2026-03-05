import pytest

from application.use_cases.search_card import SearchCard, SearchCardInput
from domain.entities.card import Edition, Name, PhysicalState, PokemonType, Rarity
from tests.conftest import FakeCardRepository
from tests.factories import make_card


@pytest.fixture(name="use_case")
def use_case_fixture():
    card = make_card()
    card2 = make_card(
        name=Name("Raichu"),
        rarity=Rarity("rare"),
        edition=Edition(code="GEN2", name="GOLDSILVER", years=2010),
        physical_state=PhysicalState("played"),
        type=PokemonType("fire"),
    )
    repo = FakeCardRepository(cards=[card, card2])
    use_case = SearchCard(repo)
    return use_case


# --- name ---

def test_search_card_by_existing_name(use_case):
    result = use_case.execute(SearchCardInput(name="Raichu"))
    assert result[0].name.value == "Raichu"


def test_search_card_by_bad_name(use_case):
    result = use_case.execute(SearchCardInput(name="Ash"))
    assert len(result) == 0


# --- rarity ---

def test_search_card_by_existing_rarity(use_case):
    result = use_case.execute(SearchCardInput(rarity="rare"))
    assert result[0].rarity.value == "rare"


def test_search_card_by_bad_rarity(use_case):
    result = use_case.execute(SearchCardInput(rarity="secret"))
    assert len(result) == 0


# --- edition_code ---

def test_search_card_by_existing_edition_code(use_case):
    result = use_case.execute(SearchCardInput(edition_code="GEN2"))
    assert result[0].edition.code == "GEN2"


def test_search_card_by_bad_edition_code(use_case):
    result = use_case.execute(SearchCardInput(edition_code="UNKNOWN"))
    assert len(result) == 0


# --- edition_name ---

def test_search_card_by_existing_edition_name(use_case):
    result = use_case.execute(SearchCardInput(edition_name="GOLDSILVER"))
    assert result[0].edition.name == "GOLDSILVER"


def test_search_card_by_bad_edition_name(use_case):
    result = use_case.execute(SearchCardInput(edition_name="UNKNOWN"))
    assert len(result) == 0


# --- edition_years ---

def test_search_card_by_existing_edition_years(use_case):
    result = use_case.execute(SearchCardInput(edition_years=2010))
    assert result[0].edition.years == 2010


def test_search_card_by_bad_edition_years(use_case):
    result = use_case.execute(SearchCardInput(edition_years=2099))
    assert len(result) == 0


# --- physical_state ---

def test_search_card_by_existing_physical_state(use_case):
    result = use_case.execute(SearchCardInput(physical_state="played"))
    assert result[0].physical_state.value == "played"


def test_search_card_by_bad_physical_state(use_case):
    result = use_case.execute(SearchCardInput(physical_state="damaged"))
    assert len(result) == 0


# --- type ---

def test_search_card_by_existing_type(use_case):
    result = use_case.execute(SearchCardInput(type="fire"))
    assert result[0].type.value == "fire"


def test_search_card_by_bad_type(use_case):
    result = use_case.execute(SearchCardInput(type="water"))
    assert len(result) == 0


# --- status ---

def test_search_card_by_existing_status(use_case):
    result = use_case.execute(SearchCardInput(status="available"))
    assert len(result) == 2


def test_search_card_by_bad_status(use_case):
    result = use_case.execute(SearchCardInput(status="sold"))
    assert len(result) == 0


# --- combined ---

def test_search_card_with_combined_criteria(use_case):
    result = use_case.execute(SearchCardInput(name="Raichu", rarity="rare", type="fire"))
    assert len(result) == 1
    assert result[0].name.value == "Raichu"
