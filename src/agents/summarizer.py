from .gate import call_llm
import requests
from bs4 import BeautifulSoup

def fetch_article(url: str) -> str:
    resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")
    # 본문 텍스트만 추출
    paragraphs = soup.find_all("p")
    return " ".join(p.get_text() for p in paragraphs[:40])

SUMMARIZER_SYSTEM = """
You are a news summarizer. Be concise and clear.
1. Write a 2-sentence summary (max 60 words)
2. List exactly 3 key facts as bullet points (1 line each)
3. List key people/organizations (name + 1 word role only)

Keep the total response under 200 words.
"""

def summarize(article_text: str) -> str:
    return call_llm(SUMMARIZER_SYSTEM, article_text[:4000])

COMPLEXITY_PROMPTS = {
    "easy": "Explain everything as if talking to a 15-year-old with no background knowledge. Use very simple words, short sentences, and everyday analogies.",
    "medium": "Assume the reader has basic general knowledge but is not an expert. Explain technical terms briefly.",
    "expert": "Assume the reader is well-informed. Skip basic explanations and focus on nuanced analysis and implications."
}

def summarize(article_text: str, level: str = "medium") -> str:
    tone = COMPLEXITY_PROMPTS.get(level, COMPLEXITY_PROMPTS["medium"])
    system = SUMMARIZER_SYSTEM + f"\n\nTone instruction: {tone}"
    return call_llm(system, article_text[:4000])