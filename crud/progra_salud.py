import models.progra_salud
import schemas.progra_salud
from sqlalchemy.orm import Session

def get_programa(db: Session, id: int):
    return db.query(models.progra_salud.ProgramaSaludable).filter(models.progra_salud.ProgramaSaludable.ID == id).first()

def get_programas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.progra_salud.ProgramaSaludable).offset(skip).limit(limit).all()

def create_programa(db: Session, programa: schemas.progra_salud.ProgramaCreate):
    db_programa = models.progra_salud.ProgramaSaludable(
        Nombre=programa.Nombre,
        Usuario_ID=programa.Usuario_ID,
        Instructor_ID=programa.Instructor_ID,
        Fecha_Creacion=programa.Fecha_Creacion,
        Estatus=programa.Estatus,
        Duracion=programa.Duracion,
        Porcentaje_Avance=programa.Porcentaje_Avance,
        Fecha_Ultima_Actualizacion=programa.Fecha_Ultima_Actualizacion
    )
    db.add(db_programa)
    db.commit()
    db.refresh(db_programa)
    return db_programa

def update_programa(db: Session, id: int, programa: schemas.progra_salud.ProgramaUpdate):
    db_programa = db.query(models.progra_salud.ProgramaSaludable).filter(models.progra_salud.ProgramaSaludable.ID == id).first()
    if db_programa:
        for var, value in vars(programa).items():
            setattr(db_programa, var, value) if value else None
        db.commit()
        db.refresh(db_programa)
    return db_programa

def delete_programa(db: Session, id: int):
    db_programa = db.query(models.progra_salud.ProgramaSaludable).filter(models.progra_salud.ProgramaSaludable.ID == id).first()
    if db_programa:
        db.delete(db_programa)
        db.commit()
    return db_programa

