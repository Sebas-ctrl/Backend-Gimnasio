from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyTipo(enum.Enum):
    Aerobico="Aerobico"
    Resistencia="Resistencia"
    Flexibilidad="Flexibilidad"
    Fuerza="Fuerza"

class MyDificultad(enum.Enum):
    Basico="Basico"
    Intermedio="Intermedio"
    Avanzado="Avanzado"

class Ejercicio(Base):
    __tablename__ = "tbc_ejercicios"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    Descripcion = Column(String(255))  
    Video = Column(String(255))
    Tipo= Column(Enum(MyTipo)) 
    Estatus = Column(Boolean, default=False)
    Dificultad= Column(Enum(MyDificultad)) 
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Recomendaciones = Column(String(255)) 
    Restricciones = Column(String(255)) 

    