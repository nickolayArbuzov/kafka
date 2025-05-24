from aiokafka import AIOKafkaConsumer
from src.broker.handler import on_kafka_message
from src.settings import kafka_connection
import json


async def start_consumer():
    consumer = AIOKafkaConsumer(
        kafka_connection.TOPIC,
        bootstrap_servers=kafka_connection.KAFKA_BOOTSTRAP_SERVERS,
        group_id="inventory-service",
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
    )
    await consumer.start()

    try:
        async for msg in consumer:
            await on_kafka_message(msg)
    finally:
        await consumer.stop()
