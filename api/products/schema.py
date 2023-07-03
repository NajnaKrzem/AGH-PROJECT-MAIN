from enum import Enum

from pydantic import BaseModel

class ProductCreateSchema(BaseModel):
    name: str
    price: str

    class Config:
        schema_extra = {
            "example": {
                "name": "shrek",
                "price": "100"
            }
        }


class ProductUpdateSchema(BaseModel):
    name: str | None
    price: str | None
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Shrek",
                "price": "100"
            }
        }


class Product(ProductCreateSchema):
    id: int


