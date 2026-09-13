"""seed tasks

Revision ID: 0003
Revises: 0002
Create Date: 2024-01-01 00:00:02.000000

"""

from collections.abc import Sequence
from datetime import datetime

import sqlalchemy as sa
from alembic import op

revision: str = "0003"
down_revision: str | None = "0002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

task_table = sa.table(
    "task",
    sa.column("id", sa.Integer),
    sa.column("title", sa.String),
    sa.column("description", sa.String),
    sa.column("deadline", sa.DateTime),
    sa.column("status_id", sa.Integer),
    sa.column("priority_id", sa.Integer),
    sa.column("created_at", sa.DateTime),
    sa.column("updated_at", sa.DateTime),
)

# status_id: 1=TODO, 2=IN_PROGRESS, 3=DONE
# priority_id: 1=LOW, 2=MEDIUM, 3=HIGH, 4=URGENT

TASKS = [
    {
        "id": 1,
        "title": "Set up CI/CD pipeline",
        "description": "Configure GitHub Actions for automated testing and deployment.",
        "deadline": datetime(2026, 10, 1),
        "status_id": 1,
        "priority_id": 4,
        "created_at": datetime(2026, 9, 1),
        "updated_at": datetime(2026, 9, 1),
    },
    {
        "id": 2,
        "title": "Write unit tests for auth module",
        "description": "Cover login, logout, and token refresh endpoints.",
        "deadline": datetime(2026, 9, 20),
        "status_id": 2,
        "priority_id": 3,
        "created_at": datetime(2026, 9, 2),
        "updated_at": datetime(2026, 9, 10),
    },
    {
        "id": 3,
        "title": "Fix pagination bug on task list",
        "description": "Last page returns duplicate entries when total count is a multiple of page size.",
        "deadline": datetime(2026, 9, 15),
        "status_id": 3,
        "priority_id": 3,
        "created_at": datetime(2026, 9, 3),
        "updated_at": datetime(2026, 9, 12),
    },
    {
        "id": 4,
        "title": "Add dark mode support",
        "description": None,
        "deadline": None,
        "status_id": 1,
        "priority_id": 1,
        "created_at": datetime(2026, 9, 4),
        "updated_at": datetime(2026, 9, 4),
    },
    {
        "id": 5,
        "title": "Migrate database to PostgreSQL",
        "description": "Replace SQLite with PostgreSQL for production readiness.",
        "deadline": datetime(2026, 10, 15),
        "status_id": 1,
        "priority_id": 4,
        "created_at": datetime(2026, 9, 5),
        "updated_at": datetime(2026, 9, 5),
    },
    {
        "id": 6,
        "title": "Implement task filtering by priority",
        "description": "Allow users to filter the task list by one or more priority levels.",
        "deadline": datetime(2026, 9, 25),
        "status_id": 2,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 5),
        "updated_at": datetime(2026, 9, 11),
    },
    {
        "id": 7,
        "title": "Update API documentation",
        "description": "Sync OpenAPI spec with the latest endpoint changes.",
        "deadline": None,
        "status_id": 3,
        "priority_id": 1,
        "created_at": datetime(2026, 9, 6),
        "updated_at": datetime(2026, 9, 13),
    },
    {
        "id": 8,
        "title": "Add email notifications for deadlines",
        "description": "Send a reminder email 24 hours before a task deadline.",
        "deadline": datetime(2026, 10, 30),
        "status_id": 1,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 6),
        "updated_at": datetime(2026, 9, 6),
    },
    {
        "id": 9,
        "title": "Refactor task service layer",
        "description": "Extract business logic from route handlers into a dedicated service module.",
        "deadline": None,
        "status_id": 2,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 7),
        "updated_at": datetime(2026, 9, 9),
    },
    {
        "id": 10,
        "title": "Implement user authentication",
        "description": "Add JWT-based login and registration endpoints.",
        "deadline": datetime(2026, 9, 30),
        "status_id": 3,
        "priority_id": 4,
        "created_at": datetime(2026, 8, 20),
        "updated_at": datetime(2026, 9, 8),
    },
    {
        "id": 11,
        "title": "Design database schema for tags",
        "description": "Allow tasks to have multiple tags for better categorisation.",
        "deadline": datetime(2026, 10, 5),
        "status_id": 1,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 8),
        "updated_at": datetime(2026, 9, 8),
    },
    {
        "id": 12,
        "title": "Performance audit — slow queries",
        "description": "Profile the 5 slowest API endpoints and add missing indexes.",
        "deadline": datetime(2026, 9, 22),
        "status_id": 2,
        "priority_id": 3,
        "created_at": datetime(2026, 9, 8),
        "updated_at": datetime(2026, 9, 12),
    },
    {
        "id": 13,
        "title": "Add export to CSV feature",
        "description": None,
        "deadline": None,
        "status_id": 1,
        "priority_id": 1,
        "created_at": datetime(2026, 9, 9),
        "updated_at": datetime(2026, 9, 9),
    },
    {
        "id": 14,
        "title": "Fix broken deadline validation",
        "description": "API accepts deadlines in the past without returning an error.",
        "deadline": datetime(2026, 9, 14),
        "status_id": 3,
        "priority_id": 3,
        "created_at": datetime(2026, 9, 9),
        "updated_at": datetime(2026, 9, 13),
    },
    {
        "id": 15,
        "title": "Add rate limiting to public endpoints",
        "description": "Prevent abuse by limiting unauthenticated requests to 60 per minute.",
        "deadline": datetime(2026, 10, 10),
        "status_id": 1,
        "priority_id": 3,
        "created_at": datetime(2026, 9, 10),
        "updated_at": datetime(2026, 9, 10),
    },
    {
        "id": 16,
        "title": "Integrate Sentry for error tracking",
        "description": "Capture unhandled exceptions and forward them to Sentry.",
        "deadline": datetime(2026, 9, 28),
        "status_id": 2,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 10),
        "updated_at": datetime(2026, 9, 12),
    },
    {
        "id": 17,
        "title": "Write end-to-end tests for task CRUD",
        "description": "Use pytest with a test database to cover create, read, update, delete flows.",
        "deadline": None,
        "status_id": 1,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 11),
        "updated_at": datetime(2026, 9, 11),
    },
    {
        "id": 18,
        "title": "Implement soft delete for tasks",
        "description": "Add a deleted_at column so tasks can be restored after deletion.",
        "deadline": datetime(2026, 10, 20),
        "status_id": 1,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 11),
        "updated_at": datetime(2026, 9, 11),
    },
    {
        "id": 19,
        "title": "Code review: PR #47 ordering feature",
        "description": None,
        "deadline": datetime(2026, 9, 14),
        "status_id": 3,
        "priority_id": 3,
        "created_at": datetime(2026, 9, 12),
        "updated_at": datetime(2026, 9, 13),
    },
    {
        "id": 20,
        "title": "Upgrade SQLModel to latest version",
        "description": "Check for breaking changes and update any affected models.",
        "deadline": None,
        "status_id": 2,
        "priority_id": 1,
        "created_at": datetime(2026, 9, 12),
        "updated_at": datetime(2026, 9, 13),
    },
    {
        "id": 21,
        "title": "Add health check endpoint",
        "description": "Return database and app status at GET /health.",
        "deadline": datetime(2026, 9, 16),
        "status_id": 3,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 1),
        "updated_at": datetime(2026, 9, 13),
    },
    {
        "id": 22,
        "title": "Document deployment process",
        "description": "Write a runbook covering Docker build, env vars, and rollback steps.",
        "deadline": None,
        "status_id": 1,
        "priority_id": 1,
        "created_at": datetime(2026, 9, 13),
        "updated_at": datetime(2026, 9, 13),
    },
    {
        "id": 23,
        "title": "Add bulk task status update endpoint",
        "description": "Allow updating the status of multiple tasks in a single PATCH request.",
        "deadline": datetime(2026, 10, 8),
        "status_id": 1,
        "priority_id": 3,
        "created_at": datetime(2026, 9, 13),
        "updated_at": datetime(2026, 9, 13),
    },
    {
        "id": 24,
        "title": "Investigate memory leak in background worker",
        "description": "Worker process RSS grows unbounded after ~500 processed tasks.",
        "deadline": datetime(2026, 9, 18),
        "status_id": 2,
        "priority_id": 4,
        "created_at": datetime(2026, 9, 13),
        "updated_at": datetime(2026, 9, 13),
    },
    {
        "id": 25,
        "title": "Set up staging environment",
        "description": "Mirror production infrastructure on a separate subdomain for QA.",
        "deadline": datetime(2026, 10, 25),
        "status_id": 1,
        "priority_id": 2,
        "created_at": datetime(2026, 9, 13),
        "updated_at": datetime(2026, 9, 13),
    },
]


def upgrade() -> None:
    op.bulk_insert(task_table, TASKS)


def downgrade() -> None:
    op.execute(sa.delete(task_table).where(task_table.c.id.in_([t["id"] for t in TASKS])))
