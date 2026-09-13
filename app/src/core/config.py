from enum import Enum

from pydantic_settings import BaseSettings


class Environment(str, Enum):
    LOCAL = "local"
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class Settings(BaseSettings):
    ENVIRONMENT: Environment
    DATABASE_URL: str
    PROJECT_NAME: str


settings = Settings()
