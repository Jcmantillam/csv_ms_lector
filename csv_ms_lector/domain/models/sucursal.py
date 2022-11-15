from typing import Optional, TYPE_CHECKING, List

from sqlmodel import Field, Relationship
from sqlalchemy import Column, String, Integer

from .auxiliar_models import BaseModel

if TYPE_CHECKING:
    from ...domain.models.producto import Product

class Subsidiary(BaseModel, table=True):

    __table_name__ = "subsidiary"
    __table_args__ = {"schema": "public"}

    id: Optional[int] = Field(default=None, primary_key=True)
    country: str = Field(sa_column=Column(
            String(length=100),
            nullable=False
        )
    )
    city: str = Field(sa_column=Column(
            String(length=100),
            nullable=False
        )
    )
    adress: str = Field(sa_column=Column(
            String(length=100),
            nullable=False
        )
    )
    phone: Optional[str] = Field(sa_column=Column(
            String(length=16),
            nullable=True
        )
    )

    # Products relationship
    products: Optional[List["Product"]] = Relationship(
        back_populates="subsidiary"
    )