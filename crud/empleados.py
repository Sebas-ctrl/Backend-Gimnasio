import models.empleados
import schemas.empleados
from sqlalchemy.orm import Session

def get_empleado(db:Session, ID:int):
    return db.query(models.empleados.Empleado).filter(models.empleados.Empleado.ID == ID).first()

def get_empleado_by_Numero(db: Session, Numero_Empleado: str):
    return db.query(models.empleados.Empleado).filter(models.empleados.Empleado == Numero_Empleado).first()

def get_empleados(db: Session, skip:int=0,limit:int=10):
    return db.query(models.empleados.Empleado).offset(skip).limit(limit).all()

def create_empleado(db: Session, empleado:schemas.empleados.EmpleadoCreate):
    db_empleado = models.empleados.Empleado(Area_ID=empleado.Area_ID, Fecha_Contratacion=empleado.Fecha_Contratacion, Puesto_ID=empleado.Puesto_ID,Persona_ID=empleado.Persona_ID,Numero_Empleado=empleado.Numero_Empleado,Fecha_Registro=empleado.Fecha_Registro,Fecha_Actualizacion=empleado.Fecha_Actualizacion,Estatus=empleado.Estatus)
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def update_empleado(db: Session, ID: int, empleado: schemas.empleados.EmpleadoUpdate):
    db_empleado = db.query(models.empleados.Empleado).filter(models.empleados.Empleado.ID == ID).first()
    if db_empleado:
        for var, value in vars(empleado).items():
            setattr(db_empleado, var, value) if value else None
        db.commit()
        db.refresh(db_empleado)
    return db_empleado


def delete_empleado(db: Session, ID: int):
    db_empleado = db.query(models.empleados.Empleado).filter(models.empleados.Empleado.ID == ID).first()
    if  db_empleado:
        db.delete(db_empleado)
        db.commit()
    return db_empleado
