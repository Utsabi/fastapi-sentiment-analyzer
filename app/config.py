from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Sentimemnt Analyzer"
    model_name: str ="textblob"

    class Config:
        env_file = ".env"

settings = Settings()