# Food Ordering Platform - FastAPI Backend

This project is a FastAPI-based backend for a food ordering platform. It includes features like Google OAuth authentication, order processing, payment validation, and analytical reporting.

## Features

-   **User Authentication**: Secure login via Google OAuth2.
-   **Order Management**: Logic to place orders only after successful payment.
-   **Database Integration**: Uses SQLAlchemy to interact with a PostgreSQL database.
-   **Data Validation**: Pydantic models for robust request and response validation.
-   **Analytics**: Endpoints to derive business insights from the data.

## Project Structure

/food_ordering_project
├── /app                  # Main application source code
├── /frontend
├── /migrations           # Database migration scripts (Alembic)
├── /venv   
├── README.md
├── .env                  # Environment variables (local)
├── .env.example          # Example environment variables
├── alembic.ini           # Alembic configuration
├── requirements.txt      # Python dependencies
└── sql_schema.sql        # Raw SQL schema for reference

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd food_ordering_project
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Copy the `.env.example` file to `.env` and fill in your database and security credentials.
    ```bash
    cp .env.example .env
    ```

5.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.
