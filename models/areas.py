from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base


class Area(Base):
    __tablename__ = 'tbb_areas'
    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(80))
    Descripcion = Column(String(80))
    Sucursal = Column(String(80))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    # Id_persona = Column(Integer)
    # intems = relationship("Item", back_populates="owner") Clave foranea   
