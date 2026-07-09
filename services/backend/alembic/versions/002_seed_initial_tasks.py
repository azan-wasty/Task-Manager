"""seed initial tasks

Revision ID: 002_seed_initial_tasks
Revises: 001_create_tasks_table
Create Date: 2026-07-08

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "002_seed_initial_tasks"
down_revision: Union[str, None] = "001_create_tasks_table"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

SEED_TASKS = [
    {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "title": "Set up project repository",
        "description": "Initialize git repo, add README, and configure Docker Compose.",
        "status": "completed",
        "is_deleted": False,
    },
    {
        "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
        "title": "Implement task CRUD API",
        "description": "Build FastAPI endpoints for creating, reading, updating, and deleting tasks.",
        "status": "in_progress",
        "is_deleted": False,
    },
    {
        "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
        "title": "Add Alembic migrations",
        "description": "Replace create_all with versioned migrations and seed data.",
        "status": "pending",
        "is_deleted": False,
    },
    {
        "id": "d4e5f6a7-b8c9-0123-def0-234567890123",
        "title": "Write integration tests",
        "description": "Cover API endpoints and database interactions with pytest.",
        "status": "pending",
        "is_deleted": False,
    },
]


def upgrade() -> None:
    connection = op.get_bind()
    for task in SEED_TASKS:
        connection.execute(
            sa.text(
                """
                INSERT INTO tasks (id, title, description, status, is_deleted)
                VALUES (:id, :title, :description, :status, :is_deleted)
                """
            ),
            task,
        )


def downgrade() -> None:
    ids = ", ".join(f"'{task['id']}'" for task in SEED_TASKS)
    op.execute(sa.text(f"DELETE FROM tasks WHERE id IN ({ids})"))
