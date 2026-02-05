# app/routes/modules.py
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.get("/home")
def home(token: str = Depends(oauth2_scheme)):
    return {"module": "home"}

@router.get("/recon")
def recon(token: str = Depends(oauth2_scheme)):
    return {"module": "recon"}

@router.get("/deep")
def deep(token: str = Depends(oauth2_scheme)):
    return {"module": "deep"}

@router.get("/web")
def web(token: str = Depends(oauth2_scheme)):
    return {"module": "web"}

@router.get("/ssl")
def ssl(token: str = Depends(oauth2_scheme)):
    return {"module": "ssl"}

@router.get("/stats")
def stats(token: str = Depends(oauth2_scheme)):
    return {"module": "stats"}

@router.get("/history")
def history(token: str = Depends(oauth2_scheme)):
    return {"module": "history"}
