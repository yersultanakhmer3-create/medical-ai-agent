# Medical AI Agent (Dental RU-only MVP scaffold)

This repo contains a runnable scaffold:
- FastAPI API
- Celery worker + Redis
- Postgres (pgvector image) + MinIO (S3)
- Pydantic v2 schema for `dental_note_v1`
- LLM prompt + strict JSON validation gate
- Celery pipeline skeleton: ASR -> Note -> Evidence

## Quick start (Docker)
1) Copy env:
```bash
cp .env.example .env
# fill OPENAI_API_KEY if you want to test note generation later