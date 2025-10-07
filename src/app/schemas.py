from pydantic import BaseModel
from typing import Optional

# Schemas for Customers
class CustomerBase(BaseModel):
    name: str
    age: Optional[int] = None

class CustomerCreate(CustomerBase):
    google_id: str

class Customer(CustomerBase):
    id: int
    google_id: str

    class Config:
        orm_mode = True

# Schemas for Orders
class OrderCreate(BaseModel):
    food_item: str
    transaction_id: int
    restaurant_id: int

class Order(OrderCreate):
    order_id: int
    customer_id: int

    class Config:
        orm_mode = True

# Schema for Google Token
class TokenData(BaseModel):
    google_id: Optional[str] = None