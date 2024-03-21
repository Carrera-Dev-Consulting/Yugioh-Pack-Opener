from fastapi import APIRouter, Body, Depends

from app.services.pack_service import PackService

from ..models.requests.open_pack_request import OpenPackRequest
from ...dependencies import get_pack_service


router = APIRouter(tags=["pack"])


@router.post("/open")
def open_packs(
    request: OpenPackRequest = Body(),
    pack_service: PackService = Depends(get_pack_service),
):
    pass
