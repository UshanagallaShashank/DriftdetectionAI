"""create behavior_records table

Revision ID: 001
Revises:
Create Date: 2026-05-31
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "001"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "behavior_records",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("system_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=True),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("action_type", sa.String(), nullable=False),
        sa.Column("input_data", sa.JSON(), nullable=False),
        sa.Column("output_data", sa.JSON(), nullable=False),
        sa.Column("metadata", sa.JSON(), nullable=True),
    )
    op.create_index("ix_behavior_records_system_id", "behavior_records", ["system_id"])


def downgrade() -> None:
    op.drop_index("ix_behavior_records_system_id", "behavior_records")
    op.drop_table("behavior_records")
