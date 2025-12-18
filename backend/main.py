from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", 8000))
    )
