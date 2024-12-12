from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

from models.ejercicios import MyTipo, MyDificultad

class EjercicioBase(BaseModel):
    
    Nombre: str
    Descripcion: str
    Video: str
    Tipo: MyTipo
    Estatus:bool
    Dificultad: MyDificultad
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
    Recomendaciones: str
    Restricciones: str

    
    
class EjercicioCreate(EjercicioBase):
    pass
class EjercicioUpdate(EjercicioBase):
    pass
class Ejercicio(EjercicioBase):
    ID: int

    class Config:
        orm_mode = True