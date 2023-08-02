from sqlalchemy import Column, String

from .base import BaseSQLModel


class YugiohCard(BaseSQLModel):
    __tablename__ = "yugioh_cards"

    id = Column(String(36), primary_key=True)
    external_id = Column(
        String(512), nullable=False
    )  # id with whatever datasource we use
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    description = Column(String(2048), nullable=False)
    archetype = Column(String(255), nullable=True)
    race = Column(String(255), nullable=True)
