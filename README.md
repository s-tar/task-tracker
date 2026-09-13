# Task Tracker

Simple Task Tracker

## Running with Docker

1. Copy the env file and fill in values:
   ```bash
   cp .env.example .env
   ```

2. Start all services:
   ```bash
   docker compose up --build
   ```

| Service     | URL                        |
|-------------|----------------------------|
| Frontend    | http://localhost:3000      |
| Backend API | http://localhost:8000      |
| API Docs    | http://localhost:8000/docs |
| Jaeger UI   | http://localhost:16686     |

## Database Migrations

Migrations run automatically on startup via Alembic. To run them manually:

```bash
docker compose run app alembic upgrade head
```
