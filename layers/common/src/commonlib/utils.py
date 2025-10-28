from aws_lambda_powertools import Logger

logger = Logger()

def hello(name: str) -> str:
    logger.info(f"Saying hello to {name}")
    return f"Hello :), {name}!"
