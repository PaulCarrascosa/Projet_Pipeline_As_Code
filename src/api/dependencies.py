"""API dependencies"""
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.session import get_db

# Re-export common dependencies
__all__ = ["get_db"]
