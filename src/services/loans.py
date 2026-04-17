"""Loans service"""
from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.loans import Loan
from ..repositories.loans import LoanRepository


class LoanService:
    """Service for loan operations"""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = LoanRepository(Loan, db)
    
    def get_loan(self, loan_id: int) -> Optional[Loan]:
        """Get a loan by ID"""
        return self.repository.get(loan_id)
    
    def list_loans(self, skip: int = 0, limit: int = 100) -> List[Loan]:
        """List all loans"""
        return self.repository.get_multi(skip=skip, limit=limit)
    
    def get_user_active_loans(self, user_id: int) -> List[Loan]:
        """Get active loans for a user"""
        return self.repository.get_active_loans_by_user(user_id)
    
    def get_overdue_loans(self) -> List[Loan]:
        """Get overdue loans"""
        return self.repository.get_overdue_loans()
