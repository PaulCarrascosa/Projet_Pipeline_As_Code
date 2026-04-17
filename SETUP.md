# Library Management System - Setup Guide

## Quick Start

### 1. Clone & Setup Environment

```bash
# Clone the repository
git clone <repo-url>
cd TP1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp .env.example .env
```

### 2. Run Application Locally

```bash
python run.py
```

Visit:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/api/v1/health

### 3. Run with Docker

```bash
docker-compose up -d
```

Services:
- FastAPI: http://localhost:8000
- SonarQube: http://localhost:9000 (admin/admin)
- Nexus: http://localhost:8081 (admin/admin123)

### 4. Run Tests

```bash
pytest tests/ -v --cov=src
```

## Project Structure

```
src/
├── api/                    # REST API Layer
│   ├── routes/            # Endpoints
│   ├── schemas/           # Pydantic models
│   └── dependencies.py    # Shared dependencies
├── services/              # Business logic
├── repositories/          # Data access
├── models/                # SQLAlchemy models
├── utils/                 # Utilities
├── db/                    # Database config
├── config.py              # Settings
└── main.py                # FastAPI app

tests/                      # Unit tests
alembic/                    # Database migrations
```

## Key Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container image |
| `docker-compose.yml` | Multi-service setup |
| `Jenkinsfile` | CI/CD pipeline |
| `sonar-project.properties` | SonarQube config |
| `nexus.properties` | Nexus config |
| `.env.example` | Environment template |

## API Endpoints

### Health
```bash
GET /api/v1/health
```

### Books
```bash
GET    /api/v1/books           # List books
POST   /api/v1/books           # Create book
GET    /api/v1/books/{id}      # Get book
```

### Users
```bash
GET    /api/v1/users           # List users
POST   /api/v1/users           # Create user
GET    /api/v1/users/{id}      # Get user
```

### Loans
```bash
GET    /api/v1/loans           # List loans
POST   /api/v1/loans           # Create loan
GET    /api/v1/loans/{id}      # Get loan
```

## DevOps Integration

### Jenkins Pipeline

The `Jenkinsfile` automates:
1. Code checkout
2. Environment setup
3. Linting & tests
4. SonarQube analysis
5. Docker build
6. Nexus push
7. Deployment

Required Jenkins credentials:
- `SONAR_HOST_URL`: SonarQube server
- `SONAR_LOGIN`: SonarQube token
- `NEXUS_REGISTRY`: Nexus registry URL
- `NEXUS_USER`: Nexus username
- `NEXUS_PASSWORD`: Nexus password

### SonarQube Analysis

```bash
sonar-scanner \
  -Dsonar.projectKey=library-app \
  -Dsonar.sources=src \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=<token>
```

### Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Troubleshooting

### ImportError: No module named 'src'

Make sure:
1. You're in the project root directory
2. Virtual environment is activated
3. Dependencies are installed: `pip install -r requirements.txt`

### Port already in use

Change port in `.env` or run:
```bash
python run.py --port 8001
```

### Docker issues

Clear images and volumes:
```bash
docker-compose down -v
docker-compose up -d
```

## Next Steps

1. **Implement full CRUD** for each resource
2. **Add authentication** with JWT tokens
3. **Create request validators** with Pydantic
4. **Write more tests** for business logic
5. **Setup CI/CD** with Jenkins
6. **Deploy to production** environment

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Docker Compose](https://docs.docker.com/compose/)
- [SonarQube Guide](https://docs.sonarqube.org/)
- [Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/)
