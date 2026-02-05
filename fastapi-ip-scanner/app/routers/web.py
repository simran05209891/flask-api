from fastapi import APIRouter, Depends, Query
from app.security import verify_token

router = APIRouter(tags=["Web"])

@router.get("/scan/web")
def web_scan(target: str = Query(...), user=Depends(verify_token)):
    return {"module": "web", "target": target, "result": "Web scan completed"}
