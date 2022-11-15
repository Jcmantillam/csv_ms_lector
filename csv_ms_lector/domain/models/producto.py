from typing import Optional, TYPE_CHECKING

from pydantic import condecimal
from sqlmodel import Field, Relationship
from sqlalchemy import Column, String, Integer

from .auxiliar_models import BaseModel

if TYPE_CHECKING:
    from ...domain.models.cliente import Client
    from ...domain.models.sucursal import Subsidiary
    from ...domain.models.inventario import InventoryProduct

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

    #Client relationship
    client: Optional["Client"] = Relationship(back_populates="products")
    client_id: Optional[int] = Field(foreign_key="public.client.id")

    #Subsidiary ralationship
    subsidiary: Optional["Subsidiary"] = Relationship(back_populates="products")
    subsidiary_id: Optional[int] = Field(foreign_key="public.subsidiary.id")

    #InventoryProduct relationship
    inventory: Optional["InventoryProduct"] = Relationship(
        back_populates="products"
    )
    inventory_id: Optional[int] = Field(foreign_key="public.inventoryproduct.id")
