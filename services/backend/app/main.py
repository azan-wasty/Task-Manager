from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.session import Base, engine, SessionLocal
from app.models import task as task_model  # noqa: F401  (registers the model with Base)
from app.routers import tasks

app = FastAPI(
    title=settings.APP_NAME,
    description="A simple Task Manager backend built with FastAPI + PostgreSQL, "
    "fully containerized with Docker Compose.",
    version="1.0.0",
)

app.include_router(tasks.router)


@app.on_event("startup")
def on_startup():
    # For an assignment/demo app, create tables automatically on startup.
    # In a production app you'd use Alembic migrations instead.
    Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Root"])
def root():
    return {"message": f"{settings.APP_NAME} is running", "env": settings.APP_ENV}


@app.get("/health", tags=["Health"])
def health_check():
    """
    Bonus endpoint: verifies the API is up AND that it can reach the database.
    """
    db_status = "ok"
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
    except Exception as exc:  # pragma: no cover
        db_status = f"error: {exc}"

    return {
        "status": "ok",
        "database": db_status,
    }
