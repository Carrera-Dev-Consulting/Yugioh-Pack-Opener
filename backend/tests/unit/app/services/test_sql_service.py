from unittest.mock import Mock

import pytest

from app.services.sql_service import SQLService


@pytest.fixture
def mock_engine():
    return Mock(name="engine")


@pytest.fixture
def sut(mock_engine):
    return SQLService(mock_engine)


def test_when_calling_scoped_session_nested__does_not_create_two_seperate_sessions(sut):
    with sut.scoped_session() as session:
        with sut.scoped_session() as nested_session:
            assert nested_session is session
