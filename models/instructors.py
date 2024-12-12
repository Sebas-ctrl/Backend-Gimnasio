from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Instructor(Base):
    __tablename__ = "tbb_instructors"

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String(80))
    email = Column(String(100), unique=True, index=True)
    specialty = Column(String(100))
    years_of_experience = Column(Integer)
    total_clients_attended = Column(Integer, default=0)
    status = Column(Boolean, default=True, nullable=False)
    registration_date = Column(DateTime)
    update_date = Column(DateTime, nullable=True)
    rating = Column(Integer, default=0)

    # Puedes agregar relaciones si es necesario
