-- file: sql_schema.sql

-- This schema is for a PostgreSQL database.

-- Create ENUM types for reusable, constrained values.
CREATE TYPE payment_status AS ENUM ('pass', 'fail');
CREATE TYPE payment_type AS ENUM ('UPI', 'card');
CREATE TYPE food_item_type AS ENUM ('veg manchurian', 'chicken manchurian', 'veg fried rice', 'chicken noodles');
CREATE TYPE area_type AS ENUM ('Mumbai', 'Bangalore');

-- Table for Customers, linked to Google OAuth
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    google_id VARCHAR(255) UNIQUE NOT NULL,
    age INTEGER
);

-- Table for Restaurants
CREATE TABLE restaurants (
    restaurant_id SERIAL PRIMARY KEY,
    restaurant_name VARCHAR(255) NOT NULL,
    area area_type
);

-- Table for Payments
CREATE TABLE payments (
    transaction_id SERIAL PRIMARY KEY,
    status payment_status NOT NULL,
    payment_type payment_type,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for Orders, linking everything together
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    food_item food_item_type,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Foreign Keys
    transaction_id INTEGER UNIQUE REFERENCES payments(transaction_id),
    restaurant_id INTEGER REFERENCES restaurants(restaurant_id),
    customer_id INTEGER REFERENCES customers(id)
);

-- Add indexes for frequently queried columns to improve performance.
CREATE INDEX idx_customer_google_id ON customers(google_id);
CREATE INDEX idx_restaurant_area ON restaurants(area);