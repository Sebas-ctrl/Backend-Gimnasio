from sqlalchemy import Column, Integer, String, DateTime, Enum, Numeric
from config.db import Base
import enum

class EstatusPrograma(str, enum.Enum):
    Registrado = "Registrado"
    Sugerido = "Sugerido"
    Aprobado_Medico = "Aprobado por el Médico"
    Aprobado_Usuario = "Aprobado por el Usuario"
    Rechazado_Medico = "Rechazado por el Médico"
    Rechazado_Usuario = "Rechazado por el Usuario"
    Terminado = "Terminado"
    Suspendido = "Suspendido"
    Cancelado = "Cancelado"

class ProgramaSaludable(Base):
    __tablename__ = "tbd_programas_saludables"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(250))
    Usuario_ID = Column(Integer)
    Instructor_ID = Column(Integer)
    Fecha_Creacion = Column(DateTime)
    Estatus = Column(Enum(EstatusPrograma), default=EstatusPrograma.Registrado)
    Duracion = Column(String(80))
    Porcentaje_Avance = Column(Numeric(5, 2))
    Fecha_Ultima_Actualizacion = Column(DateTime)