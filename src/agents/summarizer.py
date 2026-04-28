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
You are a news summarizer. Given article text:
1. Write a 3-sentence summary
2. List the 3 most important facts
3. Identify all key people and organizations mentioned
Return as structured text.
"""

def summarize(article_text: str) -> str:
    return call_llm(SUMMARIZER_SYSTEM, article_text[:4000])