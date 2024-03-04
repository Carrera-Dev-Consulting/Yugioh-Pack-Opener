from fastapi import APIRouter, Body, Depends

from .models.requests.open_pack_request import OpenPackRequest
from app.services.pack_service import PackService
from ..dependencies import pack_service

router = APIRouter(tags=["core"])


@router.post("/packs/open")
def open_packs(
    request: OpenPackRequest = Body(), pack_service: PackService = Depends(pack_service)
):
    pass
