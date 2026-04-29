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

def chat(article_context: str, conversation_history: list, user_message: str, level: str = "medium") -> str:
    from .summarizer import COMPLEXITY_PROMPTS
    tone = COMPLEXITY_PROMPTS.get(level, COMPLEXITY_PROMPTS["medium"])
    system = CHAT_SYSTEM + f"\n\nTone instruction: {tone}"
    full_context = f"Article context:\n{article_context}\n\nUser question: {user_message}"
    return call_llm(system, full_context)

def extract_links(text: str) -> list:
    urls = re.findall(r'https?://[^\s\)\"]+', text)
    return urls[:2]  # 최대 2개만 (무한루프 방지)

def analyze_article(url_or_text: str, depth: int = 0, level: str = "medium") -> dict:
    if url_or_text.startswith("http"):
        article_text = fetch_article(url_or_text)
    else:
        article_text = url_or_text

    iteration = 0
    result = ""

    while iteration < MAX_ITERATIONS:
        iteration += 1
        print(f"\n=== Ralph Mode: 반복 {iteration} 시작 ===")
        
        summary = summarize(article_text, level=level)
        context = add_context(summary, level=level)
        result = f"{summary}\n\n---\n\n{context}"
        
        passed, reason = evaluate(result)
        print(f"Evaluator 결과: {'PASS ✅' if passed else 'RETRY ❌'}")
        if not passed:
            print(f"이유: {reason}")
        
        if passed:
            break
        article_text = f"{article_text}\n\nPrevious attempt insufficient: {reason}"

    print(f"=== 총 {iteration}회 반복 후 완료 ===\n")

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