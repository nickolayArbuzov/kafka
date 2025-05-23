from src.features.movement.repositories.movement_query_repository import (
    MovementQueryRepository,
)


class GetMovementByIdQuery:
    def __init__(self, movement_id: str):
        self.movement_id = movement_id


class GetMovementByIdUseCase:
    def __init__(self, movement_repository: MovementQueryRepository):
        self.movement_repository = movement_repository

    async def execute(self, query: GetMovementByIdQuery):
        movement = await self.movement_repository.get_movement_by_id(query.movement_id)
        return movement
