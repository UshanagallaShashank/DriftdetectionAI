from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings, settings
from app.core.database import SessionLocal


# Returns the current application settings as a FastAPI dependency
def get_settings() -> Settings:
    return settings

# Yields a database session per request and closes it when done
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
