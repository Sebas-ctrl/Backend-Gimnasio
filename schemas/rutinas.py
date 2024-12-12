from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class RutinasBase(BaseModel):
    Nombre: str
    Programa_Saludable_ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    Tiempo_Aproximado: str
    Estatus: str
    Resultados_Esperados: str

class RutinasCreate(RutinasBase):
    pass

class RutinasUpdate(RutinasBase):
    pass

class Rutina(RutinasBase):
    ID: int
    Programa_Saludable_ID: int
    class Config:
        orm_mode = True
