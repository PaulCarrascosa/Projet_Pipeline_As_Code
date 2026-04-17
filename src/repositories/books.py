"""Book repository implementations"""
from typing import List, Optional
from sqlalchemy.orm import Session
from ...models import Book
from .base import BaseRepository
from ...api.schemas.books import BookCreate, BookUpdate


class BookRepository(BaseRepository[Book, BookCreate, BookUpdate]):
    """Repository for Book model"""
    
    def get_by_isbn(self, isbn: str) -> Optional[Book]:
        """Get book by ISBN"""
        return self.db.query(self.model).filter(self.model.isbn == isbn).first()

    def get_available_books(self, limit: int = 100) -> List[Book]:
        """Get books with available copies"""
        return self.db.query(self.model).filter(
            self.model.available_copies > 0
        ).limit(limit).all()

    def search_by_title(self, title: str) -> List[Book]:
        """Search books by title"""
        return self.db.query(self.model).filter(
            self.model.title.ilike(f"%{title}%")
        ).all()

    def search_by_author(self, author: str) -> List[Book]:
        """Search books by author"""
        return self.db.query(self.model).filter(
            self.model.author.ilike(f"%{author}%")
        ).all()
