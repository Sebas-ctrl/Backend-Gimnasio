from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime

class DietaBase(BaseModel):
    Nombre:str
    Detalle:str
    Descripcion:str
    Objetivo:str
    Estatus:bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class DietaCreate(DietaBase):
    pass

class DietaUpdate(DietaBase):
    pass

class Dieta(DietaBase):
    ID:int
    class Config:
        orm_mode = True

        