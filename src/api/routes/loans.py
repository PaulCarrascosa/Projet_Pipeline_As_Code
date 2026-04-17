"""Loans routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db

router = APIRouter(prefix="/loans", tags=["loans"])


@router.get("/")
async def list_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all loans"""
    return {"loans": [], "total": 0, "skip": skip, "limit": limit}


@router.post("/")
async def create_loan(db: Session = Depends(get_db)):
    """Create a new loan"""
    return {"id": 1, "message": "Loan created"}


@router.get("/{loan_id}")
async def get_loan(loan_id: int, db: Session = Depends(get_db)):
    """Get loan by ID"""
    return {"id": loan_id, "user_id": 1, "book_id": 1}
