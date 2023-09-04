from unittest.mock import Mock
import pytest
from app.models.gacha_configuration import WeightedCollection, WeightedRarityPool


def test_when_weighted_pool_total_does_not_work__raise_value_error():
    pool = WeightedRarityPool(quantity=1, weights=[])
    with pytest.raises(ValueError):
        pool.pick_weight()


@pytest.fixture()
def random():
    return Mock(name="random")


def test_when_random_selects_less_then_light_weight__picks_light_weight_item(random):
    low_weight = WeightedCollection(cards=[], weight=0.1)
    high_weight = WeightedCollection(cards=[], weight=0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.01
    picked = sut.pick_weight(random_float=random)

    assert picked is low_weight


def test_when_random_selects_exactly_same_as_low_weight_weight__picks_high_weight_item(
    random,
):
    low_weight = WeightedCollection(cards=[], weight=0.1)
    high_weight = WeightedCollection(cards=[], weight=0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.1
    picked = sut.pick_weight(random_float=random)

    assert picked is high_weight


def test_when_random_selects_less_then_light_weight_by_a_single_percentage__picks_light_weight_item(
    random,
):
    low_weight = WeightedCollection(cards=[], weight=0.1)
    high_weight = WeightedCollection(cards=[], weight=0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.09
    picked = sut.pick_weight(random_float=random)

    assert picked is low_weight


def test_when_random_selects_less_then_light_weight_by_two_nines__picks_light_weight_item(
    random,
):
    low_weight = WeightedCollection(cards=[], weight=0.1)
    high_weight = WeightedCollection(cards=[], weight=0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.01
    picked = sut.pick_weight(random_float=random)

    assert picked is low_weight


def test_when_random_selects_less_then_light_weight__picks_light_weight_item(random):
    low_weight = WeightedCollection(cards=[], weight=0.1)
    high_weight = WeightedCollection(cards=[], weight=0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.01
    picked = sut.pick_weight(random_float=random)

    assert picked is low_weight


def test_when_random_selects_gets_one_greater_then_first_percentage_but_less_than_second__returns_second_weight(
    random,
):
    low_weight = WeightedCollection(cards=[], weight=0.1)
    other_low_weight = WeightedCollection(cards=[], weight=0.2)
    high_weight = WeightedCollection(cards=[], weight=0.7)
    sut = WeightedRarityPool(
        quantity=1, weights=[low_weight, high_weight, other_low_weight]
    )
    random.return_value = 0.1
    picked = sut.pick_weight(random_float=random)

    assert picked is other_low_weight


def test_when_random_selects_gets_one_greater_then_first_percentage_but_less_than_second__returns_second_weight(
    random,
):
    low_weight = WeightedCollection(cards=[], weight=0.1)
    other_low_weight = WeightedCollection(cards=[], weight=0.2)
    high_weight = WeightedCollection(cards=[], weight=0.7)
    sut = WeightedRarityPool(
        quantity=1, weights=[low_weight, high_weight, other_low_weight]
    )
    random.return_value = 0.1
    picked = sut.pick_weight(random_float=random)

    assert picked is other_low_weight


def test_when_random_selects_equal_to_second_position__returns_third_weight(
    random,
):
    low_weight = WeightedCollection(cards=[], weight=0.1)
    other_low_weight = WeightedCollection(cards=[], weight=0.2)
    high_weight = WeightedCollection(cards=[], weight=0.7)
    sut = WeightedRarityPool(
        quantity=1, weights=[low_weight, high_weight, other_low_weight]
    )
    random.return_value = 0.3
    picked = sut.pick_weight(random_float=random)

    assert picked is other_low_weight


def test_when_weights_are_greater_than_one__still_selects_weights_properly(random):
    low_weight = WeightedCollection(cards=[], weight=0.16)
    other_low_weight = WeightedCollection(cards=[], weight=0.14285)
    other_lowish_weight = WeightedCollection(cards=[], weight=0.2)
    high_weight = WeightedCollection(cards=[], weight=1)

    random.return_value = 0.5

    sut = WeightedRarityPool(
        quantity=1,
        weights=[low_weight, other_low_weight, other_lowish_weight, high_weight],
    )

    selected = sut.pick_weight(random_float=random)

    assert selected is other_lowish_weight
