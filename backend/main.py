from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
from ai_chat import apex_ai, APEXAIChat
from pydantic import BaseModel
from typing import Optional, Dict, Any

load_dotenv()

app = FastAPI(
    title="APEX Sports Analytics API",
    description="API para analise de apostas esportivas",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "APEX Sports Analytics API v1.0.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "chat": "/api/v1/chat"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "APEX"}

@app.post("/api/v1/chat")
async def chat(message: str):
    return {
        "status": "success",
        "message": message,
        "response": "Chat endpoint em desenvolvimento"
    }

# Pydantic Models
class ChatRequest(BaseModel):
    user_id: str
    message: str
    context: Optional[Dict[str, Any]] = None
    game_data: Optional[Dict[str, Any]] = None

# Enhanced Endpoints with APEX AI
@app.post("/api/v1/chat")
async def smart_chat(request: ChatRequest):
    """Intelligent chat endpoint with Perplexity AI"""
    try:
        result = await apex_ai.chat(request.user_id, request.message, request.context)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/analyze-game")
async def analyze_game(request: ChatRequest):
    """Analyze a game for betting recommendations"""
    try:
        if not request.game_data:
            raise HTTPException(status_code=400, detail="game_data required")
        result = await apex_ai.analyze_game(request.game_data)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/chat/history/{user_id}")
async def get_history(user_id: str):
    """Get conversation history"""
    history = apex_ai.get_user_history(user_id)
    return {"status": "success", "user_id": user_id, "history": history}

@app.delete("/api/v1/chat/history/{user_id}")
async def clear_history(user_id: str):
    """Clear conversation history"""
    apex_ai.clear_history(user_id)
    return {"status": "success", "message": "History cleared"}

@app.get("/api/v1/stats")
async def get_stats():
    """Get system statistics"""
    return {"status": "success", "stats": apex_ai.get_stats()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", 8000))
    )
