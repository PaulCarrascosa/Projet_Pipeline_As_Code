"""User service with business logic"""
from sqlalchemy.orm import Session
from typing import List, Optional
from ...models import User
from ...repositories.base import BaseRepository
from ...api.schemas.users import UserCreate, UserUpdate


class UserRepository(BaseRepository):
    """Repository for User model"""
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.db.query(self.model).filter(self.model.email == email).first()


class UserService:
    """Service for user-related operations"""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(User, db)

    def get_user(self, user_id: int) -> Optional[User]:
        """Get a user by ID"""
        return self.repository.get(user_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get a user by email"""
        return self.repository.get_by_email(email)

    def list_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """List all users with pagination"""
        return self.repository.get_multi(skip=skip, limit=limit)

    def create_user(self, user_in: UserCreate) -> User:
        """Create a new user"""
        return self.repository.create(obj_in=user_in)

    def update_user(self, user_id: int, user_in: UserUpdate) -> Optional[User]:
        """Update an existing user"""
        user = self.repository.get(user_id)
        if user:
            return self.repository.update(db_obj=user, obj_in=user_in)
        return None

    def delete_user(self, user_id: int) -> Optional[User]:
        """Delete a user"""
        return self.repository.remove(id=user_id)
