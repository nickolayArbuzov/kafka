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


@router.get("/movements/{movement_id}")
async def GetStatusGenerate(
    movement_id: str,
    repo: MovementQueryRepository = Depends(get_query_repo),
):
    query = GetMovementByIdQuery(movement_id=movement_id)
    use_case = GetMovementByIdUseCase(repo)
    return await use_case.execute(query)
