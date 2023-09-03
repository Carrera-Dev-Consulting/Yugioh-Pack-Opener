from scripts.seed_database_with_yugioh_card.ygopro_api import YGOProCard

sut = YGOProCard.model_validate


def test_when_given_pendulumn_effect_monster__parses_model_correctly():
    card = {
        "id": 15308295,
        "name": "Abyss Actor - Comic Relief",
        "type": "Pendulum Effect Monster",
        "frameType": "effect_pendulum",
        "desc": '[ Pendulum Effect ] You can target 1 "Abyss Actor" Pendulum Monster you control and 1 monster your opponent controls; switch control of both monsters, then destroy this card. You can only use this effect of "Abyss Actor - Comic Relief" once per turn.\n[ Monster Effect ] You take no battle damage from attacks involving this card. Once per turn, during your Standby Phase: Give control of this card to your opponent. Once per turn, if control of this face-up card changes: Activate this effect; the owner of this card can destroy 1 Set "Abyss Script" Spell in their Spell & Trap Zone.',
        "atk": 1000,
        "def": 2000,
        "level": 3,
        "race": "Fiend",
        "attribute": "DARK",
        "archetype": "Abyss Actor",
        "scale": 8,
        "card_sets": [
            {
                "set_name": "Legendary Duelists: Season 2",
                "set_code": "LDS2-EN061",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.05",
            },
            {
                "set_name": "Legendary Duelists: White Dragon Abyss",
                "set_code": "LED3-EN046",
                "set_rarity": "Rare",
                "set_rarity_code": "(R)",
                "set_price": "1.25",
            },
        ],
        "card_images": [
            {
                "id": 15308295,
                "image_url": "https://images.ygoprodeck.com/images/cards/15308295.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/15308295.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/15308295.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.09",
                "tcgplayer_price": "0.17",
                "ebay_price": "0.99",
                "amazon_price": "0.25",
                "coolstuffinc_price": "0.25",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 1000


def test_when_given_union_effect_monster__parses_into_model_correctly():
    card = {
        "id": 30012506,
        "name": "A-Assault Core",
        "type": "Union Effect Monster",
        "frameType": "effect",
        "desc": "Once per turn, you can either: Target 1 LIGHT Machine monster you control; equip this card to that target, OR: Unequip this card and Special Summon it. A monster equipped with this card is unaffected by your opponent's monster effects (except its own), also if the equipped monster would be destroyed by battle or card effect, destroy this card instead. If this card is sent from the field to the GY: You can add 1 other Union monster from your GY to your hand.",
        "atk": 1900,
        "def": 200,
        "level": 4,
        "race": "Machine",
        "attribute": "LIGHT",
        "archetype": "ABC",
        "card_sets": [
            {
                "set_name": "Legendary Collection Kaiba Mega Pack",
                "set_code": "LCKC-EN019",
                "set_rarity": "Secret Rare",
                "set_rarity_code": "(ScR)",
                "set_price": "3.79",
            },
            {
                "set_name": "Structure Deck: Seto Kaiba",
                "set_code": "SDKS-EN001",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "2.2",
            },
        ],
        "card_images": [
            {
                "id": 30012506,
                "image_url": "https://images.ygoprodeck.com/images/cards/30012506.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/30012506.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/30012506.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.98",
                "tcgplayer_price": "0.75",
                "ebay_price": "1.99",
                "amazon_price": "3.31",
                "coolstuffinc_price": "1.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 1900


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

    parsed = sut(card)

    assert parsed


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

    parsed = sut(card)

    assert parsed.attack is not None, "Attack was not set"
    assert parsed.defense is not None, "Defense was not set"
    assert parsed.level is not None, "Level was not set"


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

    parsed = sut(card)

    assert parsed.desc is not None, "Description was not set"
    assert parsed.attack is not None, "Attack was not set"
    assert parsed.level is not None, "Level was not set"


def test_when_given_tuner_monster__parses_into_model_correctly():
    card = {
        "id": 11302671,
        "name": "Adamancipator Analyzer",
        "type": "Tuner Monster",
        "frameType": "effect",
        "desc": 'If only your opponent controls a monster: You can Special Summon this card from your hand. During your Main Phase: You can excavate the top 5 cards of your Deck, and if you do, you can Special Summon 1 excavated Level 4 or lower non-Tuner Rock monster, also place the rest on the bottom of your Deck in any order. You can only use each effect of "Adamancipator Analyzer" once per turn.',
        "atk": 1500,
        "def": 700,
        "level": 4,
        "race": "Rock",
        "attribute": "EARTH",
        "archetype": "Adamancipator",
        "card_sets": [
            {
                "set_name": "2021 Tin of Ancient Battles",
                "set_code": "MP21-EN226",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "1.32",
            },
            {
                "set_name": "Secret Slayers",
                "set_code": "SESL-EN003",
                "set_rarity": "Secret Rare",
                "set_rarity_code": "(ScR)",
                "set_price": "2.44",
            },
        ],
        "card_images": [
            {
                "id": 11302671,
                "image_url": "https://images.ygoprodeck.com/images/cards/11302671.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/11302671.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/11302671.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.20",
                "tcgplayer_price": "0.13",
                "ebay_price": "0.99",
                "amazon_price": "0.99",
                "coolstuffinc_price": "0.79",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 1500


def test_when_given_gemini_monster__parses_into_model_correctly():
    card = {
        "id": 38468214,
        "name": "Alien Hypno",
        "type": "Gemini Monster",
        "frameType": "effect",
        "desc": "This card is treated as a Normal Monster while face-up on the field or in the Graveyard. While this card is face-up on the field, you can Normal Summon it to have it be treated as an Effect Monster with this effect:\n\u25cf During your Main Phase, you can select 1 monster your opponent controls with an A-Counter(s), and take control of it while this card is on the field. During each of your End Phases, remove 1 A-Counter from each controlled monster. If all A-Counters are removed from one of these monsters, destroy it.",
        "atk": 1600,
        "def": 700,
        "level": 4,
        "race": "Reptile",
        "attribute": "WATER",
        "archetype": "Alien",
        "card_sets": [
            {
                "set_name": "Gladiator's Assault",
                "set_code": "GLAS-EN035",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.49",
            }
        ],
        "card_images": [
            {
                "id": 38468214,
                "image_url": "https://images.ygoprodeck.com/images/cards/38468214.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/38468214.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/38468214.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.29",
                "tcgplayer_price": "0.55",
                "ebay_price": "1.00",
                "amazon_price": "1.18",
                "coolstuffinc_price": "0.49",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.level == 4


def test_when_given_normal_tuner_monster__parses_into_model_correctly():
    card = {
        "id": 40155554,
        "name": "Ally Mind",
        "type": "Normal Tuner Monster",
        "frameType": "normal",
        "desc": "A high-performance unit developed to enhance the Artificial Intelligence program of the Allies of Justice. Loaded with elements collected from a meteor found in the Worm Nebula, it allows for highly tuned processing. But its full capacity is not yet determined.",
        "atk": 1800,
        "def": 1400,
        "level": 5,
        "race": "Machine",
        "attribute": "DARK",
        "archetype": "Ally of Justice",
        "card_sets": [
            {
                "set_name": "Duel Terminal 2",
                "set_code": "DT02-EN023",
                "set_rarity": "Duel Terminal Normal Parallel Rare",
                "set_rarity_code": "(DNPR)",
                "set_price": "1.47",
            },
            {
                "set_name": "Hidden Arsenal 2",
                "set_code": "HA02-EN017",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "1.26",
            },
            {
                "set_name": "Hidden Arsenal: Chapter 1",
                "set_code": "HAC1-EN077",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.02",
            },
            {
                "set_name": "Hidden Arsenal: Chapter 1",
                "set_code": "HAC1-EN077",
                "set_rarity": "Duel Terminal Normal Parallel Rare",
                "set_rarity_code": "(DNPR)",
                "set_price": "1.02",
            },
        ],
        "card_images": [
            {
                "id": 40155554,
                "image_url": "https://images.ygoprodeck.com/images/cards/40155554.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/40155554.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/40155554.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.05",
                "tcgplayer_price": "0.03",
                "ebay_price": "0.99",
                "amazon_price": "0.25",
                "coolstuffinc_price": "0.25",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.level == 5


def test_when_given_spirit_monster__parses_into_model_correctly():
    card = {
        "id": 32181268,
        "name": "Amano-Iwato",
        "type": "Spirit Monster",
        "frameType": "effect",
        "desc": "Cannot be Special Summoned. Monsters cannot activate their effects, except Spirit monsters. Once per turn, during the End Phase, if this card was Normal Summoned or flipped face-up this turn: Return this card to the hand.",
        "atk": 1900,
        "def": 1200,
        "level": 4,
        "race": "Rock",
        "attribute": "EARTH",
        "card_sets": [
            {
                "set_name": "2018 Mega-Tin Mega Pack",
                "set_code": "MP18-EN125",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.51",
            },
            {
                "set_name": "Circuit Break",
                "set_code": "CIBR-EN036",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.46",
            },
        ],
        "card_images": [
            {
                "id": 32181268,
                "image_url": "https://images.ygoprodeck.com/images/cards/32181268.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/32181268.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/32181268.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.19",
                "tcgplayer_price": "0.59",
                "ebay_price": "2.00",
                "amazon_price": "1.00",
                "coolstuffinc_price": "0.79",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 1900


def test_when_given_ritual_effect_monster__parses_into_model_correctly():
    card = {
        "id": 98287529,
        "name": "Amorphactor Pain, the Imagination Dracoverlord",
        "type": "Ritual Effect Monster",
        "frameType": "ritual",
        "desc": 'You can Ritual Summon this card with "Amorphous Persona". If this card is Ritual Summoned: Your opponent skips their next Main Phase 1. Negate the effects of face-up Fusion, Synchro, and Xyz Monsters while they are on the field. If this card is sent from the field to the Graveyard: You can add 1 "Dracoverlord" monster from your Deck to your hand, except "Amorphactor Pain, the Imagination Dracoverlord".',
        "atk": 2950,
        "def": 2500,
        "level": 8,
        "race": "Dragon",
        "attribute": "EARTH",
        "archetype": "Dracoverlord",
        "card_sets": [
            {
                "set_name": "OTS Tournament Pack 15",
                "set_code": "OP15-EN021",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.25",
            },
            {
                "set_name": "OTS Tournament Pack 15 (POR)",
                "set_code": "OP15-PT021",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0",
            },
            {
                "set_name": "Shining Victories",
                "set_code": "SHVI-EN044",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "2.74",
            },
        ],
        "card_images": [
            {
                "id": 98287529,
                "image_url": "https://images.ygoprodeck.com/images/cards/98287529.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/98287529.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/98287529.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.15",
                "tcgplayer_price": "0.25",
                "ebay_price": "2.50",
                "amazon_price": "1.01",
                "coolstuffinc_price": "1.49",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 2950


def test_when_given_ritual_monster__parses_into_model_correctly():
    card = {
        "id": 5405694,
        "name": "Black Luster Soldier",
        "type": "Ritual Monster",
        "frameType": "ritual",
        "desc": 'You can Ritual Summon this card with "Black Luster Ritual".',
        "atk": 3000,
        "def": 2500,
        "level": 8,
        "race": "Warrior",
        "attribute": "EARTH",
        "archetype": "Black Luster Soldier",
        "card_sets": [
            {
                "set_name": "Duel Terminal 7a",
                "set_code": "DT07-EN030",
                "set_rarity": "Duel Terminal Rare Parallel Rare",
                "set_rarity_code": "(DRPR)",
                "set_price": "18.08",
            },
            {
                "set_name": "Duelist Pack: Battle City",
                "set_code": "DPBC-EN006",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "3.88",
            },
            {
                "set_name": "Duelist Pack: Yugi",
                "set_code": "DPYG-EN017",
                "set_rarity": "Rare",
                "set_rarity_code": "(R)",
                "set_price": "1.93",
            },
            {
                "set_name": "Legendary Collection 3: Yugi's World Mega Pack",
                "set_code": "LCYW-EN046",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "3.51",
            },
            {
                "set_name": "Speed Duel Starter Decks: Match of the Millennium",
                "set_code": "SS04-ENA16",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "2.89",
            },
            {
                "set_name": "Speed Duel Tournament Pack 3",
                "set_code": "STP3-EN008",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "3.58",
            },
            {
                "set_name": "Starter Deck: Yugi Evolution",
                "set_code": "SYE-024",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "9.4",
            },
            {
                "set_name": "Yugi's Legendary Decks",
                "set_code": "YGLD-ENA01",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "3.08",
            },
        ],
        "card_images": [
            {
                "id": 5405694,
                "image_url": "https://images.ygoprodeck.com/images/cards/5405694.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/5405694.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/5405694.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.18",
                "tcgplayer_price": "0.50",
                "ebay_price": "3.95",
                "amazon_price": "84.99",
                "coolstuffinc_price": "0.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 3000


def test_when_given_toon_monster__parses_into_model_correctly():
    card = {
        "id": 53183600,
        "name": "Blue-Eyes Toon Dragon",
        "type": "Toon Monster",
        "frameType": "effect",
        "desc": 'Cannot be Normal Summoned/Set. Must first be Special Summoned (from your hand) by Tributing 2 monsters, while you control "Toon World". Cannot attack the turn it is Special Summoned. You must pay 500 LP to declare an attack with this monster. If "Toon World" on the field is destroyed, destroy this card. Can attack your opponent directly, unless they control a Toon monster, in which case this card must target a Toon monster for its attacks.',
        "atk": 3000,
        "def": 2500,
        "level": 8,
        "race": "Dragon",
        "attribute": "LIGHT",
        "archetype": "Toon",
        "card_sets": [
            {
                "set_name": "Dark Beginning 1",
                "set_code": "DB1-EN066",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "32.05",
            },
            {
                "set_name": "Dark Legends",
                "set_code": "DLG1-EN051",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "3.44",
            },
            {
                "set_name": "Duelist Pack: Battle City",
                "set_code": "DPBC-EN043",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.83",
            },
            {
                "set_name": "Legendary Collection 3: Yugi's World Mega Pack",
                "set_code": "LCYW-EN103",
                "set_rarity": "Rare",
                "set_rarity_code": "(R)",
                "set_price": "13.62",
            },
            {
                "set_name": "Legendary Duelists: Season 1",
                "set_code": "LDS1-EN056",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.93",
            },
            {
                "set_name": "Magic Ruler",
                "set_code": "MRL-000",
                "set_rarity": "Secret Rare",
                "set_rarity_code": "(ScR)",
                "set_price": "204.1",
            },
            {
                "set_name": "Magic Ruler",
                "set_code": "MRL-E000",
                "set_rarity": "Secret Rare",
                "set_rarity_code": "(ScR)",
                "set_price": "377.93",
            },
            {
                "set_name": "Retro Pack",
                "set_code": "RP01-EN050",
                "set_rarity": "Rare",
                "set_rarity_code": "(R)",
                "set_price": "36.09",
            },
            {
                "set_name": "Spell Ruler",
                "set_code": "SRL-000",
                "set_rarity": "Secret Rare",
                "set_rarity_code": "(ScR)",
                "set_price": "75.02",
            },
            {
                "set_name": "Spell Ruler",
                "set_code": "SRL-EN000",
                "set_rarity": "Secret Rare",
                "set_rarity_code": "(ScR)",
                "set_price": "76.56",
            },
            {
                "set_name": "Starter Deck: Pegasus",
                "set_code": "SDP-020",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "5.27",
            },
        ],
        "card_images": [
            {
                "id": 53183600,
                "image_url": "https://images.ygoprodeck.com/images/cards/53183600.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/53183600.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/53183600.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.33",
                "tcgplayer_price": "0.69",
                "ebay_price": "14.95",
                "amazon_price": "4.98",
                "coolstuffinc_price": "1.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 3000


def test_when_given_pendulum_normal_monster__parses_into_model_correctly():
    card = {
        "id": 70026064,
        "name": "Bujin Hiruko",
        "type": "Pendulum Normal Monster",
        "frameType": "normal_pendulum",
        "desc": '[ Pendulum Effect ]\r\nYou can banish this card in your Pendulum Zone, then target 1 "Bujin" Xyz Monster you control; Special Summon from your Extra Deck, 1 "Bujin" Xyz Monster with a different name, by using that target as the Xyz Material. (This Special Summon is treated as an Xyz Summon. Xyz Materials attached to it also become Xyz Materials on the Summoned monster.)\r\n----------------------------------------\r\n[ Flavor Text ]\r\nImprisoned after a showdown with "Bujin Hirume" over the Sky Throne, this master schemer eventually escaped by manipulating Hirume and creating the sinister "Bujinki Amaterasu", then went on to almost engulf the world in darkness, but was finally defeated by Yamato and his allies.',
        "atk": 1000,
        "def": 2000,
        "level": 4,
        "race": "Beast-Warrior",
        "attribute": "LIGHT",
        "archetype": "Bujin",
        "scale": 3,
        "card_sets": [
            {
                "set_name": "Maximum Crisis",
                "set_code": "MACR-EN092",
                "set_rarity": "Rare",
                "set_rarity_code": "(R)",
                "set_price": "2.22",
            }
        ],
        "card_images": [
            {
                "id": 70026064,
                "image_url": "https://images.ygoprodeck.com/images/cards/70026064.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/70026064.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/70026064.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.11",
                "tcgplayer_price": "0.22",
                "ebay_price": "1.49",
                "amazon_price": "0.25",
                "coolstuffinc_price": "0.49",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 1000


def test_when_given_pendulumn_tuner_effect_monster__parses_into_model_correctly():
    card = {
        "id": 72181263,
        "name": "D/D Orthros",
        "type": "Pendulum Tuner Effect Monster",
        "frameType": "effect_pendulum",
        "desc": '[ Pendulum Effect ]\r\nOnce per turn: You can target 1 Spell/Trap Card on the field and 1 other "D/D" or "Dark Contract" card you control; destroy them.\r\n----------------------------------------\r\n[ Monster Effect ]\r\nWhen you take battle or effect damage: You can Special Summon this card from your hand. If this card is Special Summoned to your field, you cannot Special Summon monsters for the rest of this turn, except Fiend-Type monsters.',
        "atk": 600,
        "def": 1800,
        "level": 4,
        "race": "Fiend",
        "attribute": "DARK",
        "archetype": "D/D",
        "scale": 3,
        "card_sets": [
            {
                "set_name": "Pendulum Domination Structure Deck",
                "set_code": "SDPD-EN004",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "3.72",
            }
        ],
        "card_images": [
            {
                "id": 72181263,
                "image_url": "https://images.ygoprodeck.com/images/cards/72181263.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/72181263.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/72181263.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "1.82",
                "tcgplayer_price": "1.60",
                "ebay_price": "3.00",
                "amazon_price": "1.29",
                "coolstuffinc_price": "1.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 600


def test_when_given_pendulum_effect_ritual_monster__parses_into_model_correctly():
    card = {
        "id": 66425726,
        "name": "Odd-Eyes Pendulumgraph Dragon",
        "type": "Pendulum Effect Ritual Monster",
        "frameType": "ritual_pendulum",
        "desc": '[ Pendulum Effect ] During the End Phase: You can add 1 Ritual Spell from your Deck or GY to your hand, then return this card to the hand. You can only use this effect of "Odd-Eyes Pendulumgraph Dragon" once per turn.\n[ Monster Effect ] You can Ritual Summon this card with "Odd-Eyes Advent". Must be either Ritual Summoned, or Pendulum Summoned (from your hand). Each time your opponent Special Summons a monster(s) from the Extra Deck, inflict 300 damage to them. Once per turn, when your opponent activates a Spell Card or effect (Quick Effect): You can place this card in your Pendulum Zone, and if you do, negate that effect, then, if this Ritual Summoned card was placed in the Pendulum Zone this way, you can Special Summon 1 "Odd-Eyes" monster from your Extra Deck.',
        "atk": 2700,
        "def": 2500,
        "level": 7,
        "race": "Dragon",
        "attribute": "LIGHT",
        "archetype": "Odd-Eyes",
        "scale": 4,
        "card_sets": [
            {
                "set_name": "Dimension Force",
                "set_code": "DIFO-EN034",
                "set_rarity": "Secret Rare",
                "set_rarity_code": "(ScR)",
                "set_price": "3.85",
            }
        ],
        "card_images": [
            {
                "id": 66425726,
                "image_url": "https://images.ygoprodeck.com/images/cards/66425726.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/66425726.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/66425726.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "1.54",
                "tcgplayer_price": "1.62",
                "ebay_price": "2.23",
                "amazon_price": "3.75",
                "coolstuffinc_price": "1.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.scale == 4


def test_when_given_pendulum_flip_effect_monster__parses_into_model_correctly():
    card = {
        "id": 20281581,
        "name": "Performapal Momoncarpet",
        "type": "Pendulum Flip Effect Monster",
        "frameType": "effect_pendulum",
        "desc": "[ Pendulum Effect ]\r\nUnless you have a card in your other Pendulum Zone, destroy this card. While this card is in the Pendulum Zone, any battle damage you take becomes halved.\r\n----------------------------------------\r\n[ Monster Effect ]\r\nFLIP: You can target 1 Set card on the field; destroy it. If this card is Special Summoned: You can change it to face-down Defense Position.",
        "atk": 1000,
        "def": 100,
        "level": 3,
        "race": "Beast",
        "attribute": "EARTH",
        "archetype": "Performapal",
        "scale": 7,
        "card_sets": [
            {
                "set_name": "Starter Deck: Yuya",
                "set_code": "YS16-EN004",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "1.68",
            }
        ],
        "card_images": [
            {
                "id": 20281581,
                "image_url": "https://images.ygoprodeck.com/images/cards/20281581.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/20281581.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/20281581.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.20",
                "tcgplayer_price": "0.17",
                "ebay_price": "1.29",
                "amazon_price": "0.25",
                "coolstuffinc_price": "0.49",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.scale == 7
