from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Base class for Instructor schemas
class InstructorBase(BaseModel):
    name: str
    email: str
    specialty: str
    years_of_experience: int
    total_clients_attended: int = 0
    status: bool = True
    registration_date: datetime = datetime.utcnow()
    update_date: Optional[datetime] = None
    rating: int = 0

class InstructorCreate(InstructorBase):
    pass

class InstructorUpdate(InstructorBase):
    pass

class Instructor(InstructorBase):
    id: int
    class Config:
        orm_mode = True
