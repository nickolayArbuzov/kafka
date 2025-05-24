from aiokafka import AIOKafkaProducer
import json
from src.settings import kafka_connection

producer: AIOKafkaProducer | None = None


async def start_producer():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=kafka_connection.KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    await producer.start()


async def stop_kafka_producer():
    if producer:
        await producer.stop()


async def publish_kafka_event(event_type: str, payload: dict):
    if not producer:
        raise RuntimeError("Kafka producer not initialized")
    await producer.send_and_wait(
        kafka_connection.TOPIC, {"event_type": event_type, "payload": payload}
    )
