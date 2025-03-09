# User Service

A FastAPI-based microservice for user management in the backend system.

## Features

- User registration and authentication
- JWT-based authentication
- Role-based access control
- User profile management
- API versioning
- Feature flags
- Comprehensive test coverage
- Development tools and scripts

## Development Setup

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Set up pre-commit hooks:
```bash
poetry run pre-commit install
```

4. Run the development server:
```bash
poetry run dev server
```

## Development Commands

- `poetry run dev server`: Start the development server
- `poetry run dev test`: Run tests
- `poetry run dev lint`: Run code linting
- `poetry run dev format`: Format code
- `poetry run dev watch`: Watch for changes and run tests

## Testing

Run tests with coverage:
```bash
poetry run dev test --coverage
```

## Code Quality

- Format code: `poetry run dev format`
- Run linting: `poetry run dev lint`
- Type checking: `poetry run mypy .`

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

Create a `.env` file with the following variables:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## License

MIT 