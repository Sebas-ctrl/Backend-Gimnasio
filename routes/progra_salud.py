from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.progra_salud, config.db, schemas.progra_salud, models.progra_salud
from typing import List
from portadortoken import Portador
key=Fernet.generate_key()
f = Fernet(key)
progra_salud = APIRouter()

models.progra_salud.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@progra_salud.get("/programas_saludables/", response_model=List[schemas.progra_salud.Programa], tags=["Programas Saludables"],dependencies=[Depends(Portador())])
def read_programas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_programas = crud.progra_salud.get_programas(db=db, skip=skip, limit=limit)
    return db_programas

@progra_salud.get("/programa/{id}", response_model=schemas.progra_salud.Programa, tags=["Programas Saludables"],dependencies=[Depends(Portador())])
def read_programa(id: int, db: Session = Depends(get_db)):
    db_programa = crud.progra_salud.get_programa(db=db, id=id)
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return db_programa

@progra_salud.post("/programas_saludables/", response_model=schemas.progra_salud.Programa, tags=["Programas Saludables"],dependencies=[Depends(Portador())])
def create_programa(programa: schemas.progra_salud.ProgramaCreate, db: Session = Depends(get_db)):
    return crud.progra_salud.create_programa(db=db, programa=programa)

@progra_salud.put("/programa/{id}", response_model=schemas.progra_salud.Programa, tags=["Programas Saludables"],dependencies=[Depends(Portador())])
def update_programa(id: int, programa: schemas.progra_salud.ProgramaUpdate, db: Session = Depends(get_db)):
    db_programa = crud.progra_salud.update_programa(db=db, id=id, programa=programa)
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return db_programa

@progra_salud.delete("/programa/{id}", response_model=schemas.progra_salud.Programa, tags=["Programas Saludables"],dependencies=[Depends(Portador())])
def delete_programa(id: int, db: Session = Depends(get_db)):
    db_programa = crud.progra_salud.delete_programa(db=db, id=id)
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return db_programa
