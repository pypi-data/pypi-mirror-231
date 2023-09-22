from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
# from sqlalchemy import Column, String, Integer

import sys
import os
sys.path.append(os.getcwd())

from config import APP_SETTING


engine = create_engine(APP_SETTING["connection"])
conn = engine.connect()
session = Session(engine)

Base = declarative_base(engine)
