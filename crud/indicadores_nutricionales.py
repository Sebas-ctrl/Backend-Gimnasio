import models.indicadores_nutricionales
import schemas.indicadores_nutricionales
from sqlalchemy.orm import Session
import models, schemas

def get_indicador_nutricional(db: Session, id: int):
    return db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()

def get_indicador_nutricional_by_usuario(db: Session, usuario_id: int):
    return db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.Usuario_Id == usuario_id).first()

def get_indicadores_nutricionales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.indicadores_nutricionales.Actividad).offset(skip).limit(limit).all()

def create_indicador_nutricional(db: Session, indicador_nutricional: schemas.indicadores_nutricionales.IndicadorNutricionalCreate):
    db_indicador_nutricional = models.indicadores_nutricionales.Actividad(
        Altura=indicador_nutricional.Altura,
        Peso=indicador_nutricional.Peso,
        Imc=indicador_nutricional.Imc,
        Porcentaje_grasa=indicador_nutricional.Porcentaje_grasa,
        Nivel_actividad=indicador_nutricional.Nivel_actividad,
        Fecha_Registro=indicador_nutricional.Fecha_Registro, 
        Fecha_Actualizacion=indicador_nutricional.Fecha_Actualizacion,
        Usuario_Id=indicador_nutricional.Usuario_Id
    )
    
    db.add(db_indicador_nutricional)
    db.commit()
    db.refresh(db_indicador_nutricional)
    return db_indicador_nutricional

def update_indicador_nutricional(db: Session, id: int, indicador_nutricional: schemas.indicadores_nutricionales.IndicadorNutricionalUpdate):
    db_indicador_nutricional = db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()
    if db_indicador_nutricional:
        for var, value in vars(indicador_nutricional).items():
            if value is not None:
                setattr(db_indicador_nutricional, var, value)
        db.commit()
        db.refresh(db_indicador_nutricional)
    return db_indicador_nutricional

def delete_indicador_nutricional(db: Session, id: int):
    db_indicador_nutricional = db.query(models.indicadores_nutricionales.Actividad).filter(models.indicadores_nutricionales.Actividad.ID == id).first()
    if db_indicador_nutricional:
        db.delete(db_indicador_nutricional)
        db.commit()
    return db_indicador_nutricional