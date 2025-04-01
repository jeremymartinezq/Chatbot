from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = datetime.utcnow()

    class Config:
        from_attributes = True

class Message(BaseModel):
    id: Optional[str] = None
    content: str
    role: str
    timestamp: datetime = datetime.utcnow()
    user_id: str

    class Config:
        from_attributes = True

class Feedback(BaseModel):
    id: Optional[str] = None
    message_id: str
    rating: int
    comment: Optional[str] = None
    timestamp: datetime = datetime.utcnow()

    class Config:
        from_attributes = True 