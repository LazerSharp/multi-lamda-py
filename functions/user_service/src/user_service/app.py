from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver
from commonlib import utils

logger = Logger(service="user_service")
app = APIGatewayRestResolver()

@app.get("/users")
def list_users():
    event = app.current_event
    context = app.lambda_context
    logger.info({"path": event.path, "request_id": context.aws_request_id})
    resp = utils.hello(str(context.aws_request_id))
    return {"users": ["alice", "bob"], "request_id": context.aws_request_id, "common_hello": resp}

@app.get("/users/health")
def health():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

def lambda_handler(event, context):
    return app.resolve(event, context)
