"""Loans repository"""
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from ..models.loans import Loan
from .base import BaseRepository


class LoanRepository(BaseRepository):
    """Repository for Loan model"""
    
    def get_active_loans_by_user(self, user_id: int) -> List[Loan]:
        """Get active loans for a user"""
        return self.db.query(self.model).filter(
            self.model.user_id == user_id,
            self.model.returned_at.is_(None)
        ).all()
    
    def get_overdue_loans(self) -> List[Loan]:
        """Get overdue loans"""
        return self.db.query(self.model).filter(
            self.model.returned_at.is_(None),
            self.model.due_date < datetime.utcnow()
        ).all()
