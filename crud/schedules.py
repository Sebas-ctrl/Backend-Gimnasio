import models.schedules
import schemas.schedules
from sqlalchemy.orm import Session
import models, schemas


def get_schedule(db:Session, id: int):
    return db.query(models.schedules.Schedule).filter(models.schedules.Schedule.ID == id).first()


def get_schedule_by_usuario(db:Session, usuario: str):
    return db.query(models.schedules.Schedule).filter(models.schedules.Schedule.Usuario == usuario).first()


def get_schedules(db:Session, skip: int=0, limit:int=10):
    return db.query(models.schedules.Schedule).offset(skip).limit(limit).all()


def create_schedule(db:Session, schedule: schemas.schedules.ScheduleCreate):
    db_schedule = models.schedules.Schedule(Usuario=schedule.Usuario,
                                      Tipo=schedule.Tipo, 
                                      Fecha_Inicio=schedule.Fecha_Inicio, 
                                      Fecha_Fin=schedule.Fecha_Fin, 
                                      Fecha_Registro=schedule.Fecha_Registro, 
                                      Estatus=schedule.Estatus,
                                      Empleado=schedule.Empleado,
                                      Sucursal=schedule.Sucursal,
                                      Servicio=schedule.Servicio)
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule


def update_schedule(db:Session, id:int, schedule:schemas.schedules.ScheduleUpdate):
    db_schedule = db.query(models.schedules.Schedule).filter(models.schedules.Schedule.ID == id).first()
    if db_schedule:
        for var, value in vars(schedule).items():
            setattr(db_schedule, var, value) if value else None
        db.commit()
        db.refresh(db_schedule)
    return db_schedule

def delete_schedule(db:Session, id:int):
    db_schedule = db.query(models.schedules.Schedule).filter(models.schedules.Schedule.ID == id).first()
    if db_schedule:
        db.delete(db_schedule)
        db.commit()
    return db_schedule
