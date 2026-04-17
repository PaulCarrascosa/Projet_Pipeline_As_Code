"""Loans SQLAlchemy model"""
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from .base import Base


class Loan(Base):
    """Loan model"""
    __tablename__ = "loans"
    
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    due_date = Column(DateTime)
    returned_at = Column(DateTime, nullable=True)
