"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Business-specific schemas

class Inquiry(BaseModel):
    """
    Customer inquiries and requests from the website
    Collection name: "inquiry"
    """
    name: str = Field(..., description="Customer full name")
    phone: str = Field(..., description="Contact phone number")
    email: Optional[EmailStr] = Field(None, description="Email address")
    subject: str = Field(..., description="Reason for contacting")
    message: str = Field(..., description="Detailed message from customer")
    preferred_brand: Optional[str] = Field(None, description="Preferred car brand for parts or cars")
    preferred_model: Optional[str] = Field(None, description="Preferred model for parts or cars")


# Example schemas (kept for reference)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
