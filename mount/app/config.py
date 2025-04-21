from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_url: str = ""

    secret_key: str = "939a839106e3cdf9ca36c754d88ff52003525cb738cf659b2a5cae208785d475"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
