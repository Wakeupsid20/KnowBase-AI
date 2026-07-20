from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.document import router as document_router
from app.core.config import settings
from app.core.database import Base, engine
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered document knowledge base",
)

app.include_router(auth_router)
app.include_router(document_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME} 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": settings.APP_VERSION
    }