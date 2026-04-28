from .gate import call_llm
from .summarizer import COMPLEXITY_PROMPTS

CONTEXT_SYSTEM = """
You are a context enrichment agent. Format your response in clean markdown.

## 🌍 Background
2-3 sentences of historical context.

## 🔗 Why It Matters
1 sentence connecting to broader trends.

## 📖 Key Terms
- **Term** — simple definition (1 line each, max 3 terms)

Rules:
- Bold all important terms using **bold**
- Keep total response under 150 words
- Write for someone with no background knowledge
"""

def add_context(summary: str) -> str:
    return call_llm(CONTEXT_SYSTEM, summary)

def add_context(summary: str, level: str = "medium") -> str:
    tone = COMPLEXITY_PROMPTS.get(level, COMPLEXITY_PROMPTS["medium"])
    system = CONTEXT_SYSTEM + f"\n\nTone instruction: {tone}"
    return call_llm(system, summary)