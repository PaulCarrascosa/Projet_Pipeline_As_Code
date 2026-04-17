"""Users repository"""
from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.users import User
from .base import BaseRepository


class UserRepository(BaseRepository):
    """Repository for User model"""
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.db.query(self.model).filter(self.model.email == email).first()
    
    def get_active_users(self) -> List[User]:
        """Get all active users"""
        return self.db.query(self.model).filter(self.model.is_active == True).all()
