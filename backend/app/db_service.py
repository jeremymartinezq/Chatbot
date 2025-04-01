from typing import Optional, List
from datetime import datetime
from .firebase_config import db
from .models import User, Message, Feedback

class DatabaseService:
    @staticmethod
    async def create_user(user: User) -> User:
        user_dict = user.dict(exclude={'id'})
        user_dict['created_at'] = datetime.utcnow()
        doc_ref = db.collection('users').document()
        doc_ref.set(user_dict)
        user.id = doc_ref.id
        return user

    @staticmethod
    async def get_user_by_username(username: str) -> Optional[User]:
        users_ref = db.collection('users')
        query = users_ref.where('username', '==', username).limit(1)
        docs = query.get()
        if not docs:
            return None
        doc = docs[0]
        user_data = doc.to_dict()
        user_data['id'] = doc.id
        return User(**user_data)

    @staticmethod
    async def create_message(message: Message) -> Message:
        message_dict = message.dict(exclude={'id'})
        message_dict['timestamp'] = datetime.utcnow()
        doc_ref = db.collection('messages').document()
        doc_ref.set(message_dict)
        message.id = doc_ref.id
        return message

    @staticmethod
    async def get_user_messages(user_id: str) -> List[Message]:
        messages_ref = db.collection('messages')
        query = messages_ref.where('user_id', '==', user_id).order_by('timestamp')
        docs = query.get()
        messages = []
        for doc in docs:
            message_data = doc.to_dict()
            message_data['id'] = doc.id
            messages.append(Message(**message_data))
        return messages

    @staticmethod
    async def create_feedback(feedback: Feedback) -> Feedback:
        feedback_dict = feedback.dict(exclude={'id'})
        feedback_dict['timestamp'] = datetime.utcnow()
        doc_ref = db.collection('feedback').document()
        doc_ref.set(feedback_dict)
        feedback.id = doc_ref.id
        return feedback

    @staticmethod
    async def get_message_feedback(message_id: str) -> Optional[Feedback]:
        feedback_ref = db.collection('feedback')
        query = feedback_ref.where('message_id', '==', message_id).limit(1)
        docs = query.get()
        if not docs:
            return None
        doc = docs[0]
        feedback_data = doc.to_dict()
        feedback_data['id'] = doc.id
        return Feedback(**feedback_data)

db_service = DatabaseService() 