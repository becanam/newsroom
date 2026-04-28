# Project Goal
Build a news context AI service where:
- User pastes a URL or article text
- Agent summarizes + adds historical context
- User can chat about the article
- Daily digest can be emailed

# Success criteria
- FastAPI backend runs via Docker
- /analyze endpoint works with a real URL
- /chat endpoint handles follow-up questions
- Email agent sends formatted digest

# Team Structure
- Developer (나): core API, FastAPI routes, frontend
- AI Agent (Claude Code): code generation, error fixing, refactoring
- Ralph Mode: iterative quality improvement loop