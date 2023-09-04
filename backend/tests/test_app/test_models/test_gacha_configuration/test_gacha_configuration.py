from unittest.mock import Mock

import pytest

from app.models import GachaConfiguration, Pool


def pool() -> Pool:
    mock = Mock(spec=Pool)
    mock.pull.return_value = []
    return mock


def test_when_pulling__returns_what_each_pull_had():
    first_pool = pool()
    second_pool = pool()

    sut = GachaConfiguration(pools=[first_pool, second_pool])

    sut.pull()

    first_pool.pull.assert_called()
    second_pool.pull.assert_called()


def card(id: str):
    mock = Mock(name=f"Card(id={id})")
    mock.card_id = id
    return mock


def test_when_pulling__aggregates_all_cards_from_a_pull_from_each_pool():
    expected_cards = ["billy", "jean", "is", "not", "my", "lover"]
    first_pool = pool()
    first_pool.pull.return_value = [card("billy"), card("jean")]
    second_pool = pool()
    second_pool.pull.return_value = [card("is"), card("not"), card("my"), card("lover")]

    sut = GachaConfiguration(pools=[first_pool, second_pool])

    pull = sut.pull()

    assert pull.results == expected_cards
