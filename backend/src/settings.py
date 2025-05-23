from pydantic_settings import BaseSettings
from pathlib import Path


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
        env_file = Path(__file__).resolve().parent.parent / ".env"
        extra = "ignore"


postgresql_connection = Postgresql()


class Kafka(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"
        extra = "ignore"


kafka_connection = Kafka()


class Redis(BaseSettings):
    REDIS_URL: str

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"
        extra = "ignore"


redis_connection = Redis()
