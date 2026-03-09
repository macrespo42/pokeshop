from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from application.use_cases.get_card import GetCard
from application.use_cases.reference_card import ReferenceCard, ReferenceCardInput
from application.use_cases.search_card import SearchCard, SearchCardInput
from application.use_cases.withdrawl_card import WithdrawCard
from dependencies import (
    get_card_use_case,
    get_reference_card_use_case,
    get_search_card_use_case,
    get_withdrawl_card_use_case,
)
from domain.entities.card import Card, Edition
from interface.api.schemas.card_schemas import CardResponse

router = APIRouter(prefix="/catalog", tags=["Catalog"])


def card_to_response(card: Card) -> CardResponse:
    return CardResponse(
        id=card.id,
        name=card.name.value,
        rarity=card.rarity.value,
        type=card.type.value,
        edition=Edition(
            code=card.edition.code, name=card.edition.name, years=card.edition.years
        ),
        physical_state=card.physical_state.value,
        status=card.status.value,
        illustration=card.illustration,
        is_holo=card.is_holo,
        created_at=card.created_at,
    )


@router.post("/cards", response_model=CardResponse, status_code=status.HTTP_201_CREATED)
def reference_card(
    body: ReferenceCardInput,
    use_case: ReferenceCard = Depends(get_reference_card_use_case),
):
    try:
        card_input = ReferenceCardInput(
            name=body.name,
            rarity=body.rarity,
            edition_code=body.edition_code,
            edition_name=body.edition_name,
            edition_years=body.edition_years,
            physical_state=body.physical_state,
            type=body.type,
            illustration=body.illustration,
            is_holo=body.is_holo,
        )
        card = use_case.execute(card_input)
        return card_to_response(card)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(e)
        )

@router.get(
    "/cards", response_model=list[CardResponse], status_code=status.HTTP_200_OK
)
def search_card(
    use_case: SearchCard = Depends(get_search_card_use_case),
    name: Optional[str] = None,
    rarity: Optional[str] = None,
    edition_code: Optional[str] = None,
    edition_name: Optional[str] = None,
    edition_years: Optional[int] = None,
    physical_state: Optional[str] = None,
    card_type: Optional[str] = Query(default=None, alias="type"),
    card_status: Optional[str] = Query(default=None, alias="status"),
):
    try:
        cards_input = SearchCardInput(
            name=name,
            rarity=rarity,
            edition_code=edition_code,
            edition_name=edition_name,
            edition_years=edition_years,
            physical_state=physical_state,
            type=card_type,
            status=card_status,
        )
        cards = use_case.execute(cards_input)
        response = []
        if cards:
            response = [card_to_response(card) for card in cards]
        return response
    except ValueError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get(
    "/cards/{card_id}", response_model=CardResponse, status_code=status.HTTP_200_OK
)
def get_card(card_id: str, use_case: GetCard = Depends(get_card_use_case)):
    try:
        card = use_case.execute(card_id)
        if card:
            return card_to_response(card)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.delete(
    "/cards/{card_id}", response_model=CardResponse, status_code=status.HTTP_200_OK
)
def withdraw_card(
    card_id: str, use_case: WithdrawCard = Depends(get_withdrawl_card_use_case)
):
    try:
        card = use_case.execute(card_id)
        return card_to_response(card)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
