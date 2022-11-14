from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import MetaData

import asyncio
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine
import os
from loguru import logger
from sqlmodel import SQLModel

from alembic import context

from csv_ms_lector.domain.models.cliente import *
from csv_ms_lector.domain.models.inventario import *
from csv_ms_lector.domain.models.producto import *
from csv_ms_lector.domain.models.sucursal import *

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
        }

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata


target_metadata = SQLModel.metadata

target_metadata.naming_convention = naming_convention

print(target_metadata.naming_convention.values())

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    """
    Return the URL to the database.
    """
    if os.name == "nt":
        load_dotenv()

    HOST = os.getenv("POSTGRES_HOST")
    DB = os.getenv("POSTGRES_DB", "")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    USER = os.getenv("POSTGRES_USER")
    return f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{DB}"


async def create_database():
    """Create the database if this not exists"""

    try:
        url = get_url()
        connectable = AsyncEngine(
            engine_from_config(
                config.get_section(config.config_ini_section),
                url=url,
                prefix="sqlalchemy.",
                poolclass=pool.NullPool,
                future=True
            )
        )

        async with connectable.connect() as connection:
            await connection.run_sync(lambda conn: conn.execute("CREATE DATABASE IF NOT EXISTS {}".format(os.getenv("POSTGRES_DB"))))
    except Exception as e:
        logger.error(e)


def do_run_migrations(connection):
    
    context.configure(connection=connection, target_metadata=target_metadata,
                      version_table="alembic_version", include_schemas=True)
    
    print("Preparing to run migrations")
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    url = get_url()

    connectable = AsyncEngine(
        engine_from_config(
            config.get_section(config.config_ini_section),
            url=url,
            prefix="sqlalchemy.",   
            poolclass=pool.NullPool,
            future=True
        )
    )

    async with connectable.connect() as connection:

        await connection.run_sync(lambda conn: do_run_migrations(conn))

asyncio.run(run_migrations_online())
