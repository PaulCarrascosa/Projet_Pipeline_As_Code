"""Books repository"""
from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.books import Book
from .base import BaseRepository


class BookRepository(BaseRepository):
    """Repository for Book model"""
    
    def get_by_isbn(self, isbn: str) -> Optional[Book]:
        """Get book by ISBN"""
        return self.db.query(self.model).filter(self.model.isbn == isbn).first()
    
    def get_available_books(self, limit: int = 100) -> List[Book]:
        """Get books with available copies"""
        return self.db.query(self.model).filter(
            self.model.available_copies > 0
        ).limit(limit).all()
