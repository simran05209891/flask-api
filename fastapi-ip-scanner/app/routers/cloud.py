from fastapi import APIRouter, Depends
from app.security import verify_token
from app.config import settings

router = APIRouter(tags=["Cloud"])

@router.get("/cloud/infrastructure")
def cloud_infra(user=Depends(verify_token)):
    return {
        "aws": {
            "status": "connected" if settings.AWS_ACCESS_KEY else "not_configured",
            "tier": "premium"
        },
        "azure": {
            "status": "connected" if settings.AZURE_CLIENT_ID else "not_configured",
            "tier": "premium"
        },
        "gcp": {
            "status": "connected" if settings.GCP_SERVICE_KEY else "not_configured",
            "tier": "premium"
        }
    }
