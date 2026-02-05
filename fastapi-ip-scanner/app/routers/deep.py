from fastapi import APIRouter, Depends, Query
from app.security import verify_token

router = APIRouter(tags=["Deep Scan"])

@router.get("/scan/deep")
def deep_scan(target: str = Query(...), user=Depends(verify_token)):
    return {"module": "deep", "target": target, "result": "Deep scan completed"}
