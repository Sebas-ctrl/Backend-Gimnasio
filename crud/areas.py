import models.areas
import schemas.areas
from sqlalchemy.orm import Session
import models, schemas


def get_area(db:Session, id: int):
    return db.query(models.areas.Area).filter(models.areas.Area.ID == id).first()


def get_area_by_nombre(db:Session, nombre: str):
    return db.query(models.areas.Area).filter(models.areas.Area.Nombre == nombre).first()


def get_areas(db:Session, skip: int=0, limit:int=10):
    return db.query(models.areas.Area).offset(skip).limit(limit).all()


def create_area(db:Session, area: schemas.areas.AreaCreate):
    db_area = models.areas.Area(Nombre=area.Nombre, 
                                      Descripcion=area.Descripcion, 
                                      Sucursal=area.Sucursal, 
                                      Estatus=area.Estatus,
                                      Fecha_Registro=area.Fecha_Registro,
                                      Fecha_Actualizacion=area.Fecha_Actualizacion)
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area


def update_area(db:Session, id:int, area:schemas.areas.AreaUpdate):
    db_area = db.query(models.areas.Area).filter(models.areas.Area.ID == id).first()
    if db_area:
        for var, value in vars(area).items():
            setattr(db_area, var, value) if value else None
        db.commit()
        db.refresh(db_area)
    return db_area

def delete_area(db:Session, id:int):
    db_area = db.query(models.areas.Area).filter(models.areas.Area.ID == id).first()
    if db_area:
        db.delete(db_area)
        db.commit()
    return db_area
