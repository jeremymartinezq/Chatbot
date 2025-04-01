import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Message
from sqlalchemy.orm import Session

def test_chat_endpoint(client: TestClient):
    response = client.post(
        "/chat",
        json={"content": "Hello, how are you?"},
        headers={"Authorization": f"Bearer {pytest.api_key}"}
    )
    assert response.status_code == 200
    assert "response" in response.json()

def test_chat_rate_limit(client: TestClient):
    for _ in range(61):  # Exceed rate limit
        response = client.post(
            "/chat",
            json={"content": "Test message"},
            headers={"Authorization": f"Bearer {pytest.api_key}"}
        )
    assert response.status_code == 429

def test_chat_invalid_token(client: TestClient):
    response = client.post(
        "/chat",
        json={"content": "Hello"},
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401

def test_chat_message_storage(client: TestClient, db_session: Session):
    response = client.post(
        "/chat",
        json={"content": "Test message"},
        headers={"Authorization": f"Bearer {pytest.api_key}"}
    )
    assert response.status_code == 200
    
    # Verify message was stored in database
    message = db_session.query(Message).first()
    assert message is not None
    assert message.content == "Test message"
    assert message.role == "user" 