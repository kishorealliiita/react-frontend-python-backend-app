from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps
from app.schemas.product import Product, ProductCreate, ProductUpdate

router = APIRouter()

@router.get("/", response_model=List[Product])
def read_products(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    active_only: bool = False,
):
    """
    Retrieve products.
    """
    if active_only:
        products = crud.product.get_active_products(db, skip=skip, limit=limit)
    else:
        products = crud.product.get_multi(db, skip=skip, limit=limit)
    return products

@router.post("/", response_model=Product)
def create_product(
    *,
    db: Session = Depends(deps.get_db),
    product_in: ProductCreate,
):
    """
    Create new product.
    """
    product = crud.product.get_by_sku(db, sku=product_in.sku)
    if product:
        raise HTTPException(
            status_code=400,
            detail="The product with this SKU already exists in the system.",
        )
    product = crud.product.create(db, obj_in=product_in)
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(
    *,
    db: Session = Depends(deps.get_db),
    product_id: int,
    product_in: ProductUpdate,
):
    """
    Update a product.
    """
    product = crud.product.get(db, id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud.product.update(db, db_obj=product, obj_in=product_in)
    return product

@router.get("/{product_id}", response_model=Product)
def read_product(
    *,
    db: Session = Depends(deps.get_db),
    product_id: int,
):
    """
    Get product by ID.
    """
    product = crud.product.get(db, id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/{product_id}", response_model=Product)
def delete_product(
    *,
    db: Session = Depends(deps.get_db),
    product_id: int,
):
    """
    Delete a product.
    """
    product = crud.product.get(db, id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud.product.remove(db, id=product_id)
    return product

@router.get("/category/{category_id}", response_model=List[Product])
def read_products_by_category(
    category_id: int,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve products by category.
    """
    products = crud.product.get_by_category(
        db, category_id=category_id, skip=skip, limit=limit
    )
    return products 