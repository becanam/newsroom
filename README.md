# 📰 Newsroom — News Context AI

뉴스 기사 URL을 붙여넣으면 AI가 즉시 맥락적 분석을 제공하고, 자연어로 대화할 수 있는 서비스.

> "완성도보다 오픈소스 도구 활용" — 오픈소스 SW 응용 중간 프로젝트

## 기능
- 🔍 URL 또는 텍스트로 기사 분석
- 🌍 역사적 맥락 및 배경 설명 자동 추가
- 💬 기사에 대해 AI와 채팅
- 📧 이메일로 데일리 다이제스트 수신
- 🔄 Ralph Mode: 품질이 통과될 때까지 자동 반복 개선
- 🔗 기사 내 하이퍼링크 자동 감지 및 추가 분석
- 📊 난이도 선택 (쉽게 / 보통 / 전문가)

## 기술 스택
- **Backend**: FastAPI + Uvicorn
- **LLM**: OpenRouter API (meta-llama/llama-3.3-70b-instruct:free)
- **Parsing**: BeautifulSoup4 + requests
- **Data**: pandas
- **Container**: Docker

## 프로젝트 구조
```
newsroom/
├── README.md
├── Dockerfile
├── requirements.txt
├── PROMPT.md
├── .env.example
├── src/
│   ├── main.py              # FastAPI 엔드포인트
│   └── agents/
│       ├── gate.py          # LLM wrapper + 라우팅
│       ├── summarizer.py    # 기사 fetch + 요약
│       ├── context_agent.py # 맥락 분석
│       ├── evaluator.py     # 품질 평가 (Ralph Mode)
│       ├── main_agent.py    # 메인 에이전트 루프
│       └── email_agent.py   # 이메일 발송
├── static/
│   └── index.html           # 프론트엔드 UI
└── docs/
    ├── ai-usage-log.md
    ├── ralph-log.md
    └── dependency-audit.md
```

## 실행 방법 (Docker)

```bash
# 1. 이미지 빌드
docker build -t newsroom .

# 2. 실행 (.env 파일 사용)
docker run -p 8000:8000 --env-file .env newsroom
```

브라우저에서 `http://localhost:8000` 접속  
API 문서: `http://localhost:8000/docs`

## 환경 변수
`.env.example`을 복사해서 `.env`로 만들고 값을 채워주세요:

```
OPENROUTER_API_KEY=your_openrouter_key
GMAIL_USER=your@gmail.com
GMAIL_PASS=your_gmail_app_password
```

## API 엔드포인트
| 엔드포인트 | 메서드 | 설명 |
|-----------|--------|------|
| `/analyze` | POST | 기사 URL 또는 텍스트 분석 |
| `/chat` | POST | 분석된 기사에 대한 후속 질문 |
| `/email` | POST | 분석 결과를 이메일로 전송 |
| `/health` | GET | 서버 상태 확인 |

## 오픈소스 라이브러리 및 라이선스
| 라이브러리 | 라이선스 | 용도 |
|-----------|---------|------|
| FastAPI | MIT | API 서버 |
| Uvicorn | BSD-3 | ASGI 서버 |
| requests | Apache 2.0 | HTTP 요청 |
| BeautifulSoup4 | MIT | HTML 파싱 |
| pandas | BSD-3 | 데이터 처리 |
| python-dotenv | BSD-3 | 환경변수 관리 |
| httpx | BSD-3 | 비동기 HTTP |

## 이 프로젝트의 라이선스
MIT License — 모든 의존성과 호환되며 자유롭게 수정/배포 가능

## AI 사용 기록
- `docs/ai-usage-log.md` — 사용한 프롬프트 및 수정 내역
- `docs/ralph-log.md` — Ralph Mode 반복 개선 기록