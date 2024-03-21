from fastapi import APIRouter
from .pack import router as pack_router
from .card import router as card_router


router = APIRouter(tags=["core"])

router.include_router(pack_router, prefix="/packs")
router.include_router(card_router, prefix="/cards")
