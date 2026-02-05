# app/routes/auth.py
from fastapi import APIRouter, HTTPException, Form
from app.core.config import settings
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username != settings.ADMIN_EMAIL or password != settings.ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}
