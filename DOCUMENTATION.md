# Library Management System - Architecture & Implementation

## Overview

This is a production-ready FastAPI application implementing a 3-tier architecture with complete DevOps integration.

## Architecture Pattern

### N-Tier Architecture

```
┌─────────────────────────────────────────────┐
│  Presentation Layer (API)                   │
│  ├─ Routes                                  │
│  ├─ Schemas (Pydantic)                      │
│  └─ Dependencies                            │
├─────────────────────────────────────────────┤
│  Business Logic Layer (Services)            │
│  ├─ BookService                             │
│  ├─ UserService                             │
│  └─ LoanService                             │
├─────────────────────────────────────────────┤
│  Data Access Layer (Repositories)           │
│  ├─ BookRepository                          │
│  ├─ UserRepository                          │
│  └─ LoanRepository                          │
├─────────────────────────────────────────────┤
│  Database Layer (SQLAlchemy ORM)            │
│  ├─ Models                                  │
│  ├─ Session Management                      │
│  └─ Migrations (Alembic)                    │
└─────────────────────────────────────────────┘
```

## Component Details

### 1. API Layer (`src/api/`)

**Routes** (`routes/`):
- `health.py` - Health check endpoint
- `books.py` - Book management endpoints
- `users.py` - User management endpoints
- `loans.py` - Loan management endpoints

**Schemas** (`schemas/`):
- Pydantic models for request/response validation
- Automatic OpenAPI documentation
- Type hints and validation

**Dependencies** (`dependencies.py`):
- Database session injection
- Shared dependencies across routes

### 2. Services Layer (`src/services/`)

Business logic implementation:
- `BookService` - Business rules for books
- `UserService` - User operations
- `LoanService` - Loan management logic

Features:
- Data validation
- Business rule enforcement
- Service composition
- Error handling

### 3. Repository Layer (`src/repositories/`)

Data access abstraction:
- `BaseRepository` - Generic CRUD operations
- `BookRepository` - Book-specific queries
- `UserRepository` - User-specific queries
- `LoanRepository` - Loan-specific queries

Pattern: Generic repository with inheritance

### 4. Database Layer

**Models** (`src/models/`):
```python
- User (id, email, password, created_at, updated_at)
- Book (id, title, author, isbn, copies, created_at, updated_at)
- Loan (id, user_id, book_id, due_date, returned_at, created_at, updated_at)
```

**Configuration** (`src/db/`):
- Session factory
- Engine configuration
- Connection pooling

**Migrations** (`alembic/`):
- Schema versioning
- Rollback support
- Automatic generation

## Code Examples

### Creating an Endpoint

```python
# src/api/routes/books.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.books import BookCreate, Book
from ...db.session import get_db

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=Book)
async def create_book(
    book_in: BookCreate,
    db: Session = Depends(get_db)
):
    service = BookService(db)
    return service.create_book(book_in)
```

### Creating a Service

```python
# src/services/books.py
class BookService:
    def __init__(self, db: Session):
        self.repository = BookRepository(Book, db)
    
    def create_book(self, book_in: BookCreate) -> Book:
        return self.repository.create(obj_in=book_in)
```

### Creating a Repository

```python
# src/repositories/books.py
class BookRepository(BaseRepository):
    def get_available_books(self) -> List[Book]:
        return self.db.query(self.model).filter(
            self.model.available_copies > 0
        ).all()
```

## Data Flow Example: Creating a Book

```
1. Client sends POST /api/v1/books
   ↓
2. FastAPI validates request against BookCreate schema
   ↓
3. Dependency injection provides database session
   ↓
4. Route handler creates BookService(db)
   ↓
5. Service creates BookRepository(Book, db)
   ↓
6. Service calls repository.create(obj_in)
   ↓
7. Repository converts to SQLAlchemy model
   ↓
8. Model is added to session and committed
   ↓
9. Database generates ID and timestamps
   ↓
10. Response is serialized to BookResponse schema
    ↓
11. FastAPI returns JSON response with 200 status
```

## Testing Strategy

### Unit Tests

Test individual components:
```python
# tests/test_api/test_books.py
def test_list_books(client, test_db):
    response = client.get("/api/v1/books")
    assert response.status_code == 200
```

### Integration Tests

Test component interactions:
```python
# Test full request/response cycle
def test_create_and_retrieve_book(client, test_db):
    create_resp = client.post("/api/v1/books", json={...})
    book_id = create_resp.json()["id"]
    
    get_resp = client.get(f"/api/v1/books/{book_id}")
    assert get_resp.status_code == 200
```

### Test Database

Using in-memory SQLite for fast tests:
```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
```

## CI/CD Pipeline Stages

```
┌────────────────┐
│    Checkout    │ Clone repository
└────────┬───────┘
         ↓
┌────────────────┐
│  Environment   │ Install Python & dependencies
└────────┬───────┘
         ↓
┌────────────────┐
│     Lint       │ Code quality checks
└────────┬───────┘
         ↓
┌────────────────┐
│     Tests      │ Run test suite
└────────┬───────┘
         ↓
┌────────────────┐
│   SonarQube    │ Code analysis
└────────┬───────┘
         ↓
┌────────────────┐
│    Docker      │ Build image
└────────┬───────┘
         ↓
┌────────────────┐
│     Nexus      │ Push artifact
└────────┬───────┘
         ↓
┌────────────────┐
│    Deploy      │ Release to prod
└────────────────┘
```

## Security Features

### Password Management
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])
hashed = pwd_context.hash("password")
pwd_context.verify("password", hashed)
```

### JWT Tokens
```python
token = create_access_token({"sub": user_id})
payload = decode_token(token)
```

### CORS Configuration
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Database Relationships

```
User (1) ──────────────── (N) Loan (N) ────────────────── (1) Book
  id                      user_id                        book_id
  email                   loan.user_id                    id
  full_name               loan.book_id                    title
  password                                                 author
```

## Configuration Management

Using Pydantic Settings:
```python
class Settings(BaseSettings):
    PROJECT_NAME: str
    DATABASE_URL: str
    DEBUG: bool
    BACKEND_CORS_ORIGINS: List[str]
    
    class Config:
        env_file = ".env"
```

Environment overrides code defaults:
```
.env → Settings → Application
```

## Deployment Options

### Local Development
```bash
python run.py
```

### Docker Container
```bash
docker build -t library-app:latest .
docker run -p 8000:8000 library-app:latest
```

### Docker Compose
```bash
docker-compose up -d
```

### Kubernetes (Future)
- Container-ready (Dockerfile provided)
- Stateless application
- Ready for horizontal scaling

## Performance Considerations

### Database Optimization
- Indexed fields: id, email, isbn, created_at
- Lazy loading via SQLAlchemy relationships
- Query optimization in repositories

### Caching Strategy (Future)
- Redis for session caching
- HTTP caching headers
- Database query results caching

### Pagination
```python
# Prevent fetching too many records
GET /api/v1/books?skip=0&limit=20
```

## Error Handling

Standard HTTP status codes:
- 200: Success
- 400: Bad request (validation error)
- 401: Unauthorized
- 403: Forbidden
- 404: Not found
- 500: Server error

## Logging

Setup logging for:
- Application startup/shutdown
- API requests/responses
- Database operations
- Errors and exceptions

## Future Enhancements

1. **Authentication & Authorization**
   - JWT token management
   - Role-based access control (RBAC)

2. **Advanced Features**
   - Book search/filtering
   - Notification system
   - Email reminders for overdue books

3. **Performance**
   - Redis caching
   - Database query optimization
   - API rate limiting

4. **Monitoring**
   - Application metrics
   - Performance monitoring
   - Error tracking (Sentry)

5. **Documentation**
   - API documentation
   - Architecture diagrams
   - Deployment guides
