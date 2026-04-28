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
```bash
pip install pip-audit
pip-audit
```

## License Choice for This Project
**MIT License** — chosen because:
1. All our dependencies are MIT/Apache/BSD compatible
2. Allows others to build on this freely
3. No copyleft restrictions (unlike GPL)
4. Standard for open-source Python tools