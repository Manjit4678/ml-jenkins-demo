from pydantic import BaseSettings


class Settings(BaseSettings):
    MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    TOP_K: int = 3

    class Config:
        env_file = ".env"


settings = Settings()
