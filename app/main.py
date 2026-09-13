from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.tracing import setup_tracing
from src.routers import priorities
from src.routers import statuses
from src.routers import tasks

app = FastAPI(title="Task Tracker API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_tracing(app)

router = APIRouter(prefix="/api/v1")

router.include_router(tasks.router)
router.include_router(statuses.router)
router.include_router(priorities.router)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
