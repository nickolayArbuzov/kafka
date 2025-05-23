from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import Base, engine
from src.features.movement import movement_controller
from src.features.warehouse import warehouse_controller


async def lifespan(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(movement_controller.router, prefix="/api", tags=["movement"])
app.include_router(warehouse_controller.router, prefix="/api", tags=["warehouse"])
