from scripts.seed_database_with_yugioh_card.ygopro_api import YGOProCard


def test_when_given_normal_spell_card__parses_value_into_card_model():
    card = {
        "id": 44256816,
        "name": "1st Movement Solo",
        "type": "Spell Card",
        "frameType": "spell",
        "desc": 'If you control no monsters: Special Summon 1 Level 4 or lower "Melodious" monster from your hand or Deck. You can only activate 1 "1st Movement Solo" per turn. You cannot Special Summon monsters during the turn you activate this card, except "Melodious" monsters.',
        "race": "Normal",
        "archetype": "Melodious",
        "card_sets": [
            {
                "set_name": "2015 Mega-Tin Mega Pack",
                "set_code": "MP15-EN169",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "2.99",
            },
            {
                "set_name": "The New Challengers",
                "set_code": "NECH-EN059",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "3.04",
            },
            {
                "set_name": "The New Challengers: Super Edition",
                "set_code": "NECH-ENS10",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "17.04",
            },
        ],
        "card_images": [
            {
                "id": 44256816,
                "image_url": "https://images.ygoprodeck.com/images/cards/44256816.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/44256816.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/44256816.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "3.26",
                "tcgplayer_price": "1.03",
                "ebay_price": "3.50",
                "amazon_price": "2.19",
                "coolstuffinc_price": "1.99",
            }
        ],
    }

    parsed = YGOProCard.model_validate(card)
    assert parsed.attack is None, "Value was set for spell card"


def test_when_given_continous_spell_card__parses_model_correctly():
    card = {
        "id": 34541863,
        "name": '"A" Cell Breeding Device',
        "type": "Spell Card",
        "frameType": "spell",
        "desc": "During each of your Standby Phases, put 1 A-Counter on 1 face-up monster your opponent controls.",
        "race": "Continuous",
        "archetype": "Alien",
        "card_sets": [
            {
                "set_name": "Force of the Breaker",
                "set_code": "FOTB-EN043",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.31",
            }
        ],
        "card_images": [
            {
                "id": 34541863,
                "image_url": "https://images.ygoprodeck.com/images/cards/34541863.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/34541863.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/34541863.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "1.97",
                "tcgplayer_price": "0.18",
                "ebay_price": "0.99",
                "amazon_price": "24.45",
                "coolstuffinc_price": "0.25",
            }
        ],
    }

    parsed = YGOProCard.model_validate(card)

    assert parsed.attack is None, "Attack was set"


def test_when_given_quick_play_spell_card__parses_into_model_correctly():
    card = {
        "id": 91231901,
        "name": '"A" Cell Recombination Device',
        "type": "Spell Card",
        "frameType": "spell",
        "desc": 'Target 1 face-up monster on the field; send 1 "Alien" monster from your Deck to the Graveyard, and if you do, place A-Counters on that monster equal to the Level of the sent monster. During your Main Phase, except the turn this card was sent to the Graveyard: You can banish this card from your Graveyard; add 1 "Alien" monster from your Deck to your hand.',
        "race": "Quick-Play",
        "archetype": "Alien",
        "card_sets": [
            {
                "set_name": "Invasion: Vengeance",
                "set_code": "INOV-EN063",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.12",
            }
        ],
        "card_images": [
            {
                "id": 91231901,
                "image_url": "https://images.ygoprodeck.com/images/cards/91231901.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/91231901.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/91231901.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.11",
                "tcgplayer_price": "0.20",
                "ebay_price": "0.99",
                "amazon_price": "0.50",
                "coolstuffinc_price": "0.49",
            }
        ],
    }

    parsed = YGOProCard.model_validate(card)

    assert parsed.attack is None, "Attack was set"


def test_when_given_equip_spell__parses_into_model_correctly():
    card = {
        "id": 98319530,
        "name": '"Infernoble Arms - Almace"',
        "type": "Spell Card",
        "frameType": "spell",
        "desc": 'While this card is equipped to a monster: You can equip 1 "Infernoble Arms" Equip Spell from your Deck or GY to 1 appropriate monster you control, except ""Infernoble Arms - Almace"", then destroy this card. If this card is sent to the GY because the equipped monster is sent to the GY: You can target 1 of your FIRE Warrior monsters that is banished or in your GY; add it to your hand. You can only use 1 ""Infernoble Arms - Almace"" effect per turn, and only once that turn.',
        "race": "Equip",
        "archetype": "Noble Knight",
        "card_sets": [
            {
                "set_name": "Duelist Nexus",
                "set_code": "DUNE-EN056",
                "set_rarity": "Quarter Century Secret Rare",
                "set_rarity_code": "",
                "set_price": "0",
            },
            {
                "set_name": "Duelist Nexus",
                "set_code": "DUNE-EN056",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "0",
            },
        ],
        "card_images": [
            {
                "id": 98319530,
                "image_url": "https://images.ygoprodeck.com/images/cards/98319530.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/98319530.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/98319530.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.00",
                "tcgplayer_price": "1.93",
                "ebay_price": "0.00",
                "amazon_price": "0.00",
                "coolstuffinc_price": "0.00",
            }
        ],
    }

    parsed = YGOProCard.model_validate(card)

    assert parsed.attack is None, "Attack was set"


def test_when_given_an_effect_monster__parses_into_model_correctly():
    card = {
        "id": 86988864,
        "name": "3-Hump Lacooda",
        "type": "Effect Monster",
        "frameType": "effect",
        "desc": 'If there are 3 face-up "3-Hump Lacooda" cards on your side of the field, Tribute 2 of them to draw 3 cards.',
        "atk": 500,
        "def": 1500,
        "level": 3,
        "race": "Beast",
        "attribute": "EARTH",
        "card_sets": [
            {
                "set_name": "Ancient Sanctuary",
                "set_code": "AST-070",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.07",
            },
            {
                "set_name": "Dark Revelation Volume 2",
                "set_code": "DR2-EN183",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.24",
            },
        ],
        "card_images": [
            {
                "id": 86988864,
                "image_url": "https://images.ygoprodeck.com/images/cards/86988864.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/86988864.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/86988864.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.12",
                "tcgplayer_price": "0.22",
                "ebay_price": "1.00",
                "amazon_price": "0.25",
                "coolstuffinc_price": "0.25",
            }
        ],
    }

    parsed = YGOProCard.model_validate(card)

    assert parsed.desc is not None, "Description was not set"
    assert parsed.attack is not None, "Attack was not set"
    assert parsed.level is not None, "Level was not set"


def test_when_given_a_normal_monster__parses_into_model_correctly():
    card = {
        "id": 11714098,
        "name": "30,000-Year White Turtle",
        "type": "Normal Monster",
        "frameType": "normal",
        "desc": "A huge turtle that has existed for more than 30,000 years.",
        "atk": 1250,
        "def": 2100,
        "level": 5,
        "race": "Aqua",
        "attribute": "WATER",
        "card_images": [
            {
                "id": 11714098,
                "image_url": "https://images.ygoprodeck.com/images/cards/11714098.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/11714098.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/11714098.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.00",
                "tcgplayer_price": "0.00",
                "ebay_price": "10.00",
                "amazon_price": "0.50",
                "coolstuffinc_price": "0.00",
            }
        ],
    }

    parsed = YGOProCard.model_validate(card)

    assert parsed.attack is not None, "Attack was not set"
    assert parsed.defense is not None, "Defense was not set"
    assert parsed.level is not None, "Level was not set"


def test_when_given_flip_effect_monster__parses_into_model():
    card = {
        "id": 83994646,
        "name": "4-Starred Ladybug of Doom",
        "type": "Flip Effect Monster",
        "frameType": "effect",
        "desc": "FLIP: Destroy all Level 4 monsters your opponent controls.",
        "atk": 800,
        "def": 1200,
        "level": 3,
        "race": "Insect",
        "attribute": "WIND",
        "card_sets": [
            {
                "set_name": "Dark Beginning 1",
                "set_code": "DB1-EN198",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.18",
            },
            {
                "set_name": "Pharaoh's Servant",
                "set_code": "PSV-088",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.28",
            },
            {
                "set_name": "Pharaoh's Servant",
                "set_code": "PSV-E088",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0.00",
            },
            {
                "set_name": "Pharaoh's Servant",
                "set_code": "PSV-EN088",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0.00",
            },
            {
                "set_name": "Retro Pack 2",
                "set_code": "RP02-EN022",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.27",
            },
            {
                "set_name": "Starter Deck: Yugi Reloaded",
                "set_code": "YSYR-EN010",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.38",
            },
        ],
        "card_images": [
            {
                "id": 83994646,
                "image_url": "https://images.ygoprodeck.com/images/cards/83994646.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/83994646.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/83994646.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.07",
                "tcgplayer_price": "0.05",
                "ebay_price": "0.99",
                "amazon_price": "0.99",
                "coolstuffinc_price": "0.39",
            }
        ],
    }

    parsed = YGOProCard.model_validate(card)

    assert parsed


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

    parsed = YGOProCard.model_validate(card)

    assert parsed.attack is None, "Attack was set"
