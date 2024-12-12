import models.dietas
import schemas.dietas
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_dieta(db:Session, id: int):
    return db.query(models.dietas.Dieta).filter(models.dietas.Dieta.ID == id).first()

# Busqueda por USUARIO
def get_dieta_by_nombre(db:Session, nombre: str):
    return db.query(models.dietas.Dieta).filter(models.dietas.Dieta.Nombre == nombre).first()

# Buscar todas las dietas
def get_dietas(db:Session, skip: int=0, limit:int=10):
    return db.query(models.dietas.Dieta).offset(skip).limit(limit).all()

# Crear una nueva dieta
def create_dieta(db:Session, dieta: schemas.dietas.DietaCreate):
    db_dieta = models.dietas.Dieta(Nombre=dieta.Nombre, 
                                    Detalle=dieta.Detalle,
                                    Descripcion=dieta.Descripcion,
                                    Objetivo=dieta.Objetivo,
                                    Estatus=dieta.Estatus, 
                                    Fecha_Registro=dieta.Fecha_Registro, 
                                    Fecha_Actualizacion=dieta.Fecha_Actualizacion)
    db.add(db_dieta)
    db.commit()
    db.refresh(db_dieta)
    return db_dieta

# Actualizar un nombre por id
def update_dieta(db:Session, id:int, dieta:schemas.dietas.DietaUpdate):
    db_dieta = db.query(models.dietas.Dieta).filter(models.dietas.Dieta.ID == id).first()
    if db_dieta:
        for var, value in vars(dieta).items():
            setattr(db_dieta, var, value) if value else None
        db.commit()
        db.refresh(db_dieta)
    return db_dieta

# Eliminar un nombre por id
def delete_dieta(db:Session, id:int):
    db_dieta = db.query(models.dietas.Dieta).filter(models.dietas.Dieta.ID == id).first()
    if db_dieta:
        db.delete(db_dieta)
        db.commit()
    return db_dieta