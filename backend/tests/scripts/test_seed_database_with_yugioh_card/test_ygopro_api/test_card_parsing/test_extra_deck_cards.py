from scripts.seed_database_with_yugioh_card.ygopro_api import YGOProCard

sut = YGOProCard.model_validate


def test_when_given_a_fusion_monster__parses_into_model_correctly():
    card = {
        "id": 65172015,
        "name": "A-to-Z-Dragon Buster Cannon",
        "type": "Fusion Monster",
        "frameType": "fusion",
        "desc": '"ABC-Dragon Buster" + "XYZ-Dragon Cannon"\nMust be Special Summoned (from your Extra Deck) by banishing cards you control with the above original names, and cannot be Special Summoned by other ways. (You do not use "Polymerization".) During either player\'s turn, when your opponent activates a Spell/Trap Card, or monster effect: You can discard 1 card; negate the activation, and if you do, destroy that card. During either player\'s turn: You can banish this card, then target 1 each of your banished "ABC-Dragon Buster", and "XYZ-Dragon Cannon"; Special Summon them.',
        "atk": 4000,
        "def": 4000,
        "level": 10,
        "race": "Machine",
        "attribute": "LIGHT",
        "archetype": "ABC",
        "card_sets": [
            {
                "set_name": "Structure Deck: Seto Kaiba",
                "set_code": "SDKS-EN040",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "2.39",
            }
        ],
        "card_images": [
            {
                "id": 65172015,
                "image_url": "https://images.ygoprodeck.com/images/cards/65172015.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/65172015.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/65172015.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.96",
                "tcgplayer_price": "0.45",
                "ebay_price": "2.49",
                "amazon_price": "0.98",
                "coolstuffinc_price": "0.39",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 4000


def test_when_given_link_monster__parses_into_model_correctly():
    card = {
        "id": 2368215,
        "name": "Abyss Actor - Hyper Director",
        "type": "Link Monster",
        "frameType": "link",
        "desc": '1 "Abyss Actor" Pendulum Monster\r\nYou can target 1 card in your Pendulum Zone; Special Summon it, then place 1 "Abyss Actor" Pendulum Monster with a different name, from your Deck or face-up Extra Deck, to your Pendulum Zone, also you cannot Normal or Special Summon monsters for the rest of this turn, except "Abyss Actor" monsters. You can only use this effect of "Abyss Actor - Hyper Director" once per turn.',
        "atk": 800,
        "race": "Fiend",
        "attribute": "DARK",
        "archetype": "Abyss Actor",
        "linkval": 1,
        "linkmarkers": ["Bottom"],
        "card_sets": [
            {
                "set_name": "Duel Overload",
                "set_code": "DUOV-EN022",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "1.5",
            }
        ],
        "card_images": [
            {
                "id": 2368215,
                "image_url": "https://images.ygoprodeck.com/images/cards/2368215.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/2368215.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/2368215.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.16",
                "tcgplayer_price": "0.23",
                "ebay_price": "0.99",
                "amazon_price": "0.25",
                "coolstuffinc_price": "0.79",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.defense is None


def test_when_given_xyz__parses_into_model():
    card = {
        "id": 21044178,
        "name": "Abyss Dweller",
        "type": "XYZ Monster",
        "frameType": "xyz",
        "desc": "2 Level 4 monsters\nWhile this card has a material attached that was originally WATER, all WATER monsters you control gain 500 ATK. Once per turn (Quick Effect): You can detach 1 material from this card; your opponent cannot activate any card effects in their GY this turn.",
        "atk": 1700,
        "def": 1400,
        "level": 4,
        "race": "Sea Serpent",
        "attribute": "WATER",
        "card_sets": [
            {
                "set_name": "Abyss Rising",
                "set_code": "ABYR-EN084",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "2.98",
            },
            {
                "set_name": "Duel Devastator",
                "set_code": "DUDE-EN016",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "1.78",
            },
            {
                "set_name": "OTS Tournament Pack 13",
                "set_code": "OP13-EN002",
                "set_rarity": "Ultimate Rare",
                "set_rarity_code": "(UtR)",
                "set_price": "93.12",
            },
            {
                "set_name": "OTS Tournament Pack 13 (POR)",
                "set_code": "OP13-PT002",
                "set_rarity": "Ultimate Rare",
                "set_rarity_code": "(UtR)",
                "set_price": "0.00",
            },
            {
                "set_name": "OTS Tournament Pack 20",
                "set_code": "OP20-EN020",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0",
            },
            {
                "set_name": "Premium Gold: Infinite Gold",
                "set_code": "PGL3-EN068",
                "set_rarity": "Gold Rare",
                "set_rarity_code": "(GUR)",
                "set_price": "2.7",
            },
            {
                "set_name": "The Secret Forces",
                "set_code": "THSF-EN047",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "2.87",
            },
        ],
        "card_images": [
            {
                "id": 21044178,
                "image_url": "https://images.ygoprodeck.com/images/cards/21044178.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/21044178.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/21044178.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.64",
                "tcgplayer_price": "0.42",
                "ebay_price": "1.75",
                "amazon_price": "1.68",
                "coolstuffinc_price": "49.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.level == 4


def test_when_given_synchro_monster__parses_into_model_correctly():
    card = {
        "id": 30983281,
        "name": "Accel Synchro Stardust Dragon",
        "type": "Synchro Monster",
        "frameType": "synchro",
        "desc": '1 Tuner + 1+ non-Tuner monsters\r\nIf this card is Synchro Summoned: You can Special Summon 1 Level 2 or lower Tuner from your GY. During the Main Phase (Quick Effect): You can Tribute this card; Special Summon 1 "Stardust Dragon" from your Extra Deck (this is treated as a Synchro Summon), then, immediately after this effect resolves, Synchro Summon 1 Synchro Monster using monsters you control as material. This turn, the monsters Synchro Summoned by this effect are unaffected by your opponent\'s activated effects. You can only use each effect of "Accel Synchro Stardust Dragon" once per turn.',
        "atk": 2500,
        "def": 2000,
        "level": 8,
        "race": "Dragon",
        "attribute": "WIND",
        "archetype": "Stardust",
        "card_sets": [
            {
                "set_name": "Maze of Memories",
                "set_code": "MAZE-EN019",
                "set_rarity": "Collector's Rare",
                "set_rarity_code": "(CR)",
                "set_price": "0",
            },
            {
                "set_name": "Maze of Memories",
                "set_code": "MAZE-EN019",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "0",
            },
        ],
        "card_images": [
            {
                "id": 30983281,
                "image_url": "https://images.ygoprodeck.com/images/cards/30983281.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/30983281.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/30983281.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "25.46",
                "tcgplayer_price": "46.52",
                "ebay_price": "99.00",
                "amazon_price": "54.99",
                "coolstuffinc_price": "44.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.level == 8


def test_when_given_synchro_tuner__parses_into_model_correctly():
    card = {
        "id": 37675907,
        "name": "Accel Synchron",
        "type": "Synchro Tuner Monster",
        "frameType": "synchro",
        "desc": '1 Tuner + 1+ non-Tuner monsters\r\nOnce per turn: You can send 1 "Synchron" monster from your Deck to the GY, then activate 1 of these effects;\r\n\u25cf Increase this card\'s Level by the Level of the sent monster.\r\n\u25cf Reduce this card\'s Level by the Level of the sent monster.\r\nDuring your opponent\'s Main Phase, you can (Quick Effect): Immediately after this effect resolves, Synchro Summon using this card you control. You can only Synchro Summon "Accel Synchron" once per turn.',
        "atk": 500,
        "def": 2100,
        "level": 5,
        "race": "Machine",
        "attribute": "DARK",
        "archetype": "Synchron",
        "card_sets": [
            {
                "set_name": "Legendary Duelists: Magical Hero",
                "set_code": "LED6-EN028",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "1.4",
            },
            {
                "set_name": "Legendary Duelists: Season 3",
                "set_code": "LDS3-EN120",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0.82",
            },
            {
                "set_name": "Synchron Extreme Structure Deck",
                "set_code": "SDSE-EN042",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "3.12",
            },
        ],
        "card_images": [
            {
                "id": 37675907,
                "image_url": "https://images.ygoprodeck.com/images/cards/37675907.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/37675907.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/37675907.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.16",
                "tcgplayer_price": "0.16",
                "ebay_price": "0.99",
                "amazon_price": "2.54",
                "coolstuffinc_price": "0.39",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.level == 5


def test_when_given_pendulum_effect_fusion_monster__parses_into_model_correctly():
    card = {
        "id": 50687050,
        "name": "Arktos XII - Chronochasm Vaylantz",
        "type": "Pendulum Effect Fusion Monster",
        "frameType": "fusion_pendulum",
        "desc": '[ Pendulum Effect ] You can activate 1 of these effects;\r\n\u25cf Special Summon this card to your Main Monster Zone in its same column.\r\n\u25cf Move 1 monster in your Main Monster Zone to an adjacent (horizontal) Monster Zone.\r\nYou can only use this effect of "Arktos XII - Chronochasm Vaylantz" once per turn.\n[ Monster Effect ] 2 Level 5 or higher "Vaylantz" monsters\r\nMust first be Special Summoned (from your face-down Extra Deck) by Tributing the above cards. (Quick Effect): You can switch the locations of 2 monsters in your Main Monster Zones or 2 monsters in your opponent\'s Main Monster Zones. If a card in the Monster Zone moves to another Monster Zone (except during the Damage Step): You can destroy 1 card on the field. You can only use each effect of "Arktos XII - Chronochasm Vaylantz" once per turn.',
        "atk": 3000,
        "def": 3000,
        "level": 12,
        "race": "Fairy",
        "attribute": "EARTH",
        "archetype": "Vaylantz",
        "scale": 12,
        "card_sets": [
            {
                "set_name": "Photon Hypernova",
                "set_code": "PHHY-EN037",
                "set_rarity": "Super Rare",
                "set_rarity_code": "(SR)",
                "set_price": "0",
            }
        ],
        "card_images": [
            {
                "id": 50687050,
                "image_url": "https://images.ygoprodeck.com/images/cards/50687050.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/50687050.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/50687050.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.17",
                "tcgplayer_price": "0.17",
                "ebay_price": "0.00",
                "amazon_price": "0.00",
                "coolstuffinc_price": "0.25",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 3000


def test_when_given_synchro_pendulum_monster__parses_into_model_correctly():
    card = {
        "id": 90036274,
        "name": "Clear Wing Fast Dragon",
        "type": "Synchro Pendulum Effect Monster",
        "frameType": "synchro_pendulum",
        "desc": '[ Pendulum Effect ]\r\nYou can send 1 face-up "Speedroid" Tuner and 1 face-up non-Tuner monster you control to the Graveyard, whose total Levels equal 7; Special Summon this card from your Pendulum Zone. You can only use this effect of "Clear Wing Fast Dragon" once per turn.\r\n----------------------------------------\r\n[ Monster Effect ]\r\n1 Tuner + 1 or more non-Tuner WIND monsters\r\nDuring either player\'s turn: You can target 1 face-up monster your opponent controls that was Special Summoned from the Extra Deck; until the end of this turn, change its ATK to 0, also that face-up monster has its effects negated. You can only use this effect of "Clear Wing Fast Dragon" once per turn. If this card in the Monster Zone is destroyed by battle or card effect: You can place this card in your Pendulum Zone.',
        "atk": 2500,
        "def": 2000,
        "level": 7,
        "race": "Dragon",
        "attribute": "WIND",
        "archetype": "Clear Wing",
        "scale": 4,
        "card_sets": [
            {
                "set_name": "Duel Devastator",
                "set_code": "DUDE-EN011",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "1.56",
            },
            {
                "set_name": "Yu-Gi-Oh! ARC-V Volume 2 promotional card",
                "set_code": "YA02-EN001",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "5.14",
            },
        ],
        "card_images": [
            {
                "id": 90036274,
                "image_url": "https://images.ygoprodeck.com/images/cards/90036274.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/90036274.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/90036274.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.24",
                "tcgplayer_price": "0.19",
                "ebay_price": "3.95",
                "amazon_price": "0.99",
                "coolstuffinc_price": "2.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 2500


def test_when_given_xyz_pendulum_effect_monster__parses_into_model_correctly():
    card = {
        "id": 46593546,
        "name": "D/D/D Deviser King Deus Machinex",
        "type": "XYZ Pendulum Effect Monster",
        "frameType": "xyz_pendulum",
        "desc": '[ Pendulum Effect ] While you have a card in your other Pendulum Zone: You can target 1 Pendulum Monster you control or in your GY; Special Summon the card in your other Pendulum Zone, and if you do, place that targeted Pendulum Monster in your Pendulum Zone. You can only use this effect of "D/D/D Deviser King Deus Machinex" once per turn.\n[ Monster Effect ] 2 Level 10 Fiend monsters\r\nYou can also Xyz Summon this card by using a "D/D/D" monster you control as material. (Transfer its materials to this card.) You can only control 1 "D/D/D Deviser King Deus Machinex" in your Monster Zone. Once per Chain, when a Monster Card your opponent controls activates its effect (Quick Effect): You can either detach 2 materials from this card, or destroy 1 "Dark Contract" card you control, and if you do, attach that opponent\'s card to this card as material. Once per turn, during your Standby Phase: You can place this card in your Pendulum Zone.',
        "atk": 3000,
        "def": 3000,
        "level": 10,
        "race": "Fiend",
        "attribute": "DARK",
        "archetype": "D/D/D",
        "scale": 10,
        "card_sets": [
            {
                "set_name": "Battle of Chaos",
                "set_code": "BACH-EN044",
                "set_rarity": "Ultra Rare",
                "set_rarity_code": "(UR)",
                "set_price": "4.61",
            }
        ],
        "card_images": [
            {
                "id": 46593546,
                "image_url": "https://images.ygoprodeck.com/images/cards/46593546.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/46593546.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/46593546.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "8.50",
                "tcgplayer_price": "4.08",
                "ebay_price": "5.74",
                "amazon_price": "1.83",
                "coolstuffinc_price": "5.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.scale == 10
