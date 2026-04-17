"""Loans routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...api.schemas.loans import Loan, LoanCreate, LoanUpdate
from ...services.loans import LoanService

router = APIRouter(prefix="/loans", tags=["loans"])


@router.get("/", response_model=list[Loan])
async def list_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all loans"""
    service = LoanService(db)
    return service.list_loans(skip=skip, limit=limit)


@router.post("/", response_model=Loan)
async def create_loan(loan_in: LoanCreate, db: Session = Depends(get_db)):
    """Create a new loan"""
    service = LoanService(db)
    return service.repository.create(obj_in=loan_in)


@router.get("/{loan_id}", response_model=Loan)
async def get_loan(loan_id: int, db: Session = Depends(get_db)):
    """Get a loan by ID"""
    service = LoanService(db)
    return service.get_loan(loan_id)
