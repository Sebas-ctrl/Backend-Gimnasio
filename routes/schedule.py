from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.schedules, config.db, schemas.schedules, models.schedules
from portadortoken import Portador
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

schedule = APIRouter()
models.schedules.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@schedule.get('/schedules/', response_model=List[schemas.schedules.Schedule],tags=['Horarios'],dependencies=[Depends(Portador())])
def read_schedules(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_schedules = crud.schedules.get_schedules(db=db,skip=skip, limit=limit)
    return db_schedules

@schedule.post("/schedule/{id}", response_model=schemas.schedules.Schedule, tags=["Horarios"],dependencies=[Depends(Portador())])
def read_schedule(id: int, db: Session = Depends(get_db)):
    db_schedule= crud.schedules.get_schedule(db=db, id=id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="schedule not found")
    return db_schedule


@schedule.post('/schedules/', response_model=schemas.schedules.Schedule,tags=['Horarios'],dependencies=[Depends(Portador())])
def create_schedule(schedule: schemas.schedules.ScheduleCreate, db: Session=Depends(get_db)):
    db_schedules = crud.schedules.get_schedule_by_usuario(db,usuario=schedule.Usuario)
    if db_schedules:
        raise HTTPException(status_code=400, detail="Horario existente intenta nuevamente")
    return crud.schedules.create_schedule(db=db, schedule=schedule)


@schedule.put('/schedules/{id}', response_model=schemas.schedules.Schedule,tags=['Horarios'],dependencies=[Depends(Portador())])
def update_schedule(id:int,schedule: schemas.schedules.ScheduleUpdate, db: Session=Depends(get_db)):
    db_schedules = crud.schedules.update_schedule(db=db, id=id, schedule=schedule)
    if db_schedules is None:
        raise HTTPException(status_code=404, detail="Horario no existe, no se pudo actualizar ")
    return db_schedules


@schedule.delete('/schedules/{id}', response_model=schemas.schedules.Schedule,tags=['Horarios'],dependencies=[Depends(Portador())])
def delete_schedule(id:int, db: Session=Depends(get_db)):
    db_schedules = crud.schedules.delete_schedule(db=db, id=id)
    if db_schedules is None:
        raise HTTPException(status_code=404, detail="Horario no existe, no se pudo eliminar ")
    return db_schedules
