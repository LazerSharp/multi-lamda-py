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
    return {"users": ["alice", "bob", "Mr. X"], "request_id": context.aws_request_id, "common_hello": resp}

@app.get("/users/health")
def health():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint1")
def ep1():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint2")
def ep2():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint3")
def ep3():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint4")
def ep4():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint5")
def ep5():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint6")
def ep6():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint7")
def ep7():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint8")
def ep8():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint9")
def ep9():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint10")
def ep10():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint11")
def ep11():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint12")
def ep12():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint13")
def ep13():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint14")
def ep14():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

@app.get("/api/endpoint15")
def ep15():
    event = app.current_event
    context = app.lambda_context
    return {"status": "ok", "request_id": context.aws_request_id}

def lambda_handler(event, context):
    return app.resolve(event, context)
