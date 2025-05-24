from src.features.movement.repositories.movement_command_repository import (
    MovementCommandRepository,
)


class CreateMovementFromBrokerCommand:
    def __init__(self, movement_id: str):
        self.movement_id = movement_id


class CreateMovementFromBrokerUseCase:
    def __init__(self, movement_repository: MovementCommandRepository):
        self.movement_repository = movement_repository

    async def execute(self, command: CreateMovementFromBrokerCommand):
        movement = await self.movement_repository.create_movement_from_broker(
            command.movement_id
        )
        return movement
