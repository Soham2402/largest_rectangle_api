import time
from typing import List, Annotated

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from utils import calculate_histogram
import models
from database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class Matrix(BaseModel):
    matrix: List[List[int]]
    
class OutputModel(BaseModel):
    matrix: str
    value: int
    occurance: int
    time_taken: float


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post('/')
async def get_matrix_size(matrix: Matrix, db: db_dependency):
    start_time: float = time.time() # Starting the timer
    rectangle: List[int, int] = calculate_histogram(matrix.matrix) 
    end_time: float = time.time()
    total_time: float = round(end_time - start_time, 3) * 10000 # Ending the timer and converting to microseconds
    data = {"matrix": str(matrix.matrix), "value": rectangle[0], "occurance": rectangle[1], "time_taken": total_time}
    output_model = OutputModel(**data) 
    add_db(output_model, db)
    return {'rectangle': rectangle, 'microseconds': total_time}


@app.get("/")
def get_stats(db:db_dependency):
    results = db.query(models.Outputs).all()
    return results

@app.get("/{id}")
def get_stats_by_id(id:int, db:db_dependency):
    result = db.query(models.Outputs).filter(models.Outputs.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="ID not found")
    return result



# Logic to register output in the database
def add_db(output: OutputModel, db: db_dependency):
    db_output = models.Outputs(
        matrix=output.matrix,   
        value=output.value,
        occurances=output.occurance,
        time_taken=output.time_taken
    )
    db.add(db_output)
    db.commit()
    db.refresh(db_output)
    print('Value added to database')
