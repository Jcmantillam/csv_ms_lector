from typing import Optional, TYPE_CHECKING

from sqlmodel import Field
from sqlalchemy import Column, String, Integer

from .base_model import BaseModel

class InventoryProduct(BaseModel, table=True):
    
    __table_name__ = "inventory"
    __table_args__ = {"schema": "public"}

    id: Optional[int] = Field(default=None, primary_key=True)
    quantity: int = Field(sa_column=Column(
            Integer,
            nullable=False
        )
    )