from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.api.v1.routers import hello_world_router

_root_path = "/api/v1"

app = FastAPI(
    version="1.0.0",
    redoc_url=None,
    root_path=_root_path
)

app.include_router(hello_world_router, prefix="/hello_world")


@app.get("", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"{_root_path}/docs")
