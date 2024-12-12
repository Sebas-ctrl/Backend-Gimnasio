from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date
import enum

class MiembrosBase(BaseModel):
    Membresia_ID: int
    Usuario_ID: int
    Tipo: str
    Estatus: bool
    Antiguedad: str
    Fecha_Registro : datetime
    Fecha_Actualizacion: datetime


class MiembroCreate(MiembrosBase):
    pass

class MiembroUpdate(MiembrosBase):
    pass

class Miembro(MiembrosBase):
    ID: int
    Membresia_ID: int
    Usuario_ID: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True


