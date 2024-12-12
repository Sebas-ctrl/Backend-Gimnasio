from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class EmpleadoBase(BaseModel):
    Area_ID: str
    Fecha_Contratacion:datetime
    Puesto_ID: str
    Persona_ID: str
    Numero_Empleado: str
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
    Estatus:bool

class EmpleadoCreate(EmpleadoBase):
    pass
class EmpleadoUpdate(EmpleadoBase):
    pass
class Empleado(EmpleadoBase):
    ID:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True 
