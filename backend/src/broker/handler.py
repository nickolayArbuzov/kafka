from sqlalchemy import select
from src.dependencies import session_scope
from src.database import AsyncSessionLocal
from uuid import UUID
from datetime import datetime

USECASE_MAP = {
    "arrival": "arrival",
    "departure": "departure",
}


async def on_kafka_message(msg):
    pass
