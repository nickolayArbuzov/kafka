from aiokafka import AIOKafkaConsumer
from src.settings import kafka_connection


async def consume():
    consumer = AIOKafkaConsumer(
        "warehouse_movements",
        bootstrap_servers=kafka_connection.KAFKA_BOOTSTRAP_SERVERS,
        group_id="warehouse_monitor",
    )
