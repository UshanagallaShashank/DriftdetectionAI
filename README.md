# DriftdetectionAI

Failure intelligence system for AI agents. Observes behavior over time and surfaces drift — without interfering with the systems it watches.

## How it works

```
AI system → POST /behaviors/ingest → PostgreSQL
                                          ↓
                              GET /behaviors?system_id=...
                                          ↓
                              Gemini analysis (coming)
                                          ↓
                              drift report / alert
```

**Principle:** observe, never interfere.

## Stack

| Layer | Technology |
|---|---|
| API | FastAPI + Python 3.12 |
| Database | PostgreSQL via asyncpg + SQLAlchemy 2.0 |
| Migrations | Alembic |
| AI analysis | Gemini via LangChain + LangSmith tracing |
| Frontend | React + TypeScript + Vite |

## Setup

```bash
make setup        # install deps + create .env from template
make dev          # start backend (port 8000) + frontend (port 5173)
make test         # run all tests
make migrate-up   # apply DB migrations
```

## Environment

Copy `backend/.env.example` to `backend/.env` and fill in:

```
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/driftdetection
GEMINI_API_KEY=...
LANGSMITH_API_KEY=...
```

## API

### Ingest a behavior
```
POST /api/v1/behaviors/ingest
{
  "system_id": "my-agent",
  "action_type": "llm_call",
  "input_data": { ... },
  "output_data": { ... },
  "session_id": "optional",
  "metadata": { "latency_ms": 120 }
}
```

### Query behaviors
```
GET /api/v1/behaviors?system_id=my-agent&limit=50&offset=0
```

### Health check
```
GET /health
```

## Project structure

```
backend/
  app/
    api/routes/     # one route handler per file
    services/       # one action per file
    models/         # ORM entities
    schemas/        # request / response shapes
    core/           # config, database engine
  alembic/          # migrations
  tests/            # one test per file
frontend/
  src/              # React components
```

## CI

Every push and PR runs: auto-fix (ruff + eslint) → 30-line limit check → lint → tests → build.
Tests require `TEST_DATABASE_URL` pointing to a live PostgreSQL instance.
