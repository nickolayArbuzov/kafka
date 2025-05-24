from sqlalchemy.ext.asyncio import AsyncSession

from src.features.movement.movement_model import Movement


class MovementCommandRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_movement_from_broker(self, movement_id: str) -> Movement:
        pass
