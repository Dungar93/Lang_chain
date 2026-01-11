from pydantic import BaseModel, Field, ValidationError, EmailStr
from typing import Optional, List, Literal


class Student(BaseModel):
    name: str = 'Dungar Soni'
    age: Optional[int] = None
    email: EmailStr
    cgpa:float = Field(gt=0.0, lt=10.0, description="CGPA must be between 0.0 and 10.0")


new_student = {
    "name": "Dungar Soni",
    "age": 21,
    "email": "dungar.soni@example.com",
    "cgpa": 8.5
}

student = Student(**new_student)
print(student)