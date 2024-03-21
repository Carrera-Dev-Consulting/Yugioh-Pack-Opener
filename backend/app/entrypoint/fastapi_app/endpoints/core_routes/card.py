from fastapi import APIRouter, Depends

from app.services.card_service import CardService

from ..models.queries import CardQuery
from ...dependencies import get_card_service


router = APIRouter(tags=["cards"])


@router.get("")
def query_cards(
    card_query: CardQuery = Depends(),
    card_service: CardService = Depends(get_card_service),
):
    return card_query
