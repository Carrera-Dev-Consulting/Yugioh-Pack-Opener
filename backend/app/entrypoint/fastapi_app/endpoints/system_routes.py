from fastapi import APIRouter

router = APIRouter(tags=["system"])


@router.get("/healthz")
def health_check():
    return {"o": "k"}
