from .summarizer import fetch_article, summarize
from .context_agent import add_context
from .evaluator import evaluate
from .gate import call_llm
import re

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

def extract_links(text: str) -> list:
    urls = re.findall(r'https?://[^\s\)\"]+', text)
    return urls[:2]  # 최대 2개만 (무한루프 방지)

def analyze_article(url_or_text: str, depth: int = 0) -> dict:
    if url_or_text.startswith("http"):
        article_text = fetch_article(url_or_text)
    else:
        article_text = url_or_text

    iteration = 0
    result = ""

    while iteration < MAX_ITERATIONS:
        iteration += 1
        summary = summarize(article_text)
        context = add_context(summary)
        result = f"{summary}\n\n---\n\n{context}"
        passed, reason = evaluate(result)
        if passed:
            break
        article_text = f"{article_text}\n\nPrevious attempt insufficient: {reason}"

    # 하이퍼링크 감지 — depth 0일 때만 (무한루프 방지)
    if depth == 0:
        links = extract_links(article_text)
        if links:
            extra = []
            for link in links:
                try:
                    linked_text = fetch_article(link)
                    linked_summary = summarize(linked_text[:2000])
                    extra.append(f"**관련 링크 분석** ({link}):\n{linked_summary}")
                except:
                    pass
            if extra:
                result += "\n\n---\n\n" + "\n\n".join(extra)

    return {"article_text": article_text, "analysis": result, "iterations": iteration}