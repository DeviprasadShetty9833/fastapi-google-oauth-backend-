# fastapi-google-oauth-backend-

Demo Video Link:

# 💡 Objective:
You are tasked with building a FastAPI-based backend for a food ordering platform. This
backend must support Google OAuth login, and maintain data about customers, payments,
orders, and restaurants. The system should ensure orders can only be placed after a
successful payment and should be able to generate complex analytical reports such as
earnings by food type or location.

# 🧪 Tasks
📌 A. DB Schema Creation
- Create SQL tables with foreign keys and constraints.
- Use ENUMs and proper indexing where necessary.

📌 B. Google OAuth
- Implement Google Login with OAuth2.
- On login, create a new user if they don’t exist using google_id.
- Return JWT token on success.

📌 C. Order Flow Logic
- A user can only place an order if the payment status is pass.
- Ensure validations are handled.

# 🔍 Queries to Implement
👉 1. Total earnings of restaurants in Mumbai last month
- Only include successful payments and completed orders.

👉 2. Total earnings from veg items in Bangalore
- Veg items: veg manchurian, veg fried rice.

👉 3. Top 3 customers with most orders placed
- Return customer name and number of orders.

👉 4. Daily revenue for past 7 days per city
- Group by date and area.

👉 5. Orders summary for a specific restaurant
- Total orders by item name and count.
