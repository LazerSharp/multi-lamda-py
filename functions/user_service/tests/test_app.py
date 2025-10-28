import json
from user_service.app import lambda_handler

def test_list_users(monkeypatch):
    event = {"path": "/users", "httpMethod": "GET"}
    context = type("ctx", (), {"aws_request_id": "test-id"})
    response = lambda_handler(event, context)
    assert "users" in json.loads(response["body"])

def test_health(monkeypatch):
    event = {"path": "/users/health", "httpMethod": "GET"}
    context = type("ctx", (), {"aws_request_id": "test-id"})
    response = lambda_handler(event, context)
    assert json.loads(response["body"])["status"] == "ok"
