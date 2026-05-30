from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import DateTime, JSON, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class BehaviorRecord(Base):
    __tablename__ = "behavior_records"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    system_id: Mapped[str] = mapped_column(String, nullable=False)
    session_id: Mapped[str | None] = mapped_column(String, nullable=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    action_type: Mapped[str] = mapped_column(String, nullable=False)
    input_data: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)
    output_data: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)
    extra: Mapped[dict[str, Any] | None] = mapped_column("metadata", JSON, nullable=True)
