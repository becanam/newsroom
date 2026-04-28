from .gate import call_llm

CONTEXT_SYSTEM = """
You are a context enrichment agent. Given a news summary:
- Explain the historical background (why this matters)
- Identify key players and their roles
- Explain any technical terms or jargon
- Connect this to broader trends
Write for someone with no background knowledge.
"""

def add_context(summary: str) -> str:
    return call_llm(CONTEXT_SYSTEM, summary)