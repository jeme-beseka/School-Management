from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    firstName: str
    lastName: str
    email: str
    dateOfBirth: date

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True