# Dependency & License Audit

## Libraries Used

| Library | License | Version | Why chosen | Alternative considered |
|---------|---------|---------|------------|----------------------|
| fastapi | MIT | 0.115.0 | Fast async API framework, auto docs at /docs | Flask (no async, no auto docs) |
| uvicorn | BSD-3 | 0.30.0 | ASGI server for FastAPI | gunicorn (no async support) |
| requests | Apache 2.0 | 2.32.3 | Simple HTTP for article fetching | httpx (overkill for sync use) |
| httpx | BSD-3 | 0.27.0 | Async HTTP, future-proofing | aiohttp (less ergonomic) |
| beautifulsoup4 | MIT | 4.12.3 | HTML parsing for article extraction | lxml (harder to install in Docker) |
| pandas | BSD-3 | 2.2.2 | Article metadata structuring | plain dict (less flexible) |
| python-dotenv | BSD-3 | 1.0.1 | Load .env variables | os.environ manually (error prone) |

## Security Audit
실행 명령어:
```bash
pip install pip-audit
pip-audit -r requirements.txt
```

| Package | Issue | Action |
|---------|-------|--------|
| requests 2.32.3 | CVE-2024-47081, CVE-2026-25645 | 2.33.0으로 업데이트 |
| python-dotenv 1.0.1 | CVE-2026-28684 | 1.2.2으로 업데이트 |
| starlette 0.38.6 | CVE-2024-47874, CVE-2025-54121 | 0.47.2으로 업데이트 |

취약점 발견 후 requirements.txt 버전을 모두 수정.

## License Choice for This Project
**MIT License** — chosen because:
1. All our dependencies are MIT/Apache/BSD compatible
2. Allows others to build on this freely
3. No copyleft restrictions (unlike GPL)
4. Standard for open-source Python tools