from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def create_kyc(db: Session, payload: schemas.KYCSubmit):
    record = models.KYCRecord(user_id=payload.user_id, full_name=payload.full_name, dob=payload.dob, passport_number=payload.passport_number)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_kyc(db: Session, kyc_id: int):
    return db.query(models.KYCRecord).filter(models.KYCRecord.id == kyc_id).first()

def update_kyc_status(db: Session, kyc_id: int, status: models.KYCStatus):
    rec = db.query(models.KYCRecord).filter(models.KYCRecord.id == kyc_id).first()
    if not rec:
        return None
    rec.status = status
    db.commit()
    db.refresh(rec)
    return rec
