from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.empleados,config.db,schemas.empleados,models.empleados
from typing import List

empleado = APIRouter()

models.empleados.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@empleado.get("/empleados/", response_model=List[schemas.empleados.Empleado], tags=["Empleados"] ,dependencies=[Depends(Portador())])
def read_empleados(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_empleados= crud.empleados.get_empleados(db=db, skip=skip, limit=limit)
    return db_empleados


@empleado.post("/empleado/{ID}", response_model=schemas.empleados.Empleado, tags=["Empleados"] ,dependencies=[Depends(Portador())])
def read_empleado(ID: int, db: Session = Depends(get_db)):
    db_empleados= crud.empleados.get_empleado(db=db, ID=ID)
    if db_empleados is None:
        raise HTTPException(status_code=404, detail="Empleado not found")
    return db_empleados

@empleado.post("/empleados/", response_model=schemas.empleados.Empleado, tags=["Empleados"],dependencies=[Depends(Portador())])
def create_empleado(empleado: schemas.empleados.EmpleadoCreate, db: Session = Depends(get_db)):
    db_empleados = crud.empleados.get_empleado_by_Numero(db, Numero_Empleado=empleado.Numero_Empleado)
    if db_empleados:
        raise HTTPException(status_code=400, detail="Empleado existente intenta nuevamente")
    return crud.empleados.create_empleado(db=db, empleado=empleado)
 

@empleado.put("/empleado/{ID}", response_model=schemas.empleados.Empleado, tags=["Empleados"] ,dependencies=[Depends(Portador())])
def update_empleado(ID: int, empleado: schemas.empleados.EmpleadoUpdate, db: Session = Depends(get_db)):
    db_empleados = crud.empleados.update_empleado(db = db, ID = ID, empleado = empleado)
    if db_empleados is None:
        raise HTTPException(status_code=404, detail="Empleado no existente, no esta actuaizado")
    return db_empleados

@empleado.delete("/empleado/{ID}", response_model=schemas.empleados.Empleado, tags=["Empleados"] ,dependencies=[Depends(Portador())])
def delete_empleado(ID: int, db: Session = Depends(get_db)):
    db_empleados = crud.empleados.delete_empleado(db = db, ID = ID)
    if db_empleados is None:
        raise HTTPException(status_code=404, detail="Empleado no existe, no se pudo eliminar")
    return db_empleados

