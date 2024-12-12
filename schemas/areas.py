from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime, date

class AreaBase(BaseModel):
    Nombre:str
    Descripcion:str
    Sucursal:str
    Estatus: bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
    # Id_persona: int

class AreaCreate(AreaBase):
    pass

class AreaUpdate(AreaBase):
    pass

class Area(AreaBase):
    ID:int
    # owner_id: int clave foranea
    class Config:
        orm_mode = True
        
