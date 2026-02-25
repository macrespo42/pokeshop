from fastapi import APIRouter, status, HTTPException

from domain.entities.card import Card
from interface.api.schemas.card_schemas import CardResponse, CardCreateRequest, Edition
from use_cases.reference_card import ReferenceCard, ReferenceCardInput
from use_cases.get_card import GetCard

router = APIRouter(prefix="/catalog", tags=["Catalog"])


def card_to_response(card: Card) -> CardResponse:
    return CardResponse(
        id=card.id,
        name=card.name.value,
        rarity=card.rarity.value,
        type=card.type.value,
        edition=Edition(code=card.edition.code, name=card.edition.name, year=card.edition.years),
        physical_state=card.physical_state.value,
        status=card.status.value,
        illustration=card.illustration,
        is_holo=card.is_holo,
        created_at=card.created_at,
    )


@router.post("/cards", response_model=CardResponse, status_code=status.HTTP_201_CREATED)
def reference_card(body: CardCreateRequest, use_case: ReferenceCard):
    try:
        card_input = ReferenceCardInput(
            name=body.name,
            rarity=body.rarity,
            edition_code=body.edition.code,
            edition_name=body.edition.name,
            edition_years=body.edition.year,
            physical_state=body.physical_state,
            type=body.type,
            status=body.status,
            illustration=body.illustration,
            is_holo=body.is_holo,
        )
        card = use_case.execute(card_input)
        return card_to_response(card)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT)

@router.get("/cards/{card_id}", response_model=CardResponse, status_code=status.HTTP_200_OK)
def get_card(card_id: str, use_case: GetCard):
    try:
        card = use_case.execute(card_id)
        return card_to_response(card)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)