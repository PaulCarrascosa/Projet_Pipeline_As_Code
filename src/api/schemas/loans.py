"""Loans schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LoanBase(BaseModel):
    """Base Loan schema"""
    user_id: int
    book_id: int
    due_date: datetime


class LoanCreate(LoanBase):
    """Loan creation schema"""
    pass


class LoanUpdate(BaseModel):
    """Loan update schema"""
    due_date: Optional[datetime] = None
    returned_at: Optional[datetime] = None


class Loan(LoanBase):
    """Loan response schema"""
    id: int
    returned_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
