from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from collections import defaultdict
import json
import asyncio
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configure CORS to allow requests from our frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Rate limiting settings
RATE_LIMIT = 60  # requests per minute
RATE_WINDOW = 60  # seconds
rate_limit_dict = defaultdict(list)

# Usage tracking
usage_log_file = "usage_logs.json"
usage_stats = {
    "total_requests": 0,
    "total_tokens": 0,
    "requests_by_ip": defaultdict(int),
    "daily_stats": defaultdict(int)
}

# Load existing usage stats if available
if os.path.exists(usage_log_file):
    with open(usage_log_file, 'r') as f:
        usage_stats.update(json.load(f))

class Message(BaseModel):
    content: str
    role: str = "user"
    stream: bool = True  # New parameter to control streaming

def save_usage_stats():
    with open(usage_log_file, 'w') as f:
        # Convert defaultdict to regular dict for JSON serialization
        stats_to_save = {
            "total_requests": usage_stats["total_requests"],
            "total_tokens": usage_stats["total_tokens"],
            "requests_by_ip": dict(usage_stats["requests_by_ip"]),
            "daily_stats": dict(usage_stats["daily_stats"])
        }
        json.dump(stats_to_save, f, indent=2)

def check_rate_limit(ip: str) -> bool:
    now = datetime.now()
    rate_limit_dict[ip] = [t for t in rate_limit_dict[ip] if now - t < timedelta(seconds=RATE_WINDOW)]
    rate_limit_dict[ip].append(now)
    return len(rate_limit_dict[ip]) <= RATE_LIMIT

async def generate_stream_response(message: str):
    try:
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and knowledgeable assistant. Provide clear, accurate, and concise responses."},
                {"role": "user", "content": message}
            ],
            stream=True,
            max_tokens=150,
            temperature=0.7
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield f"data: {chunk.choices[0].delta.content}\n\n"
            await asyncio.sleep(0.1)  # Small delay to prevent overwhelming the client
            
    except Exception as e:
        logger.error(f"Error in stream generation: {str(e)}")
        yield f"data: Error: {str(e)}\n\n"

@app.get("/")
async def read_root():
    return {"status": "healthy", "message": "Backend is running!"}

@app.get("/stats")
async def get_stats():
    return {
        "total_requests": usage_stats["total_requests"],
        "total_tokens": usage_stats["total_tokens"],
        "requests_today": usage_stats["daily_stats"][datetime.now().strftime("%Y-%m-%d")]
    }

@app.post("/chat")
async def chat(message: Message, request: Request):
    client_ip = request.client.host
    
    # Check rate limit
    if not check_rate_limit(client_ip):
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")
    
    try:
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")

        # Update usage statistics
        usage_stats["total_requests"] += 1
        usage_stats["requests_by_ip"][client_ip] += 1
        today = datetime.now().strftime("%Y-%m-%d")
        usage_stats["daily_stats"][today] += 1

        # Save usage stats
        asyncio.create_task(save_usage_stats())

        if message.stream:
            # Return streaming response
            return StreamingResponse(
                generate_stream_response(message.content),
                media_type="text/event-stream"
            )
        else:
            # Return regular response
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and knowledgeable assistant. Provide clear, accurate, and concise responses."},
                    {"role": "user", "content": message.content}
                ],
                max_tokens=150,
                temperature=0.7
            )
            
            # Update token usage
            usage_stats["total_tokens"] += response.usage.total_tokens
            
            return {"response": response.choices[0].message.content.strip()}

    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        return {"response": f"I encountered an error: {str(e)}. Please make sure the OpenAI API key is properly configured."} 