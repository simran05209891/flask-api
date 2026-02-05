from fastapi import APIRouter, Depends, Query
from app.security import verify_token

router = APIRouter(tags=["Fast Scan"])

@router.get("/scan/fast")
def fast_scan(target: str = Query(...), user=Depends(verify_token)):
    return {"module": "fast", "target": target, "result": "Fast scan completed"}
