# Description: This file contains the API endpoints for the application.

# Importing the required libraries
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from products import products

from OrderDetails import Order , OrderItem , UserAddress

app = FastAPI(debug=True)


# api to get all the products
@app.get("/products")
def get_products():
    return products

# order list contains all the orders
orders = []

# api to get all the orders
@app.get("/orders")
def get_orders(limit: int = 10, offset: int = 0):
    return orders[offset : offset + limit]


#api to get a specific product by order id 
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order_id == order.order_id:
            return order
    return {"message": "The order with the given ID was not found"}


# api to create a new order
@app.post("/orders")
def create_order(order: Order):
    orders.append(order)
    return {"message": "Order is created successfully"}

# api to update an existing order
@app.put("/products/{product_id}")
def update_product(product_id: int, quantity: int):
    for product in products:
        if product["product_id"] == product_id:
            product["quantity"] = quantity
            return {"message": "Product quantity updated successfully"}
    return {"message": "Product not found"}

