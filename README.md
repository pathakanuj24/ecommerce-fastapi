# eCommerce-fast API
This repository contains the backend code for an e-commerce application built using FastAPI and Python.

## Features
The API exposes the following endpoints:

- GET /products: API to list all available products in the system
- POST /create_order to create a new order
- GET /get_order to fetch all orders from the system with pagination
- GET /get_order/{order_id} to fetch a single order from the system using the Order ID
- PUT /products/{products_id} to update a product quantity

## Requirements

- Python 3.7+
- FastAPI
- uvicorn
- pydantic
  
## Installation

1. Clone the repository.
   ```bash
   git clone https://github.com/pathakanuj24/ecommerce-fastapi.git

2. install dependencies by using pip
    ```bash
    pip install requirements.txt
    
3. Run this command to start the application in local env.
   ```bash
   uvicorn api:app --reload

## Working of API endpoints
## 1. API to list all available products (GET /products):
  - This endpoint retrieves a list of all available products in the system.
  - When a GET request is made to /products, the server responds with the list of products.
  - The list of products is stored in the products variable in the backend code.
  - The response contains the details of each product, including the product name, price, and available quantity.

## 2. API to create a new order (POST /orders):
- This endpoint allows you to create a new order.
- When a POST request is made to /orders with the order details in the request body, the server processes the request.
- The order details include a timestamp, items (a list of products bought in the order), total amount, and user address.
- The order is then appended to the orders list in the backend code.
- The server responds with a message indicating that the order was created successfully.

## 3. API to fetch all orders from the system with pagination (GET /orders):
- This endpoint fetches all the orders from the system with pagination support.
- When a GET request is made to /orders, the server retrieves the list of orders.
- The endpoint supports pagination using the limit and offset query parameters.
- The limit parameter determines the maximum number of orders to return in the response, and the offset parameter determines the starting index of the orders.
- The server responds with a list of orders based on the provided pagination parameters.

## 4. API to fetch a single order from the system using Order ID (GET /orders/{order_id}):
- This endpoint retrieves a single order from the system based on the provided Order ID.
- When a GET request is made to /orders/{order_id}, the server searches for the order in the orders list.
- If the order with the specified ID is found, the server responds with the details of the order.
- If the order is not found, the server responds with a message indicating that the order was not found for a particular order_id.

## 5. API to update a product when updating the available quantity for the product (PUT /products/{product_id}):
- This endpoint allows you to update the available quantity of a product based on the provided product ID.
- When a PUT request is made to /products/{product_id} with the product ID and the new quantity in the request, the server searches for the product with the specified ID in the products list.
- If the product is found, the server updates its available quantity with the new value.
- The server responds with a message indicating that the product quantity was updated successfully.
- If the product is not found, the server responds with a message indicating that the product was not found.
