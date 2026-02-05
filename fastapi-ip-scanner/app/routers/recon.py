from fastapi import APIRouter, Depends, Query
from app.security import verify_token

router = APIRouter(tags=["Recon"])

@router.get("/recon")
def recon(target: str = Query(...), user=Depends(verify_token)):
    return {"module": "recon", "target": target, "status": "Recon executed"}
