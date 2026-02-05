from fastapi import APIRouter, Depends
from app.security import verify_token

router = APIRouter(tags=["Home"])

@router.get("/")
def home():
    return {"message": "Enterprise VAPT Security Dashboard Running"}

@router.get("/home")
def home_ui(user=Depends(verify_token)):
    return {"module": "home", "status": "ok"}
