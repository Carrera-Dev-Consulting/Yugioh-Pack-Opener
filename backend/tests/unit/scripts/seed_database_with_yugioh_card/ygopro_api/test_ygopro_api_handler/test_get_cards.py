from unittest.mock import MagicMock, Mock
import pytest
from scripts.seed_database_with_yugioh_card.ygopro_api import (
    YGOProAPIHandler,
    DirectoryCacher,
)


@pytest.fixture
def requests():
    return Mock(name="requests")


@pytest.fixture
def cacher():
    return MagicMock(name="cacher", spec=DirectoryCacher)


@pytest.fixture
def sleep():
    return Mock(name="sleep")


@pytest.fixture
def sut(requests, cacher, sleep) -> YGOProAPIHandler:
    return YGOProAPIHandler(cacher=cacher, sleep=sleep, requests=requests)


def test_when_getting_cards_that_have_already_been_cached__returns_what_cacher_read(
    sut: YGOProAPIHandler, cacher: DirectoryCacher
):
    cacher.exists.return_value = True
    cacher.read.return_value = [
        {
            "id": -1,
            "name": "name",
            "type": "type",
            "frameType": "frameType",
            "desc": "desc",
        }
    ]
    cards = sut.get_cards()

    assert len(cards) == 1


def test_when_getting_cards_from_api__uses_data_key_for_parsing_records(
    sut: YGOProAPIHandler, cacher: DirectoryCacher, requests
):
    cacher.exists.return_value = False
    requests.get.return_value.json.return_value = {
        "data": [
            {
                "id": -1,
                "name": "name",
                "type": "type",
                "frameType": "frameType",
                "desc": "desc",
            }
        ]
    }

    cards = sut.get_cards()

    assert len(cards) == 1


def test_when_getting_cards_from_api__writes_data_using_buffer(
    sut: YGOProAPIHandler, cacher: DirectoryCacher, requests
):
    cacher.exists.return_value = False
    requests.get.return_value.json.return_value = {
        "data": [
            {
                "id": -1,
                "name": "name",
                "type": "type",
                "frameType": "frameType",
                "desc": "desc",
            }
        ]
    }

    sut.get_cards()

    cacher.open_write_buffer.assert_called_once()


def test_when_making_multiple_requests__sleeps(
    sut: YGOProAPIHandler, cacher: DirectoryCacher, requests, sleep
):
    cacher.exists.return_value = False
    requests.get.return_value.json.return_value = {
        "data": [
            {
                "id": -1,
                "name": "name",
                "type": "type",
                "frameType": "frameType",
                "desc": "desc",
            }
        ]
    }

    for _ in range(10):
        sut.get_cards()

    sleep.assert_called()


def test_when_making_first_request__does_not_sleep(
    sut: YGOProAPIHandler, cacher: DirectoryCacher, requests, sleep
):
    cacher.exists.return_value = False
    requests.get.return_value.json.return_value = {
        "data": [
            {
                "id": -1,
                "name": "name",
                "type": "type",
                "frameType": "frameType",
                "desc": "desc",
            }
        ]
    }

    sut.get_cards()

    sleep.assert_not_called()
