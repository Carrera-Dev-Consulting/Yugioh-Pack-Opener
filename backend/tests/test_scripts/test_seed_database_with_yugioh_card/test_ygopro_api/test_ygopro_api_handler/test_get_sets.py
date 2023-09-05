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


def test_when_getting_sets__uses_cached_response(
    cacher: DirectoryCacher, sut: YGOProAPIHandler
):
    cacher.exists.return_value = True
    cacher.read.return_value = [
        {"set_name": "set_name", "set_code": "set_code", "num_of_cards": 69}
    ]
    sets = sut.get_sets()

    assert len(sets) == 1


def test_when_no_entry_exists__parses_response_correctly(
    cacher: DirectoryCacher, sut: YGOProAPIHandler, requests
):
    requests.get.return_value.json.return_value = [
        {"set_name": "set_name", "set_code": "set_code", "num_of_cards": 69}
    ]
    cacher.exists.return_value = False

    sets = sut.get_sets()

    assert len(sets) == 1


def test_when_making_muliple_requests_in_quick_succession__sleeps(
    cacher: DirectoryCacher, sut: YGOProAPIHandler, requests, sleep
):
    cacher.exists.return_value = False
    requests.get.return_value.json.return_value = [
        {"set_name": "set_name", "set_code": "set_code", "num_of_cards": 69}
    ]

    for _ in range(10):  # we should sleep after so many requests
        sut.get_sets()

    sleep.assert_called()


def test_when_making_first_requests__does_not_sleep(
    cacher: DirectoryCacher, sut: YGOProAPIHandler, requests, sleep
):
    cacher.exists.return_value = False
    requests.get.return_value.json.return_value = [
        {"set_name": "set_name", "set_code": "set_code", "num_of_cards": 69}
    ]

    sut.get_sets()

    sleep.assert_not_called()
