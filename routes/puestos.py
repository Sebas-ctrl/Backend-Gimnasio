from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.puestos,config.db,schemas.puestos,models.puestos
from typing import List

puesto = APIRouter()

models.puestos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@puesto.get("/puestos/", response_model=List[schemas.puestos.Puesto], tags=["Puestos"] ,dependencies=[Depends(Portador())])
def read_puestos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_puestos= crud.puestos.get_puestos(db=db, skip=skip, limit=limit)
    return db_puestos

@puesto.post("/puesto/{ID}", response_model=schemas.puestos.Puesto, tags=["Puestos"] ,dependencies=[Depends(Portador())])
def read_puesto(ID: int, db: Session = Depends(get_db)):
    db_puestos= crud.puestos.get_puesto(db=db, ID=ID)
    if db_puestos is None:
        raise HTTPException(status_code=404, detail="Puesto not found")
    return db_puestos

@puesto.post("/puestos/", response_model=schemas.puestos.Puesto, tags=["Puestos"],dependencies=[Depends(Portador())])
def create_puesto(puesto: schemas.puestos.PuestoCreate, db: Session = Depends(get_db)):
    db_puesto = crud.puestos.get_puesto_by_Nombre(db, Nombre=puesto.Nombre)
    if db_puesto:
        raise HTTPException(status_code=400, detail="Puesto existente intenta nuevamente")
    return crud.puestos.create_puesto(db=db, puesto=puesto)

@puesto.put("/puesto/{ID}", response_model=schemas.puestos.Puesto, tags=["Puestos"] ,dependencies=[Depends(Portador())])
def update_puesto(ID: int, puesto: schemas.puestos.PuestoUpdate, db: Session = Depends(get_db)):
    db_puesto = crud.puestos.update_puesto(db = db, ID = ID, puesto = puesto)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no existente, no esta actuaizado")
    return db_puesto

@puesto.delete("/puesto/{ID}", response_model=schemas.puestos.Puesto, tags=["Puestos"] ,dependencies=[Depends(Portador())])
def delete_puesto(ID: int, db: Session = Depends(get_db)):
    db_puesto = crud.puestos.delete_puesto(db = db, ID = ID)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no existe, no se pudo eliminar")
    return db_puesto

