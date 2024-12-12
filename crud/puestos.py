import models.puestos
import schemas.puestos
from sqlalchemy.orm import Session

def get_puesto(db:Session, ID:int):
    return db.query(models.puestos.Puesto).filter(models.puestos.Puesto.ID == ID).first()

def get_puesto_by_Nombre(db: Session, Nombre: str):
    return db.query(models.puestos.Puesto).filter(models.puestos.Puesto == Nombre).first()

def get_puestos(db: Session, skip:int=0,limit:int=10):
    return db.query(models.puestos.Puesto).offset(skip).limit(limit).all()

def create_puesto(db: Session, puesto:schemas.puestos.PuestoCreate):
    db_puesto = models.puestos.Puesto(Nombre=puesto.Nombre, Descripcion=puesto.Descripcion, Salario=puesto.Salario,Requisitos=puesto.Requisitos,Estatus=puesto.Estatus,Fecha_Registro=puesto.Fecha_Registro,Fecha_Actualizacion=puesto.Fecha_Actualizacion)
    db.add(db_puesto)
    db.commit()
    db.refresh(db_puesto)
    return db_puesto

def update_puesto(db: Session, ID: int, puesto: schemas.puestos.PuestoUpdate):
    db_puesto = db.query(models.puestos.Puesto).filter(models.puestos.Puesto.ID == ID).first()
    if db_puesto:
        for var, value in vars(puesto).items():
            setattr(db_puesto, var, value) if value else None
        db.commit()
        db.refresh(db_puesto)
    return db_puesto

def delete_puesto(db: Session, ID: int):
    db_puesto = db.query(models.puestos.Puesto).filter(models.puestos.Puesto.ID == ID).first()
    if  db_puesto:
        db.delete(db_puesto)
        db.commit()
    return db_puesto
