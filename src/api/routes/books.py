"""Books routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/")
async def list_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all books"""
    return {"books": [], "total": 0, "skip": skip, "limit": limit}


@router.post("/")
async def create_book(db: Session = Depends(get_db)):
    """Create a new book"""
    return {"id": 1, "message": "Book created"}


@router.get("/{book_id}")
async def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get book by ID"""
    return {"id": book_id, "title": "Sample Book"}
