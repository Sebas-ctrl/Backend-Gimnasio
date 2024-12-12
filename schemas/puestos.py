from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class PuestoBase(BaseModel):
    Nombre: str
    Descripcion: str
    Salario: str
    Requisitos: str
    Estatus:bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime

class PuestoCreate(PuestoBase):
    pass
class PuestoUpdate(PuestoBase):
    pass
class Puesto(PuestoBase):
    ID:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True
