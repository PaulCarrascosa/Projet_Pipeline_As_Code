"""Users SQLAlchemy model"""
from sqlalchemy import Column, String, Boolean
from .base import Base


class User(Base):
    """User model"""
    __tablename__ = "users"
    
    email = Column(String(255), unique=True, index=True)
    full_name = Column(String(255))
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
