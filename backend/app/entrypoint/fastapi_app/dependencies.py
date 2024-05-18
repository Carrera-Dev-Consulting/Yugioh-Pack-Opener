from functools import cache

from fastapi import Depends
from sqlalchemy import Engine, create_engine
from app.config import ServerConfig, server_config
from app.services.card_store import CardStore
from app.services.sql_service import SQLService


def pack_service():
    pass


def get_server_config():
    return server_config()


@cache
def get_engine(config: ServerConfig = Depends(get_server_config)):
    return create_engine(config.mysql_url)


@cache
def get_sql_service(engine: Engine = Depends(get_engine)):
    return SQLService(engine)


def get_card_store():
    return CardStore()
