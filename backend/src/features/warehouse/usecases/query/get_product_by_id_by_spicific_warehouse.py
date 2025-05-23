from src.features.warehouse.repositories import WarehouseQueryRepository


class GetProductByIdBySpicificWarehouseQuery:
    def __init__(self, product_id: str, warehouse_id: str):
        self.product_id = product_id
        self.warehouse_id = warehouse_id


class GetProductByIdBySpicificWarehouseUseCase:
    def __init__(self, warehouse_repository: WarehouseQueryRepository):
        self.warehouse_repository = warehouse_repository

    async def execute(self, query: GetProductByIdBySpicificWarehouseQuery):
        product = (
            await self.warehouse_repository.get_product_by_id_by_spicific_warehouse(
                query.product_id, query.warehouse_id
            )
        )
        return product
