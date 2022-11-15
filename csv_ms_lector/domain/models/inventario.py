from datetime import datetime
from typing import Optional, TYPE_CHECKING, List

from sqlmodel import Field, Relationship
from sqlalchemy import Column, String, Integer, DateTime

from .auxiliar_models import BaseModel

if TYPE_CHECKING:
    from ...domain.models.producto import Product

class InventoryProduct(BaseModel, table=True):
    
    __table_name__ = "inventoryproduct"
    __table_args__ = {"schema": "public"}

    id: Optional[int] = Field(default=None, primary_key=True)
    quantity: int = Field(sa_column=Column(
            Integer,
            nullable=False
        )
    )
    inventory_date: Optional[datetime] = Field(sa_column=Column(
            DateTime,
            default=datetime.utcnow,
            nullable=False,
            comment="Created at. Time when the record was created."
        )
    )
    #Product Relationship
    product: Optional[List["Product"]] = Relationship(

    )
