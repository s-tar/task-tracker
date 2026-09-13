"""seed statuses and priorities

Revision ID: 0002
Revises: 0001
Create Date: 2024-01-01 00:00:01.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0002"
down_revision: str | None = "0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

status_table = sa.table(
    "status",
    sa.column("id", sa.Integer),
    sa.column("code", sa.String),
    sa.column("name", sa.String),
)

priority_table = sa.table(
    "priority",
    sa.column("id", sa.Integer),
    sa.column("code", sa.String),
    sa.column("name", sa.String),
)


def upgrade() -> None:
    op.bulk_insert(
        status_table,
        [
            {"id": 1, "code": "TODO", "name": "To Do"},
            {"id": 2, "code": "IN_PROGRESS", "name": "In Progress"},
            {"id": 3, "code": "DONE", "name": "Done"},
        ],
    )
    op.bulk_insert(
        priority_table,
        [
            {"id": 1, "code": "LOW", "name": "Low"},
            {"id": 2, "code": "MEDIUM", "name": "Medium"},
            {"id": 3, "code": "HIGH", "name": "High"},
            {"id": 4, "code": "URGENT", "name": "Urgent"},
        ],
    )


def downgrade() -> None:
    op.execute(sa.delete(status_table).where(status_table.c.code.in_(["TODO", "IN_PROGRESS", "DONE"])))
    op.execute(sa.delete(priority_table).where(priority_table.c.code.in_(["LOW", "MEDIUM", "HIGH", "URGENT"])))
