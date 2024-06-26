import uuid
from sqlalchemy import Column, String, ForeignKey, Date, Integer
from sqlalchemy.orm import Relationship, Mapped

from .base import BaseSQLModel
from .yugioh_card_orm import YugiohCardORM


class YugiohSetORM(BaseSQLModel):
    __tablename__ = "yugioh_sets"
    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False
    )
    set_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    release_date = Column(Date, nullable=True)
    card_count = Column(Integer, nullable=False)

    cards: Mapped[list["YugiohCardSetAssociation"]] = Relationship(
        "YugiohCardSetAssociation", lazy="select", uselist=True
    )


class YugiohCardSetAssociation(BaseSQLModel):
    __tablename__ = "yugioh_card_set_associations"

    card_id = Column(
        String(36), ForeignKey(YugiohCardORM.id), nullable=False, primary_key=True
    )
    set_id = Column(
        String(36), ForeignKey(YugiohSetORM.id), nullable=False, primary_key=True
    )
    rarity = Column(String(255), nullable=False)
    rarity_code = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)

    card = Relationship(
        YugiohCardORM,
        lazy="select",
        back_populates="sets",
        uselist=False,
    )

    set = Relationship(
        YugiohSetORM, lazy="select", back_populates="cards", uselist=False
    )
