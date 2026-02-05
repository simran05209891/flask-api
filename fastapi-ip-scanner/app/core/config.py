from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Enterprise VAPT Security Dashboard"
    environment: str = "production"
    frontend_url: str = "http://localhost:5173"

    captcha_secret: str = "MY_CAPTCHA_SECRET"
    jwt_secret_key: str = "CHANGE_THIS_SECRET"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60

    aws_access_key: str = ""
    aws_secret_key: str = ""

    azure_client_id: str = ""
    azure_tenant_id: str = ""
    azure_client_secret: str = ""

    gcp_service_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
