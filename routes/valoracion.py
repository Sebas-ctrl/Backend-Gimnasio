from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.val_nutricional, config.db, schemas.valoracion, models.valoracion
from typing import List
import json
from fastapi.responses import JSONResponse
from jwt_config import solicita_token
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

valoracion = APIRouter()
models.valoracion.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@valoracion.get('/valoracionNutricional/', response_model=List[schemas.valoracion.Valoracion],tags=['Valoracion-Nutricional'], dependencies=[Depends(Portador())])
def read_valoracion(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_valoracion = crud.val_nutricional.get_valoracion(db = db, skip = skip, limit = limit)
    return db_valoracion

@valoracion.post('/valoracionNutricional/', response_model=schemas.valoracion.Valoracion,tags=['Valoracion-Nutricional'], dependencies=[Depends(Portador())])
def create_valoracion(valoracion: schemas.valoracion.ValoracionCreate, db: Session=Depends(get_db)):
    db_valoracion = crud.val_nutricional.get_valoracion_by_ids(db, miembro_id=valoracion.Miembro_ID, indicador_id=valoracion.Indicador_ID, pregunta_id=valoracion.Pregunta_ID)
    if db_valoracion:
        raise HTTPException(status_code=400, detail="Valoracion existente intenta nuevamente")
    return crud.val_nutricional.create_valoracion(db=db, valoracion=valoracion)

#@valoracion.get("/valoracionNutricional/{miembro_id}/{indicador_id}/{pregunta_id}", response_model=schemas.valoracion.Valoracion, tags=["Valoracion-Nutricional"], dependencies=[Depends(Portador())])
#def get_valoracion_by_ids( miembro_id: int, indicador_id: int,pregunta_id:int, db: Session = Depends(get_db)):
    #db_valoracion = crud.val_nutricional.get_valoracion_by_ids(db=db, miembro_id=miembro_id, indicador_id=indicador_id, pregunta_id=pregunta_id)
    #if db_valoracion is None:
        #raise HTTPException(status_code=404, detail="Val-Nut not found")
    #return db_valoracion



# Ruta para actualizar un usuario-rol
@valoracion.put("/valoracionNutricional/{miembro_id}/{indicador_id}/{pregunta_id}", response_model=schemas.valoracion.Valoracion, tags=["Valoracion-Nutricional"], dependencies=[Depends(Portador())])
def update_valoracion(miembro_id: int, indicador_id: int,pregunta_id:int, valoracion:schemas.valoracion.ValoracionUpdate, db: Session = Depends(get_db)):
    db_valoracion = crud.val_nutricional.update_valoracion(db=db, miembro_id=miembro_id, indicador_id=indicador_id, pregunta_id=pregunta_id, valoracion=valoracion)
    if db_valoracion is None:
        raise HTTPException(status_code=404, detail="Val-Nut not found")
    return db_valoracion

# Ruta para eliminar un Rol
@valoracion.delete('/valoracionNutricional/{miembro_id}/{indicador_id}/{pregunta_id}', response_model=schemas.valoracion.Valoracion,tags=['Valoracion-Nutricional'], dependencies=[Depends(Portador())])
def delete_rol(miembro_id: int, indicador_id: int, pregunta_id:int, db: Session=Depends(get_db)):
    db_valoracions = crud.val_nutricional.delete_valoracion(db=db, miembro_id=miembro_id,indicador_id=indicador_id, pregunta_id=pregunta_id )
    if db_valoracions is None:
        raise HTTPException(status_code=404, detail="Val-Nut no existe, no se pudo eliminar ")
    return db_valoracions