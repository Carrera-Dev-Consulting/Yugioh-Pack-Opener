import uuid
from sqlalchemy import Column, String, ForeignKey, Date, Integer
from .base import BaseSQLModel
from .yugioh_card import YugiohCard


class YugiohSet(BaseSQLModel):
    __tablename__ = "yugioh_sets"
    id = Column(String(36), primary_key=True, default=uuid.uuid4, nullable=False)
    set_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    release_date = Column(Date, nullable=False)
    card_count = Column(Integer, nullable=False)


class YugiohCardSetAssociation(BaseSQLModel):
    __tablename__ = "yugioh_card_set_associations"

    card_id = Column(
        String(36), ForeignKey(YugiohCard.id), nullable=False, primary_key=True
    )
    set_id = Column(
        String(36), ForeignKey(YugiohSet.id), nullable=False, primary_key=True
    )
    rarity = Column(String(255), nullable=False)
    rarity_code = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)
