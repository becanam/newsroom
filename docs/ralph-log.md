# Ralph Mode Log

## 개요
Ralph Mode는 AI 에이전트가 결과를 스스로 평가하고 품질 기준을 통과할 때까지 반복 개선하는 패턴입니다.
최대 3회 반복하며, PASS가 나오면 즉시 결과를 반환한다.
---

## 실제 앱 실행 중 Ralph Mode 동작 예시

### 예시 1 — 1회 반복 후 PASS

```
=== Ralph Mode: 반복 1 시작 ===
Evaluator 결과: PASS ✅
=== 총 1회 반복 후 완료 ===
```

### 예시 2 — 3회 반복 후 PASS

```
=== Ralph Mode: 반복 1 시작 ===
Evaluator 결과: RETRY ❌
이유: Lacks sufficient historical context (e.g., previous approval levels, prior market performance, background of Virginia gerrymandering) and depth for a comprehensive summary.
=== Ralph Mode: 반복 2 시작 ===
Evaluator 결과: RETRY ❌
이유: The response offers a clear and concise summary, but it lacks sufficient historical context about approval ratings, market trends, and previous political developments. It is understandable, yet it doesn't meet the >=7 score criteria.
=== Ralph Mode: 반복 3 시작 ===
Evaluator 결과: PASS ✅
=== 총 3회 반복 후 완료 ===
```

### 예시 3 — 2회 반복 후 PASS

```
=== Ralph Mode: 반복 1 시작 ===
Evaluator 결과: RETRY ❌
이유: The reply provides a decent summary and key facts, but it lacks sufficient historical context (e.g., past market cycles, prior BOE warnings) and could be too brief for readers without background. This shortcoming keeps it below a satisfactory score.
=== Ralph Mode: 반복 2 시작 ===
Evaluator 결과: PASS ✅
=== 총 2회 반복 후 완료 ===
```