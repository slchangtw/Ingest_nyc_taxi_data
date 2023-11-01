import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

project_folder = Path(__file__).parent

# Load env files before importing hrf_smarter
if os.environ.get("DOCKER_ENV") == "True":
    load_dotenv(project_folder / ".env.docker")
else:
    load_dotenv(project_folder, ".env.local")


class Settings(BaseSettings):
    POSTGRES_DB_HOST: str
    POSTGRES_DB_PORT: str
    POSTGRES_DB_NAME: str
    POSTGRES_DB_USER: str
    POSTGRES_DB_PASSWORD: str


settings = Settings(
    _env_file_encoding="utf-8",
)
