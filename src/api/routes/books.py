"""Books routes"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...api.schemas.books import Book, BookCreate, BookUpdate
from ...services.books import BookService

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[Book])
async def list_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all books"""
    service = BookService(db)
    return service.list_books(skip=skip, limit=limit)


@router.post("/", response_model=Book)
async def create_book(book_in: BookCreate, db: Session = Depends(get_db)):
    """Create a new book"""
    service = BookService(db)
    return service.repository.create(obj_in=book_in)


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get a book by ID"""
    service = BookService(db)
    return service.get_book(book_id)
