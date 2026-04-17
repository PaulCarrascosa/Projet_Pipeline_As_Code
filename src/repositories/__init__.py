"""Repository layer for data access"""
from .base import BaseRepository
from .books import BookRepository
from .users import UserRepository
from .loans import LoanRepository

__all__ = ["BaseRepository", "BookRepository", "UserRepository", "LoanRepository"]
