"""Pydantic schemas for loans"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LoanBase(BaseModel):
    """Base schema for loan"""
    user_id: int
    book_id: int
    due_date: datetime


class LoanCreate(LoanBase):
    """Schema for creating a loan"""
    pass


class LoanUpdate(BaseModel):
    """Schema for updating a loan"""
    due_date: Optional[datetime] = None
    returned_at: Optional[datetime] = None


class Loan(LoanBase):
    """Schema for loan response"""
    id: int
    returned_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
