from .base import Base


class PackRequest(Base):
    pack_id: str
    total_desired: int
