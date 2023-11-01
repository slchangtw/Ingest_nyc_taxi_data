from sqlalchemy import create_engine

from src.config import settings


def create_pg_engine():
    user = f"{settings.POSTGRES_DB_USER}:{settings.POSTGRES_DB_PASSWORD}"
    server = f"{settings.POSTGRES_DB_HOST}:{settings.POSTGRES_DB_PORT}"

    return create_engine(f"postgresql://{user}@{server}/{settings.POSTGRES_DB_NAME}")
