-- This script runs automatically the FIRST time the postgres container
-- initializes an empty data directory (via docker-entrypoint-initdb.d).
-- It won't re-run on subsequent restarts because the volume already
-- has data. Useful for extensions or one-time seed data.

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Note: the `tasks` table itself is created by SQLAlchemy
-- (Base.metadata.create_all) when the backend starts up, so we don't
-- redefine it here to avoid conflicts. If you disable that startup
-- behavior in favor of Alembic migrations, you could create the table
-- and seed rows here instead.
