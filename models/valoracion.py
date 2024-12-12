from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy import PrimaryKeyConstraint

class Valoracion(Base):
    __tablename__ = 'tbd_valoracion_nutricional'
    ID = Column(Integer, primary_key=True, index=True)
    Miembro_ID = Column(Integer)
    Indicador_ID = Column(Integer)
    Pregunta_ID = Column(Integer)
    Valor = Column(String(60))
    Comentarios = Column(String(60))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    # # Definimos la clave primaria compuesta
    # __table_args__ = (
    #     PrimaryKeyConstraint('Miembro_ID', 'Indicador_ID', 'Pregunta_ID'),
    # )