from .gate import call_llm
from .summarizer import COMPLEXITY_PROMPTS

CONTEXT_SYSTEM = """
You are a context agent. Given a news summary, provide:
- 2-3 sentences of historical background
- 1 sentence connecting to broader trends
- A simple glossary (max 3 terms, 1 line each)

Keep total response under 150 words. Be direct and concise.
"""

def add_context(summary: str) -> str:
    return call_llm(CONTEXT_SYSTEM, summary)

def add_context(summary: str, level: str = "medium") -> str:
    tone = COMPLEXITY_PROMPTS.get(level, COMPLEXITY_PROMPTS["medium"])
    system = CONTEXT_SYSTEM + f"\n\nTone instruction: {tone}"
    return call_llm(system, summary)