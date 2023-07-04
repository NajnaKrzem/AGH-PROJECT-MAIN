from enum import Enum

from pydantic import BaseModel

class CustomerCreateSchema(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Shrek",
                "surname": "Fiona",
                "email": "shrek@example.com",
                "phone_number": "13-072-001",
            }
        }


class CustomerUpdateSchema(BaseModel):
    name: str | None
    surname: str | None
    email: str | None
    phone_number: str | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Osioł",
                "surname": "Kot"
            }
        }


class Customer(CustomerCreateSchema):
    id: int


