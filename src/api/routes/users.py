"""Users routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all users"""
    return {"users": [], "total": 0, "skip": skip, "limit": limit}


@router.post("/")
async def create_user(db: Session = Depends(get_db)):
    """Create a new user"""
    return {"id": 1, "message": "User created"}


@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID"""
    return {"id": user_id, "email": "user@example.com"}
