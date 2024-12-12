
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class ProgramaBase(BaseModel):
    Nombre: str
    Usuario_ID: int
    Instructor_ID: int
    Fecha_Creacion: datetime
    Estatus: str
    Duracion: str
    Porcentaje_Avance: float
    Fecha_Ultima_Actualizacion: Optional[datetime] = None

class ProgramaCreate(ProgramaBase):
    pass

class ProgramaUpdate(ProgramaBase):
    pass

class Programa(ProgramaBase):
    ID: int
    Usuario_ID: int
    Instructor_ID: int
    class Config:
        orm_mode = True
