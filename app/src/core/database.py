from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.config import Environment
from src.core.config import settings

# Sync engine kept for Alembic
engine = create_engine(settings.DATABASE_URL, echo=settings.ENVIRONMENT == Environment.DEVELOPMENT)

_async_url = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
async_engine = create_async_engine(_async_url, echo=settings.ENVIRONMENT == Environment.DEVELOPMENT)

async_session_maker = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    async with async_session_maker() as session:
        yield session


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
