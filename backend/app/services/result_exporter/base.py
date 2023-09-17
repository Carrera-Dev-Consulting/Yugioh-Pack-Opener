from abc import ABC, abstractmethod
from typing import Iterable
from app.models import PackRequestResult


class ResultExporter(ABC):
    def __init__(
        self, charcode: str = "utf-8", creator_name: str | None = None
    ) -> None:
        self.encoding = charcode
        self.creator_name = creator_name or "Yugioh Card Puller"

    @abstractmethod
    def export(self, pack_request_result: PackRequestResult) -> Iterable[bytes]:
        pass
