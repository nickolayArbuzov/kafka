from pydantic_settings import BaseSettings


class Postgresql(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    POSTGRES_HOST: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        extra = "ignore"


postgresql_connection = Postgresql()


class Kafka(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str
    TOPIC: str = "warehouse.events"

    class Config:
        extra = "ignore"


kafka_connection = Kafka()


class Redis(BaseSettings):
    REDIS_URL: str

    class Config:
        extra = "ignore"


redis_connection = Redis()
