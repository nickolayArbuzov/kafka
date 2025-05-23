from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.features.product.product_model import Product


class WarehouseQueryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_product_by_id_by_spicific_warehouse(
        self, product_id: str, warehouse_id: str
    ) -> Product:
        pass
