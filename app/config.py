from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    LLM_API_KEY: str
    GITHUB_API_URL: str = "https://api.github.com"

    
    class Config:
        env_file = ".env"  # Specifies the environment file

settings = Settings()

print(settings.CELERY_BROKER_URL)  # This will print the value from the .env file
print(settings.LLM_API_KEY)       # Prints the API key from the .env file
