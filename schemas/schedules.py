from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime, date

class ScheduleBase(BaseModel):
    Usuario:str
    Tipo:str
    Fecha_Inicio:datetime
    Fecha_Fin:datetime
    Fecha_Registro:datetime
    Estatus: bool
    Empleado:str
    Sucursal:str
    Servicio:str
    # Id_persona: int

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleUpdate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    ID:int
    # owner_id: int clave foranea
    class Config:
        orm_mode = True
        
