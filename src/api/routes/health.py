"""Health check routes"""
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", tags=["health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
