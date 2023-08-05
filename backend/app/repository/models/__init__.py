from sqlalchemy.orm import Relationship

from .base import BaseSQLModel
from .yugioh_card import YugiohCardORM
from .yugioh_set import YugiohSetORM, YugiohCardSetAssociation


YugiohCardORM.sets = Relationship(
    YugiohCardSetAssociation, YugiohCardSetAssociation.card_id, lazy="joined"
)

YugiohSetORM.cards = Relationship(
    YugiohCardSetAssociation, YugiohCardSetAssociation.set_id, lazy="joined"
)


__all__ = ["BaseSQLModel", "YugiohCardORM", "YugiohSetORM", "YugiohCardSetAssociation"]
