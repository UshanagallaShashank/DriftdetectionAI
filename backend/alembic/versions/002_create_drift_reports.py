"""create drift_reports table

Revision ID: 002
Revises: 001
Create Date: 2026-05-31
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "002"
down_revision: Union[str, Sequence[str], None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "drift_reports",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("system_id", sa.String(), nullable=False),
        sa.Column("analyzed_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("behavior_count", sa.Integer(), nullable=False),
        sa.Column("drift_detected", sa.Boolean(), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("summary", sa.String(), nullable=False),
        sa.Column("anomalies", sa.JSON(), nullable=False),
    )
    op.create_index("ix_drift_reports_system_id", "drift_reports", ["system_id"])


def downgrade() -> None:
    op.drop_index("ix_drift_reports_system_id", "drift_reports")
    op.drop_table("drift_reports")
