from fastapi import APIRouter, Depends
from app.security import verify_token

router = APIRouter(tags=["History"])

@router.get("/history")
def history(user=Depends(verify_token)):
    return {"module": "history", "data": []}
