
from typing import Optional, TYPE_CHECKING, List

from sqlmodel import Field, Relationship
from sqlalchemy import Column, String, Integer

if TYPE_CHECKING:
    from ...domain.models.producto import Product

from .auxiliar_models import BaseModel
class Client(BaseModel, table=True):

    __tablename__ = "client"
    __table_args__ = {"schema": "public"}

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(
            String(length=100),
            nullable=False
        )
    )
    phone: Optional[str] = Field(sa_column=Column(
            String(length=16),
            nullable=True
        )
    )
    adress: Optional[str] = Field(sa_column=Column(
            String(length=200),
            nullable=True
        )
    )
    email: Optional[str] = Field(sa_column=Column(
            String(length=100),
            nullable=True
        )
    )

    #Products relationship:
    products: Optional[List["Product"]] = Relationship(
        back_populates="client"
    )
    