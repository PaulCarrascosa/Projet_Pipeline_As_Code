"""Books SQLAlchemy model"""
from sqlalchemy import Column, String, Integer
from .base import Base


class Book(Base):
    """Book model"""
    __tablename__ = "books"
    
    title = Column(String(255), index=True)
    author = Column(String(255))
    isbn = Column(String(13), unique=True, index=True)
    description = Column(String(1000), nullable=True)
    available_copies = Column(Integer, default=1)
    total_copies = Column(Integer, default=1)
