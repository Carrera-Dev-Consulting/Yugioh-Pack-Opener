from logging import getLogger
from fastapi import FastAPI
import uvicorn

from app.services.logging import configure_logging

app = FastAPI()


def main():
    configure_logging()
    logger = getLogger(__name__)
    logger.info('Starting up server')
    uvicorn.run(app, host='0.0.0.0', port=8080)
