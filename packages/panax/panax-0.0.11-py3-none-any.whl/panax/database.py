from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
import os
from migrate.versioning import api
from urllib.parse import quote


db = ''
engine = create_engine(db)
Base = declarative_base(engine)


class Poo(Base):
    __tablename__ = 'poo'
    id = Column(String(128), primary_key=True, unique=True, nullable=False)
    poo = Column(String(128), primary_key=True, unique=True)
    capa = Column(String(128), nullable=True)
    mou = Column(String(128), nullable=True)
    ded = Column(String(128), nullable=True)
    de = Column(String(128), nullable=True)
