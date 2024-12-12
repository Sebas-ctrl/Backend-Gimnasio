import models.ejercicios
import schemas.ejercicios
from sqlalchemy.orm import Session

def get_ejercicio(db:Session, ID:int):
    return db.query(models.ejercicios.Ejercicio).filter(models.ejercicios.Ejercicio.ID == ID).first()

def get_ejercicio_by_nombre(db: Session, nombre: str):
    return db.query(models.ejercicios.Ejercicio).filter(models.ejercicios.Ejercicio.Nombre == nombre).first()


def get_ejercicios(db: Session, skip:int=0,limit:int=10):
    return db.query(models.ejercicios.Ejercicio).offset(skip).limit(limit).all()

def create_ejercicio(db: Session, ejercicio:schemas.ejercicios.EjercicioCreate):
    db_ejercicio = models.ejercicios.Ejercicio(
                                                Nombre=ejercicio.Nombre,
                                                Descripcion=ejercicio.Descripcion,
                                                Video=ejercicio.Video,
                                                Tipo=ejercicio.Tipo,
                                                Estatus=ejercicio.Estatus,
                                                Dificultad=ejercicio.Dificultad,
                                                Fecha_Registro=ejercicio.Fecha_Registro,
                                                Fecha_Actualizacion=ejercicio.Fecha_Actualizacion,
                                                Recomendaciones=ejercicio.Recomendaciones,
                                                Restricciones=ejercicio.Restricciones)
    db.add(db_ejercicio)
    db.commit()
    db.refresh(db_ejercicio)
    return db_ejercicio

def update_ejercicio(db: Session, ID: int, ejercicio: schemas.ejercicios.EjercicioUpdate):
    db_ejercicio = db.query(models.ejercicios.Ejercicio).filter(models.ejercicios.Ejercicio.ID == ID).first()
    if db_ejercicio:
        for var, value in vars(ejercicio).items():
            setattr(db_ejercicio, var, value) if value is not None else None
        db.commit()
        db.refresh(db_ejercicio)
    return db_ejercicio

def delete_ejercicio(db: Session, ID: int):
    db_ejercicio = db.query(models.ejercicios.Ejercicio).filter(models.ejercicios.Ejercicio.ID == ID).first()
    if  db_ejercicio:
        db.delete(db_ejercicio)
        db.commit()
    return db_ejercicio

