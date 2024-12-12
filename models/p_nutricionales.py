from sqlalchemy import Column, Boolean, Integer, String, DateTime, Enum
from config.db import Base
import enum

# Define el modelo de SQLAlchemy
class p_nutricionales(Base):
    __tablename__ = 'tbb_preguntas_nutricionales'

    ID = Column(Integer, primary_key=True, index=True)
    Pregunta = Column(String(255))  
    Fecha_Creacion = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
