# file: app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, orders, analytics, payments, restaurants

# This command creates your database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)

# Include the API endpoint routers
app.include_router(auth.router)
app.include_router(orders.router)
app.include_router(analytics.router)
app.include_router(payments.router)
app.include_router(restaurants.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Food Ordering API!"}
