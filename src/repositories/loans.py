"""Loan repository implementations"""
from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime
from ...models import Loan
from .base import BaseRepository
from ...api.schemas.loans import LoanCreate, LoanUpdate


class LoanRepository(BaseRepository[Loan, LoanCreate, LoanUpdate]):
    """Repository for Loan model"""
    
    def get_active_loans_by_user(self, user_id: int) -> List[Loan]:
        """Get active (unreturned) loans for a user"""
        return self.db.query(self.model).filter(
            self.model.user_id == user_id,
            self.model.returned_at.is_(None)
        ).all()

    def get_active_loans_by_book(self, book_id: int) -> List[Loan]:
        """Get active loans for a book"""
        return self.db.query(self.model).filter(
            self.model.book_id == book_id,
            self.model.returned_at.is_(None)
        ).all()

    def get_overdue_loans(self) -> List[Loan]:
        """Get overdue loans (unreturned and past due date)"""
        return self.db.query(self.model).filter(
            self.model.returned_at.is_(None),
            self.model.due_date < datetime.utcnow()
        ).all()

    def get_returned_loans_by_user(self, user_id: int) -> List[Loan]:
        """Get returned loans for a user"""
        return self.db.query(self.model).filter(
            self.model.user_id == user_id,
            self.model.returned_at.isnot(None)
        ).all()
