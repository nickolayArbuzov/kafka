from uuid import uuid4
from sqlalchemy import UUID, DateTime, Enum, Integer, Column

from src.database import Base
from src.common.mixins.timestamp_mixin import TimestampMixin


class Movement(TimestampMixin, Base):
    __tablename__ = "movement"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    movement_id = Column(UUID(as_uuid=True), index=True, nullable=False)
    warehouse_id = Column(UUID(as_uuid=True), nullable=False)
    product_id = Column(UUID(as_uuid=True), nullable=False)

    timestamp = Column(DateTime(timezone=True), nullable=False)
    event = Column(Enum("arrival", "departure", name="movement_type"), nullable=False)
    quantity = Column(Integer, nullable=False)
