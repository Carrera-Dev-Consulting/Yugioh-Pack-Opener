from logging import getLogger

from fastapi import FastAPI
import uvicorn
from starlette.middleware.sessions import SessionMiddleware

from app.config import server_config
from app.services.logging import configure_logging
from .endpoints import api_router

config = server_config()

app = FastAPI()
app.include_router(api_router)
app.add_middleware(SessionMiddleware, secret_key=config.app_secret_key)


def main():
    log_config = configure_logging()
    logger = getLogger(__name__)
    logger.info("Starting up server")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_config=log_config)
