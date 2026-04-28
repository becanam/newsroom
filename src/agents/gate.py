import requests
import os

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "anthropic/claude-3.5-haiku"

def call_llm(system_prompt: str, user_message: str) -> str:
    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_KEY}"},
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        }
    )
    return resp.json()["choices"][0]["message"]["content"]


GATE_SYSTEM = """
You are a routing agent. Given user input, decide what action to take.
Respond ONLY with one of: ANALYZE, CHAT, EMAIL

- ANALYZE: user pasted a URL or article text for the first time
- CHAT: user is asking a follow-up question about an article
- EMAIL: user wants to receive a daily digest
"""

def gate(user_input: str, has_context: bool) -> str:
    if has_context:
        hint = "There is an existing article in context."
    else:
        hint = "No article context yet."
    result = call_llm(GATE_SYSTEM, f"{hint}\nUser: {user_input}")
    return result.strip()