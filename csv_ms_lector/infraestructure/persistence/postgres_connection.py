from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from loguru import logger
from dotenv import load_dotenv

import os

def get_url():
    """
    Return the URL to the database.
    """
    if os.name is "nt":
        load_dotenv()

    HOST = os.getenv("POSTGRES_HOST")
    DB = os.getenv("POSTGRES_DB", "")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    USER = os.getenv("POSTGRES_USER")
    return f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{DB}"

async_engine = create_async_engine(
    get_url(),
    echo=True if os.getenv("DEBUG") else False,
    future=True
)

async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            logger.error(str(e))
            raise e
