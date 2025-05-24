from fastapi import APIRouter, Depends

from src.features.load_testing.usecases.command import (
    LoadTestingBrokerUseCase,
    LoadTestingCommand,
)

router = APIRouter()


@router.post("/load_testing")
async def load_testing(
    iterations: int,
    use_case: LoadTestingBrokerUseCase = Depends(),
):
    command = LoadTestingCommand(iterations=iterations)
    use_case = LoadTestingBrokerUseCase()
    await use_case.execute(command)
    return {"status": "success", "sent": command.count}
