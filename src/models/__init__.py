"""SQLAlchemy models for domain entities"""
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    """User model for library system"""
    __tablename__ = "users"
    
    email = Column(String(255), unique=True, index=True)
    full_name = Column(String(255))
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    
    loans = relationship("Loan", back_populates="user")


class Book(Base):
    """Book model for library system"""
    __tablename__ = "books"
    
    title = Column(String(255), index=True)
    author = Column(String(255))
    isbn = Column(String(13), unique=True, index=True)
    description = Column(String(1000))
    available_copies = Column(Integer, default=1)
    total_copies = Column(Integer, default=1)
    
    loans = relationship("Loan", back_populates="book")


class Loan(Base):
    """Loan model for tracking book loans"""
    __tablename__ = "loans"
    
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    returned_at = Column(DateTime, nullable=True)
    due_date = Column(DateTime)
    
    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")
