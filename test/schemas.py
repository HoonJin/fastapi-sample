from sqlalchemy import Table, Column, Integer, VARCHAR, DATETIME

from database import metadata

tests = Table(
    'tests',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('varchar', VARCHAR, nullable=False),
    Column('created', DATETIME, nullable=False)
)
