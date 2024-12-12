import models.p_nutricionales
import schemas.p_nutricionales
from sqlalchemy.orm import Session

# Busqueda por ID
def get_p_nutricional(db: Session, id: int):
    return db.query(models.p_nutricionales.p_nutricionales).filter(models.p_nutricionales.p_nutricionales.ID == id).first()

# Busqueda por nombre
def get_p_nutricional_by_nombre(db: Session, Pregunta: str):
    return db.query(models.p_nutricionales.p_nutricionales).filter(models.p_nutricionales.p_nutricionales.Pregunta == Pregunta).first()

# Buscar todos las personas
def get_p_nutricionales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.p_nutricionales.p_nutricionales).offset(skip).limit(limit).all()

# Crear una nueva persona
def p_nutricionalesCreate(db: Session, p_nutricionales: schemas.p_nutricionales.p_nutricionalesCreate):
    db_p_nutricionales = models.p_nutricionales.p_nutricionales(
        Pregunta=p_nutricionales.Pregunta,
        Fecha_Creacion=p_nutricionales.Fecha_Creacion,
        Fecha_Actualizacion=p_nutricionales.Fecha_Actualizacion
    )
    
    db.add(db_p_nutricionales)
    db.commit()
    db.refresh(db_p_nutricionales)
    return db_p_nutricionales

# Actualizar una persona por ID
def p_nutricionalesUpdate(db: Session, id: int, p_nutricionales: schemas.p_nutricionales.p_nutricionalesUpdate):
    db_p_nutricionales = db.query(models.p_nutricionales.p_nutricionales).filter(models.p_nutricionales.p_nutricionales.ID == id).first()
    if db_p_nutricionales:
        for var, value in p_nutricionales.dict(exclude_unset=True).items():
            setattr(db_p_nutricionales, var, value)
        db.commit()
        db.refresh(db_p_nutricionales)
    return db_p_nutricionales

# Eliminar una persona por ID
def delete_p_nutricionales(db: Session, id: int):
    db_p_nutricionales = db.query(models.p_nutricionales.p_nutricionales).filter(models.p_nutricionales.p_nutricionales.ID == id).first()
    if db_p_nutricionales:
        db.delete(db_p_nutricionales)
        db.commit()
    return db_p_nutricionales
