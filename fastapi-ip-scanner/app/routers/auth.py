from fastapi import APIRouter, HTTPException
from app.schemas import LoginRequest, LoginResponse
from app.security import create_access_token
from app.config import settings
from app.routers.captcha import validate_captcha

router = APIRouter(prefix="/api", tags=["Auth"])

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    validate_captcha(payload.captcha)

    if payload.email != settings.ADMIN_EMAIL or payload.password != settings.ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": payload.email})
    return {"token": token, "token_type": "bearer"}

@router.post("/logout")
def logout():
    # JWT logout usually frontend side token remove
    return {"message": "Logged out successfully"}
