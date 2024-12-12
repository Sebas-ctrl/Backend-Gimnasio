from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.p_nutricionales
import config.db
import schemas.p_nutricionales
import models.p_nutricionales
from typing import List

p_nutricional = APIRouter()
models.p_nutricionales.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@p_nutricional.get('/p_nutricionales/', response_model=List[schemas.p_nutricionales.p_nutricional], tags=['Preguntas Nutricionales'])
def read_p_nutricionales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.p_nutricionales.get_p_nutricionales(db, skip=skip, limit=limit)

@p_nutricional.get("/p_nutricionales/{id}", response_model=schemas.p_nutricionales.p_nutricional, tags=["Preguntas Nutricionales"])
def read_p_nutricional(id: int, db: Session = Depends(get_db)):
    db_p_nutricional = crud.p_nutricionales.get_p_nutricional(db, id=id)
    if db_p_nutricional is None:
        raise HTTPException(status_code=404, detail="Pregunta not found")
    return db_p_nutricional

@p_nutricional.post('/p_nutricionales/', response_model=schemas.p_nutricionales.p_nutricional, tags=['Preguntas Nutricionales'])
def create_p_nutricionales(p_nutricional: schemas.p_nutricionales.p_nutricionalesCreate, db: Session = Depends(get_db)):
    db_p_nutricional = crud.p_nutricionales.get_p_nutricional_by_nombre(db, Pregunta=p_nutricional.Pregunta)
    if db_p_nutricional:
        raise HTTPException(status_code=400, detail="Pregunta existente, intenta nuevamente")
    return crud.p_nutricionales.p_nutricionalesCreate(db=db, p_nutricionales=p_nutricional)

@p_nutricional.put('/p_nutricionales/{id}', response_model=schemas.p_nutricionales.p_nutricional, tags=['Preguntas Nutricionales'])
def update_p_nutricionales(id: int, p_nutricional: schemas.p_nutricionales.p_nutricionalesUpdate, db: Session = Depends(get_db)):
    db_p_nutricional = crud.p_nutricionales.p_nutricionalesUpdate(db, id=id, p_nutricionales=p_nutricional)
    if db_p_nutricional is None:
        raise HTTPException(status_code=404, detail="Pregunta no existe, no se pudo actualizar")
    return db_p_nutricional

@p_nutricional.delete('/p_nutricionales/{id}', response_model=schemas.p_nutricionales.p_nutricional, tags=['Preguntas Nutricionales'])
def delete_p_nutricionales(id: int, db: Session = Depends(get_db)):
    db_p_nutricional = crud.p_nutricionales.delete_p_nutricionales(db, id=id)
    if db_p_nutricional is None:
        raise HTTPException(status_code=404, detail="Pregunta no existe, no se pudo eliminar")
    return db_p_nutricional
