from unittest.mock import Mock
import pytest
from app.models import WeightedCollection, WeightedRarityPool, YugiohCardInSet
from app.models.exceptions.gacha_exceptions import InvalidPool, NotEnoughCards


def test_when_weighted_pool_total_does_not_work__raise_value_error():
    pool = WeightedRarityPool(quantity=1, weights=[])
    with pytest.raises(InvalidPool):
        pool.pick_weight()


@pytest.fixture()
def random():
    return Mock(name="random")


def card(id):
    return YugiohCardInSet(
        card_id=id, rarity="rarity", rarity_code="code", price="price"
    )


def weighted_collection(weight: float, cards: list[YugiohCardInSet] = None):
    cards = cards if cards is not None else [card("default")]
    return WeightedCollection(cards=cards, weight=weight)


def test_when_random_selects_less_then_light_weight__picks_light_weight_item(random):
    low_weight = weighted_collection(0.1)
    high_weight = weighted_collection(0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.01
    picked = sut.pick_weight(random_float=random)

    assert picked is low_weight


def test_when_random_selects_exactly_same_as_low_weight_weight__picks_high_weight_item(
    random,
):
    low_weight = weighted_collection(0.1)
    high_weight = weighted_collection(0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.1
    picked = sut.pick_weight(random_float=random)

    assert picked is high_weight


def test_when_random_selects_less_then_light_weight_by_a_single_percentage__picks_light_weight_item(
    random,
):
    low_weight = weighted_collection(0.1)
    high_weight = weighted_collection(0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.09
    picked = sut.pick_weight(random_float=random)

    assert picked is low_weight


def test_when_random_selects_less_then_light_weight_by_two_nines__picks_light_weight_item(
    random,
):
    low_weight = weighted_collection(0.1)
    high_weight = weighted_collection(0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.01
    picked = sut.pick_weight(random_float=random)

    assert picked is low_weight


def test_when_random_selects_less_then_light_weight__picks_light_weight_item(random):
    low_weight = weighted_collection(0.1)
    high_weight = weighted_collection(0.9)
    sut = WeightedRarityPool(quantity=1, weights=[low_weight, high_weight])
    random.return_value = 0.01
    picked = sut.pick_weight(random_float=random)

    assert picked is low_weight


def test_when_random_selects_gets_one_greater_then_first_percentage_but_less_than_second__returns_second_weight(
    random,
):
    low_weight = weighted_collection(0.1)
    other_low_weight = weighted_collection(0.2)
    high_weight = weighted_collection(0.7)
    sut = WeightedRarityPool(
        quantity=1, weights=[low_weight, high_weight, other_low_weight]
    )
    random.return_value = 0.1
    picked = sut.pick_weight(random_float=random)

    assert picked is other_low_weight


def test_when_random_selects_gets_one_greater_then_first_percentage_but_less_than_second__returns_second_weight(
    random,
):
    low_weight = weighted_collection(0.1)
    other_low_weight = weighted_collection(0.2)
    high_weight = weighted_collection(0.7)
    sut = WeightedRarityPool(
        quantity=1, weights=[low_weight, high_weight, other_low_weight]
    )
    random.return_value = 0.1
    picked = sut.pick_weight(random_float=random)

    assert picked is other_low_weight


def test_when_random_selects_equal_to_second_position__returns_third_weight(
    random,
):
    low_weight = weighted_collection(0.1)
    other_low_weight = weighted_collection(0.2)
    high_weight = weighted_collection(0.7)
    sut = WeightedRarityPool(
        quantity=1, weights=[low_weight, high_weight, other_low_weight]
    )
    random.return_value = 0.3
    picked = sut.pick_weight(random_float=random)

    assert picked is other_low_weight


def test_when_weights_are_greater_than_one__still_selects_weights_properly(random):
    low_weight = weighted_collection(0.16)
    other_low_weight = weighted_collection(0.14285)
    other_lowish_weight = weighted_collection(0.2)
    high_weight = weighted_collection(1)

    random.return_value = 0.5

    sut = WeightedRarityPool(
        quantity=1,
        weights=[low_weight, other_low_weight, other_lowish_weight, high_weight],
    )

    selected = sut.pick_weight(random_float=random)

    assert selected is other_lowish_weight


def test_when_last_empty_pool_is_removed__raises_invalid_pool(random):
    weight = weighted_collection(1, cards=[])
    sut = WeightedRarityPool(quantity=1, weights=[weight])
    random.return_value = 0.5

    with pytest.raises(InvalidPool):
        sut.pick_weight(random_float=random)


def test_when_pool_is_empty__returns_non_empty_pool(random):
    weight = weighted_collection(1, cards=[])
    expected_weight = weighted_collection(0.1)
    sut = WeightedRarityPool(quantity=1, weights=[weight, expected_weight])
    random.side_effect = [0.5, 0]

    actual_weight = sut.pick_weight(random_float=random)

    assert actual_weight is expected_weight


def test_when_generating_a_pull_and_not_enough_items_to_meet_required_amount__raises_not_enough_cards():
    sut = WeightedRarityPool(quantity=2, weights=[weighted_collection(1)])
    with pytest.raises(NotEnoughCards):
        sut.pull()


def test_when_pulling_from_pool_without_any_individual_weight_more_than_others__pulls_from_every_pool_available():
    cards = [card("this"), card("magic"), card("moment")]
    sut = WeightedRarityPool(
        quantity=3,
        weights=[
            weighted_collection(1, cards=cards[0:1]),
            weighted_collection(1, cards=cards[1:]),
        ],
    )

    items = sut.pull()

    def sort_by_id(a: YugiohCardInSet):
        return a.card_id

    items.sort(key=sort_by_id)
    cards.sort(key=sort_by_id)
    assert items == cards


@pytest.fixture
def random_range():
    return Mock(name="random_range")


def test_when_pulling_from_pool__selects_weight_based_on_random_float(
    random, random_range
):
    expected = card("this")
    sut = WeightedRarityPool(
        quantity=1,
        weights=[
            weighted_collection(1, cards=[expected]),
            weighted_collection(1, cards=[card("magic"), card("moment")]),
        ],
    )

    random.return_value = 0.5
    random_range.return_value = 0

    [selected_card] = sut.pull(random_float=random, random_range=random_range)

    assert selected_card == expected


def test_when_pulling_multiple_times__pulls_are_unique():
    sut = WeightedRarityPool(
        quantity=1,
        weights=[
            weighted_collection(
                1, cards=[card("items"), card("this magic moment"), card("other")]
            ),
            weighted_collection(1, cards=[card("trunks")]),
        ],
    )

    first = sut.pull()
    second = sut.pull()

    assert first != second
