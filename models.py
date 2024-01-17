from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, Float
from database import Base

class Outputs(Base):
    __tablename__ = 'outputs'
    
    id = Column(Integer, primary_key=True, index = True)
    matrix = Column(String, index = True)
    value = Column(Integer, index = True)
    occurances = Column(Integer, index = True)
    time_taken = Column(Float, index = True)