import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Contact(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    age: int = Field(min=0)
    phone_number: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Michael",
                "age": 20,
                "phone_number": "69696969696",
            }
        }


class ContactUpdate(BaseModel):
    id: Optional[str]
    name: Optional[str]
    age: Optional[int]
    phone_number: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Michael",
                "age": 20,
                "phone_number": "69696969696",
            }
        }
