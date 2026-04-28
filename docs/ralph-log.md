# Ralph Mode Log

## Iteration 1
**Date**: (오늘 날짜)
**Prompt**: "Generate a news summarizer that fetches a URL and returns a 3-sentence summary with key facts"
**Tool**: Claude Code
**Result**: summarizer.py 기본 버전 생성. BeautifulSoup import 누락으로 ModuleNotFoundError 발생
**Changes made**: requirements.txt에 beautifulsoup4 추가, import 수정

## Iteration 2
**Date**: (오늘 날짜)
**Prompt**: "Fix the summarizer — it's returning empty strings for some news sites that block scrapers"
**Tool**: Claude Code
**Result**: User-Agent 헤더 추가 + try/except로 fallback 처리
**Changes made**: fetch_article()에 headers 파라미터 추가, 예외 처리 추가

## Iteration 3
**Date**: (오늘 날짜)
**Prompt**: "The evaluator is too lenient — it passes low quality summaries. Make it stricter"
**Tool**: Claude Code
**Result**: EVAL_SYSTEM 프롬프트 개선, 기준 명확화
**Changes made**: evaluator.py EVAL_SYSTEM 업데이트 — 더 구체적인 PASS 기준 명시