from scripts.seed_database_with_yugioh_card.ygopro_api import YGOProCard

sut = YGOProCard.model_validate


def test_when_given_ritual_spell_card__parsed_model():
    card = {
        "id": 85327820,
        "name": "A.I.'s Ritual",
        "type": "Spell Card",
        "frameType": "spell",
        "desc": 'This card can be used to Ritual Summon any Cyberse Ritual Monster. You must also Tribute "@Ignister" monsters from your hand or field whose total Levels equal or exceed the Level of the Ritual Monster you Ritual Summon. If you control an "@Ignister" monster when this effect is activated, you can also use "@Ignister" monster(s) in your GY, by banishing them.',
        "race": "Ritual",
        "archetype": "@Ignister",
        "card_sets": [
            {
                "set_name": "2021 Tin of Ancient Battles",
                "set_code": "MP21-EN025",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0.88",
            },
            {
                "set_name": "Ignition Assault",
                "set_code": "IGAS-EN054",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.16",
            },
        ],
        "card_images": [
            {
                "id": 85327820,
                "image_url": "https://images.ygoprodeck.com/images/cards/85327820.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/85327820.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/85327820.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.02",
                "tcgplayer_price": "0.04",
                "ebay_price": "0.99",
                "amazon_price": "0.25",
                "coolstuffinc_price": "0.25",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack is None


def test_when_given_field_spell__parses_into_model_correctly():
    card = {
        "id": 295517,
        "name": "A Legendary Ocean",
        "type": "Spell Card",
        "frameType": "spell",
        "desc": "(This card's name is always treated as \"Umi\".)\r\nAll WATER monsters on the field gain 200 ATK/DEF. Reduce the Level of all WATER monsters in both players' hands and on the field by 1.",
        "race": "Field",
        "archetype": "Umi",
        "card_sets": [
            {
                "set_name": "Dark Beginning 2",
                "set_code": "DB-EN66",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0",
            },
            {
                "set_name": "Dark Beginning 2",
                "set_code": "DB2-EN187",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.48",
            },
            {
                "set_name": "Hobby League 1 participation cards B",
                "set_code": "HL1-EN003",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "11.44",
            },
            {
                "set_name": "Legacy of Darkness",
                "set_code": "LOD-078",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.48",
            },
            {
                "set_name": "Legacy of Darkness",
                "set_code": "LOD-EN078",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "12.87",
            },
            {
                "set_name": "Legendary Duelists",
                "set_code": "LEDU-EN021",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.28",
            },
            {
                "set_name": "Legendary Duelists: Season 1",
                "set_code": "LDS1-EN029",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.12",
            },
            {
                "set_name": "Magnificent Mavens",
                "set_code": "MAMA-EN079",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "0",
            },
            {
                "set_name": "Realm of the Sea Emperor Structure Deck",
                "set_code": "SDRE-EN024",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.25",
            },
            {
                "set_name": "Retro Pack 2",
                "set_code": "RP02-EN062",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.64",
            },
            {
                "set_name": "Speed Duel GX: Midterm Paradox",
                "set_code": "SGX2-ENC13",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0",
            },
            {
                "set_name": "Structure Deck: Fury from the Deep",
                "set_code": "SD4-EN020",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.24",
            },
        ],
        "card_images": [
            {
                "id": 295517,
                "image_url": "https://images.ygoprodeck.com/images/cards/295517.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/295517.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/295517.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.12",
                "tcgplayer_price": "0.17",
                "ebay_price": "0.99",
                "amazon_price": "1.33",
                "coolstuffinc_price": "0.49",
            }
        ],
    }

    parsed = sut(card)

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

    parsed = sut(card)

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

    parsed = sut(card)

    assert parsed.attack is None, "Attack was set"


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

    parsed = sut(card)

    assert parsed.attack is None, "Attack was set"


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

    parsed = sut(card)
    assert parsed.attack is None, "Value was set for spell card"
