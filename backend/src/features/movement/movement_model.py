from sqlalchemy import UUID, DateTime, ForeignKey, Integer, Column

from src.database import Base
from src.common.mixins.timestamp_mixin import TimestampMixin


class Movement(TimestampMixin, Base):
    __tablename__ = "movement"

    id = Column(UUID(as_uuid=True), primary_key=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))
    from_warehouse_id = Column(UUID(as_uuid=True), ForeignKey("warehouse.id"))
    to_warehouse_id = Column(UUID(as_uuid=True), ForeignKey("warehouse.id"))
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    departure_quantity = Column(Integer)
    arrival_quantity = Column(Integer)
