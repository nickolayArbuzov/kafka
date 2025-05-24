from sqlalchemy.ext.asyncio import AsyncSession

from src.features.inventory.inventory_model import Inventory


class InventoryQueryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_product_by_id_by_specify_warehouse(
        self, warehouse_id: str, product_id: str
    ) -> Inventory:
        pass
