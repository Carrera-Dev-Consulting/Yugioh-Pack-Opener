from .base import Repository
from app.repository.models.yugioh_card import YugiohCard as YugiohCardORM
from app.models.yugioh_card import YugiohCard


class YugiohCardRepository(Repository):
    def get_all(self) -> list[YugiohCard]:
        items = self.session.query(YugiohCardORM).all()
