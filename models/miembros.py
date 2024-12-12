
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyTipo(str, enum.Enum):
    Frecuente = "Frecuente"
    Ocasional = "Ocasional"
    Nuevo = "Nuevo"
    Esporadico = "Esporadico"
    Visita = "Visita"

class Miembro(Base):
    __tablename__ = "tbb_miembros"

    ID= Column(Integer, primary_key=True, index=True)
    # Membresia_ID = Column(Integer, ForeignKey("tbc_membresias.ID"))
    # Usuario_ID = Column(Integer, ForeignKey("tbb_usuarios.ID"))
    Membresia_ID = Column(Integer)
    Usuario_ID = Column(Integer)
    Tipo = Column( Enum(MyTipo)) 
    Estatus = Column(Boolean, default=False)
    Antiguedad = Column(String(80))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    # membresia = relationship("Membresia")
    # usuario = relationship("User")