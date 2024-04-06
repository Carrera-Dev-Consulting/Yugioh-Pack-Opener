from unittest.mock import Mock
import uuid

import pytest

from app.services import GachaService, SetDiscoveryService
from app.services.exceptions.set_exceptions import InvalidSetOptions

from app.models import (
    YugiohSet,
    YugiohCardInSet,
    SetOptions,
    Option,
    WeightedRarity,
    SingleRarityPool,
    WeightedRarityPool,
)


@pytest.fixture
def set_discovery_service():
    return Mock(spec=SetDiscoveryService)


@pytest.fixture
def sut(set_discovery_service: SetDiscoveryService):
    return GachaService(set_discovery_service)


def card_set(name: str, cards: list[YugiohCardInSet]):
    return YugiohSet(id=uuid.uuid4(), code="code", name=name, cards=cards)


def card(rarity: str, id: str = None):
    return YugiohCardInSet(
        card_id=id or str(uuid.uuid4()),
        price="price is right",
        rarity=rarity,
        rarity_code="code",
    )


def test_when_options_are_basic_creates_configuration_with_correct_objects(
    sut: GachaService,
):
    options = SetOptions(
        options=[
            Option(
                rarity="rarity",
                amount_for=1,
            ),
            Option(rarity="common", amount_for=7),
        ]
    )
    requested_set = card_set(
        name="hemmie",
        cards=[
            card("rarity"),
            card("rarity"),
            card("rarity"),
            card("common"),
            card("common"),
            card("uncommon"),
        ],
    )

    config = sut.build_configuration_from_set_with_options(requested_set, options)

    assert len(config.pools) == 2

    assert all(isinstance(pool, SingleRarityPool) for pool in config.pools)


def test_when_options_have_only_weighted_rules__configuration_returns_with_weighted_pools(
    sut: GachaService,
):
    requested_set = card_set(
        name="hemmie",
        cards=[
            card("common"),
            card("common"),
            card("uncommon"),
        ],
    )

    options = SetOptions(
        options=[
            Option(
                amount_for=1,
                weighted_rarities=[
                    WeightedRarity(rarity="common", weight=1),
                    WeightedRarity(rarity="uncommon", weight=1),
                ],
            )
        ]
    )

    config = sut.build_configuration_from_set_with_options(requested_set, options)

    assert len(config.pools) == 1
    assert all(isinstance(c, WeightedRarityPool) for c in config.pools)


def test_when_give_both_weighted_and_single_rarity_items__returns_correct_pools_accordingly(
    sut: GachaService,
):
    requested_set = card_set(
        name="hemmie",
        cards=[
            card("item"),
            card("item"),
            card("item"),
            card("common"),
            card("common"),
            card("uncommon"),
        ],
    )
    options = SetOptions(
        options=[
            Option(rarity="item", amount_for=2),
            Option(
                amount_for=1,
                weighted_rarities=[
                    WeightedRarity(rarity="common", weight=1),
                    WeightedRarity(rarity="uncommon", weight=1),
                ],
            ),
        ]
    )

    config = sut.build_configuration_from_set_with_options(requested_set, options)

    assert len(config.pools) == 2

    [single, weighted] = config.pools

    assert isinstance(single, SingleRarityPool)
    assert isinstance(weighted, WeightedRarityPool)


def test_when_option_cannot_be_understood__raises_invalid_set_options(
    sut: GachaService,
):
    invalid_opts = SetOptions(options=[Option()])
    requested_set = card_set(
        name="hemmie",
        cards=[
            card("item"),
            card("item"),
            card("item"),
            card("common"),
            card("common"),
            card("uncommon"),
        ],
    )

    with pytest.raises(InvalidSetOptions):
        sut.build_configuration_from_set_with_options(requested_set, invalid_opts)


def test_when_no_cards_found_for_a_rarity__raises_invalid_set_options(
    sut: GachaService,
):
    invalid_opts = SetOptions(options=[Option(rarity="non defined", amount_for=1)])
    requested_set = card_set(
        name="hemmie",
        cards=[
            card("item"),
            card("item"),
            card("item"),
            card("common"),
            card("common"),
            card("uncommon"),
        ],
    )

    with pytest.raises(InvalidSetOptions):
        sut.build_configuration_from_set_with_options(requested_set, invalid_opts)


def test_when_rolling_for_set__build_and_pull_a_gacha_config(sut: GachaService):
    config = Mock(name="gacha_config")
    sut.build_configuration_from_set_with_options = Mock(
        name="GachaService.build_configuration_from_set_with_options"
    )
    sut.build_configuration_from_set_with_options.return_value = config

    sut.roll_for_set(Mock(name="yugioh_set"))

    config.pull.assert_called()
