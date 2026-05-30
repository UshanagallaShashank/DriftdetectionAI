from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# Async SQLAlchemy engine — connects to PostgreSQL via asyncpg driver
engine = create_async_engine(settings.database_url, echo=settings.debug)

# Session factory — each request gets its own session
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# Base class all ORM models inherit from
class Base(DeclarativeBase):
    pass
