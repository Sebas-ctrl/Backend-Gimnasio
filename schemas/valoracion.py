from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime

class ValoracionBase(BaseModel):
    Miembro_ID:int
    Indicador_ID:int
    Pregunta_ID:int
    Valor:str
    Comentarios:str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class ValoracionCreate(ValoracionBase):
    pass

class ValoracionUpdate(BaseModel):
    Valor: str
    Comentarios: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class Valoracion(ValoracionBase):
    Miembro_ID:int
    Indicador_ID:int
    Pregunta_ID:int
    class Config:
        orm_mode = True