from src.broker.producer import publish_kafka_event


class LoadTestingCommand:
    def __init__(self, iterations: int):
        self.iterations = iterations


class LoadTestingBrokerUseCase:
    def __init__(self):
        pass

    async def execute(self, command: LoadTestingCommand):
        pass
