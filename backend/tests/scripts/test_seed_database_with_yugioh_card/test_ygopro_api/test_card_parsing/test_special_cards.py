from scripts.seed_database_with_yugioh_card.ygopro_api import YGOProCard

sut = YGOProCard.model_validate


def test_when_given_skill_card__parses_into_model_correctly():
    card = {
        "id": 300302022,
        "name": "Ancient Fusion",
        "type": "Skill Card",
        "frameType": "skill",
        "desc": 'Once per Duel, you can discard 1 card to Fusion Summon 1 "Ancient Gear" Fusion Monster from your Extra Deck, using monsters from your field as Fusion Material. If 1 of those materials is an "Ancient Gear Golem" monster, you can also use monsters from your hand and/or Deck as the other material. Your opponent takes no damage for the rest of this turn. Any battle damage your opponent takes from that Fusion Monster is halved.',
        "race": "Dr. Vellian C",
        "card_sets": [
            {
                "set_name": "Speed Duel GX: Duel Academy Box",
                "set_code": "SGX1-ENS04",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "0",
            }
        ],
        "card_images": [
            {
                "id": 300302022,
                "image_url": "https://images.ygoprodeck.com/images/cards/300302022.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/300302022.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/300302022.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.00",
                "tcgplayer_price": "0.16",
                "ebay_price": "4.74",
                "amazon_price": "49.99",
                "coolstuffinc_price": "0.79",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack is None


def test_when_given_token__parses_into_model_correctly():
    card = {
        "id": 44052075,
        "name": "Ancient Gear Token",
        "type": "Token",
        "frameType": "token",
        "desc": 'This card can be used as an "Ancient Gear Token".\n\n\n*If used for another Token, apply that Token\'s Type/Attribute/Level/ATK/DEF.',
        "atk": 0,
        "def": 0,
        "level": 1,
        "race": "Machine",
        "attribute": "EARTH",
        "archetype": "Ancient Gear",
        "card_sets": [
            {
                "set_name": "Machine Reactor Structure Deck",
                "set_code": "SR03-ENTKN",
                "set_rarity": "Common",
                "set_rarity_code": "(C)",
                "set_price": "3.25",
            }
        ],
        "card_images": [
            {
                "id": 44052075,
                "image_url": "https://images.ygoprodeck.com/images/cards/44052075.jpg",
                "image_url_small": "https://images.ygoprodeck.com/images/cards_small/44052075.jpg",
                "image_url_cropped": "https://images.ygoprodeck.com/images/cards_cropped/44052075.jpg",
            }
        ],
        "card_prices": [
            {
                "cardmarket_price": "0.64",
                "tcgplayer_price": "1.33",
                "ebay_price": "6.82",
                "amazon_price": "2.81",
                "coolstuffinc_price": "2.99",
            }
        ],
    }

    parsed = sut(card)

    assert parsed.attack == 0
