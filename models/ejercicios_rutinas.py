from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models
import enum
from sqlalchemy import PrimaryKeyConstraint

class MyType(str, enum.Enum):
    Repeticiones = "Repeticiones"
    Tiempo = "Tiempo"

class EjcRtn(Base):
    __tablename__ = 'tbd_ejercicios_rutinas'
    Ejercicio_ID = Column(Integer)
    Rutina_ID = Column(Integer)
    Cantidad = Column(String(10))
    Tipo = Column(Enum(MyType))
    Observaciones = Column(Text)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Estatus = Column(Boolean)

    # Definimos la clave primaria compuesta
    __table_args__ = (
        PrimaryKeyConstraint('Ejercicio_ID', 'Rutina_ID'),
    )
    