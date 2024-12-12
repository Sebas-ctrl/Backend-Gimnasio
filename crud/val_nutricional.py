import models.valoracion
import schemas.valoracion
from sqlalchemy.orm import Session
import models, schemas

#Busqueda por usuario_id y rol_id
def get_valoracion_by_ids(db: Session, miembro_id: int, indicador_id: int, pregunta_id: int):
    return db.query(models.valoracion.Valoracion).filter(
        models.valoracion.Valoracion.Miembro_ID == miembro_id,
        models.valoracion.Valoracion.Indicador_ID == indicador_id,  
        models.valoracion.Valoracion.Pregunta_ID == pregunta_id
    ).first()

def get_valoracion(db:Session, skip: int=1, limit:int=10):
    return db.query(models.valoracion.Valoracion).offset(skip).limit(limit).all()

def create_valoracion(db:Session, valoracion: schemas.valoracion.ValoracionCreate):
    db_valoracion = models.valoracion.Valoracion(
        Miembro_ID=valoracion.Miembro_ID, 
        Indicador_ID=valoracion.Indicador_ID,
        Pregunta_ID=valoracion.Pregunta_ID,
        Valor=valoracion.Valor, 
        Comentarios=valoracion.Comentarios, 
        Fecha_Registro=valoracion.Fecha_Registro, 
        Fecha_Actualizacion=valoracion.Fecha_Actualizacion) 
    db.add(db_valoracion)
    db.commit()
    db.refresh(db_valoracion)
    return db_valoracion

def update_valoracion(db: Session, miembro_id: int, indicador_id: int, pregunta_id: int, valoracion: schemas.valoracion.ValoracionUpdate):
    db_valoracion = db.query(models.valoracion.Valoracion).filter(
        models.valoracion.Valoracion.Miembro_ID == miembro_id,
        models.valoracion.Valoracion.Indicador_ID == indicador_id,
        models.valoracion.Valoracion.Pregunta_ID == pregunta_id
    ).first()
    if db_valoracion:
        # Actualiza solo los campos deseados
        db_valoracion.Valor = valoracion.Valor
        db_valoracion.Comentarios = valoracion.Comentarios
        db_valoracion.Fecha_Registro = valoracion.Fecha_Registro
        db_valoracion.Fecha_Actualizacion = valoracion.Fecha_Actualizacion

        db.commit()
        db.refresh(db_valoracion)
    return db_valoracion

def delete_valoracion(db:Session,  miembro_id: int, indicador_id: int, pregunta_id: int):
    db_valoracion = db.query(models.valoracion.Valoracion).filter(models.valoracion.Valoracion.Miembro_ID == miembro_id,
                                                                models.valoracion.Valoracion.Indicador_ID == indicador_id,
                                                                models.valoracion.Valoracion.Pregunta_ID == pregunta_id
    ).first()
    if db_valoracion:
        db.delete(db_valoracion)
        db.commit()
    return db_valoracion