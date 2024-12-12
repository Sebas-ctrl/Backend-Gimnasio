from typing import List, Union
from pydantic import BaseModel
import enum
from datetime import datetime

# Define los Enum para coincidir con SQLAlchemy

class IndicadorNutricionalBase(BaseModel):
    Altura: float
    Peso: float
    Imc: float
    Porcentaje_grasa: float
    Nivel_actividad: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    Usuario_Id : int


class IndicadorNutricionalCreate(IndicadorNutricionalBase):
    pass

class IndicadorNutricionalUpdate(IndicadorNutricionalBase):
    pass

class IndicadorNutricional(IndicadorNutricionalBase):
    ID: int
    class Config:
        orm_mode = True
