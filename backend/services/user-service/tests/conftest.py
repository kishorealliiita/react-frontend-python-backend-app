import os
import sys
from pathlib import Path
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.core.config import settings
import uuid
from typing import Generator, Dict
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.db.session import SessionLocal
from app.core.security import create_access_token
from app.models.user import User

# Add the project root directory to the Python path
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

# Set TESTING environment variable
os.environ["TESTING"] = "1"

# Test database URL
TEST_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="session")
def db_engine():
    # Create engine with test database URL
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    
    # Drop and recreate tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    yield engine
    
    # Drop tables and close engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()

@pytest.fixture(scope="session")
def db() -> Generator:
    """Create a fresh database session for each test."""
    connection = SessionLocal()
    try:
        yield connection
    finally:
        connection.close()

@pytest.fixture(scope="module")
def client() -> Generator:
    """Create a test client for the FastAPI application."""
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def test_user(db: Session) -> Dict[str, str]:
    """Create a test user and return its credentials."""
    user = User(
        email="test@example.com",
        hashed_password="hashed_password",
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    access_token = create_access_token(subject=user.email)
    return {
        "email": user.email,
        "password": "test_password",
        "access_token": access_token,
        "token_type": "bearer"
    }

@pytest.fixture(scope="module")
def superuser_token_headers(db: Session) -> Dict[str, str]:
    """Create a superuser and return its authentication headers."""
    user = User(
        email="admin@example.com",
        hashed_password="hashed_password",
        is_active=True,
        is_superuser=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    access_token = create_access_token(subject=user.email)
    return {"Authorization": f"Bearer {access_token}"}

@pytest.fixture(scope="module")
def normal_user_token_headers(db: Session) -> Dict[str, str]:
    """Create a normal user and return its authentication headers."""
    user = User(
        email="user@example.com",
        hashed_password="hashed_password",
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    access_token = create_access_token(subject=user.email)
    return {"Authorization": f"Bearer {access_token}"} 