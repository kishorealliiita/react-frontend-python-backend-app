import pytest
from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.category import Category
from app.db.base import Base
from app.db.session import engine

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

def test_create_product(db):
    product = Product(
        name="Test Product",
        description="Test Description",
        price=99.99,
        category="Electronics",
        image="test-image.jpg"
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    
    assert product.id is not None
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 99.99
    assert product.category == "Electronics"
    assert product.image == "test-image.jpg"

def test_create_category(db):
    category = Category(name="Electronics")
    db.add(category)
    db.commit()
    db.refresh(category)
    
    assert category.id is not None
    assert category.name == "Electronics"

def test_product_category_relationship(db):
    # Create a category
    category = Category(name="Electronics")
    db.add(category)
    db.commit()
    
    # Create a product with the category
    product = Product(
        name="Test Product",
        description="Test Description",
        price=99.99,
        category=category.name,
        image="test-image.jpg"
    )
    db.add(product)
    db.commit()
    
    # Verify the relationship
    assert product.category == category.name
    assert category.name in [p.category for p in category.products]

def test_update_product(db):
    # Create a product
    product = Product(
        name="Test Product",
        description="Test Description",
        price=99.99,
        category="Electronics",
        image="test-image.jpg"
    )
    db.add(product)
    db.commit()
    
    # Update the product
    product.price = 149.99
    db.commit()
    db.refresh(product)
    
    assert product.price == 149.99

def test_delete_product(db):
    # Create a product
    product = Product(
        name="Test Product",
        description="Test Description",
        price=99.99,
        category="Electronics",
        image="test-image.jpg"
    )
    db.add(product)
    db.commit()
    
    # Delete the product
    db.delete(product)
    db.commit()
    
    # Verify it's deleted
    deleted_product = db.query(Product).filter_by(id=product.id).first()
    assert deleted_product is None 