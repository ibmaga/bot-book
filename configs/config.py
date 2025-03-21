from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    TOKEN: str
    ADMIN_IDS: list[int]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
