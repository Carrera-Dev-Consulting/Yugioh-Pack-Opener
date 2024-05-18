from fastapi import APIRouter, Body, Depends

from app.models.pagination import PaginationOptions, PaginationResult
from app.models.set_request import SetRequest
from app.models.yugioh_set import YugiohSet
from app.services.card_store import CardStore

from .models.pack import OpenPackRequest
from app.services.pack_service import PackService
from ..dependencies import pack_service, get_card_store
from .models.base import page_parameters
from .models.set import set_request

router = APIRouter(tags=["core"])

pack_router = APIRouter(
    tags=["pack"],
    prefix="/packs",
)


@pack_router.post("/packs/open")
def open_packs(
    request: OpenPackRequest = Body(), pack_service: PackService = Depends(pack_service)
):
    pass


set_router = APIRouter(
    prefix="/sets",
    tags=["sets"],
)


@set_router.get(
    "/",
)
def get_all_sets(
    page_ops: PaginationOptions = Depends(page_parameters),
    request: SetRequest = Depends(set_request),
    store: CardStore = Depends(get_card_store),
) -> PaginationResult[YugiohSet]:
    results = store.get_sets(request, page_ops)
    return results


router.include_router(set_router)
router.include_router(pack_router)
