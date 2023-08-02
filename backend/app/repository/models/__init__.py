from sqlalchemy.orm import Relationship

from .base import BaseSQLModel
from .yugioh_card import YugiohCard
from .yugioh_set import YugiohSet, YugiohCardSetAssociation


YugiohCard.sets = Relationship(
    YugiohCardSetAssociation, YugiohCardSetAssociation.card_id, lazy="joined"
)

YugiohSet.cards = Relationship(
    YugiohCardSetAssociation, YugiohCardSetAssociation.set_id, lazy="joined"
)


__all__ = ["BaseSQLModel", "YugiohCard", "YugiohSet", "YugiohCardSetAssociation"]
