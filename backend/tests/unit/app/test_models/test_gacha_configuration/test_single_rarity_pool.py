from unittest.mock import Mock
import pytest

from app.models import SingleRarityPool, YugiohCardInSet
from app.models.exceptions.gacha_exceptions import NotEnoughCards


def card(id):
    return YugiohCardInSet(
        card_id=id, rarity="rarity", rarity_code="code", price="price"
    )


def test_when_less_cards_then_required_for_pull__raises_not_enough_cards():
    sut = SingleRarityPool(quantity=10, cards=[])
    with pytest.raises(NotEnoughCards):
        sut.pull()


@pytest.fixture
def random():
    return Mock(name="random")


def test_when_cards_are_getting_pulled__cards_are_removed_from_collection(random):
    random.return_value = 0
    sut = SingleRarityPool(quantity=1, cards=[card("scary"), card("terry")])

    [pulled] = sut.pull(random_range=random)

    assert pulled not in sut.cards
    assert len(sut.cards) == 1


def test_when_pulling_card__uses_value_from_random_function(random):
    random.return_value = 0
    expected = card("berry")
    sut = SingleRarityPool(quantity=1, cards=[expected, card("-chan")])

    [pulled] = sut.pull(random_range=random)

    assert pulled is expected
