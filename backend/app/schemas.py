from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: str

class UserOut(UserCreate):
    id: int
    class Config:
        orm_mode = True

class KYCSubmit(BaseModel):
    user_id: int
    full_name: str
    dob: Optional[str]
    passport_number: Optional[str]

class KYCOut(BaseModel):
    id: int
    user_id: int
    full_name: str
    status: str
    class Config:
        orm_mode = True

class AMLRequest(BaseModel):
    kyc_id: int

class AMLResponse(BaseModel):
    kyc_id: int
    result: str