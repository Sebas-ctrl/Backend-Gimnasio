from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime, date

class p_nutricionalBase(BaseModel):
    Pregunta:str
    Fecha_Creacion:datetime
    Fecha_Actualizacion:datetime
    # Id_persona: int

class p_nutricionalesCreate(p_nutricionalBase):
    pass

class p_nutricionalesUpdate(p_nutricionalBase):
    pass

class p_nutricional(p_nutricionalBase):
    ID:int
    # owner_id: int clave foranea
    class Config:
        orm_mode = True
        