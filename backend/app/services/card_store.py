from app.models.pagination import PaginationOptions, PaginationResult
from app.models.set_request import SetRequest
from app.models.yugioh_set import YugiohSet


class CardStore:
    def get_sets(
        self, request: SetRequest, page_ops: PaginationOptions = None
    ) -> PaginationResult[YugiohSet]:
        # defaults to what is in the options.
        page_ops = page_ops or PaginationOptions()
        return PaginationResult[YugiohSet].from_results([], page_ops, 0)
