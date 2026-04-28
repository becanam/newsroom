# AI Usage Log

## Gate Prompt (gate.py)
**Tool**: Claude Code
**Prompt**: "Write a routing agent that classifies user input into ANALYZE, CHAT, or EMAIL using OpenRouter API"
**Generated**: gate.py initial version with call_llm() wrapper
**Modifications**: Added `has_context` parameter — AI missed session state tracking, so CHAT was never triggered without it
**Verified**: Manually tested with URL input (→ ANALYZE), follow-up question (→ CHAT)

## Evaluator (evaluator.py)
**Tool**: Claude Code
**Prompt**: "Write a quality evaluator sub-agent that returns PASS or RETRY:<reason>"
**Generated**: evaluator.py
**Modifications**: Changed return format parsing — AI used regex which broke on multi-line reasons. Switched to startswith() check
**Verified**: Tested with intentionally short summaries — correctly returns RETRY

## Main Agent Loop (main_agent.py)
**Tool**: Claude Code
**Prompt**: "Implement a Ralph Mode loop that retries analysis if evaluator fails, max 3 times"
**Generated**: main_agent.py with while loop
**Modifications**: Added failure reason injection back into article_text for next iteration — AI didn't include this context passing
**Verified**: Confirmed loop stops at MAX_ITERATIONS even if evaluator keeps failing