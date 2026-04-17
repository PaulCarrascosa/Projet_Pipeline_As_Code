"""Books schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BookBase(BaseModel):
    """Base Book schema"""
    title: str
    author: str
    isbn: str
    description: Optional[str] = None
    available_copies: int = 1
    total_copies: int = 1


class BookCreate(BookBase):
    """Book creation schema"""
    pass


class BookUpdate(BaseModel):
    """Book update schema"""
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    available_copies: Optional[int] = None
    total_copies: Optional[int] = None


class Book(BookBase):
    """Book response schema"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
