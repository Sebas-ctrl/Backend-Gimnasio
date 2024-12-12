from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Time, Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum
class MyStatus(str, enum.Enum):
    Concluido = "Concluido"
    Actual = "Actual"
    Suspendida = "Suspendida"

class Rutina(Base):
    __tablename__ = "tbd_rutinas"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100))
    Programa_Saludable_ID = Column(Integer)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Tiempo_Aproximado = Column(String(10))
    Estatus = Column(Enum(MyStatus), default=MyStatus.Actual)
    Resultados_Esperados = Column(Text)
