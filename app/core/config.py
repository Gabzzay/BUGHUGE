from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "BUGHUGE"
    app_version: str = "0.1.0"
    app_env: str = "development"

    mongodb_uri: str = ""
    mongodb_database: str = "bughuge"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()