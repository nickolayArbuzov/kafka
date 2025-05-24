from src.features.inventory.repositories.inventory_query_repository import (
    InventoryQueryRepository,
)


class GetProductByIdBySpecifyWarehouseQuery:
    def __init__(self, warehouse_id: str, product_id: str):
        self.warehouse_id = warehouse_id
        self.product_id = product_id


class GetProductByIdBySpecifyWarehouseUseCase:
    def __init__(self, inventory_repository: InventoryQueryRepository):
        self.inventory_repository = inventory_repository

    async def execute(self, query: GetProductByIdBySpecifyWarehouseQuery):
        inventory = (
            await self.inventory_repository.get_product_by_id_by_specify_warehouse(
                query.warehouse_id, query.product_id
            )
        )
        return inventory
