from fastapi import APIRouter, Depends
from app.security import verify_token

router = APIRouter(tags=["Stats"])

@router.get("/stats")
def stats(user=Depends(verify_token)):
    return {"module": "stats", "total_scans": 0, "critical": 0, "high": 0, "medium": 0, "low": 0}
