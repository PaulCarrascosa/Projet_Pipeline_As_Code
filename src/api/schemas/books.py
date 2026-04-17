"""Pydantic schemas for books"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BookBase(BaseModel):
    """Base schema for book"""
    title: str
    author: str
    isbn: str
    description: Optional[str] = None
    available_copies: int = 1
    total_copies: int = 1


class BookCreate(BookBase):
    """Schema for creating a book"""
    pass


class BookUpdate(BaseModel):
    """Schema for updating a book"""
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    available_copies: Optional[int] = None
    total_copies: Optional[int] = None


class Book(BookBase):
    """Schema for book response"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
