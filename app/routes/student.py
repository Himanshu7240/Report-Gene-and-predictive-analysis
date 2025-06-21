from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/students/performance")
async def get_student_performance():
    """
    Retrieve student performance including score, attendance, behavior, and remarks.
    Remarks are derived based on the score.
    """
    # Load student data
    student_data = pd.read_csv("data/students.csv")

    # Define a function to assign remarks based on score
    def get_remarks(score):
        if score >= 90:
            return "Excellent"
        elif score >= 80:
            return "Good"
        elif score >= 70:
            return "Fair"
        else:
            return "Needs Improvement"

    # Apply remarks
    student_data["remarks"] = student_data["score"].apply(get_remarks)

    # Return selected fields including calculated remarks
    result = student_data[['name', 'score', 'attendance', 'behavior', 'remarks']].head(5)
    return result.to_dict(orient="records")
