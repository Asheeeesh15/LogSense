from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "LogSense API"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = True


settings = Settings()