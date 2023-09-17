import uuid
from .base import Base


class PackRequest(Base):
    pack_id: uuid.UUID
    total_desired: int
