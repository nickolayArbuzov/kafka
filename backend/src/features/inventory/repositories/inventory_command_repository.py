from sqlalchemy.ext.asyncio import AsyncSession

from src.features.inventory.inventory_model import Inventory


class InventoryCommandRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_inventory_from_broker(self, inventory_id: str) -> Inventory:
        pass
