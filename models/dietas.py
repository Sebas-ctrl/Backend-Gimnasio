from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base

class Dieta(Base):
    __tablename__ = 'tbd_dietas'
    ID = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Detalle = Column(LONGTEXT)
    Descripcion = Column(LONGTEXT)
    Objetivo = Column(LONGTEXT)
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
