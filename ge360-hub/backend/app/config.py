from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    env: str = "development"
    api_host: str = "0.0.0.0"
    api_port: int = 8789
    database_url: str = "sqlite:///./ge360_marketing.sqlite3"
    redis_url: str = "redis://localhost:6379/0"
    log_level: str = "INFO"

    prospex_enabled: bool = False
    prospex_base_url: str = ""
    prospex_api_key: str = ""

    twenty_enabled: bool = False
    twenty_base_url: str = ""
    twenty_api_key: str = ""

    mautic_enabled: bool = False
    mautic_base_url: str = ""
    mautic_client_id: str = ""
    mautic_client_secret: str = ""

    opencrm_enabled: bool = False
    opencrm_base_url: str = ""
    opencrm_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="GE360_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
