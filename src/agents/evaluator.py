from .gate import call_llm

EVAL_SYSTEM = """
You are a quality evaluator. Rate the following response 1-10.
A good response (score >= 7) must:
- Have a clear summary
- Include historical context
- Be understandable without prior knowledge
Reply with ONLY: PASS or RETRY:<reason>
"""

def evaluate(response: str) -> tuple[bool, str]:
    result = call_llm(EVAL_SYSTEM, response)
    if result.startswith("PASS"):
        return True, ""
    return False, result.replace("RETRY:", "").strip()