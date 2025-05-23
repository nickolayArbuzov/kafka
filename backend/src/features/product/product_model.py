import uuid
from sqlalchemy import UUID, Column

from src.database import Base
from src.common.mixins.timestamp_mixin import TimestampMixin


class Product(TimestampMixin, Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
