from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, func
from .database import Base
import enum

class KYCStatus(enum.Enum):
    pending = 'pending'
    approved = 'approved'
    rejected = 'rejected'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)

class KYCRecord(Base):
    __tablename__ = 'kyc_records'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    full_name = Column(String(255), nullable=False)
    dob = Column(String(20), nullable=True)
    passport_number = Column(String(100), nullable=True)
    status = Column(Enum(KYCStatus), default=KYCStatus.pending)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True, index=True)
    event = Column(String(255), nullable=False)
    actor = Column(String(255), nullable=True)
    resource = Column(String(255), nullable=True)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())