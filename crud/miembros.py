import models.miembros
import schemas.miembros
from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime
from sqlalchemy import func, extract, desc

def get_miembro(db: Session, id: int):
    return db.query(models.miembros.Miembro).filter(models.miembros.Miembro.ID == id).first()

def get_miembro_by_id(db: Session, tipo: str):
    return db.query(models.miembros.Miembro).filter(models.miembros.Miembro.Tipo == tipo).first()

def get_miembros(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.miembros.Miembro).order_by(desc(models.miembros.Miembro.ID)).offset(skip).limit(limit).all()

def get_miembros_count(db: Session):
    current_year = datetime.now().year
    
    result = db.query(
        extract('month', models.miembros.Miembro.Fecha_Registro).label('month'),
        func.count(models.miembros.Miembro.Fecha_Registro).label('count')
    ).filter(
        extract('year', models.miembros.Miembro.Fecha_Registro) == current_year
    ).group_by(
        extract('month', models.miembros.Miembro.Fecha_Registro)
    ).all()

    result_dict = {month: count for month, count in result}
    
    return result_dict

def create_miembros(db: Session, nom: schemas.miembros.MiembroCreate):
    db_user = models.miembros.Miembro(
                                      Membresia_ID=nom.Membresia_ID,
                                      Usuario_ID=nom.Usuario_ID, 
                                      Tipo=nom.Tipo,  
                                      Estatus=nom.Estatus, 
                                      Antiguedad=nom.Antiguedad, 
                                      Fecha_Registro=nom.Fecha_Registro, 
                                      Fecha_Actualizacion=nom.Fecha_Actualizacion )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_miembros(db: Session, id: int, person: schemas.miembros.MiembroUpdate):
    db_user = db.query(models.miembros.Miembro).filter(models.miembros.Miembro.ID == id).first()
    if db_user:
        for var, value in vars(person).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_miembros(db: Session, id: int):
    db_user = db.query(models.miembros.Miembro).filter(models.miembros.Miembro.ID == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user