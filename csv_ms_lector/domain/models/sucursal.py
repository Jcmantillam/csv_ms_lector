from typing import Optional, TYPE_CHECKING

from sqlmodel import Field
from sqlalchemy import Column, String, Integer

from .base_model import BaseModel

class Subsidiary(BaseModel, table=True):

    __table_name__ = "Subsidiary"
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