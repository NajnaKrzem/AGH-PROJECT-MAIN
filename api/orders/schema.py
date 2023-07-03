from enum import Enum

from pydantic import BaseModel

class OrderCreateSchema(BaseModel):
    customer_id: str
    product_id: str

    class Config:
        schema_extra = {
            "example": {
                "customer_id": "1",
                "product_id": "1",
            }
        }


class OrderUpdateSchema(BaseModel):
    customer_id: str | None
    product_id: str | None
    

    class Config:
        schema_extra = {
            "example": {
                "customer_id": "1",
                "product_id": "1"
            }
        }


class Order(OrderCreateSchema):
    id: int


