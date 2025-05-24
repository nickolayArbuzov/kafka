from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies import get_db

from src.features.movement.usecases.query import (
    GetMovementByIdUseCase,
    GetMovementByIdQuery,
)
from src.features.movement.repositories import MovementQueryRepository

router = APIRouter()


def get_query_repo(db: AsyncSession = Depends(get_db)) -> MovementQueryRepository:
    return MovementQueryRepository(db)


@router.get("/warehouses/{warehouse_id}/products/{product_id}")
async def GetMovementById(
    warehouse_id: str,
    product_id: str,
    repo: MovementQueryRepository = Depends(get_query_repo),
):
    query = GetMovementByIdQuery(warehouse_id=warehouse_id, product_id=product_id)
    use_case = GetMovementByIdUseCase(repo)
    return await use_case.execute(query)
