-- Runs once when the Postgres data directory is first initialized.
-- Schema and seed data are managed by Alembic (see services/backend/alembic/).

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
