import uuid
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import Relationship

from .base import BaseSQLModel


class YugiohCardORM(BaseSQLModel):
    __tablename__ = "yugioh_cards"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    external_id = Column(
        String(512), nullable=False
    )  # id with whatever datasource we use
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    description = Column(String(2048), nullable=False)
    archetype = Column(String(255), nullable=True)
    race = Column(String(255), nullable=True)
    scale = Column(Integer, nullable=True)
    defense = Column(Integer, nullable=True)
    attack = Column(Integer, nullable=True)
    attribute = Column(String(255), nullable=True)
    level = Column(Integer, nullable=True)
    link_value = Column(Integer, nullable=True)
    links = Column(
        String(255), nullable=True
    )  # will be a comma-separated list of the ygopro link markers


class YugiohCardImageORM(BaseSQLModel):
    __tablename__ = "yugioh_card_images"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    card_id = Column(String(36), ForeignKey(YugiohCardORM.id), nullable=False)
    regular = Column(String(255), nullable=False)
    small = Column(String(255), nullable=False)
    cropped = Column(String(255), nullable=False)

    card = Relationship(YugiohCardORM, lazy="select", back_populates="images", uselist=False)


class YugiohCardPriceORM(BaseSQLModel):
    __tablename__ = "yugioh_card_prices"

    card_id = Column(String(36), ForeignKey(YugiohCardORM.id), primary_key=True)
    tcgplayer_price = Column(String(255), nullable=True)
    cardmarket_price = Column(String(255), nullable=True)
    ebay_price = Column(String(255), nullable=True)
    amazon_price = Column(String(255), nullable=True)
    coolstuffinc_price = Column(String(255), nullable=True)

    card = Relationship(YugiohCardORM, lazy="select", back_populates="price", uselist=False)


class YugiohCardBanListInfoORM(BaseSQLModel):
    __tablename__ = "yugioh_card_ban_list_entries"
    card_id = Column(String(36), ForeignKey(YugiohCardORM.id), primary_key=True)
    format = Column(String(255), primary_key=True)
    level = Column(String(255), nullable=False)

    card = Relationship(YugiohCardORM, lazy="select", back_populates="bans", uselist=False)
