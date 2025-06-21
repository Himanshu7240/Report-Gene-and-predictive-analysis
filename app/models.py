# app/ml/model.py

from sqlalchemy import Column, Integer, String, Float
from app.database import Base

# Define a simple Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Float)
    attendance = Column(Float)
    behavior = Column(Float)

    def __repr__(self):
        return f"<Student(name={self.name}, score={self.score}, attendance={self.attendance}, behavior={self.behavior})>"
