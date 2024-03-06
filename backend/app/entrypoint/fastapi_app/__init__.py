from logging import getLogger

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import uvicorn
from starlette.middleware.sessions import SessionMiddleware

from app.config import server_config
from app.entrypoint.fastapi_app.endpoints.oauth import Unauthenticated
from app.services.logging import configure_logging
from .endpoints import api_router

logger = getLogger(__name__)
config = server_config()

app = FastAPI()
app.include_router(api_router)
app.add_middleware(SessionMiddleware, secret_key=config.app_secret_key)


@app.exception_handler(Unauthenticated)
def unauthenticated(request: Request, exc: Unauthenticated):
    logger.warning("User was unauthenticated and trying to access secure resource")
    return RedirectResponse(request.url_for("auth:login"))


def main():
    log_config = configure_logging()
    logger.info("Starting up server")
    uvicorn.run(
        app, host="0.0.0.0", port=8080, log_config=log_config, proxy_headers=True
    )
