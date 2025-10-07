from sqlalchemy.orm import Session
from . import models, schemas

# Customer CRUD functions
def get_user_by_google_id(db: Session, google_id: str):
    return db.query(models.Customer).filter(models.Customer.google_id == google_id).first()

def create_user(db: Session, user: schemas.CustomerCreate):
    db_user = models.Customer(name=user.name, google_id=user.google_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Payment CRUD functions (example)
def get_payment(db: Session, transaction_id: int):
    return db.query(models.Payment).filter(models.Payment.transaction_id == transaction_id).first()

# Order CRUD functions
def create_user_order(db: Session, order: schemas.OrderCreate, user_id: int):
    db_order = models.Order(**order.dict(), customer_id=user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order