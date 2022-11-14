from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime


class BaseModel(SQLModel):

    created_at: Optional[datetime] = Field(sa_column=Column(
            DateTime,
            default=datetime.utcnow,
            nullable=False,
            comment="Created at. Time when the record was created."
        )
    )

    updated_at: Optional[datetime] = Field(sa_column=Column(
            DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
            nullable=False,
            comment="Updated at. Time when the record was updated."
        )
    )
