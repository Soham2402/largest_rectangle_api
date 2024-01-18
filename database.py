from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DB_URL = 'postgresql://postgres:postgres@localhost:5432/MatrixDb' 

#You can use the below url if you dont want to setup pgadmin
DB_URL = 'postgresql://soham:uZWbPEXO9zghLvtSxTJlxyzYGhfvKLZh@dpg-cmkapbf109ks739kki80-a.singapore-postgres.render.com/matrixdb'
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

