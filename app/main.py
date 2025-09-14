"""FastAPI entry point."""

from fastapi import FastAPI

from .routers import health, v1

app = FastAPI(title="hk-callshield-data-pipeline")

app.include_router(health.router)
app.include_router(v1.router, prefix="/v1")


@app.get("/")
async def root():
    return {"message": "HK Call Shield"}
