# app/routes/student.py

from fastapi import APIRouter
from app.ml.model import train_student_performance_model
import pandas as pd

router = APIRouter()

# Sample student data (You can replace this with actual DB or CSV data)
student_data = pd.read_csv("data/students.csv")

@router.get("/students/performance")
async def get_student_performance():
    """
    Retrieve student performance including score, attendance, and behavior data.
    """
    # In a real scenario, you might query the database here.
    # For simplicity, we're using static data.

    # For this POC, returning first 5 rows of student data
    return student_data[['name', 'score', 'attendance', 'behavior']].head(5)
