from unittest.mock import Mock
import uuid

import pytest

from app.services import SetDiscoveryService
from app.services.exceptions.set_exceptions import NoSetOptions
from app.models import YugiohSet
from app.models.set_options import DEFAULT_SET_OPTIONS, SetOptions


def yugioh_set() -> YugiohSet:
    card_set = YugiohSet(id=uuid.uuid4(), code="", name="")
    return card_set


def test_when_getting_options_for_set_that_is_explcitly_not_mapped__raises_no_options():
    set_id = "dne"
    sut = SetDiscoveryService({set_id: None})
    card_set = yugioh_set()

    card_set.id = set_id
    card_set.code = set_id

    with pytest.raises(NoSetOptions):
        sut.discover_set_options(card_set)


def test_when_raising_no_set_options__sets_set_id_correctly():
    set_id = "dne"
    sut = SetDiscoveryService({set_id: None})
    card_set = yugioh_set()

    card_set.id = set_id
    card_set.code = set_id

    with pytest.raises(NoSetOptions) as err:
        sut.discover_set_options(card_set)

    assert err.value.set_id == set_id


def test_when_getting_unmapped_set__returns_default_options():
    sut = SetDiscoveryService()
    card_set = yugioh_set()

    options = sut.discover_set_options(card_set)

    assert options is DEFAULT_SET_OPTIONS


def test_when_getting_mapped_set__returns_mapped_options():
    card_set = yugioh_set()
    expected_options = SetOptions(options=[])
    sut = SetDiscoveryService({card_set.code: expected_options})

    actual_options = sut.discover_set_options(card_set)

    assert actual_options is expected_options
