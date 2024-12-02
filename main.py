import os

import uvicorn

from app.api import app

uvicorn.run(
    app,
    host=os.getenv("APP_HOST", "localhost"),
    port=int(os.getenv("APP_PORT", 8000))
)
