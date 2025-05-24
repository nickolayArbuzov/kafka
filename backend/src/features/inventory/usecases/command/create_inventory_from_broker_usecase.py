from src.features.inventory.repositories.inventory_command_repository import (
    InventoryCommandRepository,
)


class CreateInventoryFromBrokerCommand:
    def __init__(self, inventory_id: str):
        self.inventory_id = inventory_id


class CreateInventoryFromBrokerUseCase:
    def __init__(self, inventory_repository: InventoryCommandRepository):
        self.inventory_repository = inventory_repository

    async def execute(self, command: CreateInventoryFromBrokerCommand):
        inventory = await self.inventory_repository.create_inventory_from_broker(
            command.inventory_id
        )
        return inventory
