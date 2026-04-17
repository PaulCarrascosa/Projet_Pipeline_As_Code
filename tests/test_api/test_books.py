"""Books API endpoint tests"""
import pytest


def test_list_books(client, test_db):
    """Test listing books"""
    response = client.get("/api/v1/books")
    assert response.status_code == 200
    data = response.json()
    assert "books" in data


def test_create_book(client, test_db):
    """Test creating a book"""
    response = client.post("/api/v1/books")
    assert response.status_code == 200


def test_get_book(client, test_db):
    """Test getting a book by ID"""
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
