from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps
from app.schemas.product import Category, CategoryCreate, CategoryUpdate

router = APIRouter()

@router.get("/", response_model=List[Category])
def read_categories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve categories.
    """
    categories = crud.category.get_multi(db, skip=skip, limit=limit)
    return categories

@router.post("/", response_model=Category)
def create_category(
    *,
    db: Session = Depends(deps.get_db),
    category_in: CategoryCreate,
):
    """
    Create new category.
    """
    category = crud.category.get_by_name(db, name=category_in.name)
    if category:
        raise HTTPException(
            status_code=400,
            detail="The category with this name already exists in the system.",
        )
    category = crud.category.create(db, obj_in=category_in)
    return category

@router.put("/{category_id}", response_model=Category)
def update_category(
    *,
    db: Session = Depends(deps.get_db),
    category_id: int,
    category_in: CategoryUpdate,
):
    """
    Update a category.
    """
    category = crud.category.get(db, id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category = crud.category.update(db, db_obj=category, obj_in=category_in)
    return category

@router.get("/{category_id}", response_model=Category)
def read_category(
    *,
    db: Session = Depends(deps.get_db),
    category_id: int,
):
    """
    Get category by ID.
    """
    category = crud.category.get(db, id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}", response_model=Category)
def delete_category(
    *,
    db: Session = Depends(deps.get_db),
    category_id: int,
):
    """
    Delete a category.
    """
    category = crud.category.get(db, id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category = crud.category.remove(db, id=category_id)
    return category 