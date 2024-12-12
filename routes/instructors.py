from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.instructors as crud
import config.db
import schemas.instructors as schemas
import models.instructors as models
from portadortoken import Portador
from typing import List
instructor = APIRouter()

# Crear las tablas si no existen

models.Instructor.__table__.create(bind=config.db.engine, checkfirst=True)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@instructor.get("/instructors/", response_model=List[schemas.Instructor], tags=["Instructors"],dependencies=[Depends(Portador())])
def read_instructors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_instructors = crud.get_instructors(db=db, skip=skip, limit=limit)
    return db_instructors

@instructor.post("/instructors/", response_model=schemas.Instructor, tags=["Instructors"],dependencies=[Depends(Portador())])
def create_instructor(instructor: schemas.InstructorCreate, db: Session = Depends(get_db)):
    db_instructor = crud.get_instructor_by_name(db, name=instructor.name)
    if db_instructor:
        raise HTTPException(status_code=400, detail="Instructor already exists")
    return crud.create_instructor(db=db, instructor=instructor)

@instructor.get("/instructors/{id}", response_model=schemas.Instructor, tags=["Instructors"],dependencies=[Depends(Portador())])
def read_instructor(id: int, db: Session = Depends(get_db)):
    db_instructor = crud.get_instructor(db=db, id=id)
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return db_instructor

@instructor.put("/instructors/{id}", response_model=schemas.Instructor, tags=["Instructors"],dependencies=[Depends(Portador())])
def update_instructor(id: int, instructor: schemas.InstructorUpdate, db: Session = Depends(get_db)):
    db_instructor = crud.update_instructor(db=db, id=id, instructor=instructor)
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found, not updated")
    return db_instructor

@instructor.delete("/instructors/{id}", response_model=schemas.Instructor, tags=["Instructors"],dependencies=[Depends(Portador())])
def delete_instructor(id: int, db: Session = Depends(get_db)):
    db_instructor = crud.delete_instructor(db=db, id=id)
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found, not deleted")
    return db_instructor