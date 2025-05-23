from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies import get_db
from src.features.warehouse.usecases.query import (
    GetProductByIdBySpicificWarehouseUseCase,
    GetProductByIdBySpicificWarehouseQuery,
)
from src.features.warehouse.repositories import WarehouseQueryRepository


router = APIRouter()


def get_query_repo(db: AsyncSession = Depends(get_db)) -> WarehouseQueryRepository:
    return WarehouseQueryRepository(db)


@router.get("/warehouses/{warehouse_id}/products/{product_id}")
async def GetStatusGenerate(
    warehouse_id: str,
    product_id: str,
    repo: WarehouseQueryRepository = Depends(get_query_repo),
):
    query = GetProductByIdBySpicificWarehouseQuery(
        warehouse_id=warehouse_id, product_id=product_id
    )
    use_case = GetProductByIdBySpicificWarehouseUseCase(repo)
    return await use_case.execute(query)
