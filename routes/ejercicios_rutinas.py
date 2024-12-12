from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.ejercicios_rutinas, models.ejercicios_rutinas, config.db, schemas.ejercicios_rutinas
from typing import List

key = Fernet.generate_key()
f = Fernet(key)
ejcrtn = APIRouter()
models.ejercicios_rutinas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los Ejercicios - Rutinas
@ejcrtn.get('/ejecrutis/', response_model=List[schemas.ejercicios_rutinas.EjcRtn], tags=["Ejercicios-Rutinas"])
def read_ejcrtns(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_ejcrtns = crud.ejercicios_rutinas.get_ejcrnts(db=db,skip=skip, limit=limit)
    return db_ejcrtns

# Ruta para obtener un Ejercicios - Rutinas por ejercicio ID
@ejcrtn.post("/ejecruti/{ejercicio_id}/{rutina_id}", response_model=schemas.ejercicios_rutinas.EjcRtn, tags=["Ejercicios-Rutinas"])
def get_ejcrtn_by_ids(ejercicio_id: int, rutina_id: int, db: Session = Depends(get_db)):
    db_ejcrtn = crud.ejercicios_rutinas.get_ejcrnt_by_ids(db=db, ejercicio_id=ejercicio_id, rutina_id=rutina_id)
    if db_ejcrtn is None:
        raise HTTPException(status_code=404, detail="Ejercicio - Rutina not found")
    return db_ejcrtn

# Ruta para crear un Ejercicios - Rutinas
@ejcrtn.post('/ejecrutis/', response_model=schemas.ejercicios_rutinas.EjcRtn, tags=["Ejercicios-Rutinas"])
def create_ejcrtn(ejcrtn: schemas.ejercicios_rutinas.EjcRtnCreate, db: Session=Depends(get_db)):
    db_ejcrtns = crud.ejercicios_rutinas.get_ejcrnt_by_ids(db, ejercicio_id=ejcrtn.Ejercicio_ID, rutina_id=ejcrtn.Rutina_ID)
    if db_ejcrtns:
        raise HTTPException(status_code=400, detail="Ejercicio - Rutina existente intenta nuevamente")
    return crud.ejercicios_rutinas.create_ejcrnt(db=db, ejcrtn=ejcrtn)

# Ruta para actualizar un Ejercicios - Rutinas
@ejcrtn.put("/ejecruti/{ejercicio_id}/{rutina_id}", response_model=schemas.ejercicios_rutinas.EjcRtn, tags=["Ejercicios-Rutinas"])
def update_ejcrtn(ejercicio_id: int, rutina_id: int, ejcrtn:schemas.ejercicios_rutinas.EjcRtnUpdate, db: Session = Depends(get_db)):
    db_ejcrtn = crud.ejercicios_rutinas.update_ejcrtn(db=db, ejercicio_id=ejercicio_id, rutina_id=rutina_id, ejcrtn=ejcrtn)
    if db_ejcrtn is None:
        raise HTTPException(status_code=404, detail="Ejercicio - Rutina not found")
    return db_ejcrtn

# Ruta para eliminar un Ejercicios - Rutinas
@ejcrtn.delete('/ejecrutis/{ejercicio_id}/{rutina_id}', response_model=schemas.ejercicios_rutinas.EjcRtn,tags=["Ejercicios-Rutinas"])
def delete_ejcrtn(ejercicio_id: int, rutina_id: int, db: Session=Depends(get_db)):
    db_ejcrtns = crud.ejercicios_rutinas.delete_ejcrt(db=db, ejercicio_id=ejercicio_id, rutina_id=rutina_id )
    if db_ejcrtns is None:
        raise HTTPException(status_code=404, detail="Ejercicio - Rutina no existe, no se pudo eliminar ")
    return db_ejcrtns