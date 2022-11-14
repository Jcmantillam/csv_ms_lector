
from typing import Optional, TYPE_CHECKING

from sqlmodel import Field
from sqlalchemy import Column, String, Integer

from .base_model import BaseModel
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

    