from logging import getLogger
from fastapi import FastAPI
import uvicorn

from app.services.logging import configure_logging
from .endpoints import api_router

app = FastAPI()
app.include_router(api_router)


def main():
    log_config = configure_logging()
    logger = getLogger(__name__)
    logger.info("Starting up server")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_config=log_config)
