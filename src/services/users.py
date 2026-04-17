"""Users service"""
from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.users import User
from ..repositories.users import UserRepository


class UserService:
    """Service for user operations"""
    
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
        """List all users"""
        return self.repository.get_multi(skip=skip, limit=limit)
    
    def get_active_users(self) -> List[User]:
        """Get active users"""
        return self.repository.get_active_users()
