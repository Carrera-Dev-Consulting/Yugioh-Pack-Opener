from app.models.pagination import PaginationOptions, PaginationResult
from app.models.set_request import SetRequest
from app.models.yugioh_set import YugiohSet
from app.repository.yugioh_set_repository import SetRepository


class CardStore:
    def __init__(self, set_repository: SetRepository) -> None:
        self.set_respository = set_repository

    def get_sets(
        self, request: SetRequest, page_ops: PaginationOptions | None = None
    ) -> PaginationResult[YugiohSet]:
        # defaults to what is in the options.
        page_ops = page_ops or PaginationOptions()
        with self.set_respository:
            query_result = self.set_respository.get_sets(
                offset=page_ops.page - 1,
                limit=page_ops.page_size,
                start_date=request.start_date,
                end_date=request.end_date,
                set_ids=request.set_ids,
            )
        return PaginationResult[YugiohSet].from_results(
            query_result.results,
            page_ops,
            query_result.total,
        )
