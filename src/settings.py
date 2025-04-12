from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRESQL_URL: str
    # MONGO_URL: str
    # REDIS_URL: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings() # type: ignore
