# backend/database/crud.py
from sqlalchemy.orm import Session
from . import models, connection # . means current package

def create_db_and_tables():
    # This will create all tables defined in models.py that inherit from Base
    models.Base.metadata.create_all(bind=connection.engine)
    print("Database tables created (if they didn't exist).")

# We will add more functions here later, e.g.:
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
# def create_user(db: Session, email: str, hashed_password: str):
#     db_user = models.User(email=email, hashed_password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user