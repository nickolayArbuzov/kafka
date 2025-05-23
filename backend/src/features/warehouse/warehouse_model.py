import uuid
from sqlalchemy import UUID, Column

from src.database import Base
from src.common.mixins.timestamp_mixin import TimestampMixin


class Warehouse(TimestampMixin, Base):
    __tablename__ = "warehouse"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
