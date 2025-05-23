from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.features.movement.movement_model import Movement


class MovementQueryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_movement_by_id(self, movement_id: str) -> Movement:
        pass
