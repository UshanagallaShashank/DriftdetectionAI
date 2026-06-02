from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


_engine: AsyncEngine | None = None


def get_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        from app.core.config import settings
        url = settings.database_url.replace("postgresql://", "postgresql+asyncpg://", 1) \
            if "asyncpg" not in settings.database_url else settings.database_url
        _engine = create_async_engine(url, echo=settings.debug)
    return _engine


def get_session_factory():
    return async_sessionmaker(get_engine(), expire_on_commit=False)
