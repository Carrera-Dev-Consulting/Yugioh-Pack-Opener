from logging import getLogger
from typing import Any, Generator
import pytest
from sqlalchemy import Engine, MetaData, create_engine, delete
from app.repository.models import BaseSQLModel

in_memory_url = "sqlite://"
logger = getLogger(__name__)


@pytest.fixture(scope="session")
def setup_database() -> Generator[Engine, Any, None]:
    engine = create_engine(in_memory_url)
    meta: MetaData = BaseSQLModel.metadata
    meta.create_all(engine, checkfirst=True)
    yield engine


@pytest.fixture(scope="function")
def database_session(setup_database: Engine) -> Generator[Engine, Any, None]:

    yield setup_database
    with setup_database.begin() as conn:
        meta: MetaData = BaseSQLModel.metadata
        for name, table in meta.tables.items():
            try:
                result = conn.execute(delete(table))
                logger.info(f"Deleted {result.rowcount} from {name}")
            except Exception as err:
                logger.exception(err)
                logger.error(f"Failed to cleanup table: {name}")
