import models.instructors
import schemas.instructors
from sqlalchemy.orm import Session
import models, schemas

def get_instructor(db: Session, id: int):
    return db.query(models.instructors.Instructor).filter(models.instructors.Instructor.id == id).first()

def get_instructor_by_name(db: Session, name: str):
    return db.query(models.instructors.Instructor).filter(models.instructors.Instructor.name == name).first()

def get_instructors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.instructors.Instructor).offset(skip).limit(limit).all()

def create_instructor(db: Session, instructor: schemas.instructors.InstructorCreate):
    db_instructor = models.instructors.Instructor(
        name=instructor.name,
        email=instructor.email,
        specialty=instructor.specialty,
        years_of_experience=instructor.years_of_experience,
        total_clients_attended=instructor.total_clients_attended,
        status=instructor.status,
        registration_date=instructor.registration_date,
        update_date=instructor.update_date,
        rating=instructor.rating
    )
    db.add(db_instructor)
    db.commit()
    db.refresh(db_instructor)
    return db_instructor

def update_instructor(db: Session, id: int, instructor: schemas.instructors.InstructorUpdate):
    db_instructor = db.query(models.instructors.Instructor).filter(models.instructors.Instructor.id == id).first()
    if db_instructor:
        for var, value in vars(instructor).items():
            setattr(db_instructor, var, value) if value is not None else None
        db.commit()
        db.refresh(db_instructor)
    return db_instructor

def delete_instructor(db: Session, id: int):
    db_instructor = db.query(models.instructors.Instructor).filter(models.instructors.Instructor.id == id).first()
    if db_instructor:
        db.delete(db_instructor)
        db.commit()
    return db_instructor
