from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# order details model schema
class OrderItem(BaseModel):
    productId: int
    boughtQuantity: int

class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str

class Order(BaseModel):
    order_id: int
    timestamp: str
    items: List[OrderItem]
    totalAmount: float
    address: UserAddress
