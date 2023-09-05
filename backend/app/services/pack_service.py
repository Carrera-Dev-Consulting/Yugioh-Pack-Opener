from ..models.pack_request import PackRequest
from ..models.pack_request_result import PackRequestResult
from .pack_builder import PackBuilder


class PackService:
    def __init__(self, pack_builder: PackBuilder) -> None:
        self.pack_builder = pack_builder

    def open_packs(self, requests: list[PackRequest]) -> list[PackRequestResult]:
        return [
            PackRequestResult(
                cards_pulled=[
                    self.pack_builder.build_pack(request.pack_id)
                    for _ in range(request.total_desired)
                ]
            )
            for request in requests
        ]
