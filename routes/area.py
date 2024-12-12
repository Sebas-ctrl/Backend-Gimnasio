from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.areas, config.db, schemas.areas, models.areas
from portadortoken import Portador
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

area = APIRouter()
models.areas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@area.get('/areas/', response_model=List[schemas.areas.Area],tags=['Areas'],dependencies=[Depends(Portador())])
def read_areas(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_areas = crud.areas.get_areas(db=db,skip=skip, limit=limit)
    return db_areas

@area.post("/area/{id}", response_model=schemas.areas.Area, tags=["Areas"],dependencies=[Depends(Portador())])
def read_area(id: int, db: Session = Depends(get_db)):
    db_area= crud.areas.get_area(db=db, id=id)
    if db_area is None:
        raise HTTPException(status_code=404, detail="Area not found")
    return db_area


@area.post('/areas/', response_model=schemas.areas.Area,tags=['Areas'],dependencies=[Depends(Portador())])
def create_area(area: schemas.areas.AreaCreate, db: Session=Depends(get_db)):
    db_areas = crud.areas.get_area_by_nombre(db,nombre=area.Nombre)
    if db_areas:
        raise HTTPException(status_code=400, detail="Area existente intenta nuevamente")
    return crud.areas.create_area(db=db, area=area)


@area.put('/areas/{id}', response_model=schemas.areas.Area,tags=['Areas'],dependencies=[Depends(Portador())])
def update_area(id:int,area: schemas.areas.AreaUpdate, db: Session=Depends(get_db)):
    db_areas = crud.areas.update_area(db=db, id=id, area=area)
    if db_areas is None:
        raise HTTPException(status_code=404, detail="Area no existe, no se pudo actualizar ")
    return db_areas


@area.delete('/areas/{id}', response_model=schemas.areas.Area,tags=['Areas'],dependencies=[Depends(Portador())])
def delete_area(id:int, db: Session=Depends(get_db)):
    db_areas = crud.areas.delete_area(db=db, id=id)
    if db_areas is None:
        raise HTTPException(status_code=404, detail="Area no existe, no se pudo eliminar ")
    return db_areas
