from datetime import date
from .base import Base


class SetRequest(Base):
    set_ids: list[str] = []
    start_date: date | None = None
    end_date: date | None = None
