from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.dietas, crud.users,config.db, schemas.dietas, models.dietas
from typing import List
import json
from fastapi.responses import JSONResponse
from jwt_config import solicita_token
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

dieta = APIRouter()
models.dietas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los dietas
@dieta.get('/dietas/', response_model=List[schemas.dietas.Dieta],tags=['Dietas'], dependencies=[Depends(Portador())])
def read_dietas(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_dietas = crud.dietas.get_dietas(db=db,skip=skip, limit=limit)
    return db_dietas

# Ruta para obtener un dieta por ID
@dieta.post("/dieta/{id}", response_model=schemas.dietas.Dieta, tags=["Dietas"], dependencies=[Depends(Portador())])
def read_dieta(id: int, db: Session = Depends(get_db)):
    db_dieta= crud.dietas.get_dieta(db=db, id=id)
    if db_dieta is None:
        raise HTTPException(status_code=404, detail="Dieta not found")
    return db_dieta

# Ruta para crear un usurio
@dieta.post('/dietas/', response_model=schemas.dietas.Dieta,tags=['Dietas'], dependencies=[Depends(Portador())])
def create_dieta(dieta: schemas.dietas.DietaCreate, db: Session=Depends(get_db)):
    db_dietas = crud.dietas.get_dieta_by_nombre(db,nombre=dieta.Nombre)
    if db_dietas:
        raise HTTPException(status_code=400, detail="Dieta existente intenta nuevamente")
    return crud.dietas.create_dieta(db=db, dieta=dieta)

# Ruta para actualizar un dieta
@dieta.put('/dietas/{id}', response_model=schemas.dietas.Dieta,tags=['Dietas'], dependencies=[Depends(Portador())])
def update_dieta(id:int,dieta: schemas.dietas.DietaUpdate, db: Session=Depends(get_db)):
    db_dietas = crud.dietas.update_dieta(db=db, id=id, dieta=dieta)
    if db_dietas is None:
        raise HTTPException(status_code=404, detail="Dieta no existe, no se pudo actualizar ")
    return db_dietas

# Ruta para eliminar un dieta
@dieta.delete('/dietas/{id}', response_model=schemas.dietas.Dieta,tags=['Dietas'], dependencies=[Depends(Portador())])
def delete_dieta(id:int, db: Session=Depends(get_db)):
    db_dietas = crud.dietas.delete_dieta(db=db, id=id)
    if db_dietas is None:
        raise HTTPException(status_code=404, detail="Dieta no existe, no se pudo eliminar ")
    return db_dietas