from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime

class EjcRtnBase(BaseModel):
    Ejercicio_ID: int
    Rutina_ID: int
    Cantidad: str
    Tipo: str
    Observaciones: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    Estatus:bool

class EjcRtnCreate(EjcRtnBase):
    pass

class EjcRtnUpdate(BaseModel):
    Cantidad: str
    Tipo: str
    Observaciones: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    Estatus: bool

class EjcRtn(EjcRtnBase):
    Ejercicio_ID: int
    Rutina_ID: int
    class Config:
        orm_mode = True