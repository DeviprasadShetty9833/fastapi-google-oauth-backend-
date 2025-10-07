import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

# ENUM definitions
class PaymentStatus(str, enum.Enum):
    PASS = "PASS"
    FAIL = "FAIL"

class PaymentType(str, enum.Enum):
    UPI = "UPI"
    CARD = "card"

class FoodItem(str, enum.Enum):
    VEG_MANCHURIAN = "veg manchurian"
    CHICKEN_MANCHURIAN = "chicken manchurian"
    VEG_FRIED_RICE = "veg fried rice"
    CHICKEN_NOODLES = "chicken noodles"

class Area(str, enum.Enum):
    MUMBAI = "Mumbai"
    BANGALORE = "Bangalore"

# Table models
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    google_id = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer)
    orders = relationship("Order", back_populates="customer")

class Payment(Base):
    __tablename__ = "payments"
    transaction_id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(PaymentStatus), nullable=False)
    payment_type = Column(Enum(PaymentType))
    created_at = Column(TIMESTAMP, server_default=func.now())

class Restaurant(Base):
    __tablename__ = "restaurants"
    restaurant_id = Column(Integer, primary_key=True, index=True)
    restaurant_name = Column(String)
    area = Column(Enum(Area))
    orders = relationship("Order", back_populates="restaurant")

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    food_item = Column(Enum(FoodItem))
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Foreign Keys
    transaction_id = Column(Integer, ForeignKey("payments.transaction_id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    
    # Relationships
    #payment = relationship("Payment", back_populates="order")
    customer = relationship("Customer", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")