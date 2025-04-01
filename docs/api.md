# CopyCoder API Documentation

## Overview
The CopyCoder API provides endpoints for interacting with the chatbot service. All endpoints require authentication using a Bearer token.

## Authentication
All requests must include an Authorization header with a Bearer token:
```
Authorization: Bearer your-api-key
```

## Rate Limiting
The API is rate limited to 60 requests per minute per IP address.

## Endpoints

### Chat
`POST /chat`

Send a message to the chatbot and receive a response.

**Request Body:**
```json
{
    "content": "string",
    "role": "user" | "assistant"
}
```

**Response:**
```json
{
    "response": "string",
    "error": "string (optional)"
}
```

### Configuration
`GET /config`

Retrieve chatbot configuration.

**Response:**
```json
{
    "theme": "light" | "dark",
    "welcome_message": "string",
    "chatbot_name": "string"
}
```

### Feedback
`POST /feedback`

Submit feedback for a specific message.

**Request Body:**
```json
{
    "message_id": "string",
    "rating": number,
    "comment": "string (optional)"
}
```

**Response:**
```json
{
    "status": "success",
    "message": "string"
}
```

### Health Check
`GET /health`

Check the health status of the API.

**Response:**
```json
{
    "status": "healthy"
}
```

## Error Responses
All endpoints may return the following error responses:

- `401 Unauthorized`: Invalid or missing API key
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server-side error

## Example Usage

```python
import requests

API_KEY = "your-api-key"
BASE_URL = "http://localhost:8000"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Send a message
response = requests.post(
    f"{BASE_URL}/chat",
    json={"content": "Hello, how are you?"},
    headers=headers
)
print(response.json())
``` 