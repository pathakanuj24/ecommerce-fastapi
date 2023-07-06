
# Importing FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import APIRouter




# Product model schema
class Product(BaseModel):
    name: str
    price: float
    quantity: int

# dummy data for products
products = [
    Product(name="TV", 
            price=500,
            quantity=10
    ),
    Product(name="Laptop",
            price=1000, 
            quantity=5
    ),
    Product(name="mouse", 
            price=600,
            quantity=10
    ),
    Product(name="keyboard",
            price=1000, 
            quantity=12
    ),
    Product(name="penTool", 
            price=100, 
            quantity=10
    ),
    Product(name="pencilTool", 
            price=10, 
            quantity=20
    ),
    Product(name="usb",
            price=200, 
            quantity=10
    ),
    Product(name="charger", 
            price=300, 
            quantity=10
    ),
    Product(name="headphone", 
            price= 5000, 
            quantity=10
    ),
    Product(name="speaker",
            price= 1000,
            quantity=10
    ),
]

