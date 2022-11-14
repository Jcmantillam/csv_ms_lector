from typing import Optional, TYPE_CHECKING

from pydantic import condecimal
from sqlmodel import Field
from sqlalchemy import Column, String, Integer

from .base_model import BaseModel

class Product(BaseModel, table=True):

    __table_name__ = "product"
    __table_args__ = {"schema": "public"}

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(
            String(length=100),
            nullable=False
        )
    )
    description: str = Field(sa_column=Column(
            String(length=200),
            nullable=False
        )
    )
    price: condecimal(max_digits=5, decimal_places=3) = Field(default=0)