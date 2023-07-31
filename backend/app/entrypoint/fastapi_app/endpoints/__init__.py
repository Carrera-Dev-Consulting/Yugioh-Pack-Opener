from fastapi import APIRouter
from .system_routes import router as system_router
from .core_routes import router as core_router

api_router = APIRouter()


api_router.include_router(system_router)
api_router.include_router(core_router)
