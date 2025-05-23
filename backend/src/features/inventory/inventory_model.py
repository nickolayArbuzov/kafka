from sqlalchemy import UUID, ForeignKey, Integer, Column

from src.database import Base
from src.common.mixins.timestamp_mixin import TimestampMixin


class Inventory(TimestampMixin, Base):
    __tablename__ = "inventory"

    warehouse_id = Column(
        UUID(as_uuid=True), ForeignKey("warehouse.id"), primary_key=True
    )
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"), primary_key=True)
    quantity = Column(Integer, default=0)
