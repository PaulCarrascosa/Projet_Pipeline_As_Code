"""Users routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...api.schemas.users import User, UserCreate, UserUpdate
from ...services.users import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[User])
async def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all users"""
    service = UserService(db)
    return service.list_users(skip=skip, limit=limit)


@router.post("/", response_model=User)
async def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    service = UserService(db)
    return service.repository.create(obj_in=user_in)


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a user by ID"""
    service = UserService(db)
    return service.get_user(user_id)
