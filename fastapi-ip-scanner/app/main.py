from fastapi import FastAPI
from app.middleware import add_middlewares

from app.routers import (
    auth,
    home,
    recon,
    fast,
    deep,
    web,
    ssl_routes,
    history,
    stats,
    health,
    cloud
)

app = FastAPI(
    title="Enterprise VAPT Security Dashboard",
    version="2.0.0",
    description="Secure VAPT platform with JWT authentication, captcha validation, scan modules and cloud integration."
)

add_middlewares(app)

app.include_router(auth.router)
app.include_router(home.router)
app.include_router(recon.router)
app.include_router(fast.router)
app.include_router(deep.router)
app.include_router(web.router)
app.include_router(ssl_routes.router)
app.include_router(history.router)
app.include_router(stats.router)
app.include_router(health.router)
app.include_router(cloud.router)
