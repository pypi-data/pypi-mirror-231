from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String, Integer

import sys
import os
sys.path.append(os.getcwd())

import config.db


engine = create_engine(config.db.conn)
Base = declarative_base(engine)