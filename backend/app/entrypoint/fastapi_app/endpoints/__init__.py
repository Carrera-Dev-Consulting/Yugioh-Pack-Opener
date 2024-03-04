from fastapi import APIRouter
from .system_routes import router as system_router
from .core_routes import router as core_router
from .oauth import router as oauth_router

api_router = APIRouter()


api_router.include_router(system_router)
api_router.include_router(core_router, prefix="/api/v1")
api_router.include_router(oauth_router, prefix="/api")
