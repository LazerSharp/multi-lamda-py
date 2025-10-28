import json
from order_service import app

def test_list_orders(monkeypatch):
    event = {"path": "/orders", "httpMethod": "GET"}
    context = type("ctx", (), {"aws_request_id": "test-id"})
    response = app.lambda_handler(event, context)
    assert "orders" in json.loads(response["body"])

def test_health(monkeypatch):
    event = {"path": "/orders/health", "httpMethod": "GET"}
    context = type("ctx", (), {"aws_request_id": "test-id"})
    response = app.lambda_handler(event, context)
    assert json.loads(response["body"])["status"] == "ok"
