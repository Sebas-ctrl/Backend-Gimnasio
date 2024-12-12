import models.rutinas
import models.users
import schemas.rutinas
import schemas.users
from sqlalchemy.orm import Session
import models, schemas

def get_rutina(db: Session, id: int):
    return db.query(models.rutinas.Rutina).filter(models.rutinas.Rutina.ID == id).first()

def get_rutinas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.rutinas.Rutina).offset(skip).limit(limit).all()

def create_rutina(db: Session, rutina: schemas.rutinas.RutinasCreate):
    db_rutina = models.rutinas.Rutina(Nombre=rutina.Nombre,
                                      Programa_Saludable_ID=rutina.Programa_Saludable_ID,
                                      Fecha_Registro=rutina.Fecha_Registro,
                                      Fecha_Actualizacion=rutina.Fecha_Actualizacion,
                                      Tiempo_Aproximado=rutina.Tiempo_Aproximado,
                                      Estatus=rutina.Estatus,
                                      Resultados_Esperados=rutina.Resultados_Esperados)
    db.add(db_rutina)
    db.commit()
    db.refresh(db_rutina)
    return db_rutina

def update_rutina(db: Session, id: int, rutina: schemas.rutinas.RutinasUpdate):
    db_rutina = db.query(models.rutinas.Rutina).filter(models.rutinas.Rutina.ID == id).first()
    if db_rutina:
        for var, value in vars(rutina).items():
            setattr(db_rutina, var, value) if value else None
        db.commit()
        db.refresh(db_rutina)
    return db_rutina

def delete_rutina(db: Session, id: int):
    db_rutina = db.query(models.rutinas.Rutina).filter(models.rutinas.Rutina.ID == id).first()
    if db_rutina:
        db.delete(db_rutina)
        db.commit()
    return db_rutina