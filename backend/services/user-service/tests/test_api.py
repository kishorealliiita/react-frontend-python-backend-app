import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.models.user import User
from app.core.security import create_access_token
from app.crud.user import create, get_by_email
from app.schemas.user import UserCreate
from app.db.session import engine
from app.db.base import Base

# Create test database tables
Base.metadata.create_all(bind=engine)

client = TestClient(app)

@pytest.fixture
def test_user():
    return {
        "email": "test@example.com",
        "password": "testpassword123",
        "full_name": "Test User"
    }

@pytest.fixture
def test_user_token(test_user):
    return create_access_token({"sub": test_user["email"]})

def test_register_user(test_user):
    response = client.post("/api/v1/users", json=test_user)
    if response.status_code != 201:
        print(f"Response body: {response.json()}")
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == test_user["email"]
    assert data["full_name"] == test_user["full_name"]
    assert "password" not in data

def test_register_existing_user(test_user):
    # First registration
    response = client.post("/api/v1/users", json=test_user)
    assert response.status_code == 201
    # Second registration with same email
    response = client.post("/api/v1/users", json=test_user)
    assert response.status_code == 400
    assert "email already exists" in response.json()["detail"].lower()

def test_login_user(test_user):
    # Register user first
    response = client.post("/api/v1/users", json=test_user)
    assert response.status_code == 201
    # Try to login
    response = client.post("/api/v1/auth/login", data={
        "username": test_user["email"],
        "password": test_user["password"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(test_user):
    response = client.post("/api/v1/auth/login", data={
        "username": test_user["email"],
        "password": "wrongpassword"
    })
    assert response.status_code == 400
    assert "incorrect email or password" in response.json()["detail"].lower()

def test_get_current_user(test_user, test_user_token):
    # Register user first
    response = client.post("/api/v1/users", json=test_user)
    assert response.status_code == 201
    # Get current user
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user["email"]
    assert data["full_name"] == test_user["full_name"]

def test_read_main():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the User Service API"}

def test_create_user(client: TestClient, superuser_token_headers: dict):
    """Test user creation endpoint."""
    data = {
        "email": "newuser@example.com",
        "password": "testpassword123",
        "full_name": "New User",
        "is_active": True,
        "is_superuser": False,
    }
    response = client.post(
        "/api/v1/users/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 201
    content = response.json()
    assert content["email"] == data["email"]
    assert content["full_name"] == data["full_name"]
    assert "id" in content

def test_read_users(client: TestClient, superuser_token_headers: dict):
    """Test reading users endpoint."""
    response = client.get("/api/v1/users/", headers=superuser_token_headers)
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)

def test_read_user_me(client: TestClient, normal_user_token_headers: dict):
    """Test reading current user endpoint."""
    response = client.get("/api/v1/users/me", headers=normal_user_token_headers)
    assert response.status_code == 200
    content = response.json()
    assert content["email"] == "user@example.com"

def test_update_user_me(client: TestClient, normal_user_token_headers: dict):
    """Test updating current user endpoint."""
    data = {"full_name": "Updated Name"}
    response = client.put(
        "/api/v1/users/me",
        headers=normal_user_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["full_name"] == data["full_name"]

def test_login_access_token(client: TestClient, test_user: dict):
    """Test login endpoint."""
    response = client.post(
        "/api/v1/login/access-token",
        data={
            "username": test_user["email"],
            "password": test_user["password"],
        },
    )
    assert response.status_code == 200
    content = response.json()
    assert "access_token" in content
    assert content["token_type"] == "bearer" 