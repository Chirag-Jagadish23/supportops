from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="SupportOps API",
    description="Internal IT ticket management API",
    version="0.1.0",
)


app.include_router(router)
