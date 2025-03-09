# E-commerce Platform

A modern, scalable e-commerce platform built with microservices architecture.

## Project Structure

```
.
├── backend/
│   └── services/
│       ├── user-service/     # User management service
│       └── product-service/  # Product catalog service
└── frontend/
    └── ecommerce-app/       # React-based frontend application
```

## Features

### Backend Services

#### User Service
- User registration and authentication
- JWT-based authentication
- Role-based access control
- User profile management
- API versioning
- Feature flags
- Comprehensive test coverage

#### Product Service
- Product catalog management
- Category management
- Product search and filtering
- Inventory tracking
- API versioning
- Feature flags

### Frontend Application
- Modern React-based UI
- Redux state management
- Material-UI components
- Responsive design
- TypeScript support
- Hot module replacement

## Prerequisites

- Python 3.11+
- Node.js 18+
- Poetry (Python package manager)
- npm or yarn
- PostgreSQL

## Development Setup

### Backend Services

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Set up each service:
```bash
cd backend/services/user-service
poetry install
poetry run dev setup

cd ../product-service
poetry install
poetry run dev setup
```

3. Create `.env` files in each service directory with required environment variables:

```env
# Common variables for all services
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Service-specific variables
SERVICE_NAME=user-service  # or product-service
SERVICE_PORT=8000         # or 8001
```

### Frontend Application

1. Install dependencies:
```bash
cd frontend/ecommerce-app
npm install
```

2. Create `.env` file:
```env
VITE_API_URL=http://localhost:8000
VITE_PRODUCT_API_URL=http://localhost:8001
```

## Development Commands

### Backend Services

```bash
# Start development server
poetry run dev server

# Run tests
poetry run dev test
poetry run dev test --coverage

# Run linting
poetry run dev lint

# Format code
poetry run dev format

# Watch for changes and run tests
poetry run dev watch
```

### Frontend Application

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run tests
npm test

# Run linting
npm run lint
```

## API Documentation

Once the services are running, you can access the API documentation:

- User Service API: http://localhost:8000/docs
- Product Service API: http://localhost:8001/docs

## Development Workflow

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "feat: your feature description"
```

3. Push your changes:
```bash
git push origin feature/your-feature-name
```

4. Create a pull request

## Testing

### Backend Services

- Unit tests: `poetry run dev test`
- Coverage report: `poetry run dev test --coverage`
- Integration tests: `poetry run dev test --integration`

### Frontend Application

- Unit tests: `npm test`
- E2E tests: `npm run test:e2e`

## Code Quality

- All code is formatted using Black and isort
- Type checking is enforced with mypy
- Linting is done with flake8
- Pre-commit hooks ensure code quality before commits

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 