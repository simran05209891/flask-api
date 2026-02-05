from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Enterprise VAPT Security Dashboard"
    ENVIRONMENT: str = "development"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120

    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    FRONTEND_URL: str = "http://localhost:5173"
    CAPTCHA_SECRET: str = "default"

    AWS_ACCESS_KEY: str | None = None
    AWS_SECRET_KEY: str | None = None
    AZURE_CLIENT_ID: str | None = None
    AZURE_TENANT_ID: str | None = None
    AZURE_CLIENT_SECRET: str | None = None
    GCP_SERVICE_KEY: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
