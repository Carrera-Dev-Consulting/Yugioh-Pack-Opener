from functools import cache

from fastapi import Depends
from sqlalchemy import Engine, create_engine
from app.config import ServerConfig, server_config
from app.services.card_store import CardStore
from app.services.sql_service import SQLService
from app.repository.yugioh_set_repository import YugiohSetRepository


def pack_service():
    pass


def get_server_config():
    return server_config()


@cache
def get_engine(
    config: ServerConfig = Depends(get_server_config),
):
    return create_engine(config.mysql_url)


@cache
def get_sql_service(
    engine: Engine = Depends(get_engine),
):
    return SQLService(engine)


def get_set_repository(
    sql_service: SQLService = Depends(get_sql_service),
):
    with sql_service.scoped_session() as session:
        yield YugiohSetRepository(session)


def get_card_store(
    set_repository: YugiohSetRepository = Depends(get_set_repository),
):
    return CardStore(
        set_repository=set_repository,
    )
