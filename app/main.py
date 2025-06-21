# app/main.py

from fastapi import FastAPI
from app.routes import student, transactions, voice

app = FastAPI()

# Include the routes in the FastAPI app
app.include_router(student.router)
app.include_router(transactions.router)
app.include_router(voice.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Report Generation and Predictive Analytics API!"}
