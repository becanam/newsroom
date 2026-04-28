from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from agents.main_agent import analyze_article, chat
from agents.gate import gate

app = FastAPI(title="News Context AI")

# In-memory session store (간단하게)
sessions = {}

class AnalyzeRequest(BaseModel):
    input: str  # URL or article text
    session_id: str = "default"

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    result = analyze_article(req.input)
    sessions[req.session_id] = {
        "article": result["article_text"],
        "history": []
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
    
    response = chat(article, history, req.message)
    
    # Update history
    history.append({"role": "user", "content": req.message})
    history.append({"role": "assistant", "content": response})
    sessions[req.session_id]["history"] = history
    
    return {"response": response}

@app.get("/health")
def health():
    return {"status": "ok"}

# Serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")