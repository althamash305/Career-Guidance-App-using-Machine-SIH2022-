from sqlalchemy.orm import Session

import models, schemas

def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()

def get_mentor_by_email(db: Session, email: str):
    return db.query(models.Mentor).filter(models.Mentor.email == email).first()

def create_student(db: Session, user: schemas.StudentCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Student(
        # id = user.id,
        name = user.name,
        email=user.email,
        
        password=user.password
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def create_donation(db: Session, user: schemas.DonationCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Donations(
        # id = user.id,
        aid=user.aid,
        why = user.why,
        driveLink = user.driveLink
        
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_mentor(db: Session, user: schemas.MentorCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Mentor(
    
    # id = user.id,
    name = user.name,
    email = user.email,
    
    password = user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

