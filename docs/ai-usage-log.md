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

## UI 개선 + 난이도 선택 (index.html)
**Tool**: Claude (채팅)
**Prompt**: "Add complexity level selector, progress bar, and typing indicator to the frontend"
**Generated**: index.html 전체 재작성
**Modifications**: progress bar 타이밍 조정, 채팅 초기화 로직 추가
**Verified**: Docker로 실행 후 브라우저에서 직접 확인

## 이메일 에이전트 (email_agent.py)
**Tool**: Claude (채팅)
**Prompt**: "Add email digest feature using Gmail SMTP"
**Generated**: email_agent.py
**Modifications**: 마크다운 제거 함수 추가 (strip_markdown), 원본 링크 포함 로직 추가
**Verified**: 실제 Gmail로 전송 테스트 완료