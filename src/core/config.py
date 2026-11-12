from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


class DatabaseConfig(BaseModel):
    url: str = "sqlite+aiosqlite:///./microshop.db"
    echo: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )

    db: DatabaseConfig = DatabaseConfig()


settings = Settings()