from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class Puesto(Base):
    __tablename__ = "tbc_puestos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100))
    Descripcion = Column(String(255)) 
    Salario = Column(String(20))  
    Requisitos = Column(String(255))  
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
