import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine)
from sqlalchemy.sql import func
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()



# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("authors", String(100)),
)

# databases query builder
database = Database(DATABASE_URL)