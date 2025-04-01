from typing import Optional
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.system_prompt = """You are a helpful AI assistant embedded on a website. 
        Your responses should be concise, friendly, and helpful. 
        If you're unsure about something, be honest about it."""
        
    async def get_response(self, message: str) -> str:
        try:
            response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=150,
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in LLM service: {str(e)}")
            return "I apologize, but I'm having trouble processing your request right now. Please try again later."

llm_service = LLMService() 