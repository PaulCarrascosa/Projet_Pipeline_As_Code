"""Book service with business logic"""
from sqlalchemy.orm import Session
from typing import List, Optional
from ...models import Book
from ...repositories.base import BaseRepository
from ...api.schemas.books import BookCreate, BookUpdate


class BookRepository(BaseRepository):
    """Repository for Book model"""
    pass


class BookService:
    """Service for book-related operations"""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = BookRepository(Book, db)

    def get_book(self, book_id: int) -> Optional[Book]:
        """Get a book by ID"""
        return self.repository.get(book_id)

    def list_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        """List all books with pagination"""
        return self.repository.get_multi(skip=skip, limit=limit)

    def create_book(self, book_in: BookCreate) -> Book:
        """Create a new book"""
        return self.repository.create(obj_in=book_in)

    def update_book(self, book_id: int, book_in: BookUpdate) -> Optional[Book]:
        """Update an existing book"""
        book = self.repository.get(book_id)
        if book:
            return self.repository.update(db_obj=book, obj_in=book_in)
        return None

    def delete_book(self, book_id: int) -> Optional[Book]:
        """Delete a book"""
        return self.repository.remove(id=book_id)
