from copy import deepcopy

import pytest

from app.repository.models.yugioh_card_orm import YugiohCardORM
from app.repository.models.yugioh_set_orm import YugiohSetORM
from scripts.seed_database_with_yugioh_card.db_layer import map_ygopro_to_orm
from scripts.seed_database_with_yugioh_card.ygopro_api import YGOProCard, YGOProSet


card = {
    "id": 76080032,
    "name": "ZW - Unicorn Spear",
    "type": "Effect Monster",
    "frameType": "effect",
    "desc": 'You can target 1 "Number C39: Utopia Ray" you control; equip this card from your hand to that target. It gains 1900 ATK. If the equipped monster battles an opponent\'s monster, the opponent\'s monster\'s effect is negated during the Battle Phase only. You can only control 1 "ZW - Unicorn Spear".',
    "atk": 1900,
    "def": 0,
    "level": 4,
    "race": "Beast",
    "attribute": "LIGHT",
    "archetype": "Utopia",
    "card_sets": [
        {
            "set_name": "Order of Chaos",
            "set_code": "ORCS-EN005",
            "set_rarity": "Rare",
            "set_rarity_code": "(R)",
            "set_price": "2.19",
        },
        {
            "set_name": "Star Pack 2014",
            "set_code": "SP14-EN004",
            "set_rarity": "Common",
            "set_rarity_code": "(C)",
            "set_price": "1.54",
        },
        {
            "set_name": "Star Pack 2014",
            "set_code": "SP14-EN004",
            "set_rarity": "Starfoil Rare",
            "set_rarity_code": "(SFR)",
            "set_price": "1.48",
        },
        {
            "set_name": "Super Starter: V for Victory",
            "set_code": "YS13-EN018",
            "set_rarity": "Common",
            "set_rarity_code": "(C)",
            "set_price": "1.12",
        },
    ],
    "card_images": [
        {
            "id": 76080032,
            "image_url": "https://images.ygoprodeck.com/images/cards/76080032.jpg",
            "image_url_small": "https://images.ygoprodeck.com/images/cards_small/76080032.jpg",
            "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/76080032.jpg",
        }
    ],
    "card_prices": [
        {
            "cardmarket_price": "0.09",
            "tcgplayer_price": "0.23",
            "ebay_price": "0.99",
            "amazon_price": "0.25",
            "coolstuffinc_price": "0.39",
        }
    ],
}


def test_when_parsing_card_to_orm__it_parses_all_fields():
    raw_card = deepcopy(card)
    model = YGOProCard.model_validate(raw_card)
    attack = raw_card.get("atk")
    assert (
        model.attack == attack
    ), f"Expected fields to be mapped correctly, actual={model.attack}, expected={attack}"

    orm: YugiohCardORM = map_ygopro_to_orm(model)

    assert orm.attack == model.attack, "We are not setting the fields for attack cards"


card_set = {
    "set_name": "Zombie World Structure Deck",
    "set_code": "SDZW",
    "num_of_cards": 37,
    "tcg_date": "2008-10-21",
    "set_image": "https://images.ygoprodeck.com/images/sets/SDZW.jpg",
}


def test_when_parsing_set_to_orm__it_parses_all_fields():
    raw_set = deepcopy(card_set)
    model = YGOProSet.model_validate(raw_set)

    set_id = raw_set.get("set_code")

    orm: YugiohSetORM = map_ygopro_to_orm(model)

    assert (
        orm.set_id == set_id
    ), f"Did not set the id as expected: actual{orm.set_id}, expected={set_id}"


def test_when_parsing_arbitrary_obj_to_orm__raises_not_value_error():
    with pytest.raises(ValueError):
        map_ygopro_to_orm(object())
