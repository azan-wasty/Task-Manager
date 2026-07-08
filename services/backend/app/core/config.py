from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    In Docker Compose, POSTGRES_HOST will be the *service name* of the
    database container (e.g. "db"), NOT "localhost". Docker Compose's
    internal DNS resolves service names to the right container IP.
    """

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "task_manager"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    APP_NAME: str = "Task Manager API"
    APP_ENV: str = "development"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()
