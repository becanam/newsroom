import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from agents.main_agent import analyze_article, chat
from agents.gate import gate
from agents.email_agent import format_digest, send_email

app = FastAPI(title="Newsroom — News Context AI")

sessions = {}

class AnalyzeRequest(BaseModel):
    input: str
    session_id: str = "default"
    level: str = "medium"

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class EmailRequest(BaseModel):
    input: str
    email: str
    session_id: str = "default"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    result = analyze_article(req.input, level=req.level)
    sessions[req.session_id] = {
        "article": result["article_text"],
        "history": [],
        "level": req.level
    }
    return {
        "analysis": result["analysis"],
        "iterations": result["iterations"]
    }

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    session = sessions.get(req.session_id, {})
    article = session.get("article", "")
    history = session.get("history", [])
    level = session.get("level", "medium")
    
    response = chat(article, history, req.message, level=level)
    
    history.append({"role": "user", "content": req.message})
    history.append({"role": "assistant", "content": response})
    sessions[req.session_id]["history"] = history
    return {"response": response}

@app.post("/email")
def send_digest(req: EmailRequest):
    result = analyze_article(req.input)
    digest = format_digest(result["analysis"])
    
    if req.input.startswith("http"):
        digest += f"\n\n─────────────────────────────\n📎 원본 기사: {req.input}"
    
    success = send_email(req.email, "📰 Your Daily News Digest", digest)
    return {"sent": success, "preview": digest[:200]}

app.mount("/", StaticFiles(directory="../static", html=True), name="static")