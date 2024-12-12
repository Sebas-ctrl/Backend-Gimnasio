from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.indicadores_nutricionales
import config.db
import schemas.indicadores_nutricionales
import models.indicadores_nutricionales
from typing import List
from portadortoken import Portador
import models,schemas

# Crea la base de datos y las tablas
models.indicadores_nutricionales.Base.metadata.create_all(bind=config.db.engine)

# Inicializa el router
indicador_nutricional = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas
@indicador_nutricional.get('/indicadores_nutricionales/', response_model=List[schemas.indicadores_nutricionales.IndicadorNutricional], tags=['Indicadores Nutricionales'], dependencies=[Depends(Portador())])
def read_indicadores_nutricionales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.indicadores_nutricionales.get_indicadores_nutricionales(db=db, skip=skip, limit=limit)

@indicador_nutricional.get('/indicadores_nutricionales/{id}', response_model=schemas.indicadores_nutricionales.IndicadorNutricional, tags=['Indicadores Nutricionales'], dependencies=[Depends(Portador())])
def read_indicador_nutricional(id: int, db: Session = Depends(get_db)):
    db_indicador_nutricional = crud.indicadores_nutricionales.get_indicador_nutricional(db=db, id=id)
    if db_indicador_nutricional is None:
        raise HTTPException(status_code=404, detail="Indicador nutricional not found")
    return db_indicador_nutricional

@indicador_nutricional.post('/indicadores_nutricionales/', response_model=schemas.indicadores_nutricionales.IndicadorNutricional, tags=['Indicadores Nutricionales'], dependencies=[Depends(Portador())])
def create_indicador_nutricional(indicador_nutricional: schemas.indicadores_nutricionales.IndicadorNutricionalCreate, db: Session = Depends(get_db)):
    db_indicador_nutricional = crud.indicadores_nutricionales.get_indicador_nutricional_by_usuario(db=db, usuario_id=indicador_nutricional.Usuario_Id)
    if db_indicador_nutricional:
        raise HTTPException(status_code=400, detail="Indicador Nutricional existente, intenta nuevamente")
    return crud.indicadores_nutricionales.create_indicador_nutricional(db=db, indicador_nutricional=indicador_nutricional)

@indicador_nutricional.put('/indicadores_nutricionales/{id}', response_model=schemas.indicadores_nutricionales.IndicadorNutricional, tags=['Indicadores Nutricionales'], dependencies=[Depends(Portador())])
def update_indicador_nutricional(id: int, indicador_nutricional: schemas.indicadores_nutricionales.IndicadorNutricionalUpdate, db: Session = Depends(get_db)):
    db_indicador_nutricional = crud.indicadores_nutricionales.update_indicador_nutricional(db=db, id=id, indicador_nutricional=indicador_nutricional)
    if db_indicador_nutricional is None:
        raise HTTPException(status_code=404, detail="Indicador nutricional not found")
    return db_indicador_nutricional

@indicador_nutricional.delete('/indicadores_nutricionales/{id}', response_model=schemas.indicadores_nutricionales.IndicadorNutricional, tags=['Indicadores Nutricionales'], dependencies=[Depends(Portador())])
def delete_indicador_nutricional(id: int, db: Session = Depends(get_db)):
    db_indicador_nutricional = crud.indicadores_nutricionales.delete_indicador_nutricional(db=db, id=id)
    if db_indicador_nutricional is None:
        raise HTTPException(status_code=404, detail="Indicador nutricional not found")
    return db_indicador_nutricional
