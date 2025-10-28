from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from commonlib import utils

logger = Logger(service="order_service")
app = APIGatewayRestResolver()

@app.get("/orders")
def list_orders():
    event = app.current_event
    context = app.lambda_context
    logger.info({"path": event.path, "request_id": context.aws_request_id})
    return {"orders": ["order1", "order2"], "request_id": context.aws_request_id}

@app.get("/orders/health")
def health():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

def lambda_handler(event, context):
    return app.resolve(event, context)
