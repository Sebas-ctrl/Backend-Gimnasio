import models.ejercicios_rutinas
import schemas.ejercicios_rutinas
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por ejercicio_id y rutina_id
def get_ejcrnt_by_ids(db: Session, ejercicio_id: int, rutina_id: int):
    return db.query(models.ejercicios_rutinas.EjcRtn).filter(
        models.ejercicios_rutinas.EjcRtn.Ejercicio_ID == ejercicio_id,
        models.ejercicios_rutinas.EjcRtn.Rutina_ID == rutina_id).first()

# Buscar todos los Ejercicios - Rutinas 
def get_ejcrnts(db:Session, skip: int=0, limit:int=10):
    return db.query(models.ejercicios_rutinas.EjcRtn).offset(skip).limit(limit).all()

# Crear nuevo registro de Ejercicios - Rutinas 
def create_ejcrnt(db:Session, ejcrtn: schemas.ejercicios_rutinas.EjcRtnCreate):
    db_ejcrtn = models.ejercicios_rutinas.EjcRtn(Ejercicio_ID=ejcrtn.Ejercicio_ID, 
                                          Rutina_ID=ejcrtn.Rutina_ID,
                                          Cantidad=ejcrtn.Cantidad, 
                                          Tipo=ejcrtn.Tipo, 
                                          Observaciones=ejcrtn.Observaciones, 
                                          Fecha_Registro=ejcrtn.Fecha_Registro, 
                                          Fecha_Actualizacion=ejcrtn.Fecha_Actualizacion,
                                          Estatus=ejcrtn.Estatus)
    db.add(db_ejcrtn)
    db.commit()
    db.refresh(db_ejcrtn)
    return db_ejcrtn

# Actualizar Ejercicios - Rutinas 
def update_ejcrtn(db: Session, ejercicio_id: int, rutina_id: int, ejcrtn: schemas.ejercicios_rutinas.EjcRtnUpdate):
    db_ejcrtn = db.query(models.ejercicios_rutinas.EjcRtn).filter(
        models.ejercicios_rutinas.EjcRtn.Ejercicio_ID == ejercicio_id,
        models.ejercicios_rutinas.EjcRtn.Rutina_ID == rutina_id
    ).first()
    if db_ejcrtn:
        # Actualiza solo los campos deseados
        db_ejcrtn.Cantidad=ejcrtn.Cantidad, 
        db_ejcrtn.Tipo=ejcrtn.Tipo, 
        db_ejcrtn.Observaciones=ejcrtn.Observaciones,
        db_ejcrtn.Fecha_Registro = ejcrtn.Fecha_Registro
        db_ejcrtn.Fecha_Actualizacion = ejcrtn.Fecha_Actualizacion
        db_ejcrtn.Estatus = ejcrtn.Estatus
        db.commit()
        db.refresh(db_ejcrtn)
    return db_ejcrtn

# Eliminar un usuaurios-roles por id
def delete_ejcrt(db:Session, ejercicio_id: int, rutina_id: int):
    db_ejcrtn = db.query(models.ejercicios_rutinas.EjcRtn).filter(models.ejercicios_rutinas.EjcRtn.Ejercicio_ID == ejercicio_id,
                                                           models.ejercicios_rutinas.EjcRtn.Rutina_ID == rutina_id).first()
    if db_ejcrtn:
        db.delete(db_ejcrtn)
        db.commit()
    return db_ejcrtn