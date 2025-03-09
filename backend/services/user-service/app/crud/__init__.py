"""
CRUD operations package
"""
from app.crud.user import (
    get,
    get_by_email,
    get_multi,
    create,
    update,
    authenticate,
    is_active,
    is_superuser,
)

class CRUDUser:
    def get(self, db, id):
        return get(db, id)

    def get_by_email(self, db, email):
        return get_by_email(db, email)

    def get_multi(self, db, skip=0, limit=100):
        return get_multi(db, skip=skip, limit=limit)

    def create(self, db, obj_in):
        return create(db, obj_in)

    def update(self, db, db_obj, obj_in):
        return update(db, db_obj, obj_in)

    def authenticate(self, db, email, password):
        return authenticate(db, email=email, password=password)

    def is_active(self, user):
        return is_active(user)

    def is_superuser(self, user):
        return is_superuser(user)

user = CRUDUser()

__all__ = ["user"] 