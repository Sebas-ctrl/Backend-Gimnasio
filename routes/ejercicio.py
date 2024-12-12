from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.ejercicios, config.db, schemas.ejercicios, models.ejercicios
from typing import List
from portadortoken import Portador
ejercicio = APIRouter()

models.ejercicios.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@ejercicio.get("/ejercicios/", response_model=List[schemas.ejercicios.Ejercicio], tags=["Ejercicios"],dependencies=[Depends(Portador())])
def read_ejercicios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_ejercicios = crud.ejercicios.get_ejercicios(db=db, skip=skip, limit=limit)
    return db_ejercicios

@ejercicio.post("/ejercicio/{ID}", response_model=schemas.ejercicios.Ejercicio, tags=["Ejercicios"],dependencies=[Depends(Portador())] )
def read_ejercicio(ID: int, db: Session = Depends(get_db)):
    db_ejercicio = crud.ejercicios.get_ejercicio(db=db, ID=ID)
    if db_ejercicio is None:
        raise HTTPException(status_code=404, detail="Ejercicio no encontrado")
    return db_ejercicio

@ejercicio.post("/ejercicios/", response_model=schemas.ejercicios.Ejercicio, tags=["Ejercicios"],dependencies=[Depends(Portador())])
def create_ejercicio(ejercicio: schemas.ejercicios.EjercicioCreate, db: Session = Depends(get_db)):
    db_ejercicio = crud.ejercicios.get_ejercicio_by_nombre(db, nombre=ejercicio.Nombre)
    if db_ejercicio:
        raise HTTPException(status_code=400, detail="Ejercicio existente, intenta nuevamente")
    return crud.ejercicios.create_ejercicio(db=db, ejercicio=ejercicio)

@ejercicio.put("/ejercicio/{ID}", response_model=schemas.ejercicios.Ejercicio, tags=["Ejercicios"],dependencies=[Depends(Portador())])
def update_ejercicio(ID: int, ejercicio: schemas.ejercicios.EjercicioUpdate, db: Session = Depends(get_db)):
    db_ejercicio = crud.ejercicios.update_ejercicio(db=db, ID=ID, ejercicio=ejercicio)
    if db_ejercicio is None:
        raise HTTPException(status_code=404, detail="Ejercicio no existente, no actualizado")
    return db_ejercicio

@ejercicio.delete("/ejercicio/{ID}", response_model=schemas.ejercicios.Ejercicio, tags=["Ejercicios"],dependencies=[Depends(Portador())])
def delete_ejercicio(ID: int, db: Session = Depends(get_db)):
    db_ejercicio = crud.ejercicios.delete_ejercicio(db=db, ID=ID)
    if db_ejercicio is None:
        raise HTTPException(status_code=404, detail="Ejercicio no existe, no se pudo eliminar")
    return db_ejercicio
