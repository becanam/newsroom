import requests
import os

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openai/gpt-oss-20b:free"


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
    try:
        data = resp.json()
    except Exception:
        return f"API error: {resp.status_code} - {resp.text[:200]}"
    
    if "choices" not in data:
        return f"API error: {data.get('error', {}).get('message', 'Unknown error')}"
    
    return data["choices"][0]["message"]["content"]


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