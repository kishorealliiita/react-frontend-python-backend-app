import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.security import create_access_token

client = TestClient(app)

@pytest.fixture
def test_product():
    return {
        "name": "Test Product",
        "description": "Test Description",
        "price": 99.99,
        "category": "Electronics",
        "image": "test-image.jpg"
    }

@pytest.fixture
def test_user_token():
    return create_access_token({"sub": "test@example.com"})

def test_create_product(test_product, test_user_token):
    response = client.post(
        "/api/v1/products/",
        json=test_product,
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == test_product["name"]
    assert data["description"] == test_product["description"]
    assert data["price"] == test_product["price"]
    assert data["category"] == test_product["category"]
    assert data["image"] == test_product["image"]

def test_create_product_unauthorized(test_product):
    response = client.post("/api/v1/products/", json=test_product)
    assert response.status_code == 401

def test_get_products(test_user_token):
    response = client.get(
        "/api/v1/products/",
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_product_by_id(test_product, test_user_token):
    # First create a product
    create_response = client.post(
        "/api/v1/products/",
        json=test_product,
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    product_id = create_response.json()["id"]
    
    # Then get it by ID
    response = client.get(
        f"/api/v1/products/{product_id}",
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id
    assert data["name"] == test_product["name"]

def test_get_categories(test_user_token):
    response = client.get(
        "/api/v1/categories/",
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_update_product(test_product, test_user_token):
    # First create a product
    create_response = client.post(
        "/api/v1/products/",
        json=test_product,
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    product_id = create_response.json()["id"]
    
    # Update the product
    updated_product = test_product.copy()
    updated_product["price"] = 149.99
    
    response = client.put(
        f"/api/v1/products/{product_id}",
        json=updated_product,
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == updated_product["price"]

def test_delete_product(test_product, test_user_token):
    # First create a product
    create_response = client.post(
        "/api/v1/products/",
        json=test_product,
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    product_id = create_response.json()["id"]
    
    # Delete the product
    response = client.delete(
        f"/api/v1/products/{product_id}",
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 204
    
    # Verify it's deleted
    get_response = client.get(
        f"/api/v1/products/{product_id}",
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert get_response.status_code == 404 