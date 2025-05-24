import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.broker.consumer import start_consumer
from src.broker.producer import start_producer
from src.features.inventory import inventory_controller
from src.features.movement import movement_controller
from src.features.load_testing import load_testing_controller


async def lifespan(app):
    asyncio.create_task(start_producer())
    asyncio.create_task(start_consumer())
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(inventory_controller.router, prefix="/api", tags=["inventory"])
app.include_router(movement_controller.router, prefix="/api", tags=["movement"])
app.include_router(load_testing_controller.router, prefix="/api", tags=["load_testing"])
