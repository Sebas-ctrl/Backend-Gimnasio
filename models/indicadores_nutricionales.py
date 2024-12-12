from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import enum

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the enum for Gender
class MyGenero(enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"

# Define the enum for Activity Level
class NivelActividad(enum.Enum):
    Sedentario = "Sedentario"
    Ligero = "Ligero"
    Moderado = "Moderado"
    Activo = "Activo"
    Muy_Activo = "Muy Activo"

# Define the model for Actividad
class Actividad(Base):
    __tablename__ = "tbd_indicadores_nutricionales"

    ID = Column(Integer, primary_key=True, index=True)
    Altura = Column(Float(5, 2))
    Peso = Column(Float(5, 2))
    Imc = Column(Float(5,2))
    Porcentaje_grasa = Column(Float(5,2))
    Nivel_actividad = Column(Enum(NivelActividad))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Usuario_Id = Column(Integer)