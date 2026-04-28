# 📰 Newsroom — News Context AI

뉴스 기사 URL을 붙여넣으면 AI가 즉시 맥락적 분석을 제공하고, 자연어로 대화할 수 있는 서비스.

## 기능
- 🔍 URL 또는 텍스트로 기사 분석
- 🌍 역사적 맥락 및 배경 설명 자동 추가
- 💬 기사에 대해 AI와 채팅
- 📧 이메일로 데일리 다이제스트 수신
- 🔄 Ralph Mode: 품질이 통과될 때까지 자동 반복 개선

## 기술 스택
- **Backend**: FastAPI + Uvicorn
- **LLM**: OpenRouter API (Claude 3.5 Haiku)
- **Parsing**: BeautifulSoup4
- **Container**: Docker

## 실행 방법 (Docker)

```bash
docker build -t newsroom .
docker run -p 8000:8000 \
  -e OPENROUTER_API_KEY=your_key \
  newsroom
```

브라우저에서 `http://localhost:8000` 접속
API 문서: `http://localhost:8000/docs`

## 환경 변수
`.env.example`을 복사해서 `.env`로 만들고 값을 채워주세요: