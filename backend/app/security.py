from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from typing import Dict
import time
from collections import defaultdict
import os
from dotenv import load_dotenv

load_dotenv()

security = HTTPBearer()

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self.requests: Dict[str, list] = defaultdict(list)

    def is_rate_limited(self, client_id: str) -> bool:
        now = time.time()
        minute_ago = now - 60

        # Clean old requests
        self.requests[client_id] = [req_time for req_time in self.requests[client_id] if req_time > minute_ago]

        # Check if rate limit is exceeded
        if len(self.requests[client_id]) >= self.requests_per_minute:
            return True

        self.requests[client_id].append(now)
        return False

rate_limiter = RateLimiter()

async def verify_token(credentials: HTTPAuthorizationCredentials = security):
    if credentials.credentials != os.getenv("API_KEY"):
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials

async def rate_limit_middleware(request: Request, call_next):
    client_id = request.client.host
    if rate_limiter.is_rate_limited(client_id):
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )
    response = await call_next(request)
    return response 