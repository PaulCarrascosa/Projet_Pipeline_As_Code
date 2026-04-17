"""Loan service with business logic"""
from sqlalchemy.orm import Session
from typing import List, Optional
from ...models import Loan
from ...repositories.base import BaseRepository
from ...api.schemas.loans import LoanCreate, LoanUpdate


class LoanRepository(BaseRepository):
    """Repository for Loan model"""
    
    def get_active_loans_by_user(self, user_id: int) -> List[Loan]:
        """Get active loans (not returned) for a user"""
        return self.db.query(self.model).filter(
            self.model.user_id == user_id,
            self.model.returned_at.is_(None)
        ).all()


class LoanService:
    """Service for loan-related operations"""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = LoanRepository(Loan, db)

    def get_loan(self, loan_id: int) -> Optional[Loan]:
        """Get a loan by ID"""
        return self.repository.get(loan_id)

    def list_loans(self, skip: int = 0, limit: int = 100) -> List[Loan]:
        """List all loans with pagination"""
        return self.repository.get_multi(skip=skip, limit=limit)

    def get_user_active_loans(self, user_id: int) -> List[Loan]:
        """Get active loans for a user"""
        return self.repository.get_active_loans_by_user(user_id)

    def create_loan(self, loan_in: LoanCreate) -> Loan:
        """Create a new loan"""
        return self.repository.create(obj_in=loan_in)

    def update_loan(self, loan_id: int, loan_in: LoanUpdate) -> Optional[Loan]:
        """Update an existing loan"""
        loan = self.repository.get(loan_id)
        if loan:
            return self.repository.update(db_obj=loan, obj_in=loan_in)
        return None

    def delete_loan(self, loan_id: int) -> Optional[Loan]:
        """Delete a loan"""
        return self.repository.remove(id=loan_id)
