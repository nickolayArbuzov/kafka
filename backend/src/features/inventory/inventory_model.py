from sqlalchemy import UUID, Integer, Column

from src.database import Base
from src.common.mixins.timestamp_mixin import TimestampMixin


class Inventory(TimestampMixin, Base):
    __tablename__ = "inventory"

    warehouse_id = Column(UUID(as_uuid=True), primary_key=True)
    product_id = Column(UUID(as_uuid=True), primary_key=True)
    quantity = Column(Integer, nullable=False, default=0)
