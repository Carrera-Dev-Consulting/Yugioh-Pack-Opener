from .exceptions.set_exceptions import SetNotFound
from ..models.pack import Pack
from ..repository.yugioh_set_repository import SetRepository
from ..repository.yugioh_card_repository import CardRepository
from .gacha_service import GachaService


class PackBuilder:
    def __init__(
        self,
        gacha_service: GachaService,
        set_repository: SetRepository,
        card_repository: CardRepository,
    ) -> None:
        self.gacha_service = gacha_service
        self.set_repository = set_repository
        self.card_repository = card_repository

    def build_pack(self, set_id: str) -> Pack:
        card_set = self.set_repository.get_set_by_id(set_id)

        if card_set is None:
            raise SetNotFound(set_id)

        pull = self.gacha_service.roll_for_set(card_set)

        return Pack(cards=self.card_repository.get_cards_for_ids(pull.results))
