"""Books service"""
from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.books import Book
from ..repositories.books import BookRepository


class BookService:
    """Service for book operations"""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = BookRepository(Book, db)
    
    def get_book(self, book_id: int) -> Optional[Book]:
        """Get a book by ID"""
        return self.repository.get(book_id)
    
    def list_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        """List all books"""
        return self.repository.get_multi(skip=skip, limit=limit)
    
    def get_available_books(self) -> List[Book]:
        """Get available books"""
        return self.repository.get_available_books()
