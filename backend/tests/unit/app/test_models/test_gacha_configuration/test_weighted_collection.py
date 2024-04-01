from unittest.mock import Mock

import pytest

from app.models import WeightedCollection, YugiohCardInSet
from app.models.exceptions.gacha_exceptions import NotEnoughCards


def card(id):
    return YugiohCardInSet(
        card_id=id, rarity="rarity", rarity_code="code", price="price"
    )


def test_when_collection_has_no_items__raises_not_enough_cards():
    sut = WeightedCollection(cards=[], weight=1)

    with pytest.raises(NotEnoughCards):
        sut.pick()


def test_when_getting_len_of_collection__returns_len_of_underlying_array():
    nested_collection = [card("mania")]
    sut = WeightedCollection(cards=nested_collection, weight=1)

    assert len(sut) == len(nested_collection)


@pytest.fixture
def random():
    return Mock(name="random")


def test_when_picking_card__uses_value_form_random_range_func(random):
    expected_card = card("e")
    random.return_value = 0
    sut = WeightedCollection(
        cards=[expected_card, card("giga"), card("thad")], weight=1
    )

    actual_pick = sut.pick(random_range=random)

    assert actual_pick is expected_card


def test_when_card_is_picked__removes_it_from_underlying_collection(random):
    random.return_value = 0
    sut = WeightedCollection(cards=[card("e"), card("giga"), card("thad")], weight=1)

    actual_pick = sut.pick(random_range=random)

    assert actual_pick not in sut.cards
