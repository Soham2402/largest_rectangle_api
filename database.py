from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'postgres://soham:uZWbPEXO9zghLvtSxTJlxyzYGhfvKLZh@dpg-cmkapbf109ks739kki80-a/matrixdb'
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

