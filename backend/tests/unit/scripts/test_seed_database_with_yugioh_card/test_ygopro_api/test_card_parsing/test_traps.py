from scripts.seed_database_with_yugioh_card.ygopro_api import YGOProCard

sut = YGOProCard.model_validate


def test_when_given_continous_trap_card__parses_into_model():
    card = {
        "id": 28645123,
        "name": "A.I. Challenge You",
        "type": "Trap Card",
        "frameType": "trap",
        "desc": 'Monsters your opponent controls lose 100 ATK for each card you control. If your "@Ignister" monster battles, your opponent cannot activate cards or effects until the end of the Damage Step. When your "@Ignister" monster is destroyed by battle: You can target 1 other Cyberse monster with 2300 ATK in your GY; Special Summon it. You can only use this effect of "A.I. Challenge You" once per turn.',
        "race": "Continuous",
        "archetype": "A.I.",
        "card_sets": [
            {
                "set_name": "Lightning Overdrive",
                "set_code": "LIOV-EN076",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0.85",
            }
        ],
        "card_images": [
            {
                "id": 28645123,
                "image_url": "https://images.ygoprodeck.com/images/cards/28645123.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/28645123.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/28645123.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.09",
                "tcgplayer_price": "0.10",
                "ebay_price": "0.99",
                "amazon_price": "0.59",
                "coolstuffinc_price": "0.49",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack is None


def test_when_given_normal_trap_card__parses_into_model_correctly():
    card = {
        "id": 68170903,
        "name": "A Feint Plan",
        "type": "Trap Card",
        "frameType": "trap",
        "desc": "A player cannot attack face-down monsters during this turn.",
        "race": "Normal",
        "card_sets": [
            {
                "set_name": "Legacy of Darkness",
                "set_code": "LOD-032",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.23",
            },
            {
                "set_name": "Legacy of Darkness",
                "set_code": "LOD-EN032",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "2.9",
            },
        ],
        "card_images": [
            {
                "id": 68170903,
                "image_url": "https://images.ygoprodeck.com/images/cards/68170903.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/68170903.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/68170903.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.14",
                "tcgplayer_price": "0.18",
                "ebay_price": "1.50",
                "amazon_price": "0.29",
                "coolstuffinc_price": "0.25",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack is None, "Attack was set"


def test_when_given_counter_trap_card__parses_into_model_correctly():
    card = {
        "id": 45730592,
        "name": "Adamancipator Resonance",
        "type": "Trap Card",
        "frameType": "trap",
        "desc": 'When a monster effect is activated, while you control an "Adamancipator" Synchro Monster: Negate the activation, and if you do, destroy it.',
        "race": "Counter",
        "archetype": "Adamancipator",
        "card_sets": [
            {
                "set_name": "2021 Tin of Ancient Battles",
                "set_code": "MP21-EN236",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.03",
            },
            {
                "set_name": "Secret Slayers",
                "set_code": "SESL-EN013",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "1.34",
            },
        ],
        "card_images": [
            {
                "id": 45730592,
                "image_url": "https://images.ygoprodeck.com/images/cards/45730592.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/45730592.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/45730592.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.06",
                "tcgplayer_price": "0.10",
                "ebay_price": "2.00",
                "amazon_price": "0.25",
                "coolstuffinc_price": "0.39",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack is None
