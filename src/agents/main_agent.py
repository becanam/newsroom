from .summarizer import fetch_article, summarize
from .context_agent import add_context
from .evaluator import evaluate
from .gate import call_llm

MAX_ITERATIONS = 3

CHAT_SYSTEM = """
You are a helpful assistant for understanding news articles.
The user has read an article. Answer their question using the context provided.
Be clear, accurate, and explain any background they might not know.
"""

def analyze_article(url_or_text: str) -> dict:
    """Main agent loop — Ralph Mode pattern"""
    
    # Step 1: fetch if URL
    if url_or_text.startswith("http"):
        article_text = fetch_article(url_or_text)
    else:
        article_text = url_or_text
    
    iteration = 0
    result = ""
    
    # Ralph Mode: loop until evaluator passes or max iterations
    while iteration < MAX_ITERATIONS:
        iteration += 1
        
        # Sub-agents in sequence
        summary = summarize(article_text)
        context = add_context(summary)
        result = f"{summary}\n\n---\n\n{context}"
        
        # Evaluate
        passed, reason = evaluate(result)
        if passed:
            break
        # If not passed, the loop retries with the reason as hint
        article_text = f"{article_text}\n\nPrevious attempt was insufficient: {reason}"
    
    return {
        "article_text": article_text,
        "analysis": result,
        "iterations": iteration
    }

def chat(article_context: str, conversation_history: list, user_message: str) -> str:
    """Chat sub-agent with full conversation history"""
    messages = []
    for msg in conversation_history:
        messages.append(msg)
    
    full_context = f"Article context:\n{article_context}\n\nUser question: {user_message}"
    return call_llm(CHAT_SYSTEM, full_context)