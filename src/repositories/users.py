"""User repository implementations"""
from typing import List, Optional
from sqlalchemy.orm import Session
from ...models import User
from .base import BaseRepository
from ...api.schemas.users import UserCreate, UserUpdate


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    """Repository for User model"""
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.db.query(self.model).filter(
            self.model.email == email
        ).first()

    def get_active_users(self) -> List[User]:
        """Get all active users"""
        return self.db.query(self.model).filter(
            self.model.is_active == True
        ).all()

    def search_by_full_name(self, name: str) -> List[User]:
        """Search users by full name"""
        return self.db.query(self.model).filter(
            self.model.full_name.ilike(f"%{name}%")
        ).all()
