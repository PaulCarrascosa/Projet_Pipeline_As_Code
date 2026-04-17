"""API tests"""


def test_read_root(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_list_books(client):
    """Test list books endpoint"""
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_users(client):
    """Test list users endpoint"""
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_loans(client):
    """Test list loans endpoint"""
    response = client.get("/api/v1/loans/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
